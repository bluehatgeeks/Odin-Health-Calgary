-- Idempotent hourly imports: upsert by Mixpanel $insert_id when present.
-- Full-column unique index (not partial) so PostgREST `.upsert(..., onConflict: 'mixpanel_insert_id')` works.
alter table public.events add column if not exists mixpanel_insert_id text;

drop index if exists public.events_mixpanel_insert_id_uidx;
create unique index if not exists events_mixpanel_insert_id_uidx
  on public.events (mixpanel_insert_id);
