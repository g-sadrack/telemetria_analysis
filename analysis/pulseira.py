def ocorrencia_pulseira(df):
    """
    Retorna a primeira ocorrência de violação de pulseira (Fib == 1).
    Retorna uma tupla: (data, índice), ou None se não houver.
    """
    violacoes = df[df["Fib"] == 1]
    if not violacoes.empty:
        primeira_ocorrencia = violacoes.iloc[0]
        return primeira_ocorrencia["Data Com"], primeira_ocorrencia.name
    return None