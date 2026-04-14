import pandas as pd
import streamlit as st

# ==========================================
# BANCO DE DADOS: FILIAIS
# ==========================================
banco_de_dados = {
    "MM Delivery": [
        {"filial": "Araçatuba", "uf": "SP", "gestor": "Wilton", "telefone": "18 99681-6003", "endereco": "Travessa Carlos Gardel, 61 - Chacaras California", "cep": "16026-630", "cnpj": "37.934.161/0006-77", "rt": "Pedro"},
        {"filial": "Bauru", "uf": "SP", "gestor": "Wilton", "telefone": "18 99681-6003", "endereco": "Rua Joaquim Marques de Figueiredo, 5-15", "cep": "17034-290", "cnpj": "37.934.161/0007-58", "rt": "Pedro"},
        {"filial": "CD Nasp (São Paulo)", "uf": "SP", "gestor": "Carlos Narita", "telefone": "11 97090-9222", "endereco": "Av. Alexandre Colares, 1188 - Parque Anhanguera", "cep": "05106-000", "cnpj": "37.934.161/0008-39", "rt": "Jozilayde"},
        {"filial": "Carapicuíba", "uf": "SP", "gestor": "Carlos Narita", "telefone": "11 97090-9222", "endereco": "Rua Ministro Nelson Hungria, 90 - Chácara Quiriri", "cep": "06341-000", "cnpj": "37.934.161/0001-62", "rt": "Jirlene"},
        {"filial": "Osasco", "uf": "SP", "gestor": "Morita", "telefone": "11 93069-3058", "endereco": "Av. Benedito Alves Turíbio, 959 - Jardim Cirino", "cep": "06160-002", "cnpj": "37.934.161/0004-05", "rt": "Jirlene"},
        {"filial": "Praia Grande", "uf": "SP", "gestor": "Alex Peres", "telefone": "Não informado", "endereco": "Rua Nancyr Feliciano de Oliveira, 540 - Vila Tupiry", "cep": "11.719-130", "cnpj": "37.934.161/0011-34", "rt": "Icaro"},
        {"filial": "São Jose Dos Campos", "uf": "SP", "gestor": "Não informado", "telefone": "Não informado", "endereco": "Rua Salviano José da Silva, 85 - Eldorado", "cep": "12238-573", "cnpj": "37.934.161/0013-04", "rt": "Andressa"},
        {"filial": "Taboão da Serra", "uf": "SP", "gestor": "Alex Chagas", "telefone": "11 96812-4561", "endereco": "Rua Guilherme de Almeida nº 32 - Jardim Saint Motriz", "cep": "06.787-440", "cnpj": "37.934.161/0014-87", "rt": "Jirlene"},
        {"filial": "Nove de Julho (São Paulo)", "uf": "SP", "gestor": "Carlos Narita", "telefone": "11 97090-9222", "endereco": "Avenida Nove de Julho, nº 240 - Bela Vista", "cep": "01312-000", "cnpj": "37.934.161/0003-24", "rt": "Jozilayde"},
        {"filial": "São Bernardo do Campo", "uf": "SP", "gestor": "Alex Peres", "telefone": "11 98231-2132", "endereco": "Rua João Antonio Butrico nº 700 - Galpão 05 e 06", "cep": "09.852-100", "cnpj": "37.934.161/0005-96", "rt": "Icaro"},
        {"filial": "Presidente Prudente", "uf": "SP", "gestor": "Winton Silva", "telefone": "18 99681-6003", "endereco": "R Marechal Candido Rondon, 49 - Vila Barbeiro", "cep": "19.013-650", "cnpj": "37.934.161/0015-68", "rt": "Pedro"},
        {"filial": "Uberlândia MM", "uf": "MG", "gestor": "Fiscal", "telefone": "Não informado", "endereco": "R Coronel Constantino, nº 130 - Altamira", "cep": "38.400-222", "cnpj": "37.934.161/0002-43", "rt": "Fiscal - Bianca"}
    ],
    "MD Delivery": [
        {"filial": "São Paulo", "uf": "SP", "gestor": "Marcio rollo", "telefone": "11 94312-1540", "endereco": "Av. Educador Paulo Freire, 900 - Pq Novo Mundo", "cep": "02187-110", "cnpj": "34.214.512/0006-87", "rt": "Aline Bernardes"},
        {"filial": "Campinas", "uf": "SP", "gestor": "Leandro Policarpo", "telefone": "21 96742-6165", "endereco": "Rua Luiz Fernando Rodriguez, 2315 - Vila Boa Vista", "cep": "13064798", "cnpj": "34.214.512/0005-04", "rt": "Robison"},
        {"filial": "Ribeirão Preto", "uf": "SP", "gestor": "Wilton", "telefone": "18 99681-6003", "endereco": "Rua Miryan Strambi, nº 945 - Recreio Anhanguera", "cep": "14097-052", "cnpj": "34.214.512/0002-53", "rt": "Antenor"},
        {"filial": "Sorocaba", "uf": "SP", "gestor": "Leandro Policarpo", "telefone": "21 96742-6165", "endereco": "Estrada dos Ferraz, nº 40 Galpao 02 - Iporanga", "cep": "18087-172", "cnpj": "34.214.512/0010-63", "rt": "Robison"},
        {"filial": "Barra Mansa", "uf": "RJ", "gestor": "Talison Lessa", "telefone": "24 99953-9840", "endereco": "Rua Projetada Variante, BR 116 - 965 - São Lucas", "cep": "27336-450", "cnpj": "34.214.512/0008-49", "rt": "Leonardo"},
        {"filial": "Campos dos Goytacazes", "uf": "RJ", "gestor": "Fabio Souza", "telefone": "21 96411-2326", "endereco": "Rua São Bartolomeu nº 30 - Parque Conselheiro Thomas Coelho", "cep": "28051-060", "cnpj": "34.214.512/0014-97", "rt": "Sara"},
        {"filial": "Duque de Caxias", "uf": "RJ", "gestor": "Laerte Martins", "telefone": "21 97178-8496", "endereco": "Rod Washington Luiz, nº 2569 - Vila São Luiz", "cep": "25085-008", "cnpj": "34.214.512/0009-20", "rt": "Leonardo"},
        {"filial": "Nova Friburgo", "uf": "RJ", "gestor": "Fabio Souza", "telefone": "21 96411-2326", "endereco": "Rod RJ 130 KM 04 - nº 50792 - Corrego D' Antas", "cep": "28.630-310", "cnpj": "34.214.512/0013-06", "rt": "Sara"},
        {"filial": "São Gonçalo", "uf": "RJ", "gestor": "Talison Lessa", "telefone": "24 99953-9840", "endereco": "Rua Frederico Gonçalves, nº 54 - Santa Luzia", "cep": "24722-810", "cnpj": "34.214.512/0004-15", "rt": "Arthur"},
        {"filial": "São Pedro da Aldeia", "uf": "RJ", "gestor": "Fabio Souza", "telefone": "21 96411-2326", "endereco": "Rod Amaral Peixoto, nº 292 - Balneário das Conchas", "cep": "28949-464", "cnpj": "34.214.512/0012-25", "rt": "Arthur"},
        {"filial": "Campo Grande", "uf": "RJ", "gestor": "Talison Lessa", "telefone": "24 99953-9840", "endereco": "Est Rio Sao Paulo, 03918 - Campo Grande", "cep": "23.075-246", "cnpj": "34.214.512/0015-78", "rt": "Leonardo"},
        {"filial": "Três Rios", "uf": "RJ", "gestor": "Ponto de Apoio", "telefone": "21 96411-2326", "endereco": "Av Prefeito Samir Nasser, Vila Isabel", "cep": "25.811-001", "cnpj": "24.225.370/0001-95", "rt": "Ponto de Apoio"},
        {"filial": "Juiz De Fora", "uf": "MG", "gestor": "Fiscal", "telefone": "Não informado", "endereco": "Rua Francisco Vaz de Magalhães, nº 301 – Cascatinha", "cep": "36033-340", "cnpj": "34.214.512/0003-34", "rt": "Fiscal - Bianca"},
        {"filial": "Uberlândia MD", "uf": "MG", "gestor": "Fiscal", "telefone": "Não informado", "endereco": "Rua Coronel Constantino, nº 130 - Tabajaras", "cep": "38400-222", "cnpj": "34.214.512/0001-72", "rt": "Fiscal - Bianca"}
    ],
    "Dias Log": [
        {"filial": "São Mateus", "uf": "SP", "gestor": "Marcio rollo", "telefone": "11 94312-1540", "endereco": "Rua André de Almeida, 2049 - Cidade São Mateus", "cep": "03966-005", "cnpj": "58.092.305/0001-50", "rt": "Aline Viana"}
    ],
    "Safe": [
        {"filial": "Matriz Curitiba", "uf": "PR", "gestor": "Jefferson", "telefone": "Não informado", "endereco": "R Pde Adelino, 2074 - Quarta Parada (SP)", "cep": "03.303-000", "cnpj": "49.559.838/0001-09", "rt": "Fiscal"},
        {"filial": "Curitiba", "uf": "PR", "gestor": "Jefferson", "telefone": "Não informado", "endereco": "R Cyro Correia Pereira, 667 - Cidade Industrial", "cep": "81.170-230", "cnpj": "49.559.838/0002-90", "rt": "Sandy"},
        {"filial": "Ponta Grossa", "uf": "PR", "gestor": "Jefferson", "telefone": "Não informado", "endereco": "R Doutor Nilton Luiz de Castro - 77 - Colonia Dona Luiza", "cep": "84.046-015", "cnpj": "49.559.838/0003-70", "rt": "Sandy"}
    ]
}

