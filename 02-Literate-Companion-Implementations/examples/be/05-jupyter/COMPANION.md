# Суправаджальны прыклад

## 1. Уводзіны

Jupyter прадстаўляе літаратурныя вылічэнні ў інтэрактыўным нататніку: тэкст, кодавыя ячэйкі, стан выканання і вынікі знаходзяцца ў `.ipynb`. `primes.ipynb` — кананічны дакумент, `primes.py` — спадарожны скрыпт хуткай праверкі.

## 2. Крыніцы і канвеер

Выкананне нататніка: `primes.ipynb -> Jupyter kernel / nbconvert --execute -> primes.executed.ipynb`.

Скрыптавая праверка: `primes.py -> python3 -> output.txt`.

`.ipynb` — JSON з ячэйкамі, метаданымі, лічыльнікамі выканання і вывадам. Ядро выконвае код і захоўвае стан. JupyterLab і Notebook — браўзерныя асяроддзі працы. Згенераваны `primes.executed.ipynb` не ўключаецца ў каміт. Галоўны вынік — выкананы інтэрактыўны дакумент; кананічная машынная крыніца, як у першых трох прыкладах, тут не вымаецца. У параўнанні з Quarto асноўны аўтарскі інтэрфейс — нататнік.

## 3. Скрыптавая праверка

```bash
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Чаканыя маркеры: `The First 1000 Prime Numbers --- Page 1`, `The First 1000 Prime Numbers --- Page 5` і `      6571      6997      7499      7919`. Скрыпт правярае алгарытм і вывад; выкананне нататніка патрабуе асобнай каманды.

## 4. Выкананне нататніка

```bash
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb
```

Каманда працуе без графічнага інтэрфейсу і запісвае выкананыя ячэйкі. У JSON чакаюцца радкі `"The First 1000 Prime Numbers --- Page 1\n"`, `"The First 1000 Prime Numbers --- Page 5\n"` і `"      6571      6997      7499      7919\n"`. Для ўзнаўляльнай праверкі выкарыстоўвайце чыстае паслядоўнае выкананне зверху ўніз.

## 5. Графічнае асяроддзе

З кораня набору з актыўным `.venv`:

```bash
jupyter lab
```

або:

```bash
jupyter notebook
```

JupyterLab прапануе аглядальнік файлаў, укладкі, нататнікі, рэдактар і тэрмінал. Notebook — класічны інтэрфейс. У WSL сервер звычайна друкуе лакальны URL з токенам, які можна адкрыць у Windows-браўзеры. Графічная праца неабавязковая; узнаўляльная праверка выкарыстоўвае `nbconvert --execute`.

## 6. Тлумачэнне і рызыка стану

Jupyter арганізуе вылічэнне і тлумачэнне як інтэрактыўны дакумент. Звычайны каментар далучае тэкст да кода; нататнік сумяшчае апавяданне, выкананне і вынікі. Ячэйкі могуць запускацца па-за парадкам, таму бачная паслядоўнасць часам адрозніваецца ад фактычнай гісторыі. Гэта асноўная рызыка ўзнаўляльнасці.

`05-jupyter` карысны для даследаванняў, навучання, прататыпаў і бачнага вываду ячэек. Параўнанне ўсіх варыянтаў — у каранёвым README.

## 7. Агульны каранёвы `.venv`

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

Чаканы шлях — `.../Literate-Companion-Implementations/.venv/bin/python`. Той жа `.venv` прыдатны для Quarto. Паўтарайце скрыптавую і notebook-каманды ў `examples/en/05-jupyter`, `examples/ru/05-jupyter`, `examples/uk/05-jupyter`, `examples/be/05-jupyter`.

## 8. Windows

Натыўная праца патрабуе Python/Jupyter у PATH:

```powershell
where.exe python
python --version
python -m jupyter --version
```

Пры адсутнасці ўсталюйце Python, дадайце Python/Scripts у PATH і ўсталюйце Jupyter у актыўнае асяроддзе. Асноўны апісаны шлях — WSL/Linux з агульным `.venv`.

## 9. Дыягностыка

Магчыма папярэджанне:

```text
MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions.
```

Яно азначае адсутнасць стабільных ID ячэек паводле новых патрабаванняў `nbformat`. Даданне `id` кожнай ячэйцы прыбірае прычыну папярэджання.

Калі інтэрактыўны запуск працуе, а `nbconvert --execute` — не, праверце схаваны стан і парадак ячэек. Пры адсутнасці ядра або Jupyter актывуйце `.venv`, праверце ўсталяванне і выканайце `python -m jupyter --version`.

## 10. Файлы

`COMPANION.md`, `primes.ipynb`, `primes.py` захоўваюцца ў Git. `output.txt` і `primes.executed.ipynb` — ігнараваныя вынікі. `.ipynb_checkpoints/` — лакальныя кантрольныя копіі Jupyter, `.venv/` — агульнае асяроддзе; яны таксама ігнаруюцца.

## Крыніцы і падзякі

- Project Jupyter documentation: [https://docs.jupyter.org/](https://docs.jupyter.org/)
- JupyterLab documentation: [https://jupyterlab.readthedocs.io/en/stable/](https://jupyterlab.readthedocs.io/en/stable/)
- Jupyter Notebook documentation: [https://jupyter-notebook.readthedocs.io/en/stable/notebook.html](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
- nbconvert documentation: [https://nbconvert.readthedocs.io/](https://nbconvert.readthedocs.io/)
- nbconvert executing notebooks: [https://nbconvert.readthedocs.io/en/latest/execute_api.html](https://nbconvert.readthedocs.io/en/latest/execute_api.html)
- Comparative CWEB reference: Donald E. Knuth and Silvio Levy, “The CWEB System of Structured Documentation”: [https://www-cs-faculty.stanford.edu/~knuth/cweb.html](https://www-cs-faculty.stanford.edu/~knuth/cweb.html)
