# Суправаджальны прыклад

Quarto — сістэма выканальных дакументаў. `primes.qmd` ператвараецца ў `primes.html`: Quarto выконвае Python-код і выкарыстоўвае дакументны канвеер для HTML.

## Крыніца і канвеер

`primes.qmd -> Quarto render -> Python/Jupyter kernel -> Pandoc -> primes.html`.

`.qmd` аб'ядноўвае Markdown, YAML-метаданыя і выканальныя блокі. Кананічная крыніца — `primes.qmd`, HTML — згенераваная публікацыя. У `01-cweb`, `02-noweb-like`, `03-org-babel` перад кампіляцыяй збіраецца машынная крыніца; тут галоўны вынік — апублікаваны дакумент з тэкстам, кодам і вылічэннямі.

## Рэндэрынг

З бягучага каталога:

```bash
quarto render primes.qmd
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Чаканыя маркеры ў HTML: `The First 1000 Prime Numbers --- Page 1`, `The First 1000 Prime Numbers --- Page 5` і `      6571      6997      7499      7919`. Smoke-check шукае іх у HTML.

YAML паміж `---` задае назву, фармат і параметры выканання. Markdown утварае апавядальны слой. Блок з `{python}` выконваецца пры рэндэрынгу, а яго вывад устаўляецца ў HTML; тут гэта старонкавая табліца простых лікаў.

## Месца ў наборы

Звычайны каментар тлумачыць код. Quarto ўбудоўвае вылічэнне ў прыдатны да публікацыі дакумент. Варыянт `04-quarto` карысны для сумеснага прадстаўлення тэксту, кода і выніку. Для мінімальнага C++-вымання крыніцы глядзіце `02-noweb-like`, гістарычнага tangle/weave — `01-cweb`, Emacs/Org-mode — `03-org-babel`. Агульная табліца — у каранёвым README.

## Усталяванне: WSL/Linux

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

З афіцыйнай старонкі Quarto вазьміце адпаведны Ubuntu/Debian `.deb`:

```bash
cd /tmp
wget https://github.com/quarto-dev/quarto-cli/releases/download/vX.Y.Z/quarto-X.Y.Z-linux-amd64.deb
sudo apt install ./quarto-X.Y.Z-linux-amd64.deb
quarto --version
```

Замяніце `X.Y.Z` версіяй выбранага афіцыйнага выпуску.

## Агульнае асяроддзе Python/Jupyter

У корані `Literate-Companion-Implementations` стварыце агульны `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter
```

Праверка:

```bash
which python
python -m jupyter --version
```

Чаканы шлях Python: `.../Literate-Companion-Implementations/.venv/bin/python`. Адно асяроддзе можа абслугоўваць `examples/en/04-quarto`, `examples/ru/04-quarto`, `examples/uk/04-quarto`, `examples/be/04-quarto`, а таксама Jupyter-прыклад. З актыўнага асяроддзя паўтарыце каманду рэндэрынгу ў кожнай галінцы.

## Windows і дыягностыка

Натыўны Windows магчымы пры ўсталяваных Quarto і Python/Jupyter у PATH. Асноўны апісаны шлях — WSL/Linux.

```powershell
where.exe quarto
quarto --version
where.exe python
python --version
python -m jupyter --version
```

Паспяховы вывад — `Output created: primes.html`. Пры праблемах Windows/WSL захоўвайце `.qmd` з LF. `primes.quarto_ipynb` можа з’яўляцца прамежкавым файлам і ігнаруецца.

Пры адсутнасці Quarto дадайце яго ў PATH. Памылкі Jupyter або Python правярайце пасля актывацыі `.venv` праз `which python` і `python -m jupyter --version`. HTML-праверка павінна чытаць вынік рэндэрынгу. Для HTML LaTeX не патрэбны; PDF патрабуе асобнай налады TeX.

## Файлы

`COMPANION.md` і `primes.qmd` — захаваныя крыніцы. `primes.html` — ігнараваны HTML-вынік. Дапаможныя `primes_files/`, кэш `.quarto/` і агульны `.venv/` таксама з'яўляюцца лакальнымі згенераванымі матэрыяламі.

## Крыніцы і падзякі

- Quarto official site and docs: <https://quarto.org/>
- Quarto download page: <https://quarto.org/docs/download/>
- Quarto Python computations: <https://quarto.org/docs/computations/python.html>
- Comparative CWEB reference: Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