# ==========================================
# BANCO DE DADOS: REGULATÓRIOS
# ==========================================
banco_de_regulatorios = [
    {"Documento": "CNPJ - CADASTRO NACIONAL DA PESSOA JURÍDICA", "Órgão": "RFB", "Vencimento": "Indeterminada", "Status": "Solicitar junto ao setor jurídico", "Link PDF": "#"},
    {"Documento": "IE - INSCRIÇÃO ESTADUAL", "Órgão": "SEFAZ", "Vencimento": "Indeterminada", "Status": "Solicitar junto ao setor jurídico", "Link PDF": "#"},
    {"Documento": "CCM - INSCRIÇÃO MUNICIPAL", "Órgão": "Prefeitura Municipal", "Vencimento": "Indeterminada", "Status": "Solicitar junto ao setor jurídico", "Link PDF": "#"},
    {"Documento": "AVCB - AUTO DE VISTORIA DO CORPO DE BOMBEIROS", "Órgão": "Corpo de Bombeiros", "Vencimento": "1 a 5 anos", "Status": "O período depende do risco de incêndio do estabelecimento e da atividade exercida.", "Link PDF": "#"},
    {"Documento": "AFE - AUTORIZAÇÃO DE FUNCIONAMENTO", "Órgão": "ANVISA", "Vencimento": "Indeterminada", "Status": "As filiais podem realizar as atividades autorizadas na AFE da matriz", "Link PDF": "#"},
    {"Documento": "LTA - LAUDO TÉCNICO DE AVALIAÇÃO", "Órgão": "VIGILÂNCIA SANITÁRIA", "Vencimento": "Indeterminada", "Status": "O LTA é um pré-requisito para a solicitação da Licença Sanitária.", "Link PDF": "#"},
    {"Documento": "LS - LICENÇA SANITÁRIA", "Órgão": "VIGILÂNCIA SANITÁRIA", "Vencimento": "1 ano", "Status": "A licença sanitária atesta que o estabelecimento tem condições sanitárias, físicas, estruturais e operacionais para funcionar.", "Link PDF": "#"},
    {"Documento": "LAUDO POTABILIDADE - LAUDO DA POTABILIDADE DA ÁGUA", "Órgão": "EXPANSÃO", "Vencimento": "Semestral", "Status": "Toda vez que for realizado a limpeza da caixa d´água solicitar o laudo da potabilidade da água.", "Link PDF": "#"},
    {"Documento": "VRE - LICENCIAMENTO INTEGRADO - VIA RAPIDO EMPRESA", "Órgão": "JUCESP", "Vencimento": "1 ano", "Status": "Solicitar as atualizações para o setor jurídico", "Link PDF": "#"},
    {"Documento": "CDL - CERTIFICADO DE DISPENÇA DE LICENÇA - CETESB", "Órgão": "CETESB", "Vencimento": "Indeterminada", "Status": "Formaliza a dispensa de licenças ambientais para atividades que não precisam de licenciamento.", "Link PDF": "#"},
    {"Documento": "CONTRATO SOCIAL", "Órgão": "JUCESP", "Vencimento": "Indeterminada", "Status": "Solicitar junto ao setor jurídico", "Link PDF": "#"},
    {"Documento": "ART - CERTIDÃO DE ANOTAÇÃO DE RESPONSABILIDADE TÉCNICA", "Órgão": "CRQ", "Vencimento": "1 ano", "Status": "Documento que define o profissional responsável por atividades na área da química. Renovação anual.", "Link PDF": "#"},
    {"Documento": "AMBIPAR RESPONSE - CERTIFICADO DE ATENDIMENTO DE EMERGÊNCIAS", "Órgão": "AMBIPAR", "Vencimento": "3 anos", "Status": "Solicitar com o coordenador", "Link PDF": "#"},
    {"Documento": "AMBIPAR RESPONSE - CERTIFICADO ACIDENTE ZERO", "Órgão": "AMBIPAR", "Vencimento": "anual", "Status": "Documento que indica se houve registro de acidentes nos últimos 12 meses.", "Link PDF": "#"},
    {"Documento": "PGR - PROGRAMA DE GERENCIAMENTO DE RISCOS", "Órgão": "VIDA CARE", "Vencimento": "2 anos", "Status": "Ações e procedimentos para identificar, avaliar e controlar os riscos ocupacionais e ambientais.", "Link PDF": "#"},
    {"Documento": "PCMSO - PROGRAMA DE CONTROLE MÉDICO DE SAÚDE OCUPACIONAL", "Órgão": "VIDA CARE", "Vencimento": "1 ano", "Status": "Ações para proteger a saúde dos trabalhadores. RT: Solicitar acesso ao sistema Vida Care.", "Link PDF": "#"},
    {"Documento": "SEGURO - APÓLICE SEGURO PREDIAL", "Órgão": "VERIFICAR", "Vencimento": "1 ano", "Status": "Solicitar junto ao setor jurídico", "Link PDF": "#"},
    {"Documento": "CERTIFICADO DE INSPEÇÃO E MANUTENÇÃO DE MANGUEIRA DE INCÊNDIO", "Órgão": "EMPRESA APROVADA", "Vencimento": "1 ano", "Status": "Teste hidrostático das mangueiras de incêndio. RT solicita orçamento.", "Link PDF": "#"},
    {"Documento": "CONTROLE DE PRAGAS - DESINSETIZAÇÃO / DESRATIZAÇÃO DO GALPÃO", "Órgão": "EXPANSÃO", "Vencimento": "Mensal", "Status": "RT responsável pelo acompanhamento mensal.", "Link PDF": "#"},
    {"Documento": "CONTROLE DE PRAGAS NOS VEÍCULOS", "Órgão": "EXPANSÃO", "Vencimento": "Semestral", "Status": "A cada seis meses. RT responsável pelo agendamento.", "Link PDF": "#"},
    {"Documento": "LIMPEZA CAIXA D´ÁGUA - HIGIENIZAÇÃO DE RESERVATÓRIOS", "Órgão": "EXPANSÃO", "Vencimento": "Semestral", "Status": "A cada seis meses. RT responsável pelo agendamento.", "Link PDF": "#"},
    {"Documento": "CERTIFICADO CALIBRAÇÃO TERMOHIGRÔMETRO", "Órgão": "LABELT", "Vencimento": "1 ano", "Status": "Realizado pela Labelt (SP). Enviar aparelhos através de malote.", "Link PDF": "#"},
    {"Documento": "TREINAMENTO BRIGADA DE INCÊNDIO", "Órgão": "EMPRESA APROVADA", "Vencimento": "1 ano", "Status": "Renovado a cada 12 meses ou quando >50% dos membros forem substituídos.", "Link PDF": "#"},
    {"Documento": "CIPA - COMISSÃO INTERNA DE PREVENÇÃO DE ACIDENTES", "Órgão": "INST. ST. CATARINA", "Vencimento": "2 anos", "Status": "Necessário designar funcionário para CIPA em filiais com <20 func. Curso online.", "Link PDF": "#"},
    {"Documento": "IBAMA - CERTIDÃO NEGATIVA DE DÉBITOS", "Órgão": "IBAMA", "Vencimento": "Mensal", "Status": "Retirar a certidão negativa de débitos - Nada Consta no site do IBAMA.", "Link PDF": "#"}
]

