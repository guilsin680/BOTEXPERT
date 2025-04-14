import requests
import json
import time
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from telegram import Bot

# Configurações
TELEGRAM_TOKEN = '8054415201:AAEs-_ZFCtBq2BM6FXYmkcmwB6l_mdeby-I'
CHAT_ID = '5775329663'
API_FOOTBALL_KEY = '7d42d1204d937e99f1139bdd3c845c48'

# Função para enviar mensagens no Telegram
def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

# Carregar e treinar modelo com dados históricos
def train_model():
    # Dados históricos simulados
    data = {
        "date": ["2023-05-01", "2023-05-02", "2023-05-03"],
        "home_team": ["Arsenal", "Chelsea", "Liverpool"],
        "away_team": ["Man United", "Tottenham", "Everton"],
        "home_goals": [3, 2, 1],
        "away_goals": [1, 1, 2],
        "home_team_last5_avg_goals": [2.4, 1.6, 1.9],
        "away_team_last5_avg_goals": [1.2, 1.4, 1.1],
        "home_team_rank": [2, 10, 5],
        "away_team_rank": [4, 7, 15],
    }
    df = pd.DataFrame(data)
    
    # Preparar os dados de treino
    features = [
        "home_team_last5_avg_goals", 
        "away_team_last5_avg_goals", 
        "home_team_rank", 
        "away_team_rank"
    ]
    X = df[features]
    
    # Transformar rótulos para treino (home, draw, away → 0, 1, 2)
    le = LabelEncoder()
    y = le.fit_transform(df["result"])
    
    # Dividir entre treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar o modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    return model

# Função para buscar jogos da API
def get_live_matches():
    url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures"
    headers = {
        'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com',
        'X-RapidAPI-Key': API_FOOTBALL_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()['response']

# Função para fazer previsões e enviar para Telegram
def predict_and_notify():
    model = train_model()
    matches = get_live_matches()

    for match in matches:
        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        prediction = model.predict([[home_team_last5_avg_goals, away_team_last5_avg_goals, home_team_rank, away_team_rank]])

        message = f"Jogo: {home_team} vs {away_team}\nPrevisão: {'Casa' if prediction[0] == 0 else 'Visitante' if prediction[0] == 2 else 'Empate'}"
        send_telegram_message(message)

# Cron job - rodar a cada 10 minutos
if __name__ == '__main__':
    while True:
        predict_and_notify()
        time.sleep(600)  # 10 minutos
