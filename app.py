import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuração da página
st.set_page_config(page_title="Gestão de Demandas", page_icon="📊", layout="wide")

# 2. Inicializando o 'banco de dados' na memória do Streamlit
# O session_state garante que os dados não sumam ao clicar em um botão
if 'demandas' not in st.session_state:
    st.session_state['demandas'] = pd.DataFrame(
        columns=['ID', 'Data', 'Título', 'Solicitante', 'GUT', 'Status']
    )

# --- BARRA LATERAL (CADASTRO DE DEMANDAS) ---
st.sidebar.header("➕ Nova Demanda")
with st.sidebar.form("form_demanda", clear_on_submit=True):
    titulo = st.text_input("Título da Demanda")
    solicitante = st.text_input("Solicitante (Seu Nome/Setor)")
    
    st.markdown("**Avaliação GUT (1 a 5)**")
    g = st.slider("Gravidade (G)", 1, 5, 3, help="Qual o impacto se não for feito?")
    u = st.slider("Urgência (U)", 1, 5, 3, help="Qual o tempo disponível para fazer?")
    t = st.slider("Tendência (T)", 1, 5, 3, help="Qual o potencial de piorar com o tempo?")
    
    submit = st.form_submit_button("Cadastrar Demanda")
    
    if submit and titulo and solicitante:
        novo_id = len(st.session_state['demandas']) + 1
        gut_score = g * u * t
        
        nova_linha = pd.DataFrame([{
            'ID': novo_id,
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Título': titulo,
            'Solicitante': solicitante,
            'GUT': gut_score,
            'Status': 'Backlog'
        }])
        
        # Adiciona a nova demanda ao DataFrame
        st.session_state['demandas'] = pd.concat([st.session_state['demandas'], nova_linha], ignore_index=True)
        st.sidebar.success("Demanda cadastrada com sucesso!")

# --- ÁREA PRINCIPAL (DASHBOARD) ---
st.title("📊 Painel de Controle de Demandas")

df = st.session_state['demandas']

# 3. Métricas Rápidas
col1, col2, col3 = st.columns(3)
col1.metric("Total de Demandas", len(df))
col2.metric("No Backlog", len(df[df['Status'] == 'Backlog']))
col3.metric("Maior Score GUT", df['GUT'].max() if not df.empty else 0)

st.divider()

# 4. Tabela de Demandas Ordenada por Prioridade
st.subheader("📋 Fila de Prioridades (Ordenado pelo Score GUT)")
if not df.empty:
    # Ordena do maior GUT para o menor
    df_ordenado = df.sort_values(by='GUT', ascending=False).reset_index(drop=True)
    
    # Exibe a tabela e destaca visualmente a coluna GUT (quanto mais vermelho, mais crítico)
    st.dataframe(
        df_ordenado.style.background_gradient(subset=['GUT'], cmap='Reds'),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Nenhuma demanda cadastrada ainda. Use o menu lateral para adicionar a primeira!")