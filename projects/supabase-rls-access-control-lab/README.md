# Supabase Row-Level Security & Tenant Isolation Lab

A Supabase/PostgreSQL security exercise for a multi-tenant billing support workspace.

## Demonstrates
- Enabling Row Level Security on application tables
- Scoping records with `auth.uid()`
- Separating organization membership and support roles
- Restricting internal case notes
- Testing cross-organization access boundaries

## Run
The migration, pgTAP policy checks, and manual verification guide are in the companion expansion pack. Use a local Supabase project, apply the migration, and run `supabase test db`. Follow the manual guide with separate authenticated test users to verify actual row access.

This is a learning exercise, not a complete production authorization design. Security-sensitive policies should be reviewed before deployment.
