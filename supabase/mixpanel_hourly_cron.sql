-- Run once in the Supabase Dashboard → SQL Editor (hosted project only), after:
-- 1. Enabling pg_net + pg_cron if prompted
-- 2. Creating Vault secrets:
--
--    select vault.create_secret('https://<project-ref>.supabase.co', 'project_url');
--    select vault.create_secret('<YOUR_ANON_PUBLISHABLE_KEY>', 'publishable_key');

select cron.unschedule(jobid)
from cron.job
where jobname = 'fetch_mixpanel_events_hourly';

select cron.schedule(
  'fetch_mixpanel_events_hourly',
  '0 * * * *',
  $$
  select net.http_post(
    url := (select decrypted_secret from vault.decrypted_secrets where name = 'project_url')
      || '/functions/v1/fetch_mixpanel_events',
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'Authorization', 'Bearer ' || (select decrypted_secret from vault.decrypted_secrets where name = 'publishable_key'),
      'apikey', (select decrypted_secret from vault.decrypted_secrets where name = 'publishable_key')
    ),
    body := '{}'::jsonb
  );
  $$
);
