---
title: "Inelastic Markets Hypothesis"
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [finance, asset-pricing, behavioral-finance]
sources:
  - type: paper
    url: "https://www.nber.org/papers/w28967"
    title: "In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis"
    authors: ["Xavier Gabaix", "Ralph S.J. Koijen"]
    date: "June 2021"
---

# Inelastic Markets Hypothesis

## Overview

The **Inelastic Markets Hypothesis** proposes that the aggregate stock market demand has surprisingly low price elasticity (ζ ≈ 0.2), meaning capital flows in and out of equities have a significant amplified impact on prices and risk premia [1]. A $1 inflow leads to approximately a $5 increase in aggregate market value [1].

## Key Parameters

- **Macro demand elasticity (ζ)**: ~0.16–0.20 [1]
- **Multiplier (M = 1/ζ)**: ~5–7x [1]
- **Flow volatility contribution**: ~89% of stock return variance [1]
- **Fundamental risk contribution**: ~11% of stock return variance [1]

## Core Mechanism

Most institutional investors operate under fixed-share mandates (e.g., 60/40 portfolios), mechanically rebalancing regardless of price changes. This creates inelastic demand [1]:

**Demand equation**: q = ζp + f [1]

Where q is quantity demanded, p is price change, f is the flow shock, and ζ is the low elasticity parameter [1].

## Key Findings

- **Price impact multiplier**: $1 capital flow → ~$5 market value increase [1]
- **Sector-specific shocks** explain 16% of aggregate price variation (R²) [1]
- **Persistent flows** lead to persistent price deviations — no mean reversion at quarterly frequency [1]
- **Share buybacks** can increase aggregate equity valuations by violating Modigliani-Miller neutrality in inelastic markets [1]
- **Government QE in equities**: 1% government purchase → ~5% market increase (consistent with Hong Kong 1998 intervention: 6% purchase → 24% abnormal return) [1]

## Implications for Finance Tenets

**"Permanent price impact must reflect information"** — False. Non-informational flows permanently change prices in inelastic markets [1].

**"Fast and smart investors provide enough elasticity"** — False. Hedge funds own <5% of the market, insufficient to provide macro elasticity despite micro efficiency [1].

**"High trading volume implies elastic markets"** — False. Most volume exchanges one share for another; aggregate flow f measures net bonds-to-equities movement [1].

**"For every buyer there is a seller"** — Misleading. Buying pressure f is measurable via change in asset holdings (bonds vs equities) and does move prices by p = f/ζ [1].

## General Equilibrium Model

The calibrated model matches key moments [1]:
- Risk-free rate: 1%
- Average equity premium: 4.4%
- Dividend-price ratio: 3.4%
- Stock return volatility: 15%
- Flow persistence (φ): 4%/year mean reversion

## Identification Strategy

Uses **Granular Instrumental Variables (GIV)** — a method developed by Gabaix & Koijen (2020) to isolate sector-specific demand shocks from common factors [1]. Data sources include:

1. Federal Reserve Flow of Funds (FoF) data (1993–2018)
2. 13F institutional investor filings + mutual fund flows (2000–2019)

## Related Concepts

- [[Xavier Gabaix]] — Co-author, Harvard University/MIT
- [[Ralph Koijen]] — Co-author, UCLA Anderson School of Management
- Behavioral finance and bounded rationality in asset pricing
- Demand-based asset pricing models (Koijen & Yogo 2019)