# ==========================================
# BANCO DE DADOS: MOTORISTAS (Por Filial)
# ==========================================
banco_de_motoristas = {
    "São Bernardo do Campo": [
        {"Motorista": "ANDERSON LEANDRO GARBIN DE LIMA", "Placa": "EUB-7J59", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "CARLOS EDUARDO DE SOUZA SANTOS", "Placa": "QPX-8C11", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "CLAUDIO FENS", "Placa": "LNU-8A29", "Veículo": "DOBLÔ", "Status": "Ativo"},
        {"Motorista": "Cleiton Soares Marques", "Placa": "OSW-6D05", "Veículo": "PALIO", "Status": "Ativo"},
        {"Motorista": "DEREK SANTOS SILVA", "Placa": "GVE-7912", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "DIAS SÃO MATEUS ( PONTO DE APOIO HELIOPOLIS )", "Placa": "DTE-3236", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "EDER PIRES DOS REIS", "Placa": "DPE-4149", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "ELAINE CRISTINA LUCAS", "Placa": "DRG-6F36", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "EVANDRO RODRIGUES", "Placa": "DRG-6F36", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "FABIANO JOSE SILVA", "Placa": "ANU-0837", "Veículo": "PALIO", "Status": "Ativo"},
        {"Motorista": "FABIO CLAUDINO OLIVEIRA", "Placa": "FDW-1633", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "FELIPE GOMES DA SILVA", "Placa": "OPQ-0171", "Veículo": "DOBLÔ", "Status": "Ativo"},
        {"Motorista": "FELIPE ULIANA", "Placa": "JET-7A09", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "GENIVALDO GONÇALVES SANTOS", "Placa": "DRG-6F36", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "GILDEVAN DE JESUS PEREIRA", "Placa": "RHK-9F50", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "GILSON OTONI QUEIROZ SILVA", "Placa": "FSS-3G75", "Veículo": "DOBLÔ", "Status": "Ativo"},
        {"Motorista": "GIOMAR FELICIANO DE BARROS", "Placa": "DTE-3236", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "GIVALDO RODRIGUES DE OLIVEIRA", "Placa": "GYN-1167", "Veículo": "STRADA", "Status": "Ativo"},
        {"Motorista": "GUILHERME COSTA PIROZZI", "Placa": "DRG-6F36", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "GUILHERME HENRIQUE DA SILVA QUARTAROLLO", "Placa": "DUP-7638", "Veículo": "UNO", "Status": "Ativo"},
        {"Motorista": "ITALO CARVALHO SILVA", "Placa": "SUI-1C57", "Veículo": "HB20", "Status": "Ativo"},
        {"Motorista": "JANAÍNA GOMES DOS SANTOS FERREIRA", "Placa": "HHR-6535", "Veículo": "AGILE", "Status": "Ativo"},
        {"Motorista": "JOSE CARLOS ESPIRITO SANTO", "Placa": "FDE-9C68", "Veículo": "CIVIC", "Status": "Ativo"},
        {"Motorista": "JOSÉ MARCELO SIQUEIRA DO NASCIMENTO", "Placa": "OMG-3590", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "JOSUEL LIMA DA SILVA", "Placa": "GYN-1167", "Veículo": "STRADA", "Status": "Ativo"},
        {"Motorista": "LUANA PATRICIA SANTOS RIBEIRO", "Placa": "PUQ-2D01", "Veículo": "SAVEIRO", "Status": "Ativo"},
        {"Motorista": "LUIS VINICIUS GOMES SANTALUCIA", "Placa": "DTE-3236", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "LUIZ PAULO DE JESUS SANTOS", "Placa": "DTE-3236", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "MAICON GONCALVES DE ALMEIDA", "Placa": "FDW-1633", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "MARCONE PAULINO DE SOUZA", "Placa": "EVQ-7C90", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "MATHEUS HENRIQUE CAMPOS VENTURA COSTA", "Placa": "AND-8A44", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "NIOMAR APARECIDO NOGUEIRA", "Placa": "EZN-3A97", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "RHAUF MARCELINO NANINI SILVA", "Placa": "FCI-2H95", "Veículo": "DOBLÔ", "Status": "Ativo"},
        {"Motorista": "ROBERTO SILVA SANTOS", "Placa": "ONO-9282", "Veículo": "HR", "Status": "Ativo"},
        {"Motorista": "SEBASTIAO DA SILVA", "Placa": "RVL-5D46", "Veículo": "HB20", "Status": "Ativo"},
        {"Motorista": "SERGIO CRISPIM DE SOUZA", "Placa": "KPP-0761", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "THIAGO LUIZ DE SOUZA", "Placa": "FIU-1B15", "Veículo": "MONTANA", "Status": "Ativo"},
        {"Motorista": "THIAGO VINICIUS BASSO FAVALLI", "Placa": "AND-8A44", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "UELINTON CLEBER DE ASIS", "Placa": "GAO-0078", "Veículo": "FIORINO", "Status": "Ativo"},
        {"Motorista": "ULISSES TOLENTINO DELFINO", "Placa": "DTE-3236", "Veículo": "KOMBI", "Status": "Ativo"},
        {"Motorista": "WILSON ALVES SANTOS", "Placa": "DRG-6F36", "Veículo": "FIORINO", "Status": "Ativo"}
    ]
}

def inicializar_estado():
    """Garante que a tabela de demandas seja mantida na memória do Streamlit"""
    if 'demandas' not in st.session_state:
        st.session_state['demandas'] = pd.DataFrame(
            columns=['ID', 'Data', 'Título', 'Solicitante', 'GUT', 'Status']
        )