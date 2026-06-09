# Companion

## 1. Краткое введение

Jupyter показывает notebook-style literate computing. Это не строгий Knuth-style WEB и не tangle/weave workflow. Это интерактивный notebook workflow, где текст, кодовые ячейки, состояние выполнения и вывод ячеек живут вместе в `.ipynb`-документе.

В этом companion `primes.ipynb` — notebook-документ, а `primes.py` — script companion для простой command-line sanity-check проверки.

## 2. Модель источников и компактный конвейер

Notebook-источник:

- `primes.ipynb`

Ветка выполнения notebook:

- `primes.ipynb -> Jupyter kernel / nbconvert --execute -> primes.executed.ipynb`

Script sanity-ветка:

- `primes.py -> python3 -> output.txt`

Примечания:

- `primes.ipynb` — это JSON notebook-документ.
- `primes.py` добавлен, чтобы быстро проверять алгоритм на уровне скрипта.
- `primes.executed.ipynb` генерируется через `nbconvert --execute` и не должен коммититься.
- В отличие от `01-cweb` / `02-noweb-like` / `03-org-babel`, Jupyter не ориентирован на генерацию канонического машинно-ориентированного исходного файла.
- В отличие от `04-quarto`, основная модель авторинга — интерактивный notebook, а не конвейер срендеренной публикации.

## 3. Что такое Jupyter / .ipynb / kernels / notebook cells

- Jupyter: интерактивная вычислительная notebook-экосистема
- `.ipynb`: JSON-документ с ячейками, metadata, execution count и outputs
- Kernel: runtime-процесс, который выполняет код и хранит состояние
- JupyterLab / Notebook: браузерный GUI для работы с notebooks

GUI есть, но воспроизводимая companion-проверка использует command-line выполнение через `nbconvert`.

## 4. Команды script sanity-check

Из этой директории:

```bash
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
```

Ожидаемые маркеры вывода:

- `The First 1000 Prime Numbers --- Page 1`
- `The First 1000 Prime Numbers --- Page 5`
- `      6571      6997      7499      7919`

Это подтверждает корректность алгоритма и вывода через обычный путь Python-скрипта. Это не доказывает выполнение notebook; оно проверяется отдельно.

## 5. Команды выполнения notebook

Из этой директории:

```bash
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb
```

Ожидаемые маркеры в выполненном notebook:

- `"The First 1000 Prime Numbers --- Page 1\n"`
- `"The First 1000 Prime Numbers --- Page 5\n"`
- `"      6571      6997      7499      7919\n"`

Эта команда выполняет notebook в headless-режиме и записывает `primes.executed.ipynb` с выводом выполненных ячеек.

Маршрут вручную протестирован в обеих языковых ветках: `examples/ru/05-jupyter` и `examples/en/05-jupyter`.

## 6. Заметки про GUI notebook

Из корня `Literate-Companion-Implementations` с активированной `.venv`:

```bash
jupyter lab
```

или:

```bash
jupyter notebook
```

- JupyterLab — более IDE-like интерфейс: file browser, tabs, notebooks, text editor, terminal и другое.
- Jupyter Notebook — классический notebook-интерфейс.
- В WSL/Linux сервер обычно печатает локальный URL с токеном; его обычно можно открыть вручную в браузере Windows.
- GUI-использование для этого companion опционально.
- Воспроизводимая проверка остаётся `nbconvert --execute`.

## 7. Почему не просто комментарии?

Обычные комментарии:

пояснение прикреплено к коду.

Jupyter:

вычисление и объяснение разложены как интерактивная notebook-тетрадь.

Важное отличие: Jupyter в первую очередь не про извлечение исходного кода для компилятора. Это про interactive literate computing.

Hidden state: ячейки можно выполнять вне порядка, поэтому видимый порядок notebook может не совпадать с фактической execution history. Это основной риск воспроизводимости.

## 8. Место в наборе

`05-jupyter` показывает notebook-style literate computing. Он полезен для интерактивного исследования, обучения, прототипирования и видимого вывода ячеек, но несёт риски hidden state и нелинейного порядка выполнения. Это не строгая WEB-style генерация исходника. Полное сравнение всех companion-вариантов см. в корневом README.

