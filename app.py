import streamlit as st

# 1. Configurações de SEO e Identidade Visual Profissional
st.set_page_config(page_title="BioEstética - Saúde e Metabolismo", page_icon="⚖️")

# Estilo Visual Profissional (Clean e Confiável)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { background-color: #d4a373; color: white; border-radius: 8px; width: 100%; }
    h1, h2, h3 { color: #588157; }
    .info-box { background-color: #f1f8e9; padding: 20px; border-radius: 10px; border-left: 5px solid #588157; }
    </style>
    """, unsafe_allow_html=True)

# 2. Menu Lateral de Navegação (Essencial para o AdSense)
st.sidebar.title("🌿 Menu BioEstética")
aba = st.sidebar.radio("Selecione uma seção:", 
                       ["Calculadora Metabólica", "Artigos: Saúde e Peso", 
                        "Sobre a Especialista", "Políticas de Privacidade"])

if aba == "Calculadora Metabólica":
    st.title("⚖️ Calculadora de Calorias e IMC")
    st.write("Calcule suas necessidades energéticas diárias e seu índice de massa corporal com precisão.")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Seu Peso (kg):", min_value=30.0, value=70.0)
            idade = st.number_input("Sua Idade:", min_value=15, value=30)
        with col2:
            altura = st.number_input("Sua Altura (cm):", min_value=100, value=170)
            sexo = st.selectbox("Sexo Biológico:", ["Feminino", "Masculino"])
    
    atividade = st.selectbox("Nível de Atividade Física:", 
                             ["Sedentário", "Leve (1-2 dias/sem)", "Moderado (3-5 dias/sem)", "Intenso (Todo dia)"])

    if st.button("Analisar Metabolismo"):
        # Cálculo Simplificado de Calorias (Harris-Benedict)
        if sexo == "Feminino":
            tmb = 655 + (9.6 * peso) + (1.8 * (altura/100)) - (4.7 * idade)
        else:
            tmb = 66 + (13.7 * peso) + (5 * (altura/100)) - (6.8 * idade)
        
        imc = peso / ((altura/100)**2)
        
        st.success(f"Seu IMC é: **{imc:.1f}**")
        st.info(f"Sua Taxa Metabólica Basal é de aproximadamente **{int(tmb)} calorias/dia**.")
        st.write("Nota: Este cálculo é uma estimativa. Consulte sempre um profissional.")

elif aba == "Artigos: Saúde e Peso":
    st.title("📚 Conteúdo Educativo e Bem-Estar")
    st.markdown("""
    <div class='info-box'>
    <h3>Como acelerar seu metabolismo de forma saudável</h3>
    Para que o corpo funcione em sua máxima performance, não basta apenas contar calorias. A hidratação correta, o sono reparador e a ingestão equilibrada de micronutrientes são fundamentais.
    
    <h3>O que é o IMC?</h3>
    O Índice de Massa Corporal é uma medida internacional usada para calcular se uma pessoa está no peso ideal. Embora útil, ele não distingue massa gorda de massa magra, por isso deve ser analisado em conjunto com outros exames biomédicos.
    
    <h3>Dicas para o Dia a Dia:</h3>
    * Priorize alimentos integrais e proteínas de alto valor biológico.
    * Mantenha uma rotina de exercícios resistidos para preservar a massa muscular.
    * Evite dietas restritivas sem acompanhamento profissional.
    </div>
    """, unsafe_allow_html=True)

elif aba == "Sobre a Especialista":
    st.title("👩‍⚕️ Vanusa Cigognini Biomédica")
    st.write("""
    Especialista em saúde integrativa e estética avançada. 
    Este portal foi desenvolvido para oferecer ferramentas de autocuidado e informações baseadas em evidências para quem busca uma vida mais equilibrada e saudável.
    """)

elif aba == "Políticas de Privacidade":
    st.title("🔒 Privacidade e Termos")
    st.write("""
    Este site cumpre todas as normas do Google AdSense. 
    * Não coletamos dados de saúde sensíveis.
    * Utilizamos cookies para análise de tráfego e exibição de anúncios.
    * Todas as informações geradas nas calculadoras são para fins informativos.
    """)

# 3. Rodapé com Assinatura Profissional (Crucial para o Google)
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Vanusa Cigognini Biomédica | Saúde e Estética Integrativa</p>", unsafe_allow_html=True)
