def fora_de_ordem(df):
    """Retorna os índices das linhas onde há ocorrência de FO."""
    return df.index[df["FO"] != 0].tolist()