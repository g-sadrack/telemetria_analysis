import numpy as np
import pandas as pd


def pacotes_descartados(df):
    df.replace(np.nan, "VAZIO", inplace=True)
    pacoteDescartado = []

    for indice, linha in df.iterrows():
        if linha["Boot"] == "VAZIO" and linha["Bat"] == "VAZIO":
            pacoteDescartado.append(indice)
    print("\n ############### \n")
    print(
        f"{len(pacoteDescartado)} Ocorrencias de pacote descartado nas linhas: \n{pacoteDescartado}"
    )


def tolerancia_comunicacao(df):
    """
    Analisa os intervalos entre comunicações e classifica os atrasos em 3 categorias:
    - alerta_min: entre 1 e 10 minutos
    - alerta_med: entre 10 e 30 minutos
    - alerta_max: mais de 30 minutos
    Retorna um dicionário com contagem e índice das ocorrências.
    """
    df = df.copy()
    df["Data Com"] = pd.to_datetime(df["Data Com"], format="%d/%m/%Y %H:%M:%S")

    df["diff"] = df["Data Com"].diff().dt.total_seconds()

    alerta_min = df[(df["diff"] >= 60) & (df["diff"] < 600)].index.tolist()
    alerta_med = df[(df["diff"] >= 600) & (df["diff"] < 1800)].index.tolist()
    alerta_max = df[df["diff"] >= 1800].index.tolist()

    total = len(df)

    return {
        "alerta_min": {
            "indices": alerta_min,
            "quantidade": len(alerta_min),
            "percentual": (len(alerta_min) / total) * 100,
        },
        "alerta_med": {
            "indices": alerta_med,
            "quantidade": len(alerta_med),
            "percentual": (len(alerta_med) / total) * 100,
        },
        "alerta_max": {
            "indices": alerta_max,
            "quantidade": len(alerta_max),
            "percentual": (len(alerta_max) / total) * 100,
        },
    }
