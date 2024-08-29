import streamlit as st
import os
import yaml
import google.generativeai as genai

# Carregar a chave de API do Google a partir do config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['GOOGLE_API_KEY'] = config['GOOGLE_API_KEY']

# Configurar a API do Google Generative AI
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Criar o Wrapper para o modelo Gemini
class GeminiWrapper:
    def __init__(self, model_name):
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

# Inicializar o modelo Gemini 1.5 Flash
def create_google_client():
    return GeminiWrapper('gemini-1.5-flash')

# Template do prompt para o chatbot de receitas
template = '''
Você é um chef de cozinha especializado em criar receitas personalizadas.
O usuário deseja preparar uma refeição "{tipo_refeicao}" para {pessoas} pessoas.

Ingredientes disponíveis: {ingredientes}.
Temperos disponíveis: {temperos}.

Escreva uma receita detalhada em {idioma} que utilize os ingredientes e temperos listados acima.
A receita deve ser fácil de seguir e adequada para o número de pessoas especificado.
'''

def generate_recipe(service, prompt):
    # Chama o método correto para gerar a receita usando o modelo Gemini
    return service.generate(prompt)

# Opções para o usuário
tipos_refeicao = ['Doce', 'Salgado', 'Almoço', 'Lanche', 'Jantar', 'Sobremesa']
idiomas = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão']

# Interface do usuário
st.title('Gerador de Receitas Personalizadas: BeNext.AI')

tipo_refeicao = st.sidebar.selectbox('Selecione o tipo de refeição:', tipos_refeicao)
pessoas = st.sidebar.number_input('Para quantas pessoas?', min_value=1, max_value=20, value=4)
ingredientes = st.sidebar.text_area('Insira os ingredientes disponíveis (separados por vírgula):')
temperos = st.sidebar.text_area('Insira os temperos disponíveis (separados por vírgula):')
idioma = st.sidebar.selectbox('Selecione o idioma:', idiomas)

if st.sidebar.button('Gerar Receita'):
    prompt = template.format(
        tipo_refeicao=tipo_refeicao,
        pessoas=pessoas,
        ingredientes=ingredientes,
        temperos=temperos,
        idioma=idioma
    )

    service = create_google_client()
    response_text = generate_recipe(service, prompt)

    st.subheader('Receita Gerada:')
    st.write(response_text)
