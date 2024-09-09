import pandas as pd
from data_processing import download_dados_cvm, processar_dados_fundos, obter_dados_cadastro

pd.options.display.float_format = '{:.4f}'.format

def calcular_variacao(dados_fundos, data_inicio, data_fim):
    """
    Calcula a variação entre o patrimônio líquido e o número de cotistas no início e no fim do mês.

    Args:
        dados_fundos (DataFrame): Dados dos fundos diários.
        data_inicio (str): Data do início do mês.
        data_fim (str): Data do fim do mês.

    Returns:
        DataFrame: Dados com variações de patrimônio e cotistas.
    """


    # Variação do patrimônio
    dados_inicio_patrimonio = dados_fundos[dados_fundos['DT_COMPTC'] == data_inicio][['CNPJ_FUNDO', 'VL_PATRIM_LIQ']].rename(columns={'VL_PATRIM_LIQ': 'VL_PATRIM_LIQ_inicio'})
    dados_fim_patrimonio = dados_fundos[dados_fundos['DT_COMPTC'] == data_fim][['CNPJ_FUNDO', 'VL_PATRIM_LIQ']].rename(columns={'VL_PATRIM_LIQ': 'VL_PATRIM_LIQ_fim'})
    
    # Variação dos cotistas
    dados_inicio_cotistas = dados_fundos[dados_fundos['DT_COMPTC'] == data_inicio][['CNPJ_FUNDO', 'NR_COTST']].rename(columns={'NR_COTST': 'NR_COTST_inicio'})
    dados_fim_cotistas = dados_fundos[dados_fundos['DT_COMPTC'] == data_fim][['CNPJ_FUNDO', 'NR_COTST']].rename(columns={'NR_COTST': 'NR_COTST_fim'})
    
    # Merge dos dados
    dados_variacao_patrimonio = pd.merge(dados_inicio_patrimonio, dados_fim_patrimonio, on='CNPJ_FUNDO', how='inner')
    dados_variacao_patrimonio['variacao_patrimonio'] = dados_variacao_patrimonio['VL_PATRIM_LIQ_fim'] - dados_variacao_patrimonio['VL_PATRIM_LIQ_inicio']
    
    dados_variacao_cotistas = pd.merge(dados_inicio_cotistas, dados_fim_cotistas, on='CNPJ_FUNDO', how='inner')
    dados_variacao_cotistas['variacao_cotistas'] = dados_variacao_cotistas['NR_COTST_fim'] - dados_variacao_cotistas['NR_COTST_inicio']
    
    # Combinar variações
    return pd.merge(dados_variacao_patrimonio[['CNPJ_FUNDO', 'variacao_patrimonio']], dados_variacao_cotistas[['CNPJ_FUNDO', 'variacao_cotistas']], on='CNPJ_FUNDO')

if __name__ == "__main__":
    ano = str(input('Digite o Ano [YYYY]: '))
    mes = str(input('Digite o Mês [mm]: '))
    save_dir = r'C:\\Users\\thallysonfreire\\developer\\github\\dados_fundos_cvm' # escolher o diretorio

    # Baixar e processar dados
    zip_path = download_dados_cvm(ano, mes, save_dir)
    dados_fundos = processar_dados_fundos(zip_path)
    dados_cadastro = obter_dados_cadastro()

    # Filtrar datas de início e fim do mês
    data_inicio_mes = dados_fundos['DT_COMPTC'].sort_values().unique()[0]
    data_fim_mes = dados_fundos['DT_COMPTC'].sort_values().unique()[-1]

    # Calcular variações
    variacoes = calcular_variacao(dados_fundos, data_inicio_mes, data_fim_mes)

    # Combinar com dados de cadastro
    base_final = pd.merge(variacoes, dados_cadastro, on='CNPJ_FUNDO', how='left')

    # Exibir os maiores fundos por patrimônio líquido
    fundos_maior_patrimonio = base_final.sort_values(by='variacao_patrimonio', ascending=False).head(10)


    print(base_final)
    print()
    print(fundos_maior_patrimonio)