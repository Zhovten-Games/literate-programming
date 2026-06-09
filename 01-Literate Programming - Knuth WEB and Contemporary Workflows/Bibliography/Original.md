# Bibliography inventory (Goal 1)

## 1) Scanned source zones

1. Main article and drafts:
- `at-work/Статья2/Обзор статьи Кнута.md`
- `at-work/Статья2/Literate Programming/knuth-lp-ru.md`
- `at-work/Статья2/Literate Programming/Литеральное программирование и LLM.md`
- `at-work/Статья2/Literate Programming/Влияние статьи “Literate Programming” и системы WEB на вычислительную практику и программную инженерию.md`

2. Research source folder:
- `at-work/Статья2/Literate Programming/*`

3. Companion implementation docs:
- `at-work/Статья2/Literate-Companion-Implementations/README.md`
- `at-work/Статья2/Literate-Companion-Implementations/examples/en/README.md`
- `at-work/Статья2/Literate-Companion-Implementations/examples/ru/README.md`
- all `examples/en/*/COMPANION.md` and `examples/ru/*/COMPANION.md` for:
  - `01-cweb`
  - `02-noweb-like`
  - `03-org-babel`
  - `04-quarto`
  - `05-jupyter`
  - `06-rmarkdown`

4. Existing bibliography/build-pipeline examples (format model only):
- `at-work/Статья2/Primer/01-Language as Infection - Media Communication as a Mechanism of Harm/authors.yml`

## 2) Proposed bibliography sections

A. Primary Knuth / WEB / CWEB sources  
B. Direct literate-programming tools and descendants  
C. Executable documents / reproducible research / notebook lineage  
D. Companion implementation and internal project materials  
E. LLM / vibe coding / AI-assisted programming  
F. AI governance / standards / provenance  
G. Build and publishing pipeline references

## 3) Raw source candidates and proposed keys

### A. Primary Knuth / WEB / CWEB
- `knuth1984a` — Donald E. Knuth, "Literate Programming" (The Computer Journal / DOI record). URL: TODO DOI URL verification.
- `knuth1992a` — Knuth & Levy, "The CWEB System of Structured Documentation". URL: https://www-cs-faculty.stanford.edu/~knuth/cweb.html
- `knuthweb1983a` — Knuth WEB page/resources. URL: TODO verify canonical page URL.

### B. Direct literate-programming tools and descendants
- `ramsey1994a` — noweb by Norman Ramsey. URL: https://github.com/nrnrnr/noweb
- `ramseyNoweb3Alpha2000a` — noweb3 note (alpha, never released). URL: https://github.com/nrnrnr/noweb3 (context only)
- `orgmanualExtractingSourceCode` — Org manual, extracting source code. URL: https://orgmode.org/manual/Extracting-Source-Code.html
- `gnuEmacsDownload` — GNU Emacs download page. URL: https://www.gnu.org/software/emacs/download.html

### C. Executable documents / reproducible research / notebooks
- `quartoDocs` — Quarto documentation. URL: TODO add official docs URL from Quarto companion.
- `jupyterDocs` — Project Jupyter documentation. URL: https://docs.jupyter.org/
- `jupyterlabDocs` — JupyterLab docs. URL: https://jupyterlab.readthedocs.io/en/stable/
- `jupyterNotebookDocs` — Jupyter Notebook docs. URL: https://jupyter-notebook.readthedocs.io/en/stable/notebook.html
- `nbconvertDocs` — nbconvert docs. URL: https://nbconvert.readthedocs.io/
- `nbconvertExecuteApi` — nbconvert execute API. URL: https://nbconvert.readthedocs.io/en/latest/execute_api.html
- `rmarkdownDocs` — R Markdown docs. URL: https://rmarkdown.rstudio.com/
- `rmarkdownRender` — render reference. URL: https://rmarkdown.rstudio.com/docs/reference/render.html
- `knitrDocs` — knitr docs. URL: https://yihui.org/knitr/
- `pandocDocs` — Pandoc docs. URL: https://pandoc.org/
- `positRstudio` — Posit / RStudio. URL: https://posit.co/products/open-source/rstudio/

### D. Internal / companion project materials
- `twocanonCompanionRoot2026` — local companion root README.
- `twocanonCompanionRu2026` — local companion RU README.
- `twocanonCompanionEn2026` — local companion EN README.
- `twocanonCompanion01cweb2026` ... `twocanonCompanion06rmarkdown2026` — each RU/EN `COMPANION.md` as internal references.

### E. LLM / AI-assisted programming
- `vscodeCopilotCustomInstructions` — VS Code Copilot customization docs. URL: https://code.visualstudio.com/docs/copilot/copilot-customization
- `githubCopilotCustomization` — GitHub Copilot customization docs. URL: https://docs.github.com/en/copilot/how-tos/custom-instructions
- `vibecodingKarpathy2025` — Wikipedia vibe-coding page. URL: https://en.wikipedia.org/wiki/Vibe_coding (weak source, TODO: replace with stronger primary source before final publication)

### F. Governance / provenance (contextual)
- `euAiAct` — EU AI Act primary text / official portal. URL: TODO.
- `euCodeOfPracticeGpai` — EU Code of Practice for GPAI. URL: TODO.
- `c2paSpec` — C2PA specification site. URL: TODO.
- `openaiProvenance` — OpenAI provenance/material authenticity notes. URL: TODO.

### G. Build/publishing pipeline references (if used)
- `pandocCiteproc` — Pandoc citations pipeline docs. URL: TODO.
- `cslSpec` — CSL reference. URL: TODO.

## 4) Duplicate candidates
- `https://www-cs-faculty.stanford.edu/~knuth/cweb.html` appears in multiple companion files; keep one canonical entry `knuth1992a`.
- `https://nbconvert.readthedocs.io/` and execute API subpage should remain separate entries.
- R Markdown docs and render reference are related but non-duplicates.

## 5) Excluded as topic sources (pipeline examples only)
- ZG horror/media bibliography JSON files from "Language as Infection" folder are excluded from Knuth-topic bibliography.
- `Primer/.../authors.yml` is used only as structure model, not as topic source.

## 6) TODO metadata checklist
- Verify secondary publication metadata fields for Knuth 1984 article beyond DOI/URL (DOI and stable URL were added).
- Verify official WEB page URL and archival stability.
- Collect Quarto official docs URL from companion materials.
- Add precise publication years for tool docs where meaningful.
- Confirm governance/provenance links only if they are actually cited in final conclusion.

## 7) Which sources should become JSON entries later
- All A/B/C high-confidence external sources.
- E/F only if corresponding conclusion sections remain in article scope.
- D internal sources should be kept as clearly marked project/internal references.

## 8) Scaffold status note (Goal 1.1)
- Draft JSON bibliography files were intentionally deferred and removed at this stage.
- They will be recreated during the final bibliography wiring step from approved inventory data.
- `Original.md` is the current inventory source of truth for bibliography planning.
- The final PDF/build pipeline will use the external `zg-journal-template`, not a custom local build pipeline inside this folder.

## 9) Goal 8 status
- Sectioned bibliography JSON files were recreated from high-confidence inventory entries.
- Uncertain metadata remains marked as `TODO` and was not invented.
- `openaiCustomInstructions` was replaced by VS Code / GitHub Copilot customization references for LLM customization claims.
- OpenAI custom instructions should not be used for this claim unless an actual OpenAI source is explicitly cited.
- Added verified entries: `gamma1994designPatterns` and `martin2017cleanArchitecture` for section A historical framing.
- Added verified entry `dijkstra1972notes` for structured-programming context (with chapter metadata and archival note).
