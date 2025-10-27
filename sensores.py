import random
import time

def gerar_dado_sensor():
    return {
        "hora": time.strftime("%H:%M:%S"),
        "temperatura": round(random.uniform(20, 35), 2),
        "umidade": round(random.uniform(40, 70), 2)
    }
