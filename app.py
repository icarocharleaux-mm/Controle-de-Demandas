import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# --- 1. FUNÇÕES DO BANCO DE DADOS (SQLite) ---

def init_db():
    """Cria o arquivo do banco e a tabela se eles não existirem."""
    conn = sqlite3.connect('demandas.db') # Cria o arquivo
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS demandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            titulo TEXT,
            solicitante TEXT,
            g INTEGER,
            u INTEGER,
            t INTEGER,
            gut_score INTEGER,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_demanda(titulo, solicitante, g, u, t, gut_score):
    """Insere uma nova linha na tabela do banco de dados."""
    conn = sqlite3.connect('demandas.db')
    cursor = conn.cursor()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    
    cursor.execute('''
        INSERT INTO demandas (data, titulo, solicitante, g, u, t, gut_score, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'Backlog')
    ''', (data_atual, titulo, solicitante, g, u, t, gut_score))
    
    conn.commit()
    conn.close()

def carregar_demandas():
    """Lê o banco de dados e transforma em um DataFrame do Pandas."""
    conn = sqlite3.connect('demandas.db')
    # O Pandas tem uma função mágica que lê o SQL direto para a tabela!
    query = "SELECT id as ID, data as Data, titulo as Título, solicitante as Solicitante, gut_score as GUT, status as Status FROM demandas"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# --- 2. CONFIGURAÇÃO DA INTERFACE (STREAMLIT) ---

st.set_page_config(page_title="Gestão de Demandas", page_icon="📊", layout="wide")

# Inicializa o banco de dados (roda toda vez que a página carrega, mas só cria na primeira vez)
init_db()

# --- BARRA LATERAL (CADASTRO DE DEMANDAS) ---
st.sidebar.header("Adicionar Demanda")
with st.sidebar.form("form_demanda", clear_on_submit=True):
    titulo = st.text_input("Título da Demanda")
    solicitante = st.text_input("Solicitante (Seu Nome/Setor)")
    
    st.markdown("**Avaliação GUT (1 a 5)**")
    g = st.slider("Gravidade (G)", 1, 5, 3)
    u = st.slider("Urgência (U)", 1, 5, 3)
    t = st.slider("Tendência (T)", 1, 5, 3)
    
    submit = st.form_submit_button("Cadastrar Demanda")
    
    if submit and titulo and solicitante:
        gut_score = g * u * t
        # Salva direto no banco de dados ao invés da memória
        inserir_demanda(titulo, solicitante, g, u, t, gut_score)
        st.sidebar.success("Demanda cadastrada com sucesso!")

# --- ÁREA PRINCIPAL (DASHBOARD) ---
st.title("📊 Painel de Controle de Demandas")

# Carrega os dados sempre fresquinhos do banco de dados
df = carregar_demandas()

# 3. Métricas Rápidas
col1, col2, col3 = st.columns(3)
col1.metric("Total de Demandas", len(df))
col2.metric("No Backlog", len(df[df['Status'] == 'Backlog']))
col3.metric("Maior Score GUT", df['GUT'].max() if not df.empty else 0)

st.divider()

# 4. Tabela de Demandas Ordenada por Prioridade
st.subheader("📋 Fila de Prioridades (Ordenado pelo Score GUT)")
if not df.empty:
    df_ordenado = df.sort_values(by='GUT', ascending=False).reset_index(drop=True)
    st.dataframe(
        df_ordenado.style.background_gradient(subset=['GUT'], cmap='Reds'),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Nenhuma demanda cadastrada ainda. Use o menu lateral para adicionar a primeira!")
