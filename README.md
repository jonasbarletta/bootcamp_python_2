# Bootcamp Python Jornada de Dados (Aulas 06 a 10)

## Aula 06 - Bibliotecas de Padronização na Formatação dos Códigos

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

Agora sempre que fizer um commit ele fará todos os testes que configurou. Se tiver algum erro de formatação ele corrige automaticamente e te avisa se algo falhou. Caso haja alguma falha e vai corrigir e basta adicionar o arquivo que falhou e comitar novamente. Desta vez tudo estará certo.

## Aula 07 - Revisão de Funções

## Aula 08 - ETL: funções de extração, tranformação e load

Leitura de aquivos JSON -> Concatena DataFrames -> Transformação de Dados -> Decisão de saída CSV ou Parquet -> Salva em CSV ou Parquet 

Opções de ferramentas:

- Ferramentas de processamento: Pandas, Polars, DuckDB, Spark ou Dask

- Ferramente de qualidade: Pydantic ou Pandera.

Vamos utilizar Pandas e Pandera.

Organização do projeto: 

    - etl.py: funções do etl
    - pipeline.py: execusão das funções
    - schema.py: validação dos dados

## Aula 09 - ETL: validação com Pandera e decoradores

Biblioteca de Log: Loguru

poetry add loguru

Tipos de Log:

    - logger.debug('Um aviso para o desenvolvedor (ou eu mesmo) no futuro')
    - logger.info('Informacao importante do processo')
    - logger.warning('Um aviso que algo vai parar de funcionar no futuro')
    - logger.error('Aconteceu uma falha')
    - logger.critical('Aconteceu uma falha que aborta a aplicacao')

Podemos definir um arquivo que receberá os armazenará os Logs:

logger.add("nome_do_arquivo_de_logs.log",
           format = "{time} {level} {message} {file}", # formato de armazenamento da mensagem, mas o formato padrão já é bem formatado.
           level = "CRITICAL" ) # qual nível de Log será armezanado
