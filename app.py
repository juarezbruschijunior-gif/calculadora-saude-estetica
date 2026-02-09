import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="BioSaúde & Estética - Calculadora de IMC", page_icon="⚖️")

# 2. ADSENSE (Obrigatório para gerar lucro)
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
    """,
    height=0,
)

# 3. MENU LATERAL PROFISSIONAL
st.sidebar.title("💎 BioEstética Menu")
aba = st.sidebar.radio("Navegar:", ["Calculadora de IMC", "Artigos de Saúde", "Sobre a Especialista", "Privacidade"])

if aba == "Calculadora de IMC":
    st.title("⚖️ Calculadora de Índice de Massa Corporal (IMC)")
    st.write("Ferramenta de análise corporal com base em parâmetros biométricos.")
    
    # Imagem profissional de estética/saúde
    st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=1000&auto=format&fit=crop", caption="Saúde Integrativa e Estética Avançada")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso (kg):", min_value=10.0, value=70.0, step=0.1)
        altura = st.number_input("Altura (m):", min_value=0.5, value=1.70, step=0.01)
    with col2:
        idade = st.number_input("Idade:", min_value=1, value=30, step=1)
        sexo = st.selectbox("Sexo:", ["Feminino", "Masculino"])

    if st.button("Analisar Composição Corporal"):
        imc = peso / (altura ** 2)
        st.subheader(f"Seu IMC: {imc:.2f}")

        if imc < 18.5:
            st.warning("Classificação: Abaixo do peso")
            st.write("💡 **Dica:** Procure um plano alimentar para ganho de massa magra e equilíbrio nutricional.")
        elif 18.5 <= imc < 24.9:
            st.success("Classificação: Peso Normal")
            st.write("💡 **Dica:** Parabéns! Mantenha a prática de exercícios e uma dieta rica em antioxidantes.")
        elif 25 <= imc < 29.9:
            st.warning("Classificação: Sobrepeso")
            st.write("💡 **Dica:** Pequenos ajustes na rotina, como reduzir açúcares processados, podem prevenir a evolução para obesidade.")
        else:
            st.error("Classificação: Obesidade")
            st.write("💡 **Dica:** É recomendável um acompanhamento multidisciplinar para reduzir riscos inflamatórios e metabólicos.")

elif aba == "Artigos de Saúde":
    st.title("🔬 Artigos e Visão Biomédica")
    
    st.image("https://images.unsplash.com/photo-1505751172876-fa1923c5c528?q=80&w=1000&auto=format&fit=crop", caption="Análise Clínica e Bem-estar")
    
    st.header("1. Os Perigos da Obesidade")
    st.write("""
    A obesidade não é apenas uma questão estética, mas uma doença crônica inflamatória. Ela aumenta drasticamente o risco de:
    * **Doenças Cardiovasculares:** O excesso de gordura visceral sobrecarrega o coração.
    * **Diabetes Tipo 2:** A resistência à insulina é uma consequência direta do tecido adiposo em excesso.
    * **Problemas Articulares:** O sobrepeso causa desgaste prematuro em joelhos e coluna.
    """)

    st.header("2. A Estética como Aliada da Saúde")
    st.write("""
    Procedimentos estéticos avançados auxiliam na redução de gordura localizada e melhora da autoestima, 
    mas devem sempre ser acompanhados de hábitos saudáveis para resultados duradouros.
    """)

elif aba == "Sobre a Especialista":
    st.title("💎 Especialista Responsável")
    st.write("Esta página conta com a curadoria técnica de:")
    st.subheader("Vanusa Cigognini")
    st.write("**Biomédica Esteta**")
    st.write("""
    Especialista em saúde integrativa e procedimentos de alta performance estética. 
    Focada em resultados que unem beleza e equilíbrio biológico.
    """)

elif aba == "Privacidade":
    st.title("Política de Privacidade")
    st.write("Este site utiliza cookies para monetização via Google AdSense. Não coletamos dados pessoais sensíveis.")

# 4. RODAPÉ DE AUTORIDADE (Personalizado com o nome da Vanusa)
st.write("---")
st.caption("Desenvolvido por **BioEstética Digital**")
st.caption("Referência Técnica: **Vanusa Cigognini - Biomédica Esteta** © 2026")
