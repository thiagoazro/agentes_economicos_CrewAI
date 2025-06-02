# main.py

import os

print("🔁 Executando coleta de indicadores econômicos...")
os.system("python scripts/indicadores_economicos.py")

print("📈 Executando coleta das ações da Bovespa...")
os.system("python scripts/acoes.py")

print("📰 Executando coleta de notícias econômicas...")
os.system("python scripts/noticias.py")

print("🧠 Executando análise dos agentes econômicos (CrewAI)...")
os.system("python scripts/agentes_economicos.py")

print("🚀 Iniciando dashboard Streamlit...")

# Comando para iniciar o Streamlit conforme especificado.
# A flag --server.headless=true é recomendada para ambientes de servidor, pois evita
# que o Streamlit tente abrir uma janela de navegador.
# Para Azure App Service, a porta geralmente é fornecida pela variável de ambiente PORT.
# Se você quiser usar a porta 8000 fixamente, o comando abaixo está correto.
# Se quiser usar a porta do Azure: server_port = os.environ.get('PORT', '8000')
# e então usar f"... --server.port={server_port} ..."
streamlit_command = "streamlit run streamlit/dashboard.py --server.port=8000 --server.address=0.0.0.0 --server.headless=true"

# Flags adicionais que podem ser úteis em alguns cenários de proxy/deploy (descomente se necessário):
# streamlit_command += " --server.enableCORS=false --server.enableXsrfProtection=false"

print(f"Executando comando Streamlit: {streamlit_command}")
os.system(streamlit_command)