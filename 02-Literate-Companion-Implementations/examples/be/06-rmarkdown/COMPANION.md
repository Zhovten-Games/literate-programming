# Суправаджальны прыклад

## 1. Уводзіны

R Markdown прадстаўляе ўзнаўляльную справаздачу. Кананічны `primes.Rmd` сумяшчае Markdown-тэкст і выканальныя R-фрагменты; рэндэрынг выконвае іх і стварае `primes.html`.

## 2. Крыніца і канвеер

`primes.Rmd -> rmarkdown::render() -> knitr -> pandoc -> primes.html`.

R — мова і асяроддзе выканання; `knitr` запускае блокі і рыхтуе прамежкавы Markdown; пакет `rmarkdown` каардынуе працэс; Pandoc ператварае дакумент у HTML або іншы фармат. RStudio ад Posit — неабавязковы IDE/GUI. Для CLI ён не патрэбны. Галоўны вынік — публікуемая справаздача, а `primes.html` з'яўляецца згенераваным файлам. Канвеер адрозніваецца ад вымання машыннай крыніцы ў першых трох прыкладах і інтэрактыўнага аўтарства Jupyter.

## 3. Рэндэрынг

З бягучага каталога:

```bash
Rscript -e 'rmarkdown::render("primes.Rmd")'
grep "Page 1" primes.html && grep "Page 5" primes.html && grep "7919" primes.html
```

Чаканыя маркеры: `The First 1000 Prime Numbers --- Page 1`, `The First 1000 Prime Numbers --- Page 5`, `6571      6997      7499      7919`. `knitr` можа дадаваць прэфікс `##` у кансольны вывад HTML — гэта нармальна.

Пры зыходнай ручной праверцы выкарыстоўваліся `rmarkdown` 2.31 і Pandoc 3.1.3. Гэта назіраныя версіі, а не мінімальныя патрабаванні.

## 4. Тлумачэнне і месца ў наборы

Звычайны каментар тлумачыць код. R Markdown змяшчае апавяданне, выканальныя блокі і вынікі ў адной крыніцы справаздачы. `06-rmarkdown` карысны справаздачам, статыстычным дакументам і вылічальным апавяданням. Яго асноўная функцыя — узнаўляльная публікацыя. Параўнанне ўсіх варыянтаў — у каранёвым README.

## 5. Усталяванне: лакальная `.rlib`

Апісаны шлях — чыстае WSL/Linux-асяроддзе з праектнай бібліятэкай пакетаў. З кораня набору:

```bash
sudo apt update
sudo apt install -y r-base r-base-dev pandoc libuv1-dev

mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"

Rscript -e '.libPaths()'
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

Праверка:

```bash
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
Rscript -e 'rmarkdown::pandoc_version()'
```

Чаканы шлях бібліятэкі:

```text
.../Literate-Companion-Implementations/.rlib
```

`install.packages()` з'яўляецца сінтаксісам R і запускаецца праз `Rscript -e`, а не непасрэдна Bash. Праект выкарыстоўвае лакальную `.rlib`; сістэмная `/usr/local/lib/R/site-library` можа быць недаступнай для запісу. `R_LIBS_USER` дзейнічае толькі ў бягучай сесіі і экспартуецца зноў пасля адкрыцця тэрмінала:

```bash
cd "/path/to/Literate-Companion-Implementations"
export R_LIBS_USER="$PWD/.rlib"
Rscript -e '.libPaths()'
Rscript -e 'packageVersion("rmarkdown")'
```

Залежнасці CRAN могуць утварыць ланцуг `fs -> sass -> bslib -> rmarkdown`, для якога патрэбны `libuv1-dev`. HTML патрабуе Pandoc; LaTeX/TinyTeX патрэбны толькі пры даданні PDF.

## 6. Windows

Натыўны Windows патрабуе R, пакета `rmarkdown` і Pandoc у PATH. RStudio зручны для рэдагавання, але CLI працуе асобна.

```powershell
where.exe Rscript
Rscript --version
Rscript -e "packageVersion('rmarkdown')"
Rscript -e "rmarkdown::pandoc_version()"
```

Асноўны апісаны шлях — WSL/Linux з каранёвай `.rlib`.

## 7. Дыягностыка

Памылковы выклік у Bash:

```bash
install.packages("rmarkdown")
```

Правільны выклік R:

```bash
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

Пры недаступнай сістэмнай бібліятэцы паведамленне выглядае так:

```text
'lib = "/usr/local/lib/R/site-library"' is not writable
```

Выкарыстоўвайце лакальную:

```bash
mkdir -p .rlib
export R_LIBS_USER="$PWD/.rlib"
```

Калі пасля новага тэрмінала пакет знік, паўтарыце экспарт `R_LIBS_USER` і праверку `.libPaths()`. Пры памылцы зборкі `fs` з адсутным libuv:

```bash
sudo apt install -y libuv1-dev
rm -rf .rlib/00LOCK-*
Rscript -e 'install.packages("rmarkdown", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cloud.r-project.org")'
```

Пры адсутнасці Pandoc:

```bash
sudo apt install -y pandoc
command -v pandoc
pandoc --version
Rscript -e 'rmarkdown::pandoc_version()'
```

## 8. Файлы

`COMPANION.md` і `primes.Rmd` — захаваныя крыніцы. `primes.html` — згенераваная справаздача. `primes.knit.md` — магчымы прамежкавы Markdown, які можа выдаляцца пасля рэндэрынгу. `*_files/` утрымлівае дапаможныя рэсурсы. Гэтыя вынікі, `.rlib/`, `.Rhistory`, `.RData`, `.Rproj.user/` ігнаруюцца і не ўключаюцца ў каміт.

## Крыніцы і падзякі

- R Markdown documentation: <https://rmarkdown.rstudio.com/>
- R Markdown lesson / guide: <https://rmarkdown.rstudio.com/lesson-1.html>
- R Markdown render documentation: <https://rmarkdown.rstudio.com/docs/reference/render.html>
- knitr documentation: <https://yihui.org/knitr/>
- Pandoc: <https://pandoc.org/>
- Posit / RStudio IDE: <https://posit.co/products/open-source/rstudio/>
- Comparative CWEB reference: Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
