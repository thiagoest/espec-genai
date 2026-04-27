# Identificador de Idioma
Este projeto realiza a extração de texto de páginas web e identifica o idioma predominante através da análise estatística da frequência de letras, comparando o perfil do texto com dados de referência.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e rodar o identificador:

### 1. Preparação do Ambiente
Este projeto utiliza o **Conda**. No terminal, dentro da pasta raiz do projeto, execute:

```bash
# Cria o ambiente na pasta local 'env'
conda create -p ./env python=3.10 -y

# Ativa o ambiente
conda activate ./env

# Instala as dependências obrigatórias
pip install requests pandas

```

### 2. Execução
```bash
python main.py
```

### 3. Detalhes da implementação

- Extração: Uso da biblioteca `requests` com tratamento de exceções e headers de navegador.

- Limpeza: Processamento com Expressões Regulares (`re`) para remoção de HTML e normalização de caracteres.

- Classificação: Cálculo de Distância Euclidiana entre o vetor de frequências observado e os perfis do arquivo `data/frequencia_letras.csv`.

- Portabilidade: Uso de caminhos dinâmicos com os.path para garantir execução em qualquer diretório.


### 3. URL's para testar
O progrma foi testado com as seguintes URL's:

- Italiano: https://www.funiviedelbaldo.it/it/" 
- Espanhol: https://es.wikipedia.org/wiki/Real_Madrid_Club_de_F%C3%BAtbol
- Alemão: https://de.wikipedia.org/wiki/Potsdam
