import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# --- 1. FUNÇÕES DO BANCO DE DADOS (SQLite) ---

def init_db():
    """Cria o arquivo do banco e a tabela se eles não existirem."""
    conn = sqlite3.connect('demandas_v2.db') # Mudei o nome para evitar conflito com o banco antigo
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS demandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            titulo TEXT,
            solicitante TEXT,
            prazo TEXT, 
            g INTEGER,
            u INTEGER,
            t INTEGER,
            gut_score INTEGER,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def excluir_demanda(id_demanda):
    """Remove uma demanda do banco de dados pelo ID."""
    conn = sqlite3.connect('demandas_v2.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM demandas WHERE id = ?', (id_demanda,))
    conn.commit()
    conn.close()

def inserir_demanda(titulo, solicitante, prazo, g, u, t, gut_score):
    """Insere uma nova linha na tabela do banco de dados."""
    conn = sqlite3.connect('demandas_v2.db')
    cursor = conn.cursor()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    
    cursor.execute('''
        INSERT INTO demandas (data, titulo, solicitante, prazo, g, u, t, gut_score, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Backlog')
    ''', (data_atual, titulo, solicitante, prazo, g, u, t, gut_score))
    
    conn.commit()
    conn.close()

def carregar_demandas():
    """Lê o banco de dados e transforma em um DataFrame do Pandas."""
    conn = sqlite3.connect('demandas_v2.db')
    # Adicionamos o prazo na consulta do banco
    query = "SELECT id as ID, data as Data, titulo as Título, solicitante as Solicitante, prazo as Prazo, gut_score as GUT, status as Status FROM demandas"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# --- 2. CONFIGURAÇÃO DA INTERFACE (STREAMLIT) ---

st.set_page_config(page_title="Gestão de Demandas", page_icon="📊", layout="wide")

init_db()

# --- BARRA LATERAL (CADASTRO DE DEMANDAS) ---
st.sidebar.header("➕ Nova Demanda")
with st.sidebar.form("form_demanda", clear_on_submit=True):
    titulo = st.text_input("Título da Demanda")
    solicitante = st.text_input("Solicitante (Seu Nome/Setor)")
    
    # Novo campo: Calendário interativo para o prazo
    prazo_input = st.date_input("Prazo Acordado")
    
    st.markdown("**Avaliação GUT (1 a 5)**")
    g = st.slider("Gravidade (G)", 1, 5, 3)
    u = st.slider("Urgência (U)", 1, 5, 3)
    t = st.slider("Tendência (T)", 1, 5, 3)
    
    submit = st.form_submit_button("Cadastrar Demanda")
    
    if submit and titulo and solicitante:
        gut_score = g * u * t
        
        # O Streamlit devolve uma data, nós transformamos em texto (DD/MM/AAAA) para salvar no banco
        prazo_formatado = prazo_input.strftime('%d/%m/%Y')
        
        # Passamos o prazo formatado para a função de salvar
        inserir_demanda(titulo, solicitante, prazo_formatado, g, u, t, gut_score)
        st.sidebar.success("Demanda cadastrada com sucesso!")

# --- ÁREA PRINCIPAL (DASHBOARD) ---
st.title("📊 Painel de Controle de Demandas")

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

# --- SEÇÃO DE GERENCIAMENTO (EXCLUSÃO) ---
st.divider()
with st.expander("🛠️ Gerenciar / Excluir Demandas"):
    if not df.empty:
        opcoes = [f"{row['ID']} - {row['Título']}" for index, row in df.iterrows()]
        selecionado = st.selectbox("Selecione a demanda para excluir:", opcoes)
        
        id_para_excluir = int(selecionado.split(" - ")[0])
        
        if st.button("❌ Confirmar Exclusão", type="primary"):
            excluir_demanda(id_para_excluir)
            st.success(f"Demanda {id_para_excluir} removida com sucesso!")
            st.rerun()
    else:
        st.write("Nenhuma demanda disponível para excluir.")
