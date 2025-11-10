import os
import pandas as pd
from sensores import gerar_dado_sensor
from armazenamento import salvar_csv
from graficos import exibir_grafico

def test_fluxo_completo(tmp_path):
    # Caminho temporário do arquivo CSV
    arquivo = tmp_path / "leituras.csv"

    # Etapa 1: gerar leituras simuladas
    leituras = [gerar_dado_sensor() for _ in range(5)]
    assert all(isinstance(l, dict) for l in leituras), "Leituras devem ser dicionários"

    # Etapa 2: salvar leituras no CSV
    for leitura in leituras:
        salvar_csv(leitura)
    assert os.path.exists("dados/leituras.csv"), "O arquivo CSV não foi criado corretamente"

    # Etapa 3: ler arquivo com pandas
    df = pd.read_csv("dados/leituras.csv")
    assert not df.empty, "O arquivo CSV está vazio"
    assert set(["Hora", "Temperatura", "Umidade"]).issubset(df.columns), "Colunas incorretas no CSV"

    # Etapa 4: gerar gráfico (sem erro)
    try:
        exibir_grafico("dados/leituras.csv")
        sucesso = True
    except Exception as e:
        sucesso = False
        print(f"Erro ao gerar gráfico: {e}")

    assert sucesso, "Erro na exibição do gráfico"

def test_dados_consistentes():
    """
    Verifica se os dados simulados mantêm consistência estatística.
    """
    leituras = [gerar_dado_sensor() for _ in range(50)]
    temps = [l["temperatura"] for l in leituras]
    umids = [l["umidade"] for l in leituras]

    assert min(temps) >= 10 and max(temps) <= 45, "Temperaturas fora do intervalo esperado"

    assert min(umids) >= 0 and max(umids) <= 100, "Umidades fora do intervalo esperado"
