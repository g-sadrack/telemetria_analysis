def satelites_nao_vistos_nao_utilizados(df):
    """
    Retorna os índices das linhas onde tanto Sat_U quanto Sat_V são 0.

    Parâmetros:
    df (DataFrame): DataFrame com colunas 'Sat_U' e 'Sat_V'.

    Retorno:
    list: Índices das linhas que atendem ao critério.
    """
    filtro = (df["Sat_U"] == 0) & (df["Sat_V"] == 0)
    return df.index[filtro].tolist()


def satelites_vistos_maior_que_utilizados(df):
    """
    Retorna os índices das linhas onde a quantidade de satélites vistos (Sat_U)
    é maior que a quantidade de satélites utilizados (Sat_V).
    """
    condicao = df["Sat_U"] > df["Sat_V"]
    return df[condicao].index.tolist()




