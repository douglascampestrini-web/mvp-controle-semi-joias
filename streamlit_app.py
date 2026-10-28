
import streamlit as st

st.set_page_config(
    page_title="Controle de Estoque",
    page_icon="📦",
    layout="centered"
)

if "produtos" not in st.session_state:
    st.session_state.produtos = []

if "alto_contraste" not in st.session_state:
    st.session_state.alto_contraste = False

st.title("📦 Controle de Estoque de Semijoias")
st.write("Cadastre produtos e acompanhe as quantidades disponíveis.")

st.session_state.alto_contraste = st.toggle(
    "Ativar alto contraste",
    value=st.session_state.alto_contraste
)

if st.session_state.alto_contraste:
    st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    p, label, h1, h2, h3, span {
        color: #FFFFFF !important;
    }
    .stButton button {
        background-color: #FFFF00;
        color: #000000;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

aba_cadastro, aba_estoque = st.tabs(
    ["Cadastrar produto", "Consultar estoque"]
)

with aba_cadastro:
    with st.form("form_cadastro"):
        nome = st.text_input("Nome do produto")
        quantidade = st.number_input(
            "Quantidade em estoque",
            min_value=0,
            step=1
        )
        enviar = st.form_submit_button("Cadastrar")

        if enviar:
            if not nome.strip():
                st.error("Informe o nome do produto.")
            else:
                st.session_state.produtos.append({
                    "nome": nome.strip(),
                    "quantidade": int(quantidade)
                })
                st.success("Produto cadastrado com sucesso!")

with aba_estoque:
    st.subheader("Produtos cadastrados")

    if not st.session_state.produtos:
        st.info("Nenhum produto cadastrado.")
    else:
        st.dataframe(
            st.session_state.produtos,
            use_container_width=True,
            hide_index=True
        )

        st.metric(
            "Total de produtos cadastrados",
            len(st.session_state.produtos)
        )
