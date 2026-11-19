# Суправаджальны прыклад

Org Babel арганізуе літаратурны працэс вакол адной кананічнай тэкставай крыніцы `primes.org`.

## Крыніца і канвеер

`primes.org -> emacs --batch / org-babel-tangle -> primes.cpp -> g++ -> primes -> output.txt`.

`primes.cpp` — лакальны згенераваны артэфакт, звычайна ігнараваны, калі яго асобна не захоўваюць для дэманстрацыі. Кампілятар бачыць толькі C++, без Org-маркераў.

Emacs — праграмуемы рэдактар і пашыральнае тэкставае асяроддзе; тут ён таксама пакетны працэсар. Org-mode задае структураваныя тэкставыя дакументы. Org Babel адказвае за назвы блокаў, спасылкі, tangling, выкананне і экспарт.

## Машынная галіна: WSL

```bash
emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")'
g++ -std=c++17 -Wall -Wextra -pedantic primes.cpp -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Маркеры поспеху: `Tangled 1 code block from primes.org`, загалоўкі `The First 1000 Prime Numbers --- Page 1` і `The First 1000 Prime Numbers --- Page 5`, апошнія значэнні `6571`, `6997`, `7499`, `7919`.

## Экспарт і сінтаксіс

Org-mode экспартуе дакументы ў чытэльныя фарматы. Гэты прыклад правярае tangling і зборку; экспарт належыць шырэйшай экасістэме і для smoke-check простых лікаў неабавязковы.

- `* Heading` утварае структуру дакумента.
- `#+name: constants` называе блок.
- `#+begin_src cpp` і `#+end_src` абмяжоўваюць C++-блок.
- `:tangle primes.cpp` задае мэтавы файл.
- `:noweb yes` уключае разгортванне спасылак.
- `<<constants>>` спасылаецца на іменаваны блок.
- `org-babel-tangle-file` разгортвае спасылкі і запісвае код.

Звычайны каментар далучае тлумачэнне да кода. Org Babel змяшчае іменаваныя блокі ў структураваны тлумачальны дакумент у зручным чытачу парадку і вымае машынную крыніцу праз tangling. `03-org-babel` асабліва карысны пры прынятым Emacs/Org-mode; мінімальны C++-шлях паказаны ў `02-noweb-like`, гістарычны tangle/weave — у `01-cweb`. Параўнанне — у каранёвым README.

## Усталяванне: WSL/Linux

```bash
sudo apt update
sudo apt install emacs-nox build-essential
```

Графічны варыянт:

```bash
sudo apt install emacs build-essential
```

Праверка:

```bash
command -v emacs
emacs --version
g++ --version
```

Зыходны прыклад правяраўся ў Debian/Ubuntu-падобным WSL з Emacs 29.3; паспяховы пакетны вывад — `Tangled 1 code block from primes.org`. Залежнасці пакета могуць адкрыць дыялог Postfix. Паштовы сервер прыкладу не патрэбны: выбірайце `No configuration`.

## Windows і рэдактары

GNU Emacs даступны як усталёўшчык і ZIP; прамы каталог — <https://ftp.gnu.org/gnu/emacs/windows/>. ZIP дазваляе запускаць `bin\runemacs.exe`. Для PowerShell патрэбны Emacs у PATH:

```powershell
where.exe emacs
emacs --version
```

Пры адсутнасці дадайце `bin` у PATH або выкарыстоўвайце поўны шлях:

```powershell
& "C:\path\to\emacs\bin\emacs.exe" --batch primes.org -l org -l ob-tangle --eval "(org-babel-tangle-file \"primes.org\")"
```

Натыўная кампіляцыя дадаткова патрабуе C++-інструментаў, напрыклад MSYS2/MinGW-w64 або Visual Studio Build Tools. Асноўны апісаны шлях поўнай праверкі — WSL/Linux. Іншыя рэдактары, уключаючы VS Code з Org-пашырэннямі, прыдатныя для рэдагавання; узнаўляльную апрацоўку выконвае пакетны Emacs.

## Дыягностыка

Магчыма пачатковае паведамленне:

```text
Could not read ‘org-id-locations’ from ~/.emacs.d/.org-id-locations, setting it to nil
```

Яно азначае адсутнасць лакальнага кэша Org ID і само па сабе зборку не спыняе. Правярайце маркер `Tangled 1 code block from primes.org`. Пры CR-артэфактах захоўвайце `.org` і `.cpp` з LF:

```bash
sed -i 's/\r$//' primes.org
emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")'
```

## Файлы

`COMPANION.md` і `primes.org` захоўваюцца як крыніцы. `primes.cpp` атрымліваецца tangling і ігнаруецца, калі асобна не прыняты для дэманстрацыі; `primes` і `output.txt` — ігнараваныя вынікі кампіляцыі і smoke-check.

## Крыніцы і падзякі

- GNU Emacs download: <https://www.gnu.org/software/emacs/download.html>
- GNU Emacs Windows FTP directory: <https://ftp.gnu.org/gnu/emacs/windows/>
- Org manual, extracting source code: <https://orgmode.org/manual/Extracting-Source-Code.html>
- Comparative CWEB reference: Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
