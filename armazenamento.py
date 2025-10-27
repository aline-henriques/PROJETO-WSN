import csv
from pathlib import Path

ARQUIVO = Path("dados/leituras.csv")
ARQUIVO.parent.mkdir(exist_ok=True)

def salvar_csv(leitura):
    criar_cabecalho = not ARQUIVO.exists()
    with open(ARQUIVO, "a", newline="") as f:
        writer = csv.writer(f)
        if criar_cabecalho:
            writer.writerow(["Hora", "Temperatura", "Umidade"])
        writer.writerow([leitura["hora"], leitura["temperatura"], leitura["umidade"]])
