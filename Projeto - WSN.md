![][image1]

**PROJETO Redes de Sensores (Wireless Sensor Networks \- WSN)**  
**INFRAESTRUTURA DE COMUNICAÇÃO**  
**REDES DE COMPUTADORES**

Recife,  
2025

## **1\. Tema do Projeto**

### **Redes de Sensores (Wireless Sensor Networks \- WSN)**

Desenvolvimento de uma aplicação Python que simula a coleta, o armazenamento e a visualização de dados de sensores (como temperatura e umidade) em uma rede de sensores sem fio simulada. O objetivo é compreender o funcionamento básico da comunicação entre nós sensores e o processamento dos dados coletados.

---

## **2\. Escopo do Projeto**

O sistema permite monitorar, de forma simulada, as variações de temperatura e umidade em uma rede de sensores virtuais. Esses sensores geram dados a intervalos de tempo configuráveis, salvam as medições em um arquivo `.csv` e, ao final, exibem um gráfico representando a evolução dos valores coletados.

### **Funcionalidades previstas:**

* Simulação de sensores virtuais de **temperatura** e **umidade**;  
* **Geração automática de dados** em intervalos regulares;  
* **Armazenamento das leituras** em arquivo CSV com cabeçalho;  
* **Leitura e análise dos dados** utilizando `pandas`;  
* **Exibição gráfica** em tempo real (linha do tempo x valores);  
* **Finalização automática da coleta** com geração do gráfico consolidado.

---

## **3\. Tecnologias e Bibliotecas**

| Componente | Biblioteca / Tecnologia | Justificativa e Descrição |
| :---- | :---- | :---- |
|  Linguagem de Programação |  Python 3.11 | Escolhida por ser moderna, multiplataforma e amplamente utilizada em simulações e tratamento de dados. |
|  Simulação de Dados |  random, time |  Geram medições aleatórias de temperatura e umidade  em intervalos definidos.  |
|  Armazenamento |  csv (biblioteca nativa) |  Permite salvar dados em formato tabular simples, de fácil leitura e importação.  |
|  Processamento de Dados |  pandas |  Facilita leitura, estruturação e manipulação de dados armazenados em CSV.  |
|  Visualização Gráfica |  matplotlib.pyplot |  Cria gráficos de linha para exibir a variação das medições coletadas.  |
|  Estrutura e Organização |  pathlib, os | Garantem a criação automática de diretórios e acesso seguro a arquivos. |

---

## **4\. Estrutura Inicial do Código**

`/projeto_wsn/`  
`│`  
`├── main.py              # Script principal`  
`├── sensores.py          # Simulação dos sensores`  
`├── armazenamento.py     # Funções para salvar e ler dados`  
`├── graficos.py          # Funções de exibição dos gráficos`  
`├── dados/leituras.csv   # Base de dados gerada`  
`└── README.md            # Documentação do projeto`

---

## **5\. Divisão de Tarefas por Integrante**

| Integrante | Responsabilidade | Descrição |
| :---- | :---- | :---- |
|  Aline de Albuquerque Henriques |  Coordenação, documentação e testes |  Organização do projeto, estruturação do relatório, criação do README e testes de funcionalidade no Windows.  |
|  Bruno de Castilho Gomes Rego |  Simulação dos Sensores |  Desenvolvimento do módulo `sensores.py`, responsável pela geração dos dados simulados.  |
|  Allan Ronald Vasconcelos |  Armazenamento e peristência de dados |  Criação do módulo `armazenamento.py`, incluindo lógica de gravação CSV e cabeçalho automático.  |
|  Thyalles de Campos Araujo |  Visualização e Interface | Implementação do módulo `graficos.py`, que lê o CSV e exibe os gráficos de temperatura e umidade. |

[image1]: <data:image/png;base64,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>