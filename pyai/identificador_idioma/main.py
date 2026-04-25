import requests
import re
import os
import pandas as pd

# Constantes
TIMEOUT = 10
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

url = input("Digite a URL para ser analisada:")

def baixar_texto(url): 
    # Simulando requisicao de um usuario humano
    headers = {'User-Agent': 'Mozilla/5.0...'}

    try:
        # Carrega conteudo da url
        resposta = requests.get(url, headers=headers, timeout=TIMEOUT)
        # Retorna erro se status <> de 200
        resposta.raise_for_status()

        # Retorna apenas o texto em string
        return resposta.text
    
    except Exception as e:
        # Captura o erro, lança uma exceçao e interrompe a execucao do programa
        print(f"Erro ao acessar {url}: {e}")
        raise

def limpar_texto(texto):
    texto_limpo = texto.lower()

    # Remove marcadores HTML
    texto_limpo = re.sub(r'<[^>]+>', '', texto_limpo)

    # Remove caracteres diferente de letras
    texto_limpo = re.sub(r'[^a-zà-ÿ\s]', '', texto_limpo)

    # Remove espacos em branco
    texto_limpo = re.sub(r'\s+', ' ', texto_limpo)

    return texto_limpo.strip()

def calcular_frequencia(texto_limpo):
    # Inicializando dicionario
    contagem = {}

    # Calcula contagem de cada letra
    for letra in texto_limpo:
        if letra != ' ':
            contagem[letra] = contagem.get(letra, 0) + 1

    # Calcula total de letras
    tot_letras = sum(contagem.values())

    # Condicao de seguranca para evitar divisao por zero
    if tot_letras == 0:
        return {}
    
    # Calcula freq relativa de cada letra
    freq = {letra: round(valor / tot_letras, 5) 
            for letra, valor in sorted(contagem.items())}

    return freq

def carregar_perfis():
    path_csv = os.path.join(DATA_DIR, 'letter_frequency.csv')

    try:
        # Carrega csv
        df = pd.read_csv(path_csv, sep=";")

        # Definindo index
        df.set_index('Letter', inplace=True)

        # Remove simbolo % e converte para float
        for col in df.columns:
            df[col] = df[col].str.replace('%', '').astype(float) / 100
        return df
    
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado em {caminho_csv}")
        return None
    
def comparar_perfis(freq_texto, perfis):

    # Converte dict para data frame com frequencias calculadas
    # As letras sao os indices
    df_freq_obs = pd.DataFrame.from_dict(freq_texto, orient= 'index', columns= ['freq'])

    # Carrega data frame com freq. de referencia de cada idioma
    df_freq_idiomas = perfis

    # Adciona nova coluna com freq calculadas no data frame de referencia
    # Inner join usando indice de ambos os data frames (letras)
    df_join = df_freq_idiomas.join(df_freq_obs, how = 'inner')

    # Calculando distancia entre a freq do texto para cada idioma
    erros = {}
    for idioma in [c for c in df_join.columns if c != 'freq']:
        # Distancia euclidiana: sqrt( soma( (a - b)^2 ) )
        distancia = ( ( df_join[idioma] - df_join['freq'] ) ** 2 ).sum() ** 0.5
        erros[idioma] = round(distancia,5)

    ranking = pd.Series(erros).sort_values()
    return ranking

# Execucao principal
#url = "https://www.funiviedelbaldo.it/it/" #italia
#url = "https://es.wikipedia.org/wiki/Real_Madrid_Club_de_F%C3%BAtbol" #espanha
#url = "https://de.wikipedia.org/wiki/Potsdam" #alemanha

if __name__ == "__main__":
    texto = baixar_texto(url)
    print("Texto carregado...")
    texto_limpo = limpar_texto(texto)
    print("Texto limpo...")

    freq_calculada = calcular_frequencia(texto_limpo)
    freq_referencia = carregar_perfis()

    print("Idiomas mais prováveis:")
    print(comparar_perfis(freq_calculada, freq_referencia).head(3))


