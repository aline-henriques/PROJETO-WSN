# Projeto: Redes de Sensores (Wireless Sensor Networks - WSN)

**Disciplina:** Infraestrutura de Comunicação – Redes de Computadores  
**Local:** Recife – 2025  

---

## 1. Tema do Projeto

**Redes de Sensores (Wireless Sensor Networks - WSN)**  

Desenvolvimento de uma aplicação Python que simula a coleta, o armazenamento e a visualização de dados de sensores (como temperatura e umidade) em uma rede de sensores sem fio simulada.  
O objetivo é compreender o funcionamento básico da comunicação entre nós sensores e o processamento dos dados coletados.

---

## 2. Escopo do Projeto

O sistema permite monitorar, de forma **simulada**, as variações de **temperatura** e **umidade** em uma rede de sensores virtuais.  
Esses sensores geram dados a intervalos de tempo configuráveis, salvam as medições em um arquivo `.csv` e, ao final, exibem um gráfico representando a evolução dos valores coletados.


### **Funcionalidades previstas**
- 🔹 Simulação de sensores virtuais de temperatura e umidade  
- 🔹 Geração automática de dados em intervalos regulares  
- 🔹 Armazenamento das leituras em arquivo CSV com cabeçalho  
- 🔹 Leitura e análise dos dados utilizando `pandas`  
- 🔹 Exibição gráfica (linha do tempo x valores) usando `matplotlib`  
- 🔹 Finalização automática da coleta com geração do gráfico consolidado  

---

## 3. Tecnologias e Bibliotecas

| **Componente** | **Biblioteca / Tecnologia** | **Justificativa e Descrição** |
|----------------|-----------------------------|--------------------------------|
| Linguagem de Programação | **Python 3.11** | Escolhida por ser moderna, multiplataforma e amplamente utilizada em simulações e tratamento de dados. |
| Simulação de Dados | **random**, **time** | Geram medições aleatórias de temperatura e umidade em intervalos definidos. |
| Armazenamento | **csv** (nativo do Python) | Permite salvar dados em formato tabular simples, de fácil leitura e importação. |
| Processamento de Dados | **pandas** | Facilita leitura, estruturação e manipulação de dados armazenados em CSV. |
| Visualização Gráfica | **matplotlib.pyplot** | Cria gráficos de linha para exibir a variação das medições coletadas. |
| Estrutura e Organização | **pathlib**, **os** | Garantem a criação automática de diretórios e acesso seguro a arquivos. |

---

## 4. Estrutura Inicial do Código

```bash
/projeto_wsn/
│
├── main.py              # Script principal
├── sensores.py          # Simulação dos sensores
├── armazenamento.py     # Funções para salvar e ler dados
├── graficos.py          # Funções de exibição dos gráficos
├── dados/leituras.csv   # Base de dados gerada
└── README.md            # Documentação do projeto
````

---

## 5. Divisão de Tarefas por Integrante


| **Integrante**                     | **Responsabilidade**                  | **Descrição**                                                                                               |
| ---------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Aline de Albuquerque Henriques** | Coordenação, documentação e testes    | Organização do projeto, estruturação do relatório, criação do README e testes de funcionalidade no Windows. |
| **Bruno de Castilhos Gomes Rego**  | Simulação dos Sensores                | Desenvolvimento do módulo `sensores.py`, responsável pela geração dos dados simulados.                      |
| **Allan Ronald Vasconcelos**       | Armazenamento e persistência de dados | Criação do módulo `armazenamento.py`, incluindo lógica de gravação CSV e cabeçalho automático.              |
| **Thyalles de Campos Araújo**      | Visualização e Interface              | Implementação do módulo `graficos.py`, que lê o CSV e exibe os gráficos de temperatura e umidade.           |

---

## 6. Semana 2 – Desenvolvimento Básico

Durante a segunda semana, a equipe implementou a **funcionalidade central do projeto**, criando o protótipo funcional da rede de sensores.
Foram desenvolvidos os módulos principais (`sensores.py`, `armazenamento.py`, `graficos.py`) e realizados os **testes unitários iniciais** com *Pytest*.

### **Marco da Semana 2**

* ✅ Funcionalidade principal de coleta e armazenamento concluída
* ✅ Protótipo funcional rodando em linha de comando
* ✅ Testes unitários criados e executados com sucesso

### **Comando de Execução**

```bash
python main.py
```

### **Comando de Testes**

```bash
pytest -v
```

---

## 7. Semana 3 – Refinamento e Interface

Na terceira semana, o foco foi o **refinamento do sistema**, o tratamento de erros e a criação de uma **interface simples no terminal**.
O código foi aprimorado para incluir um menu interativo e a exibição de **estatísticas das leituras** (média, mínima e máxima de temperatura e umidade).

### **Menu Principal**

```
=== 🌡️ PROJETO WSN - MENU PRINCIPAL ===
1 - Iniciar Coleta de Dados
2 - Exibir Gráfico
3 - Mostrar Estatísticas
4 - Sair
Escolha uma opção:
```

### **Novas Funcionalidades da Semana 3**

* 🧭 Menu interativo no terminal
* ⚙️ Intervalo de coleta configurável pelo usuário
* 📊 Exibição de estatísticas das leituras (média, mínima e máxima)
* 🧩 Tratamento de erros e mensagens informativas
* 💾 Estrutura de dados aprimorada e código modular


### **Marco da Semana 3**

* ✅ Projeto funcionalmente completo e utilizável
* ✅ Interface simples implementada
* ✅ Tratamento de exceções e validações básicas

---

## 🧪 8. Testes Automatizados

O projeto conta com uma suíte de *testes unitários automatizados* desenvolvida com o framework *Pytest*.
Esses testes garantem o funcionamento correto de todos os módulos do sistema: geração de dados, armazenamento e exibição dos gráficos.


### Estrutura dos Testes

```
tests/
│
├── test_sensores.py        # Testes do módulo de simulação dos sensores
├── test_armazenamento.py   # Testes do módulo de gravação de dados CSV
└── test_graficos.py        # Testes do módulo de visualização de gráficos
```

### O que é verificado

| *Arquivo*               | *Objetivo do Teste*              | *O que é Validado*                                                                                           |
| ----------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `test_sensores.py`      | Validação das medições simuladas | Formato de hora, presença dos campos esperados e valores numéricos dentro de faixas aceitáveis               |
| `test_armazenamento.py` | Teste de persistência de dados   | Criação automática do arquivo CSV, escrita correta do cabeçalho e registro das leituras                      |
| `test_graficos.py`      | Teste de exibição gráfica        | Geração de gráficos sem erros, leitura adequada do CSV e compatibilidade com ambientes sem interface gráfica |

### Execução dos Testes

```bash
pytest -v
```

### Dependências Necessárias

```bash
pip install pytest pandas matplotlib
```

### Resultado Esperado

```
========================= test session starts =========================
collected 5 items

tests/test_armazenamento.py::test_salvar_csv_cria_arquivo PASSED
tests/test_graficos.py::test_exibir_grafico_roda_sem_erro PASSED
tests/test_sensores.py::test_gerar_dado_sensor_retorna_dict PASSED
tests/test_sensores.py::test_gerar_dado_sensor_campos_presentes PASSED
tests/test_sensores.py::test_gerar_dado_sensor_valores_validos PASSED

========================= 5 passed in 1.02s ===========================
```

---

## 📄 9. Licença

Projeto acadêmico desenvolvido para fins **educacionais** na disciplina
**Infraestrutura de Comunicação – CESAR School (2025)**.

📘 Todos os direitos reservados aos autores do grupo.