# Projeto: Redes de Sensores (Wireless Sensor Networks - WSN)

**Disciplina:** Infraestrutura de Comunicação – Redes de Computadores  
**Local:** Recife – 2025  
**Equipe:** Aline Henriques, Allan Ronald, Bruno Castilho, Thyalles Araujo  

---

## 🗓️ Semana 1 (27/10/2025) – Planejamento e Configuração

### Objetivo
Definição da solução, divisão de tarefas, pesquisa de bibliotecas Python e configuração do ambiente de desenvolvimento.

### Tema
**Redes de Sensores (Wireless Sensor Networks - WSN)**  

Desenvolvimento de uma aplicação Python que simula a coleta, o armazenamento e a visualização de dados de sensores (como temperatura e umidade) em uma rede de sensores sem fio simulada.  
O objetivo é compreender o funcionamento básico da comunicação entre nós sensores e o processamento dos dados coletados.

### Marco e Entrega
- Documento de planejamento inicial (Tema, Escopo, Tecnologias, Divisão de Tarefas).  
- Ambiente Python configurado e código inicial (esqueleto) pronto para a funcionalidade principal.

---

## 🧩 Semana 2 (03/11/2025) – Desenvolvimento Básico

### Objetivo
Implementação da funcionalidade central do projeto (parte mais básica da rede) e testes unitários iniciais.

### Descrição
Durante a segunda semana, a equipe implementou a **funcionalidade principal**, criando o protótipo funcional da rede de sensores.  
Foram desenvolvidos os módulos principais (`sensores.py`, `armazenamento.py`, `graficos.py`) e realizados os **testes automatizados** com *Pytest*.

### Marco e Entrega
- ✅ Funcionalidade de rede principal implementada e testada  
- ✅ Protótipo funcional rodando em linha de comando  
- ✅ Testes unitários executados com sucesso  

### ▶️ Comandos
python main.py     # Executar o programa
pytest -v          # Rodar os testes

---

## 🧠 Semana 3 (10/11/2025) – Refinamento e Interface

### Objetivo

Adicionar funcionalidades secundárias, tratamento de erros e desenvolver uma interface simples (terminal).

### Descrição

Na terceira semana, o foco foi o **refinamento do sistema** e a **criação de um menu interativo**.
O código passou a permitir que o usuário escolha ações no terminal e visualize estatísticas consolidadas das leituras.

### Novas Funcionalidades

* Menu interativo no terminal
* Intervalo de coleta configurável pelo usuário
* Exibição de estatísticas (média, mínima e máxima)
* Tratamento de erros e mensagens informativas
* Estrutura modular e aprimorada

### 🖥️ Menu Principal

```
=== 🌡️ PROJETO WSN - MENU PRINCIPAL ===
1 - Iniciar Coleta de Dados
2 - Exibir Gráfico
3 - Mostrar Estatísticas
4 - Sair
Escolha uma opção:
```

### Marco e Entrega

* ✅ Projeto funcionalmente completo e utilizável
* ✅ Interface simples implementada
* ✅ Tratamento de exceções e validações básicas

---

## ⚙️ Tecnologias Utilizadas

| **Componente**           | **Biblioteca / Tecnologia** | **Justificativa e Descrição**                                               |
| ------------------------ | --------------------------- | --------------------------------------------------------------------------- |
| Linguagem de Programação | **Python 3.11**             | Moderna, multiplataforma e amplamente usada para simulações.                |
| Simulação de Dados       | **random**, **time**        | Geram medições aleatórias de temperatura e umidade em intervalos definidos. |
| Armazenamento            | **csv** (nativo)            | Salva dados em formato tabular simples e legível.                           |
| Processamento de Dados   | **pandas**                  | Estrutura e manipula os dados armazenados em CSV.                           |
| Visualização Gráfica     | **matplotlib.pyplot**       | Gera gráficos de linha com as medições coletadas.                           |
| Organização              | **pathlib**, **os**         | Criação de diretórios e acesso seguro aos arquivos.                         |

---

## 🧱 Estrutura do Projeto

PROJETO-WSN/
├── dados/                       # Pasta onde o arquivo CSV de leituras será salvo
├── tests/
│   ├── test_sensores.py         # Testes para o módulo de geração de dados
│   ├── test_armazenamento.py    # Testes para o módulo de armazenamento
│   ├── test_graficos.py         # Testes para o módulo de gráficos
│   └── test_grupo.py            # Teste de integração (fluxo completo)
├── armazenamento.py             # Lógica para salvar dados no CSV
├── graficos.py                  # Lógica para ler o CSV e gerar visualizações
├── main.py                      # Ponto de entrada e orquestração do projeto
├── sensores.py                  # Lógica para simular a geração de dados
└── README.md                    # Este arquivo

---

## 👥 Divisão de Tarefas por Integrante

| **Integrante**                     | **Responsabilidade**                  | **Descrição**                                                                                     |
| ---------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Aline de Albuquerque Henriques** | Coordenação, documentação e testes    | Organização do projeto, estruturação do relatório, criação do README e testes no Windows.         |
| **Bruno de Castilhos Gomes Rego**  | Simulação dos Sensores                | Desenvolvimento do módulo `sensores.py`, responsável pela geração dos dados simulados.            |
| **Allan Ronald Vasconcelos**       | Armazenamento e persistência de dados | Criação do módulo `armazenamento.py`, incluindo lógica de gravação CSV e cabeçalho automático.    |
| **Thyalles de Campos Araújo**      | Visualização e Interface              | Implementação do módulo `graficos.py`, que lê o CSV e exibe os gráficos de temperatura e umidade. |

---

## 🧪 Testes Automatizados

O projeto inclui uma suíte de *testes unitários* utilizando o framework **Pytest**.

### Estrutura

```
tests/
├── test_sensores.py
├── test_armazenamento.py
└── test_graficos.py
└── test_grupo.py
```

### O que é testado

| **Arquivo**             | **Objetivo**                | **Validação**                                          |
| ----------------------- | --------------------------- | ------------------------------------------------------ |
| `test_sensores.py`      | Testa geração de dados      | Verifica campos e valores dentro dos limites esperados |
| `test_armazenamento.py` | Testa persistência de dados | Confirma criação do CSV e escrita correta              |
| `test_graficos.py`      | Testa exibição de gráficos  | Garante leitura e renderização sem erros               |

### Execução

pytest -v

### Dependências

pip install pytest pandas matplotlib

### Resultado Esperado

========================= test session starts =========================
collected 5 items

tests/test_armazenamento.py::test_salvar_csv_cria_arquivo PASSED
tests/test_graficos.py::test_exibir_grafico_roda_sem_erro PASSED
tests/test_sensores.py::test_gerar_dado_sensor_retorna_dict PASSED
tests/test_sensores.py::test_gerar_dado_sensor_campos_presentes PASSED
tests/test_sensores.py::test_gerar_dado_sensor_valores_validos PASSED

========================= 5 passed in 1.02s ===========================

---

## 📄 Licença

Projeto acadêmico desenvolvido para fins **educacionais** na disciplina
**Infraestrutura de Comunicação – CESAR School (2025)**.

📘 Todos os direitos reservados aos autores do grupo.
