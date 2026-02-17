# Skill: Quarto/tidyverse compliance

**Agent:** octavius  
**Index:** `docs/agent-skills.md` § octavius

## Source

Agent body (Octavius coding standards: Quarto integration, tidyverse orthodoxy, tidymodels, chunk options, reproducibility).

## When to use

All R/Quarto code and documents. Every code chunk and document must follow the standards defined in the Octavius agent file.

## Fallback

Follow existing body text; no separate fallback. If in doubt, prefer tidyverse syntax, proper chunk options, and reproducible setup (seeds, `here::here()`, package version notes).

## Procedure

1. Use `.qmd` with correct YAML and chunk options (`#| label:`, `#| echo:`, etc.).
2. Use tidyverse (dplyr, tidyr, ggplot2, purrr, readr, stringr, forcats, lubridate) and tidymodels where applicable.
3. Set seeds, document packages, use `here::here()` for paths.
4. No placeholder code; all code runnable and reproducible.
