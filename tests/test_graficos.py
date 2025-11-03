import pandas as pd
from graficos import exibir_grafico
import matplotlib

# Usa backend "Agg" para evitar janelas gráficas durante o teste
matplotlib.use("Agg")

def test_exibir_grafico_roda_sem_erro(tmp_path):
    arquivo = tmp_path / "leituras.csv"
    df = pd.DataFrame({
        "Hora": ["10:00:00", "10:00:02", "10:00:04"],
        "Temperatura": [25.1, 25.5, 26.0],
        "Umidade": [60.0, 61.2, 62.5],
    })
    df.to_csv(arquivo, index=False)

    try:
        exibir_grafico(arquivo)
        sucesso = True
    except Exception:
        sucesso = False

    assert sucesso, "A função exibir_grafico apresentou erro com CSV válido."