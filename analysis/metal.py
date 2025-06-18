def detectado(df):
    """
    Retorna os índices das linhas onde houve reinicialização do dispositivo (coluna 'Boot' diferente de 0).

    Parâmetros:
    df (DataFrame): DataFrame com a coluna 'Boot'.

    Retorno:
    list: Índices das linhas com reinicializações.
    """
    filtro = df["MTD"] != 0
    return df.index[filtro].tolist()

def movimentacao_sem_gps(df):
    """
    Retorna os índices das linhas onde houve reinicialização do dispositivo (coluna 'Boot' diferente de 0).

    Parâmetros:
    df (DataFrame): DataFrame com a coluna 'Boot'.

    Retorno:
    list: Índices das linhas com reinicializações.
    """
    filtro = (df["MTD"] != 0) & (df["MOV_S_GPS"] !=0)
    return df.index[filtro].tolist()