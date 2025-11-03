import re
from sensores import gerar_dado_sensor

def test_gerar_dado_sensor_retorna_dict():
    dado = gerar_dado_sensor()
    assert isinstance(dado, dict), "A função deve retornar um dicionário."

def test_gerar_dado_sensor_campos_presentes():
    dado = gerar_dado_sensor()
    for campo in ["hora", "temperatura", "umidade"]:
        assert campo in dado, f"Campo '{campo}' deve existir no retorno."

def test_gerar_dado_sensor_valores_validos():
    dado = gerar_dado_sensor()
    assert 0 <= dado["umidade"] <= 100, "Umidade fora do intervalo esperado."
    assert 10 <= dado["temperatura"] <= 45, "Temperatura fora do intervalo esperado."
    assert re.match(r"\d{2}:\d{2}:\d{2}", dado["hora"]), "Formato de hora inválido."