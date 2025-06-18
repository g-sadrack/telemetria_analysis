import pandas as pd

def criar_dataframe_virgula(entrada, saida):
    """Retorna um arquivo csv delimitado por virgula"""
    df = pd.read_csv(entrada, delimiter="|")
    df.to_csv(saida, index=False)


def limpar_colunas(df):
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    colunas_remover = [
        "Nº",
        "Rede/APN",
        "Monitorado",
        "Mem",
        "Mem. Livre",
        "Vel",
        "Passos",
        "Coordenadas",
        "TL",
    ]
    return df.drop(columns=colunas_remover, errors="ignore")
