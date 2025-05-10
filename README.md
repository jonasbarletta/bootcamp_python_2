# Bootcamp Python Jornada de Dados (Aulas 06 a 10)


pyenv local 3.12

poetry init

poetry add


## Bibliotecas para formatação de código Python

flake8, black e blue.

flake8: faz sugestões do que corrigir (de acordo com a PEP8) na formatação do código, mas não o altera.

black e blue: fazem a correção da formatação do código de acordo com a PEP8. O blue utiliza o black e o flake8.

isort: biblioteca para organizar a parte de importação de bibliotecas.

Para rodar:

flake8: poetry run flake8 script.py

black: poetry run flake8 script.py

isort: poetry run isort script.py


O isort e o black podem não concordar com algumas formatações. Então para que ambos funcionem juntos é necessário acrescentar o seguinte no arquivo pyproject.toml:

[tool.isort]
profile = black

Para complementar podemos criar um comando para rodar o isort e black em sequência. Para isso precisaremos adicionar a biblioteca taskipy.

poetry add taskipy

Adicionar os comando no arquivo pyproject.toml

[tool.taskipy.tasks]
format = """
isort *py
black *.py
flake8 *.py
"""

pre-commit: biblioteca que bloqueia salvar o código localmente sem que determinas condições sejam satisfeitas, por exemplo a formatação do código de acordo com as bibliotecas anteriores.

Para usar essa biblioteca você deve definir o que deve ser conferido pelo pre-commit no arquivo .pre-commit-config.yaml.

Rodar o comando poetry run pre-commit install.

Isso era adicionar a pasta hook dentro da pasta .git.
