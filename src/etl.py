import glob
import os
import re

import pandas as pd
from loguru import logger


def extrair_dados(pasta: str) -> pd.DataFrame:

    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))

    data_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

    data = pd.concat(data_list, ignore_index=True)

    return data


def to_snake_case(name):

    name = re.sub(r"(?<!^)(?=[A-Z])", "_", name)

    return name.lower()


def transformacoes(data: pd.DataFrame) -> pd.DataFrame:

    data.columns = [to_snake_case(col) for col in data.columns]

    data["total"] = data["quantidade"] * data["venda"]

    return data


def load(data: pd.DataFrame, formato: str) -> pd.DataFrame:

    if formato not in ("csv", "parquet"):

        logger.critical('O parâmetro "formato" deve ser "csv" ou "parquet"')

        raise ValueError("O parâmetro 'formato' deve ser 'csv' ou 'parquet'")

    if formato == "csv":

        data.to_csv("data/data_saida.csv", index=False)

    if formato == "parquet":

        data.to_parquet("data/data_saida.parquet", index=False)

    return None


def pipeline(pasta: str):

    logger.add("log_pipeline.log", level="INFO")

    pasta = "data"

    logger.info("Inicio do Pipeline")

    df_raw = extrair_dados(pasta)

    logger.info("Extração de dados Concluída")

    df = transformacoes(df_raw)

    logger.info("Transformação Concluída")

    formato = input("Indique o formato do arquivo: ")

    load(data=df, formato=formato)

    logger.info(f"Load no Formato {formato} Concluído")


# Testando as funções
# if __name__ == '__main__':
