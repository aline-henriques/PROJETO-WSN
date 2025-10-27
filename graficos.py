import pandas as pd
import matplotlib.pyplot as plt

def exibir_grafico(caminho_csv):
    try:
        # Tenta ler com cabeçalho
        df = pd.read_csv(caminho_csv)
        # Se as colunas não forem as esperadas, tenta forçar nomes
        if "Hora" not in df.columns:
            df = pd.read_csv(caminho_csv, names=["Hora", "Temperatura", "Umidade"], header=None, skiprows=1)

        plt.figure(figsize=(8,4))
        plt.plot(df["Hora"], df["Temperatura"], label="Temperatura (°C)")
        plt.plot(df["Hora"], df["Umidade"], label="Umidade (%)")
        plt.title("Leituras dos Sensores (Simulação)")
        plt.xlabel("Hora")
        plt.ylabel("Valor")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("❌ Arquivo de dados não encontrado. Execute o programa e gere algumas leituras primeiro.")
    except Exception as e:
        print(f"⚠️ Erro ao gerar gráfico: {e}")
