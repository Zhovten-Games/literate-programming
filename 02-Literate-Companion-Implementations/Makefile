SHELL := /bin/bash
CXXFLAGS := -std=c++17 -Wall -Wextra -pedantic

.PHONY: noweb-en noweb-uk noweb-ru cweb-en cweb-uk cweb-ru org-en org-uk org-ru quarto-en quarto-uk quarto-ru rmarkdown-en rmarkdown-uk rmarkdown-ru jupyter-en jupyter-uk jupyter-ru validate-locales all

check_cmd = command -v $(1) >/dev/null 2>&1

noweb-en:
	@if $(call check_cmd,notangle) && $(call check_cmd,g++); then \
		cd examples/en/02-noweb-like && notangle -Rprogram primes.nw > primes.cpp && g++ $(CXXFLAGS) primes.cpp -o primes && ./primes; \
	elif ! $(call check_cmd,notangle); then echo "Tool not found: notangle"; \
	else echo "Tool not found: g++"; fi

noweb-uk:
	@if $(call check_cmd,notangle) && $(call check_cmd,g++); then \
		cd examples/uk/02-noweb-like && notangle -Rprogram primes.nw > primes.cpp && g++ $(CXXFLAGS) primes.cpp -o primes && ./primes; \
	elif ! $(call check_cmd,notangle); then echo "Tool not found: notangle"; \
	else echo "Tool not found: g++"; fi

noweb-ru:
	@if $(call check_cmd,notangle) && $(call check_cmd,g++); then \
		cd examples/ru/02-noweb-like && notangle -Rprogram primes.nw > primes.cpp && g++ $(CXXFLAGS) primes.cpp -o primes && ./primes; \
	elif ! $(call check_cmd,notangle); then echo "Tool not found: notangle"; \
	else echo "Tool not found: g++"; fi

cweb-en:
	@if $(call check_cmd,ctangle) && $(call check_cmd,cc); then \
		cd examples/en/01-cweb && ctangle primes.w && cc -Wall -Wextra -pedantic primes.c -o primes && ./primes; \
	elif ! $(call check_cmd,ctangle); then echo "Tool not found: ctangle"; \
	else echo "Tool not found: cc"; fi

cweb-uk:
	@if $(call check_cmd,ctangle) && $(call check_cmd,cc); then \
		cd examples/uk/01-cweb && ctangle primes.w && cc -Wall -Wextra -pedantic primes.c -o primes && ./primes; \
	elif ! $(call check_cmd,ctangle); then echo "Tool not found: ctangle"; \
	else echo "Tool not found: cc"; fi

cweb-ru:
	@if $(call check_cmd,ctangle) && $(call check_cmd,cc); then \
		cd examples/ru/01-cweb && ctangle primes.w && cc -Wall -Wextra -pedantic primes.c -o primes && ./primes; \
	elif ! $(call check_cmd,ctangle); then echo "Tool not found: ctangle"; \
	else echo "Tool not found: cc"; fi

org-en:
	@if $(call check_cmd,emacs) && $(call check_cmd,g++); then \
		cd examples/en/03-org-babel && emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")' && g++ $(CXXFLAGS) primes.cpp -o primes && ./primes; \
	elif ! $(call check_cmd,emacs); then echo "Tool not found: emacs"; \
	else echo "Tool not found: g++"; fi

org-uk:
	@if $(call check_cmd,emacs) && $(call check_cmd,g++); then \
		cd examples/uk/03-org-babel && emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")' && g++ $(CXXFLAGS) primes.cpp -o primes && ./primes; \
	elif ! $(call check_cmd,emacs); then echo "Tool not found: emacs"; \
	else echo "Tool not found: g++"; fi

org-ru:
	@if $(call check_cmd,emacs) && $(call check_cmd,g++); then \
		cd examples/ru/03-org-babel && emacs --batch primes.org -l org -l ob-tangle --eval '(org-babel-tangle-file "primes.org")' && g++ $(CXXFLAGS) primes.cpp -o primes && ./primes; \
	elif ! $(call check_cmd,emacs); then echo "Tool not found: emacs"; \
	else echo "Tool not found: g++"; fi

quarto-en:
	@if $(call check_cmd,quarto); then cd examples/en/04-quarto && quarto render primes.qmd; else echo "Tool not found: quarto"; fi
quarto-uk:
	@if $(call check_cmd,quarto); then cd examples/uk/04-quarto && quarto render primes.qmd; else echo "Tool not found: quarto"; fi
quarto-ru:
	@if $(call check_cmd,quarto); then cd examples/ru/04-quarto && quarto render primes.qmd; else echo "Tool not found: quarto"; fi
rmarkdown-en:
	@if $(call check_cmd,Rscript); then cd examples/en/06-rmarkdown && Rscript -e "rmarkdown::render('primes.Rmd')"; else echo "Tool not found: Rscript"; fi
rmarkdown-uk:
	@if $(call check_cmd,Rscript); then cd examples/uk/06-rmarkdown && Rscript -e "rmarkdown::render('primes.Rmd')"; else echo "Tool not found: Rscript"; fi
rmarkdown-ru:
	@if $(call check_cmd,Rscript); then cd examples/ru/06-rmarkdown && Rscript -e "rmarkdown::render('primes.Rmd')"; else echo "Tool not found: Rscript"; fi
jupyter-en:
	@if $(call check_cmd,python3); then cd examples/en/05-jupyter && python3 primes.py; else echo "Tool not found: python3"; fi
jupyter-uk:
	@if $(call check_cmd,python3); then cd examples/uk/05-jupyter && python3 primes.py; else echo "Tool not found: python3"; fi
jupyter-ru:
	@if $(call check_cmd,python3); then cd examples/ru/05-jupyter && python3 primes.py; else echo "Tool not found: python3"; fi

validate-locales:
	@python3 methodology/extensions/primes-example/tests/validate-primes-locales.py \
		examples/en/07-prompt-literate \
		examples/uk/07-prompt-literate \
		examples/ru/07-prompt-literate

all: noweb-en noweb-uk noweb-ru cweb-en cweb-uk cweb-ru org-en org-uk org-ru quarto-en quarto-uk quarto-ru rmarkdown-en rmarkdown-uk rmarkdown-ru jupyter-en jupyter-uk jupyter-ru validate-locales
