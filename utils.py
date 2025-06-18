# Função que conta o número de linhas vazias
def linhas_vazias(df):
    print(df.isna().sum())