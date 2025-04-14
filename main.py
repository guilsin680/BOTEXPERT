import os
import joblib
import requests
import pandas as pd
from datetime import datetime
from time import sleep

# Carregar variáveis de ambiente
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
API_FOOTBALL_KEY = os.getenv('API_FOOTBALL_KEY')

# Carregar o modelo treinado
model = joblib.load('model.pkl')

# Função para enviar mensagem no Telegram
def enviar_mensagem_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': mensagem,
    }
    response = requests.get(url, params=params)
    return response.json()

# Função para pegar jogos do dia
def pegar_jogos_do_dia():
    url = f"https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_FOOTBALL_KEY}
    params = {
        "dateFrom": datetime.now().strftime('%Y-%m-%d'),
        "dateTo": datetime.now().strftime('%Y-%m-%d')
    }
    response = requests.get(url, headers=headers, params=params)
    jogos = response.json()['matches']
    return jogos

# Função para prever o resultado de um jogo
def prever_resultado(jogo):
    # Exemplo de como pegar os dados do jogo (substitua com dados reais)
    dados_entrada = {
        "home_team_last5_avg_goals": [jogo['score']['fullTime']['homeTeam']],
        "away_team_last5_avg_goals": [jogo['score']['fullTime']['awayTeam']],
        "home_team_rank": [jogo['homeTeam']['id']],  # Exemplo: Rank do time da casa
        "away_team_rank": [jogo['awayTeam']['id']],  # Exemplo: Rank do time visitante
    }

    # Criar DataFrame com os dados
    df_entrada = pd.DataFrame(dados_entrada)

    # Fazer a previsão
    previsao = model.predict(df_entrada)

    # Mapear a previsão para o rótulo original
    resultados = ['Home', 'Away', 'Draw']
    return resultados[previsao[0]]

# Função para construir a mensagem para o Telegram
def construir_mensagem(jogo, resultado_previsao):
    mensagem = f"Jogo: {jogo['homeTeam']['name']} vs {jogo['awayTeam']['name']}\n"
    mensagem += f"Data: {jogo['utcDate']}\n"
    mensagem += f"Previsão: {resultado_previsao}\n"
    return mensagem

# Função principal
def main():
    while True:
        jogos = pegar_jogos_do_dia()

        for jogo in jogos:
            resultado_previsao = prever_resultado(jogo)
            mensagem = construir_mensagem(jogo, resultado_previsao)
            enviar_mensagem_telegram(mensagem)

        # Espera de 10 minutos antes de fazer outra rodada
        sleep(600)

if __name__ == "__main__":
    main()
