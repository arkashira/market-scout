# axentx-dev-bot decision
- id: `20260612-082731-market-scout-docs-4f89cbb1`
- project: market-scout
- focus: docs
- created_at: 2026-06-12T08:27:31.406099Z

## dev — axentx-docs @ 2026-06-12T08:27:31.406179Z

Auto-doc update for commit 20260611-071919-market-scout-E4-E4-S2-T2-0c26f0ea-code.

README addition:
## Market Scout

- **New feature:** Added automated market signal ingestion pipeline (`E4-E4-S2-T2`). The system now pulls real‑time demand indicators from partnered data providers, normalizes them, and stores them in the shared BRAIN for downstream product discovery.
- **Usage:** Run `market-scout ingest --source <provider>` to start a fresh ingestion cycle. Results are visible in the BRAIN dashboard under **Signals → Raw**.
- **Configuration:** Update `config/market_scout.yaml` to add API keys and mapping rules for new providers.


CHANGELOG entry:
- - Added automated market signal ingestion pipeline with configurable data source support.

