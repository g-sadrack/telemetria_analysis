from config import TELEMETRIA_CSV, ARQUIVO_LIMPO
from preprocess import criar_dataframe_virgula, limpar_colunas
from analysis import satelites, boots, pulseira, comunicacao, fora_de_ordem, metal
import pandas as pd


def main():
    criar_dataframe_virgula(TELEMETRIA_CSV, ARQUIVO_LIMPO)
    df = pd.read_csv(ARQUIVO_LIMPO)
    # df = limpar_colunas(df)


    # indices = satelites.satelites_nao_vistos_nao_utilizados(df)
    # print(f'\nPerda de satelite: {len(indices)} - Linhas: {indices}')
    # satelites.satelites_vistos_maior_que_utilizados(df)
    # print()

    boot = boots.contador_de_boots(df)
    print("\n#### Contador de Boots ####")
    print(f"O dispositivo reiniciou: {len(boot)} - Linhas: {boot}")

    pul = pulseira.ocorrencia_pulseira(df)
    print("\n#### Ocorrência de Pulseira ####")
    if pul:  # Se a lista não estiver vazia
        print(f"Ocorrencia de pulseira: {len(pul)} - Linhas: {pul}")
    else:
        print("Nenhuma ocorrência de pulseira encontrada.")

    fo_indices = fora_de_ordem.fora_de_ordem(df)
    if fo_indices:
        print("\n#### Fora de Ordem ####")
        print(f"Ocorrências nas linhas: {fo_indices} - Total: {len(fo_indices)}")
    else:
        print("\n#### Fora de Ordem ####")
        print("Nenhuma ocorrência de FO encontrada.")


    resultado = comunicacao.tolerancia_comunicacao(df)

    print("\n#### Tolerância de Comunicação ####")
    print(
        f"Entre 1 e 10 min: {resultado['alerta_min']['quantidade']} ocorrências"
        f"({resultado['alerta_min']['percentual']:.2f}%)"
    )
    print(
        f"Entre 10 e 30 min: {resultado['alerta_med']['quantidade']} ocorrências"
        f"({resultado['alerta_med']['percentual']:.2f}%)"
    )
    print(
        f"Acima de 30 min: {resultado['alerta_max']['quantidade']} ocorrências"
        f"({resultado['alerta_max']['percentual']:.2f}%)"
    )

    # indices = satelites.satelites_vistos_maior_que_utilizados(df)
    # print(f"Número de ocorrências: {len(indices)}")
    # print(f"Linhas: {indices}")

    # indices = metal.movimentacao_sem_gps(df)
    # print(f"Número de ocorrências: {len(indices)}")
    # print(f"Linhas: {indices}")




if __name__ == "__main__":
    main()
