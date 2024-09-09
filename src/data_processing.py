import pandas as pd
import requests
import zipfile
import os

def download_dados_cvm(ano, mes, save_dir):
    """
    Faz o download dos dados diários dos fundos da CVM e salva o arquivo zip localmente.
    
    Args:
        ano (str): Ano dos dados a serem baixados.
        mes (str): Mês dos dados a serem baixados.
        save_dir (str): Diretório onde o arquivo será salvo.
    """


    url = f'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{ano}{mes}.zip'
    os.chdir(save_dir)
    
    download = requests.get(url)
    zip_path = f'inf_diario_fi_{ano}{mes}.zip'
    
    with open(zip_path, 'wb') as arquivo_cvm:
        arquivo_cvm.write(download.content)

    return zip_path


def processar_dados_fundos(zip_path):
    """
    Lê e processa o arquivo CSV contido no arquivo zip baixado da CVM.
    
    Args:
        zip_path (str): Caminho para o arquivo zip baixado.

    Returns:
        DataFrame: Dados dos fundos processados.
    """


    with zipfile.ZipFile(zip_path, 'r') as arquivo_zip:
        csv_name = arquivo_zip.namelist()[0]
        dados_fundos = pd.read_csv(arquivo_zip.open(csv_name), sep=';', encoding='ISO-8859-1')
    
    return dados_fundos


def obter_dados_cadastro():
    """
    Faz o download dos dados de cadastro dos fundos e retorna um DataFrame com as informações.

    Returns:
        DataFrame: Dados de cadastro dos fundos.
    """


    url_cadastro = 'https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv'
    dados_cadastro = pd.read_csv(url_cadastro, sep=';', encoding='ISO-8859-1')
    dados_cadastro = dados_cadastro[['CNPJ_FUNDO', 'DENOM_SOCIAL']].drop_duplicates()
    
    return dados_cadastro