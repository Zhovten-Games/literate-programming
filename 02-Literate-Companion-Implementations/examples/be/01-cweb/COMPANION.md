# Суправаджальны прыклад

Прыклад паказвае практычны CWEB-працэс для аднаго літаратурнага файла `primes.w`.

## Дзве галіны канвеера

Машынная галіна: `primes.w -> ctangle -> primes.c -> cc/gcc -> primes -> output.txt`.

Чытацкая галіна: `primes.w -> cweave -> primes.tex -> pdftex -> primes.pdf`.

## Машынная галіна

```bash
ctangle primes.w
cc -Wall -Wextra -pedantic primes.c -o primes
./primes > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

`ctangle` разгортвае спасылкі на CWEB-секцыі і стварае звычайны C у `primes.c`. Кампілятар атрымлівае толькі гэты C-код.

## Чытацкая галіна

```bash
cweave primes.w
pdftex primes.tex
```

З той жа крыніцы атрымліваецца чытэльны дакумент `primes.pdf`.

## Маркеры CWEB

- `@` — кіравальны прэфікс.
- `@*` пачынае буйную секцыю дакумента.
- `@c` пачынае праграмны фрагмент для `ctangle`.
- `@<Section name@>` спасылаецца на іменаваны фрагмент.
- `@ @<Section name@>=` вызначае фрагмент.
- `ctangle` падстаўляе азначэнні замест спасылак і стварае звычайны C; C-кампілятар маркераў CWEB не бачыць.

## Арганізацыя тлумачэння

Звычайны каментар далучае тлумачэнне да кода і пераважна захоўвае праграмны парадак. CWEB арганізуе код унутры тлумачальнай крыніцы: фрагменты ўводзяцца ў парадку чалавечага разумення, а `ctangle` збірае машынны парадак.

`01-cweb` — гістарычны шлях для сямейства C, блізкі да ідэі WEB Кнута, з поўным падзелам tangle/weave. Параўнанне ўсіх варыянтаў знаходзіцца ў каранёвым README.

## Усталяванне: Debian/Ubuntu/WSL

Працэс арыентаваны на Unix-падобнае асяроддзе; для Windows практычны варыянт — WSL.

```bash
sudo apt update
sudo apt install texlive-binaries build-essential
```

Праверка інструментаў:

```bash
command -v ctangle
command -v cweave
ctangle --version
```

Пры стварэнні PDF магчыма паведамленне:

```text
I can't find file `cwebmac`.
```

Выпраўленне, праверанае ў Debian/Ubuntu/WSL:

```bash
sudo apt install texlive-extra-utils texlive-formats-extra
kpsewhich cwebmac.tex
```

Паўторная зборка:

```bash
cweave primes.w
pdftex primes.tex
```

Назвы пакетаў адпавядаюць апісанаму асяроддзю і могуць адрознівацца ў іншых дыстрыбутывах.

## Файлы і вынікі

| Файл | Роля |
| --- | --- |
| `COMPANION.md` | Гэтая дакументацыя; захоўваецца ў Git |
| `primes.w` | Кананічная CWEB-крыніца; захоўваецца ў Git |
| `primes.c` | C-код ад `ctangle`; ручное рэдагаванне забаронена |
| `primes` | Скампіляваная праграма |
| `output.txt` | Лакальны вывад для smoke-check |
| `primes.tex` | TeX-крыніца ад `cweave` |
| `primes.pdf` | Чытэльны PDF ад `pdftex` |
| `primes.idx`, `primes.scn`, `primes.toc` | Індэкс, секцыі і змест weave/PDF |
| `primes.log` | Журнал TeX |

Усе згенераваныя файлы выключаюцца лакальным `.gitignore`. Асноўныя аўтары CWEB — Donald E. Knuth і Silvio Levy; сучасная распрацоўка паказана ў вывадзе TeX Live `CTANGLE`.

## Крыніцы і падзякі

- Contemporary development is referenced by the TeX Live `CTANGLE` output at: <https://github.com/ascherer/cweb>.
- Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: <https://www-cs-faculty.stanford.edu/~knuth/cweb.html>
