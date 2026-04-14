import pandas as pd
from dados import banco_de_dados, banco_de_regulatorios, banco_de_motoristas

def listar_empresas():
    """Retorna uma lista com os nomes das empresas"""
    return list(banco_de_dados.keys())

def listar_filiais(empresa):
    """Retorna uma lista de filiais pertencentes a uma empresa"""
    if empresa in banco_de_dados:
        return [f["filial"] for f in banco_de_dados[empresa]]
    return []

def obter_dados_filial(empresa, nome_filial):
    """Busca o dicionário com os detalhes técnicos de uma filial específica"""
    for f in banco_de_dados.get(empresa, []):
        if f["filial"] == nome_filial:
            return f
    return None

def obter_regulatorios():
    """Converte a lista de regulatórios em um DataFrame do Pandas"""
    return pd.DataFrame(banco_de_regulatorios)

def obter_motoristas(nome_filial):
    """Retorna um DataFrame com os motoristas da filial, ou vazio se não houver"""
    motoristas = banco_de_motoristas.get(nome_filial, [])
    if motoristas:
        return pd.DataFrame(motoristas)
    return pd.DataFrame()