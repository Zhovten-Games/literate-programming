# Companion

## 1. Short introduction

R Markdown demonstrates a reproducible-report workflow. In this companion, `primes.Rmd` is the canonical document source; rendering executes the R code chunk and produces `primes.html`.

This is a dynamic-document workflow: prose and executable chunks live in one source. It is not strict Knuth-style WEB and not a canonical tangle/weave source-generation pipeline.

## 2. Source model and compact pipeline

R Markdown source:

- `primes.Rmd`

Rendered report branch:

- `primes.Rmd -> rmarkdown::render() -> knitr -> pandoc -> primes.html`

Notes:

- `primes.Rmd` contains Markdown prose and executable R chunks.
- `rmarkdown::render()` drives the rendering process.
- `knitr` executes R chunks and prepares an intermediate Markdown representation.
- `pandoc` converts the intermediate document into HTML.
- `primes.html` is generated output and should not be committed.
- Unlike `01-cweb`, `02-noweb-like`, and `03-org-babel`, this companion does not generate a canonical machine-oriented source file.
- Unlike `05-jupyter`, this is not primarily an interactive notebook workflow; it is a renderable report workflow.

## 3. What R Markdown / Rmd / knitr / rmarkdown / Pandoc / RStudio are

- **R Markdown**: document format that combines Markdown prose and executable code chunks.
- **`.Rmd`**: R Markdown source file.
- **R**: programming language/runtime used for executable chunks in this companion.
- **`knitr`**: engine that executes chunks and injects results into the document.
- **`rmarkdown`**: R package that coordinates rendering.
- **Pandoc**: document conversion layer used by R Markdown for HTML and other formats.
- **RStudio (Posit)**: optional IDE/GUI for R and R Markdown. Useful, but not required for CLI verification.

Compact formula:

- R Markdown: Markdown + executable code chunks
- `.Rmd`: canonical R Markdown source file
- `knitr`: chunk execution and result insertion
- `rmarkdown::render()`: render entry point
- Pandoc: document conversion layer
- RStudio: optional IDE/GUI, not required for CLI verification

## 4. Render commands

From `examples/en/06-rmarkdown`:

```bash
Rscript -e 'rmarkdown::render("primes.Rmd")'
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Expected smoke-check markers:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `6571      6997      7499      7919`

Note: rendered R console output in HTML can be prefixed with `##` by `knitr`. This is normal.

The Ukrainian branch is included in the same render route and locale validation; run its documented render command to record publication evidence. Recorded manual render checks currently cover `examples/en/06-rmarkdown` and `examples/ru/06-rmarkdown`.

Observed successful versions during manual test:

- `rmarkdown`: `2.31`
- `rmarkdown::pandoc_version()`: `3.1.3`

These are tested versions, not minimum required versions.

## 5. Why not just comments?

Ordinary comments:

- explanation attached to code.

R Markdown:

- prose, executable R chunks, and rendered output live together in one report source.

Important difference: R Markdown is not mainly about extracting source code for a compiler. It is about generating a reproducible rendered report from a document that contains executable chunks.

Short formula:

- Ordinary comments: explanation attached to code.
- R Markdown: report contains explanation, executable chunks, and rendered results.

## 6. Place in the set

`06-rmarkdown` shows the reproducible-report branch of the companion set. It is useful for reports, statistical documents, and rendered computational narratives, but it is closer to document publication than to canonical WEB-style source generation. For the full comparison of all companion variants, see the root README.

## 7. Installation notes: local root `.rlib`

Documented route: clean WSL/Linux workflow with project-local package library.

From the `Literate-Companion-Implementations` root:

