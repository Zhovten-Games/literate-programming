# Companion

Quarto is an executable-document system. In this companion, `primes.qmd` is rendered into `primes.html`: Quarto executes the embedded Python code and then uses the document-rendering pipeline to produce HTML.

## Source model and compact pipeline

Quarto source:

- `primes.qmd`

Rendered publication branch:

- `primes.qmd -> Quarto render -> Python/Jupyter kernel -> Pandoc -> primes.html`

`primes.qmd` is the canonical Quarto source. `primes.html` is a generated rendered artifact. The output here is a publication-oriented document, not generated canonical program source. This differs from `01-cweb`, `02-noweb-like`, and `03-org-babel`, where a machine-oriented source file is generated or assembled before compilation.

## What Quarto / .qmd / executable documents are

- Quarto: executable document / computational publishing system
- `.qmd`: Markdown + YAML metadata + executable code blocks
- Python/Jupyter kernel: executes the embedded Python block
- Pandoc/render pipeline: produces `primes.html`

## Render branch commands

From this directory:

```bash
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Expected output markers include:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

The smoke-check searches inside rendered `primes.html`, not inside a plain output text file.

## Markers / document syntax

- YAML front matter between `---` lines defines metadata such as title, format, and execution options.
- Markdown prose is the readable narrative layer.
- A fenced code block with `{python}` starts an executable Python block.
- Quarto executes the code block during render.
- Output is embedded into rendered HTML.
- In this companion, the code prints the paginated prime table.

## Why not just comments?

Ordinary comments:

- explanation attached to code.

Quarto:

- computation embedded inside a publishable document.

CWEB/noweb/Org Babel keep a stronger source-generation framing where machine-oriented source is extracted or assembled. Quarto centers a rendered publication where prose, code, and computed output are published together.

## Place in the set

`04-quarto` shows the executable-document / computational-publishing branch. It is useful when the main goal is a rendered document that combines prose, code, and computed output. It is not the best example of strict WEB-style source generation. For the minimal C++ literate source-generation path, see `02-noweb-like`; for the historical tangle/weave model, see `01-cweb`; for an Emacs/Org-mode environment, see `03-org-babel`.

For the full comparison of all companion variants, see the root README / comparison table.

## Installation notes: primary WSL/Linux route

This companion was tested through a WSL/Linux route.

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Install Quarto from the official download page using the current Ubuntu/Debian `.deb` package:

```bash
cd /tmp
wget https://github.com/quarto-dev/quarto-cli/releases/download/vX.Y.Z/quarto-X.Y.Z-linux-amd64.deb
sudo apt install ./quarto-X.Y.Z-linux-amd64.deb
quarto --version
```

Replace `X.Y.Z` with the current version from the official Quarto download page.

## Python/Jupyter environment notes

The tested setup used one shared virtual environment at the root of `Literate-Companion-Implementations/.venv`.

From the `Literate-Companion-Implementations` root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter
```

Verification:

```bash
which python
python -m jupyter --version
```

Expected `which python` shape:

- `.../Literate-Companion-Implementations/.venv/bin/python`

The shared root `.venv` can be reused for `examples/en/04-quarto`, `examples/uk/04-quarto`, and `examples/ru/04-quarto`.

Smoke-check all three language branches:

```bash
cd examples/en/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html

cd ../../uk/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html

cd ../../ru/04-quarto
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Run `quarto render` from an activated `.venv` so Quarto can use Jupyter/Python packages installed there.

## Windows notes

Windows is possible but was not the primary tested route for this companion.

- Quarto has a Windows installer.
- Native Windows rendering can work if Quarto and Python/Jupyter are installed and available in `PATH`.

Checks:

```powershell
where.exe quarto
quarto --version
where.exe python
python --version
python -m jupyter --version
```

If tools are not found:

- add Quarto and Python to `PATH`;
- install Jupyter into the active Python environment.

For this companion, the reproducible tested route is WSL/Linux with a root `.venv`.

## Troubleshooting notes

- If Quarto cannot execute Python blocks, ensure `.venv` is activated and `jupyter` is installed.
- If `quarto render primes.qmd` succeeds, the key success marker is `Output created: primes.html`.
- If `grep` fails, inspect `primes.html` and confirm that code output is embedded.
- If Windows/WSL line endings cause issues, keep `.qmd` files with stable LF endings.

## Generated files

- `COMPANION.md`
  Documentation for this companion example. Committed source.
- `primes.qmd`
  Canonical Quarto source. Committed source.
- `primes.html`
  Rendered HTML output. Generated and ignored.
- `primes.quarto_ipynb`
  Possible Quarto execution intermediate. Generated and ignored if produced.
- `.quarto/`
  Possible local Quarto cache/state directory. Generated and ignored.
- `*_files/`
  Possible Quarto supporting files directory. Generated and ignored.
- `.venv/`
  Local shared Python virtual environment when created at root. Generated and ignored.

## Acknowledgements / references

- Quarto official site and docs: <https://quarto.org/>
- Quarto download page: <https://quarto.org/docs/download/>
- Quarto Python computations: <https://quarto.org/docs/computations/python.html>
- Comparative CWEB reference: Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
