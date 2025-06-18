def contador_de_boots(df):
    """
    Retorna os índices das linhas onde houve reinicialização do dispositivo (coluna 'Boot' diferente de 0).

    Parâmetros:
    df (DataFrame): DataFrame com a coluna 'Boot'.

    Retorno:
    list: Índices das linhas com reinicializações.
    """
    filtro = df["Boot"] != 0
    return df.index[filtro].tolist()
