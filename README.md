# Gerador de Receitas Personalizadas com Google Generative AI

Este projeto é um aplicativo de geração de receitas personalizadas utilizando o modelo Gemini 1.5 da API Google Generative AI. A aplicação permite que o usuário insira ingredientes, temperos e o tipo de refeição desejado, e retorna uma receita personalizada em vários idiomas.

## Funcionalidades

- Geração de receitas com base em ingredientes e temperos disponíveis.
- Suporte para diferentes tipos de refeições, como doces, salgados, almoço, jantar, etc.
- Geração de receitas em múltiplos idiomas.
- Interface interativa utilizando Streamlit.

## Pré-requisitos

Antes de começar, você precisará ter os seguintes softwares instalados em sua máquina:

- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

   2. **Crie e ative um ambiente virtual:**

   - No Linux/macOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - No Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Instale as dependências:**

   - Após ativar o ambiente virtual, instale todas as dependências necessárias para o projeto executando:

     ```bash
     pip install -r requirements.txt
     ```

     Isso garantirá que todas as bibliotecas necessárias, como `streamlit`, `google-generativeai`, e outras mencionadas no arquivo `requirements.txt`, sejam instaladas corretamente.

4. **Configure sua chave de API do Google:**

   - Crie um arquivo chamado `config.yaml` na raiz do projeto. Esse arquivo será usado para armazenar sua chave de API do Google, garantindo que ela não seja exposta no código-fonte.

   - O conteúdo do `config.yaml` deve ser:

     ```yaml
     GOOGLE_API_KEY: 'sua_chave_de_api_aqui'
     ```

   - Substitua `'sua_chave_de_api_aqui'` pela sua chave de API real, que você pode obter no [Google Cloud Console](https://console.cloud.google.com/).

## Execução

1. **Inicie a aplicação:**

   - Com todas as dependências instaladas e a chave de API configurada, você pode iniciar a aplicação Streamlit com o seguinte comando:

     ```bash
     streamlit run chat.py
     ```

   - Esse comando irá abrir o aplicativo no seu navegador padrão, onde você poderá interagir com a interface para gerar receitas personalizadas.

2. **Utilize a Interface:**

   - Na interface do Streamlit, você poderá:
     - Selecionar o tipo de refeição (doce, salgado, almoço, jantar, etc.).
     - Inserir os ingredientes e temperos disponíveis.
     - Selecionar o idioma em que a receita deve ser gerada.
     - Gerar a receita clicando no botão "Gerar Receita".

   - A receita gerada será exibida na própria interface.

## Estrutura do Projeto

- `chat.py`: Script principal que executa a aplicação.
- `config.yaml`: Arquivo de configuração que contém a chave de API.
- `.gitignore`: Arquivo para ignorar arquivos e pastas desnecessárias no controle de versão.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto.

## Tecnologias Utilizadas

- **Python 3.9+**
- **Streamlit**
- **Google Generative AI (Gemini 1.5)**

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou faça um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

