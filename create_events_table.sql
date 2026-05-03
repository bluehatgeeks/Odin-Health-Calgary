-- Supabase table for Mixpanel events (friendly name version)
-- Run this in Supabase SQL editor

create table if not exists public.events (
    id uuid default gen_random_uuid() primary key,
    distinct_id text not null,
    event_name text not null,            -- original Mixpanel event name (e.g. $mp_web_page_view)
    friendly_name text,                  -- our readable label, may be null if not mapped
    url text,                            -- $current_url property if present
    event_time timestamptz not null,      -- Mixpanel timestamp ("time" property)
    raw_properties jsonb                 -- all other event properties for future analysis
);

-- optional indexes for faster queries
create index if not exists idx_events_distinct on public.events(distinct_id);
create index if not exists idx_events_time on public.events(event_time desc);