## 9. Установка: общая корневая `.venv`

Из корня `Literate-Companion-Implementations`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter
```

Проверка:

```bash
which python
python -m jupyter --version
```

Ожидаемая форма `which python`:

- `.../Literate-Companion-Implementations/.venv/bin/python`

Одна и та же корневая `.venv` переиспользуется для `04-quarto` и `05-jupyter`.

Проверка обеих языковых веток:

```bash
cd examples/ru/05-jupyter
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb

cd ../../en/05-jupyter
python3 primes.py > output.txt
grep "Page 1" output.txt && grep "Page 5" output.txt && grep "7919" output.txt
jupyter nbconvert --to notebook --execute primes.ipynb --output primes.executed.ipynb
grep "Page 1" primes.executed.ipynb && grep "Page 5" primes.executed.ipynb && grep "7919" primes.executed.ipynb
```

## 10. Заметки для Windows

Windows возможен, но не был основным протестированным маршрутом для этого companion.

- Jupyter может запускаться нативно на Windows при установленном Python/Jupyter.
- Инструменты должны быть доступны в PATH.

Проверка:

```powershell
where.exe python
python --version
python -m jupyter --version
```

Если не найдено:

- установить Python;
- добавить Python/Scripts в PATH;
- установить Jupyter в активную среду.

Для этого companion воспроизводимый протестированный маршрут — WSL/Linux с общей корневой `.venv`.

## 11. Диагностика и частые проблемы

A. MissingIDFieldWarning

В ручном тесте встречалось предупреждение:

```text
MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions.
```

Оно означает, что в notebook-ячейках отсутствуют стабильные `id`, ожидаемые новыми версиями `nbformat`. После добавления `id` во все ячейки предупреждение должно исчезнуть.

B. Hidden state

Если notebook работает интерактивно, но падает в `nbconvert --execute`, причина может быть в hidden state или out-of-order execution. Воспроизводимая проверка — чистое top-to-bottom выполнение через `nbconvert`.

C. Kernel/Jupyter not found

Если `nbconvert` не запускается:

- активировать `.venv`;
- убедиться, что `jupyter` установлен;
- выполнить `python -m jupyter --version`.

D. Generated executed notebook

`primes.executed.ipynb` — это generated output, он не должен коммититься.

## 12. Сгенерированные файлы

- `COMPANION.md`  
  Документация для этого companion-примера. Коммитится как исходник.
- `primes.ipynb`  
  Канонический Jupyter notebook source. Коммитится как исходник.
- `primes.py`  
  Script companion для быстрых command-line sanity-check проверок. Коммитится как исходник.
- `output.txt`  
  Локально сохранённый вывод скрипта. Генерируется и игнорируется.
- `primes.executed.ipynb`  
  Выполненный notebook, сгенерированный через `nbconvert --execute`. Генерируется и игнорируется.
- `.ipynb_checkpoints/`  
  Локальная директория checkpoint-файлов Jupyter. Генерируется и игнорируется.
- `.venv/`  
  Общая Python virtual environment при создании в `Literate-Companion-Implementations/.venv`. Генерируется и игнорируется.

## 13. Благодарности и ссылки

- Документация Project Jupyter: [https://docs.jupyter.org/](https://docs.jupyter.org/)
- Документация JupyterLab: [https://jupyterlab.readthedocs.io/en/stable/](https://jupyterlab.readthedocs.io/en/stable/)
- Документация Jupyter Notebook: [https://jupyter-notebook.readthedocs.io/en/stable/notebook.html](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
- Документация nbconvert: [https://nbconvert.readthedocs.io/](https://nbconvert.readthedocs.io/)
- nbconvert: выполнение notebooks: [https://nbconvert.readthedocs.io/en/latest/execute_api.html](https://nbconvert.readthedocs.io/en/latest/execute_api.html)
- Сравнительный источник по CWEB: Дональд Э. Кнут и Сильвио Леви, “The CWEB System of Structured Documentation”: [https://www-cs-faculty.stanford.edu/~knuth/cweb.html](https://www-cs-faculty.stanford.edu/~knuth/cweb.html)
