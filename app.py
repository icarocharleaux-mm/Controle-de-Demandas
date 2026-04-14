import streamlit as st
import pandas as pd
from datetime import datetime

# Importamos nossos novos módulos
import dados
import filtros

# ==========================================
# CONFIGURAÇÃO DA PÁGINA E ESTADO
# ==========================================
st.set_page_config(page_title="Painel Integrado - Grupo Dias+", page_icon="🏢", layout="wide")

# Inicializa o estado das demandas puxando a função lá do dados.py
dados.inicializar_estado()

# ==========================================
# MENU LATERAL (NAVEGAÇÃO)
# ==========================================
st.sidebar.image("https://via.placeholder.com/200x80.png?text=Grupo+Dias%2B", use_container_width=True)
st.sidebar.title("Navegação")
menu_selecionado = st.sidebar.radio("Ir para:", ["🏢 Visão Geral & Filiais", "📊 Gestão de Demandas (GUT)"])

st.sidebar.divider()

# ==========================================
# MÓDULO 1: GESTÃO DE FILIAIS
# ==========================================
if menu_selecionado == "🏢 Visão Geral & Filiais":
    st.title("🏢 Painel de Controle de Filiais")
    
    col_empresa, col_filial = st.columns(2)
    
    with col_empresa:
        empresa_selecionada = st.selectbox("Selecione a Empresa:", filtros.listar_empresas())
    
    filiais_disponiveis = filtros.listar_filiais(empresa_selecionada)
    
    with col_filial:
        if filiais_disponiveis:
            filial_selecionada = st.selectbox("Selecione a Filial:", filiais_disponiveis)
        else:
            st.warning("Nenhuma filial cadastrada.")
            filial_selecionada = None

    if filial_selecionada:
        dados_filial = filtros.obter_dados_filial(empresa_selecionada, filial_selecionada)
        
        st.subheader(f"📍 Detalhes: {dados_filial['filial']} - {dados_filial['uf']}")
        c1, c2, c3 = st.columns(3)
        c1.info(f"**Gestor:** {dados_filial['gestor']}\n\n**Telefone:** {dados_filial['telefone']}")
        c2.success(f"**CNPJ:** {dados_filial['cnpj']}\n\n**Resp. Técnico (RT):** {dados_filial['rt']}")
        c3.warning(f"**Endereço:** {dados_filial['endereco']}\n\n**CEP:** {dados_filial['cep']}")
        
        st.divider()
        aba1, aba2, aba3 = st.tabs(["📄 Regulatórios", "🚗 Motoristas", "🛠️ Outras Pastas"])
        
        with aba1:
            st.markdown(f"### Documentos Regulatórios ({filial_selecionada})")
            df_reg = filtros.obter_regulatorios()
            st.dataframe(
                df_reg, 
                use_container_width=True, 
                hide_index=True,
                column_config={"Link PDF": st.column_config.LinkColumn("Ver Documento")}
            )

        with aba2:
            st.markdown(f"### Frota e Motoristas ({filial_selecionada})")
            df_mot = filtros.obter_motoristas(filial_selecionada)
            if not df_mot.empty:
                st.dataframe(df_mot, use_container_width=True, hide_index=True)
            else:
                st.info("Nenhum motorista cadastrado para esta filial.")
                
        with aba3:
            st.markdown("### Treinamentos, Controle de Pragas e Funcionários")
            st.info("Módulos em desenvolvimento.")

# ==========================================
# MÓDULO 2: GESTÃO DE DEMANDAS
# ==========================================
elif menu_selecionado == "📊 Gestão de Demandas (GUT)":
    st.title("📊 Painel de Controle de Demandas")
    
    with st.expander("➕ Adicionar Nova Demanda (Matriz GUT)", expanded=False):
        with st.form("form_demanda", clear_on_submit=True):
            col_t, col_s = st.columns(2)
            titulo = col_t.text_input("Título da Demanda")
            solicitante = col_s.text_input("Solicitante (Seu Nome/Setor)")
            
            st.markdown("**Avaliação GUT (1 a 5)**")
            c_g, c_u, c_t = st.columns(3)
            g = c_g.slider("Gravidade (G)", 1, 5, 3, help="Impacto se não for feito?")
            u = c_u.slider("Urgência (U)", 1, 5, 3, help="Tempo disponível para fazer?")
            t = c_t.slider("Tendência (T)", 1, 5, 3, help="Potencial de piorar com o tempo?")
            
            submit = st.form_submit_button("Cadastrar Demanda", type="primary", use_container_width=True)
            
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
                
                st.session_state['demandas'] = pd.concat([st.session_state['demandas'], nova_linha], ignore_index=True)
                st.success("Demanda cadastrada com sucesso!")

    df = st.session_state['demandas']

    st.markdown("### Visão Geral")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Demandas", len(df))
    col2.metric("No Backlog", len(df[df['Status'] == 'Backlog']))
    col3.metric("Maior Score GUT", df['GUT'].max() if not df.empty else 0)

    st.divider()

    st.subheader("📋 Fila de Prioridades (Ordenado pelo Score GUT)")
    if not df.empty:
        df_ordenado = df.sort_values(by='GUT', ascending=False).reset_index(drop=True)
        # Removido o uso do style.background_gradient para evitar dependência do Matplotlib
        st.dataframe(
            df_ordenado,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Nenhuma demanda cadastrada ainda. Use o botão acima para adicionar a primeira!")