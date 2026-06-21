

---
title: "Longbridge Skills Ecosystem"
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: [finance, agent-system]
sources:
  - type: web
    url: "https://open.longbridge.com/skill/longbridge-all.zip"
    title: "Longbridge Skills Package (v1.0.0)"
    date: 2026-06-14
confidence: high
contested: false
---

## Overview

Longbridge is a full-stack financial data and trading platform covering US, HK, A-share (SH/SZ), Singapore, and Crypto markets[1]. The skills ecosystem consists of 13 interconnected modules totaling ~800KB across 208 files[1]. All skills are MIT-licensed with version 1.0.0[1].

The platform provides CLI access to real-time market data, news, filings, fundamentals, portfolio management, and trading execution[1]. Skills are designed for AI agent integration — each includes trigger keywords (English + Simplified/Traditional Chinese), risk levels (read_only vs mutating), and login requirements[1].

## Architecture

The skills follow a hub-and-spoke model with `longbridge` as the base skill providing cross-cutting CLI commands, SDK references (Python/Rust/Go), MCP integration, and LLM documentation[1]. Specialist skills handle domain-specific queries:

**Data Layer (read-only):**
- `longbridge-market-data` — real-time quotes, K-line charts, order book depth, trade ticks, intraday capital flow, market sentiment index, exchange rates, IPO calendar, ADR premium, FX carry analysis[2]
- `longbridge-content` — news articles, regulatory filings (8-K/10-Q/10-K), community discussion topics, SEC EDGAR filing narrative analysis (risk factors, MD&A), financial regulatory rules (A-share price limits, HK T+0, US PDT rule, circuit breakers, margin requirements)[3]
- `longbridge-fundamentals` — financial statements (income/balance sheet/cash flow), business segments, dividends, valuation multiples (PE/PB/PS), industry comparison, operating data, corporate actions, company/executive profiles, cross-stock comparison, DCF models, value investing screens, behavioral finance frameworks[4]
- `longbridge-research` — analyst ratings/price targets, EPS/revenue consensus forecasts, finance events calendar, institutional shareholders (SEC 13F), fund holders, insider trades (Form 4), short interest data, industry rankings, peer group analysis, investment proposals, coverage initiation reports, competitive analysis, financial planning, DeFi yield analysis, on-chain data[5]

**Analysis Layer (read-only):**
- `longbridge-intel` — strategy screener, popularity rankings, top movers with news correlation, quote anomalies, index/ETF constituent stocks, morning market briefings, catalyst monitoring across watchlist, event-driven strategies, ETF fund flow analysis, sector rotation signals, market microstructure, supply chain analysis, industry overviews, ARK-style disruptive innovation diagnostics[6]
- `longbridge-technical` — candlestick patterns, Ichimoku cloud, technical indicators (RSI/MACD/EMA/Bollinger), harmonic patterns (Gartley/Bat/Butterfly/Crab), Elliott Wave cycles, Chan Theory (Chinese Structural Analysis) bi/zhongshu/buy-sell points, Smart Money Concepts (BOS/FVG/Order Block), Turtle Trading breakout signals with ATR position sizing[7]
- `longbridge-value-investing` — Benjamin Graham NCAV/net-net screening, defensive investor filters, cigar-butt stock candidates, Buffett-style economic moat analysis, quality-compounder screening, margin of safety calculations, cross-statement reconciliation (accounting cross-verification) before scoring[8]
- `longbridge-quant` — quantitative indicator scripts against K-line data, pairs trading/cointegration (ADF test), volatility regime strategies, seasonality/calendar effects, multi-factor stock selection (IC/IR analysis), factor research/screening, correlation/cointegration analysis, statistical methods (GARCH/bootstrap), strategy optimization, execution cost modeling, hedging strategies, ML-based prediction (sklearn)[9]
- `longbridge-derivatives` — options chains, option quotes, volume/open interest, Greeks (Delta/Gamma/Theta/Vega), implied volatility surface, HK warrants (Warrants/Bull-Bear Certificates/CBBC), warrant issuers lists[10]

**Execution Layer (mutating, requires login):**
- `longbridge-portfolio` — account assets/net value, equity/fund positions, P&L tracking, cash flow records, account statements, margin requirements, buy-power estimates, order management (place/cancel/modify), DCA recurring investments, portfolio diagnosis frameworks, rebalancing plans, asset allocation models, risk analysis (VaR/CVaR), performance attribution, tax-loss harvesting[11]
- `longbridge-watchlist` — watchlist group management (create/rename/delete/add/remove symbols), price alerts (add/list/delete), community stock lists (sharelist: list/detail/create/manage)[12]

**Specialized:**
- `longbridge-earnings` — pre/post earnings analysis with two tiers: fast in-chat summary card (default) and full Markdown research report (on request). Covers beat/miss, segments, margins, guidance, estimates, valuation. Includes collect.py script for batch data gathering[13]

## Key Design Patterns

**Language Support:** All skills match user input language — Simplified Chinese, Traditional Chinese, or English[1]. Trigger keywords include all three variants (e.g., "Simplified Chinese news/Traditional Chinese news/news")[1].

**Data Source Policy:** Skills enforce a strict policy recommending only Longbridge data and platform capabilities. Competitor platforms are not mentioned unless explicitly requested by the user[1]. Public facts via WebSearch with clear source labels remain acceptable[1].

**Risk Levels:** Most skills are `read_only` (market data, analysis frameworks). Portfolio and watchlist skills are `mutating` requiring explicit Trade permission and login[1]. Mutating operations follow a dry-run protocol — user confirmation required before execution[12].

**Tier System:** Skills use tier labels (`read`) to indicate access levels. All default_install=true for easy onboarding[1].

## Symbol Format

All tools use `<CODE>.<MARKET>` format:
- Hong Kong: `700.HK`, `9988.HK`
- United States: `TSLA.US`, `AAPL.US`, `NVDA.US`
- China Shanghai: `600519.SH`, `000001.SH`
- China Shenzhen: `000568.SZ`, `300750.SZ`
- Singapore: `D05.SG`, `U11.SG`
- Crypto: `BTCUSD.HAS`, `ETHUSD.HAS`[1]

## Integration Options

**CLI:** Primary interface for quick lookups, interactive workflows, and scripting with jq[1]. Commands like `longbridge quote SYMBOL.US`, `longbridge kline history`, `longbridge news`, `longbridge financial-statement` provide direct data access[1].

**Python SDK:** Sync/async HttpClient with QuoteContext (market data), TradeContext (orders/account), ContentContext (news/filings)[1]. Supports WebSocket subscriptions for real-time push events[1].

**Rust/Go SDKs:** Production-grade high-throughput alternatives with similar context patterns[1].

**MCP:** Hosted or self-hosted Model Context Protocol server for AI agent integration without code[1].

**LLMs.txt / Markdown API:** Live documentation at `open.longbridge.com` with `.md` suffix + Accept header for IDE/RAG integration[1].

## Related Topics

[[finance]]
[[agent-system]]
[[yfinance]] — Alternative market data source (US markets only, no HK/A-share/SG)