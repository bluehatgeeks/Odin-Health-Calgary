-- Idempotent: strip existing [session start] markers, then prefix first event
-- of each inactivity-based session (per distinct_id).

create or replace function public.mark_session_start_friendly_names(
  session_gap_minutes integer default 30
)
returns integer
language plpgsql
security definer
set search_path = public
as $$
declare
  updated_count int;
begin
  if session_gap_minutes is null or session_gap_minutes < 1 then
    session_gap_minutes := 30;
  end if;

  update public.events
  set friendly_name = regexp_replace(friendly_name, '^\[session start\] ', '')
  where friendly_name is not null
    and friendly_name like '[session start]%';

  with ordered as (
    select
      id,
      event_time,
      lag(event_time) over (
        partition by distinct_id
        order by event_time asc, id asc
      ) as prev_time
    from public.events
  ),
  starts as (
    select
      id,
      (
        prev_time is null
        or (event_time - prev_time) > make_interval(mins => session_gap_minutes)
      ) as is_start
    from ordered
  )
  update public.events e
  set friendly_name =
    '[session start] '
    || coalesce(
      nullif(
        trim(
          regexp_replace(coalesce(e.friendly_name, ''), '^\[session start\] ', '')
        ),
        ''
      ),
      '(unmapped)'
    )
  from starts s
  where e.id = s.id
    and s.is_start;

  get diagnostics updated_count = row_count;
  return coalesce(updated_count, 0);
end;
$$;

comment on function public.mark_session_start_friendly_names(integer) is
  'Prefixes friendly_name with "[session start] " for session boundary rows per distinct_id (gap in minutes between consecutive events).';

grant execute on function public.mark_session_start_friendly_names(integer) to service_role;