```bash
sudo apt update
sudo apt install -y r-base r-base-dev pandoc libuv1-dev

mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"

Rscript -e '.libPaths()'
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

Verification:

```bash
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
Rscript -e 'rmarkdown::pandoc_version()'
```

Expected `.libPaths()` includes:

```text
.../Literate-Companion-Implementations/.rlib
```

Practical notes:

1. Do not run `install.packages("rmarkdown")` directly in Bash; it is R syntax. Use `Rscript -e 'install.packages(...)'`.
2. Do not install project packages into the system R library (`/usr/local/lib/R/site-library` may be non-writable). Use local `.rlib`.
3. `R_LIBS_USER` is session-local. In a new terminal, run:
   ```bash
   cd "/path/to/Literate-Companion-Implementations"
   export R_LIBS_USER="$PWD/.rlib"
   ```
4. `libuv1-dev` may be needed because CRAN dependencies can include:
   ```text
   fs -> sass -> bslib -> rmarkdown
   ```
5. `pandoc` is required for HTML rendering:
   ```bash
   command -v pandoc
   pandoc --version
   Rscript -e 'rmarkdown::pandoc_version()'
   ```
6. HTML output is sufficient for this companion; LaTeX/TinyTeX is not required unless PDF output is added later.

## 8. Windows notes

Windows is possible but was not the primary tested route for this companion.

- R can be installed natively on Windows.
- RStudio is a convenient GUI/IDE for R Markdown, but not required for the documented CLI route.
- Tools must be available in `PATH`.
- Native Windows setup needs R, package `rmarkdown`, and Pandoc.

PowerShell checks:

```powershell
where.exe Rscript
Rscript --version
Rscript -e "packageVersion('rmarkdown')"
Rscript -e "rmarkdown::pandoc_version()"
```

For this companion, the reproducible tested route is WSL/Linux with local root `.rlib`.

## 9. Troubleshooting notes

### A. `install.packages` typed in Bash

Problem:

```bash
install.packages("rmarkdown")
```

This causes Bash syntax errors because `install.packages()` is R syntax.

Correct:

```bash
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

### B. System R library is not writable

Problem:

```text
'lib = "/usr/local/lib/R/site-library"' is not writable
```

Fix:

```bash
mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"
```

### C. Package not found after reopening terminal

Problem: `rmarkdown` was installed, but a later `Rscript -e 'packageVersion("rmarkdown")'` reports package not found.

Cause: `R_LIBS_USER` was not exported in the new shell session.

Fix:

```bash
cd "/path/to/Literate-Companion-Implementations"
export R_LIBS_USER="$PWD/.rlib"
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
```

### D. `fs` / `sass` / `bslib` / `rmarkdown` dependency failure

Problem: installation fails because `fs` cannot build and reports missing libuv.

Fix:

```bash
sudo apt install -y libuv1-dev
rm -rf .rlib/00LOCK-*
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

### E. Pandoc not found

Fix:

```bash
sudo apt install -y pandoc
command -v pandoc
pandoc --version
Rscript -e 'rmarkdown::pandoc_version()'
```

### F. Generated HTML

`primes.html` is generated output and should not be committed.

## 10. Generated files

- `COMPANION.md`  
  Documentation for this companion example. Committed source.
- `primes.Rmd`  
  Canonical R Markdown source. Committed source.
- `primes.html`  
  Rendered HTML generated by `rmarkdown::render("primes.Rmd")`. Generated and ignored.
- `primes.knit.md`  
  Possible intermediate Markdown generated by `knitr`/`rmarkdown` during rendering. Generated and ignored if it appears.
- `*_files/`  
  Possible supporting asset directory for rendered HTML. Generated and ignored.
- `.rlib/`  
  Local root R package library for this companion set. Generated and ignored.
- `.Rhistory`, `.RData`, `.Rproj.user/`  
  Local R/RStudio artifacts. Generated and ignored.

Note: `primes.knit.md` is a possible intermediate artifact; it may or may not remain after render.

## 11. Acknowledgements / references

- R Markdown documentation: <https://rmarkdown.rstudio.com/>
- R Markdown lesson / guide: <https://rmarkdown.rstudio.com/lesson-1.html>
- R Markdown render documentation: <https://rmarkdown.rstudio.com/docs/reference/render.html>
- knitr documentation: <https://yihui.org/knitr/>
- Pandoc: <https://pandoc.org/>
- Posit / RStudio IDE: <https://posit.co/products/open-source/rstudio/>
- Comparative CWEB reference: Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
