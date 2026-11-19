# Суправаджальны прыклад

Прыклад паказвае практычны noweb-падобны працэс для кананічнай літаратурнай крыніцы `primes.nw`.

## Мадэль крыніцы і канвеер

Машынная галіна: `primes.nw -> notangle -Rprogram -> primes.cpp -> g++ -> primes -> output.txt`. Чытэльным дакументам застаецца сам `primes.nw`; асобны PDF або HTML неабавязковы.

`primes.cpp` наўмысна захоўваецца ў Git як прыклад tangled-выніку і павінен дакладна адпавядаць крыніцы:

```bash
notangle -Rprogram primes.nw > /tmp/primes-from-noweb.cpp
diff -u primes.cpp /tmp/primes-from-noweb.cpp
```

Варыянт захоўвае іменаваныя фрагменты, тлумачальны парадак, каранёвы фрагмент і яўнае выманне машыннага кода. Гэта мінімальнае практычнае ядро літаратурнага праграмавання без абавязковых CWEB-маркераў, `cweave`, TeX-макрасаў і PDF-этапу.

## Машынная галіна

```bash
notangle -Rprogram primes.nw > /tmp/primes-from-noweb.cpp
diff -u primes.cpp /tmp/primes-from-noweb.cpp
g++ -std=c++17 -Wall -Wextra -pedantic primes.cpp -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Чаканыя маркеры: `The First 1000 Prime Numbers --- Page 1`, `The First 1000 Prime Numbers --- Page 5` і апошні радок `      6571      6997      7499      7919`.

## Неабавязковая дакументная галіна

Класічны noweb мае `noweave`: `primes.nw -> noweave -> TeX/LaTeX/HTML`. Гэты прыклад дэманструе палегчаны tangle-only шлях, дзе чытаецца зыходны `.nw`.

## Сінтаксіс фрагментаў

- `<<program>>=` вызначае фрагмент `program`.
- `<<name>>` спасылаецца на іншы фрагмент.
- `@` завяршае бягучы фрагмент.
- `notangle -Rprogram` выбірае корань `program`.
- `notangle` разгортвае спасылкі ў звычайны C++; кампілятар атрымлівае толькі `primes.cpp`.

## Арганізацыя тлумачэння і месца ў наборы

Звычайны каментар далучае тлумачэнне да кода. Noweb арганізуе код у тлумачальнай крыніцы іменаванымі фрагментамі ў чытацкім парадку, пасля чаго `notangle` збірае машынны парадак. Такая форма мае меншыя накладныя выдаткі, чым поўны CWEB, і нагадвае Markdown-блокі, дакументацыйныя прыклады, ячэйкі нататнікаў і выканальныя дакументы. Яна прыдатная малым дэманстрацыям, алгарытмічным нататкам, навучанню і вузкім эталонным рэалізацыям.

CWEB захоўвае гістарычную блізкасць да Кнута і поўны tangle/weave. `02-noweb-like` служыць асноўным мінімальным C++-прыкладам гэтага набору. Агульная табліца параўнання — у каранёвым README.

## Усталяванне: Debian/Ubuntu/WSL

Працэс Unix-падобны; на Windows выкарыстоўваецца WSL.

```bash
sudo apt update
sudo apt install noweb build-essential
```

Праверка:

```bash
command -v notangle
command -v noweave
```

Неабавязкова:

```bash
notangle -V
```

Асноўная праверка — шлях ад `command -v notangle`. Noweb можа адсутнічаць у стандартнай сістэме. Рэкамендуюцца пакеты АС: upstream таксама раіць іх, бо старая зборка з крыніц можа быць складанай і нестабільнай.

Пры сумеснай працы Windows/WSL CRLF у `.nw` можа дадаць CR у вывад і шум у diff. Захоўвайце LF у `.nw` і `.cpp`:

```bash
sed -i 's/\r$//' primes.nw
notangle -Rprogram primes.nw > primes.cpp
```

Лакальны `.gitattributes` падтрымлівае LF.

## Файлы

`COMPANION.md` і `primes.nw` — захаваныя крыніцы. `primes.cpp` — наўмысна захаваны tangled-прыклад; яго змена патрабуе рэгенерацыі і сінхранізацыі. `primes` і `output.txt` — лакальныя ігнараваныя вынікі. Абавязковы працэс не стварае `primes.tex` і `primes.pdf`.

Аўтар noweb — Norman Ramsey. Прыклад арыентуецца на практычную лінейку noweb 2.x з Debian/Ubuntu. Noweb3 — невыдадзеная Lua-alpha, якая тут не выкарыстоўваецца.

## Крыніцы і падзякі

- Main repository: <https://github.com/nrnrnr/noweb>.
- Note only (not recommended for this companion): <https://github.com/nrnrnr/noweb3> is a never-released alpha Lua-based reimplementation and is not used here.
