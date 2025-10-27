from sensores import gerar_dado_sensor
from armazenamento import salvar_csv
from graficos import exibir_grafico
import time

def main():
    print("\n=== PROJETO: REDE DE SENSORES (WSN) ===")
    print("Simulando geração de dados... (Ctrl+C para encerrar)\n")

    try:
        while True:
            leitura = gerar_dado_sensor()
            salvar_csv(leitura)
            print(f"[{leitura['hora']}] Temperatura: {leitura['temperatura']} °C | Umidade: {leitura['umidade']} %")
            time.sleep(2)  
    except KeyboardInterrupt:
        print("\nColeta finalizada. Gerando gráfico...\n")
        exibir_grafico("dados/leituras.csv")

if __name__ == "__main__":
    main()
