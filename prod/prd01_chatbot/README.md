# Coach Virtual de Endurance 🏃‍♂️🚴‍♀️

## Como rodar localmente
Para executar este projeto na sua máquina, siga os passos abaixo.

## Pré-requisitos
- Conda instalado (ou [Miniconda](https://docs.conda.io/en/latest/miniconda.html)).
- Uma chave API da NVIDIA NIM (obtenha [aqui](https://build.nvidia.com/) )

## 1. Clonar o repositório
Abra seu terminal e clone o repositório:
 ```bash 
 git clone https://github.com/thiagoest/espec-genai.git
cd espec-genai
```
## 2. Configurar o Ambiente Virtual (Conda)
Crie um ambiente isolado para o projeto:
```bash
# Criar o ambiente com Python 3.10
conda create -n chatbot-env python=3.10 -y

# Ativa o ambiente
conda activate chatbot-env
```
## 3. Instalar dependências
``` bash
pip instal -r prod/prd01_chatbot/requirements.txt
```

## 4. Configurar as Secrets
Por segurança, sua chave de API não deve ficar exposta no código.
1. Na pasta ```prod/prd01_chatbot/```, crie uma pasta chamada ```.streamlit```.
2. Dentro dela, crie um arquivo chamado ```secrets.toml```.
3. Adicione sua chave no arquivo:

``` bash
# prod/prd01_chatbot/.streamlit/secrets.toml
NVIDIA_API_KEY = "sua-chave-aqui"
```

## 5. Executar o Chatbot
Navegue até o diretório do app e inicie o Streamlit

``` bash
cd prod/prd01_chatbot/
streamlit run app.py
```

O chatbot abrirá automaticamente no seu navegador em ```http://localhost:8501```.

## 📂 Estrutura do Projeto
- ```app.py```: Código principal do Chatbot.

- ```requirements.txt```: Dependências do projeto.

- ```.streamlit/```: Pasta de configurações e segredos (ignorada pelo Git).

Desenvolvido como parte do programa de especialização em GenAI.
