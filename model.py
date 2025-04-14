import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

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

# Preparar os dados para treino
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

# Salvar o modelo
import joblib
joblib.dump(model, 'model.pkl')
