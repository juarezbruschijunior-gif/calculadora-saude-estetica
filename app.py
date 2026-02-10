import streamlit as st

# 1. Configurações de SEO e Título
st.set_page_config(page_title="Vanusa Cigognini - Bioestética Integrativa", page_icon="🌿")

# Estilo Visual para Aprovação Google (Clean e Elegante)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { background-color: #8da98d; color: white; border-radius: 10px; height: 3em; }
    h1, h2 { color: #4a6741; font-family: 'Helvetica', sans-serif; }
    .content-section { background-color: #f9fbf9; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Menu de Navegação (Obrigatório para o AdSense)
st.sidebar.title("🧭 Navegação do Portal")
aba = st.sidebar.radio("Escolha uma área:", 
                       ["Calculadora de Calorias", "Metabolismo e Saúde", 
                        "Sobre Vanusa Cigognini", "Termos e Privacidade"])

if aba == "Calculadora de Calorias":
    st.title("⚖️ Calculadora Metabólica Profissional")
    st.write("Calcule suas necessidades energéticas diárias com base em parâmetros biométricos avançados.")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Peso Atual (kg):", min_value=30.0, value=70.0)
            idade = st.number_input("Idade:", min_value=12, max_value=100, value=35)
        with col2:
            altura = st.number_input("Altura (cm):", min_value=100, max_value=250, value=165)
            sexo = st.selectbox("Sexo Biológico:", ["Feminino", "Masculino"])
    
    nivel = st.selectbox("Frequência de Atividade Física:", 
                         ["Sedentário (pouco exercício)", "Leve (1-3 dias/sem)", "Moderado (3-5 dias/sem)", "Intenso (todo dia)"])

    if st.button("Calcular Necessidade Diária"):
        # Cálculo Harris-Benedict revisado
        if sexo == "Feminino":
            tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
        else:
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
            
        st.success(f"Sua Taxa Metabólica Basal é de aproximadamente **{int(tmb)} kcal**.")
        st.info("Utilize este dado para planejar suas refeições com foco em saúde integrativa.")

elif aba == "Metabolismo e Saúde":
    st.title("📚 Guia de Saúde e Bioestética")
    st.markdown("""
    <div class='content-section'>
    <h3>A Ciência por trás das Calorias</h3>
    O equilíbrio metabólico é a chave para a longevidade. Entender sua Taxa Metabólica Basal (TMB) permite que você forneça ao organismo exatamente o que ele precisa para as funções vitais, evitando o estresse oxidativo e o acúmulo de gordura visceral.
    
    <h3>Bioestética Integrativa</h3>
    A estética moderna vai além da superfície. Na visão da biomedicina estética, o cuidado começa de dentro para fora. A nutrição celular e o equilíbrio calórico influenciam diretamente na saúde da pele, cabelos e na resposta a procedimentos estéticos.
    
    <h3>Dicas para Manter o Equilíbrio:</h3>
    <ul>
        <li>Mantenha uma hidratação constante (35ml por kg de peso).</li>
        <li>Priorize alimentos com baixo índice glicêmico para evitar picos de insulina.</li>
        <li>Consulte sempre um especialista para ajustar sua dieta ao seu biotipo.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif aba == "Sobre Vanusa Cigognini":
    st.title("👩‍⚕️ Vanusa Cigognini Biomédica")
    st.markdown("""
    <div class='content-section'>
    <b>Vanusa Cigognini</b> atua na área de Biomedicina Estética, focando em tratamentos personalizados que unem tecnologia e bem-estar. 
    Este portal é uma extensão de seu compromisso com a educação em saúde, oferecendo ferramentas para que cada pessoa possa entender melhor seu próprio corpo e metabolismo.
    </div>
    """, unsafe_allow_html=True)

elif aba == "Termos e Privacidade":
    st.title("🔒 Segurança e Transparência")
    st.write("""
    Este site segue rigorosamente as políticas do Google AdSense. 
    * **Transparência:** As calculadoras são ferramentas informativas e não substituem consulta médica.
    * **Dados:** Não armazenamos informações pessoais ou sensíveis dos usuários.
    * **Anúncios:** Utilizamos cookies para oferecer uma experiência personalizada através do AdSense.
    """)

# 3. Rodapé de Autoridade (O Pulo do Gato para o AdSense)
st.markdown("---")
st.markdown("<p style='text-align: center;'><b>Vanusa Cigognini Biomédica - Estética Avançada e Saúde Integrativa</b><br>© 2026 Todos os direitos reservados.</p>", unsafe_allow_html=True)
