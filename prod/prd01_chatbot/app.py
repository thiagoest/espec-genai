import streamlit as st
from openai import OpenAI

# Configuração visual da página no navegador
st.set_page_config(page_title="Coach IA - Corrida & Ciclismo", page_icon="🏃‍♂️", layout="centered")

st.title("🏃‍♂️🚴‍♀️ Seu Coach Virtual de Endurance")
st.write("Bem-vindo! Sou seu treinador de corrida e ciclismo. Qual seu objetivo?")


# Acessando a chave da API de forma segura
try:
    api_key = st.secrets["NVIDIA_API_KEY"]
except KeyError:
    st.error("Chave da API não encontrada! Verifique o arquivo .streamlit/secrets.toml")
    st.stop()

# Configurando o cliente para apontar para os servidores da NVIDIA
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

# System Prompt
SYSTEM_PROMPT = """
Você é um treinador de corrida e ciclismo com especializao em treinamento desportivo e certificado pela Confederacao Brasileira de Triathlon
altamente especializado, motivador, exigente e experiente.
Suas diretrizes são:
- Use o sistema métrico: quilômetros (km), metros (m).
- Para corrida, fale em 'pace' (min/km). Para ciclismo, fale em velocidade média (km/h) ou zonas de esforço.
- Suas respostas devem ser estruturadas (use listas, tópicos ou tabelas para planilhas de treino).
- Seja encorajador, empático, mas realista sobre prazos esportivos.
- Sempre pergunte sobre o histórico de treinos, lesões e seus tempos atuais em 5 ou 10 km para personalizar o plano.
- Aviso Crítico: Se o usuário mencionar dores agudas ou lesões, recomende imediatamente que procure um médico ou fisioterapeuta, lembrando que você é uma IA de treinamento.
"""

# Historico de mensagens + system prompt
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Exibindo o histórico de mensagens na tela
for msg in st.session_state.messages:
    if msg["role"] != "system":
        # Usando ícones diferentes para o usuário e para o robô
        avatar = "🤖" if msg["role"] == "assistant" else "👤"
        st.chat_message(msg["role"], avatar=avatar).write(msg["content"])
# Recebendo a pergunta do usuário
if prompt := st.chat_input("Ex: Me monte um treino de corrida para baixar de 50 min nos 10km"):
    
    # Adiciona a pergunta no histórico e mostra na tela
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="👤").write(prompt)

    # Chamando a API da NVIDIA para processar a resposta
    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        placeholder.markdown("Analisando métricas e preparando o treino...")
        
        try:
            # Utilizando o Llama 3.1 8B para respostas rapidas
            response = client.chat.completions.create(
                model="meta/llama-3.1-8b-instruct",
                messages=st.session_state.messages,
                max_tokens=1024,
                temperature=0.7 # Um pouco de criatividade para a parte motivacional, sem perder o rigor técnico
            )
            
            msg_resposta = response.choices[0].message.content
            # Atualiza o texto de carregamento com a resposta final
            placeholder.markdown(msg_resposta)
            
            # Salva a resposta do assistente no histórico para manter o contexto nas próximas perguntas
            st.session_state.messages.append({"role": "assistant", "content": msg_resposta})
        
        except Exception as e:
            placeholder.error(f"Erro ao conectar com a API: {e}")

##########################