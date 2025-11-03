import os
import csv
from armazenamento import salvar_csv, ARQUIVO

def test_salvar_csv_cria_arquivo(tmp_path):
    # Define diretório temporário para os testes
    dados_dir = tmp_path / "dados"
    dados_dir.mkdir(exist_ok=True)
    arquivo = dados_dir / "leituras.csv"

    # Cria uma leitura simulada
    leitura = {"hora": "12:00:00", "temperatura": 25.5, "umidade": 60.2}

    # Executa a função de salvamento
    salvar_csv(leitura)

    # Verifica se o arquivo padrão foi criado (dados/leituras.csv)
    caminho_real = ARQUIVO
    assert os.path.exists(caminho_real), "Arquivo CSV não foi criado."

    # Lê o conteúdo e confere se tem as colunas corretas
    with open(caminho_real, newline="") as f:
        reader = csv.reader(f)
        linhas = list(reader)
        assert linhas[0] == ["Hora", "Temperatura", "Umidade"], "Cabeçalho incorreto."
        assert any("25.5" in l for linha in linhas for l in linha), "Valor de temperatura não encontrado."