from sensores import gerar_dado_sensor
from armazenamento import salvar_csv
from graficos import exibir_grafico
from pathlib import Path
import time
import pandas as pd

ARQUIVO = Path("dados/leituras.csv")

def iniciar_coleta(intervalo=2):
    print("\n📡 Iniciando coleta de dados... (Ctrl + C para parar)\n")
    try:
        while True:
            leitura = gerar_dado_sensor()
            salvar_csv(leitura)
            print(f"[{leitura['hora']}] Temperatura: {leitura['temperatura']} °C | Umidade: {leitura['umidade']} %")
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\n✅ Coleta finalizada. Dados salvos em 'dados/leituras.csv'.")
        time.sleep(1)
    except Exception as e:
        print(f"⚠️ Erro durante a coleta: {e}")


def mostrar_estatisticas():
    if not ARQUIVO.exists():
        print("❌ Nenhum dado encontrado. Execute uma coleta primeiro.")
        return

    try:
        df = pd.read_csv(ARQUIVO)
        print("\n📊 Estatísticas das Leituras:")
        print(f"Temperatura média: {df['Temperatura'].mean():.2f} °C")
        print(f"Temperatura máxima: {df['Temperatura'].max():.2f} °C")
        print(f"Temperatura mínima: {df['Temperatura'].min():.2f} °C")
        print(f"Umidade média: {df['Umidade'].mean():.2f} %")
        print(f"Umidade máxima: {df['Umidade'].max():.2f} %")
        print(f"Umidade mínima: {df['Umidade'].min():.2f} %\n")
    except Exception as e:
        print(f"⚠️ Erro ao calcular estatísticas: {e}")


def menu():
    while True:
        print("\n=== 🌡️ PROJETO WSN - MENU PRINCIPAL ===")
        print("1 - Iniciar Coleta de Dados")
        print("2 - Exibir Gráfico")
        print("3 - Mostrar Estatísticas")
        print("4 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            try:
                intervalo = int(input("⏱️ Intervalo de coleta (em segundos): "))
            except ValueError:
                intervalo = 2
                print("Valor inválido. Usando intervalo padrão de 2 segundos.")
            iniciar_coleta(intervalo)

        elif escolha == "2":
            exibir_grafico("dados/leituras.csv")

        elif escolha == "3":
            mostrar_estatisticas()

        elif escolha == "4":
            print("\n👋 Encerrando o programa... Até logo!")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()