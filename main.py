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
€•]      Œsklearn.ensemble._forest”ŒRandomForestClassifier”“”)”}”(Œ	estimator”Œsklearn.tree._classes”ŒDecisionTreeClassifier”“”)”}”(Œ	criterion”Œgini”Œsplitter”Œbest”Œ	max_depth”NŒmin_samples_split”KŒmin_samples_leaf”KŒmin_weight_fraction_leaf”G        Œmax_features”NŒmax_leaf_nodes”NŒrandom_state”NŒmin_impurity_decrease”G        Œclass_weight”NŒ	ccp_alpha”G        Œ
monotonic_cst”NŒ_sklearn_version”Œ1.6.1”ubŒn_estimators”KdŒestimator_params”(hhhhhhhhhhht”Œ	bootstrap”ˆŒ	oob_score”‰Œn_jobs”NhK*Œverbose”K Œ
warm_start”‰hNŒmax_samples”NhhhNhKhKhG        hŒsqrt”hNhG        hNhG        Œfeature_names_in_”Œjoblib.numpy_pickle”ŒNumpyArrayWrapper”“”)”}”(Œsubclass”Œnumpy”Œndarray”“”Œshape”K…”Œorder”ŒC”Œdtype”h-Œdtype”“”ŒO8”‰ˆ‡”R”(KŒ|”NNNJÿÿÿÿJÿÿÿÿK?t”bŒ
allow_mmap”‰Œnumpy_array_alignment_bytes”Kub€cnumpy._core.multiarray
_reconstruct
q cnumpy
ndarray
qK …qc_codecs
encode
qX   bqX   latin1q†qRq‡qRq	(KK…q
cnumpy
dtype
qX   O8q‰ˆ‡q
Rq(KX   |qNNNJÿÿÿÿJÿÿÿÿK?tqb‰]q(X   home_team_last5_avg_goalsqX   away_team_last5_avg_goalsqX   home_team_rankqX   away_team_rankqetqb.•ƒ       Œn_features_in_”KŒ
_n_samples”KŒ
n_outputs_”KŒclasses_”h))”}”(h,h/h0K…”h2h3h4h6Œi8”‰ˆ‡”R”(KŒ<”NNNJÿÿÿÿJÿÿÿÿK t”bh<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿ               •ç       Œ
n_classes_”KŒ_n_samples_bootstrap”KŒ
estimator_”h	Œestimators_”]”(h)”}”(hhh
hhNhKhKhG        hh%hNhJfÜá_hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4h6Œf8”‰ˆ‡”R”(KhHNNNJÿÿÿÿJÿÿÿÿK t”bh<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•”       hJŒnumpy._core.multiarray”Œscalar”“”hGC       ”†”R”Œ
max_features_”KŒtree_”Œsklearn.tree._tree”ŒTree”“”Kh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿ       •i      K‡”R”}”(hK Œ
node_count”KŒnodes”h))”}”(h,h/h0K…”h2h3h4h6ŒV64”‰ˆ‡”R”(Kh:N(Œ
left_child”Œright_child”Œfeature”Œ	threshold”Œimpurity”Œn_node_samples”Œweighted_n_node_samples”Œmissing_go_to_left”t”}”(hqh6Œi8”‰ˆ‡”R”(KhHNNNJÿÿÿÿJÿÿÿÿK t”bK †”hrh}K†”hsh}K†”hthVK†”huhVK †”hvh}K(†”hwhVK0†”hxh6Œu1”‰ˆ‡”R”(Kh:NNNJÿÿÿÿJÿÿÿÿK t”bK8†”uK@KKt”bh<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •0       Œvalues”h))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kubÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ³=êKhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ\bshG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ•õ.hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJjôc;hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJGÔ™GhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ¼®AhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ,ËhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJfÖð'hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJy"rhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÒAï'hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÖô—hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJJ‘ÞhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÊU‘uhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJW¸½]hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJtímUhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJc¬âhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJgë’$hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ—>D5hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ‚  &hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ•EhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ4ýphG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJLxhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJWéÔ8hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJëõUhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJýDphG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ%Û[6hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ	3 hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ¿Œ.hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ»“~hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ™ó.hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ DhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJËÑâMhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ9M•hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJpVhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJüÏhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJëò“nhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJXkçhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ0þJhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÚ¡WhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ:d¢hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJþI]fhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ©Þµ#hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÿGòhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÛýÉJhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ»
HyhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÏãÉ]hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJç–;hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ½ ÁthG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ½û1hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ®JIhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ½‹NhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ2Ò3hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJkéahG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ6Þ¤hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJóµ{hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ?{¨hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJøÅ}whG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ‚,ähG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJä
%\hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ2ˆhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ†¢(.hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJx§+hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJHëSshG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ¦8§hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJUehG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJƒ)êrhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJX"4qhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ;©3whG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ
¨3hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJñ óNhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJù§ªbhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ+ûMhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJY]hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ4
hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÛ;hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJSå)/hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ[Ø³=hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJnÕ­phG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ»[ê.hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÆå=hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ«½(hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJüéÃ~hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJCLUhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ®¯ÍhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                            ü?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ" a,hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÍ8ÉhhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJPŒdhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ£g?BhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ1§.hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           &@      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?              ð?      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJg›)hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJƒ]_AhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJLÌOhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJý×lhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ…-#hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           @      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ5ª;5hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      ð?        •…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJi4õhG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÏThG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJ5ŸR/hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hKhiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿ                           ô?      à?              @        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                     ð?        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ      à?      à?      ð?                      ð?•…       ubhhubh)”}”(hhh
hhNhKhKhG        hh%hNhJÜ%hG        hNhG        hNh>Kh@KhAh))”}”(h,h/h0K…”h2h3h4hVh<ˆh=Kubÿ              ð?•B       hJhZhGC       ”†”R”h^Kh_hbKh))”}”(h,h/h0K…”h2h3h4hGh<ˆh=Kubÿÿÿÿ       •6       K‡”R”}”(hK hiKhjh))”}”(h,h/h0K…”h2h3h4hph<ˆh=Kubÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿþÿÿÿÿÿÿÿ       À                      @        •)       hŒh))”}”(h,h/h0KKK‡”h2h3h4hVh<ˆh=Kub
ÿÿÿÿÿÿÿÿÿÿÿÿÿ              ð?•       ubhhubehhub.