# 💵 Calculadora e Conversor de Salário USD - BRL

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 💡 Sobre o Projeto
Este projeto é uma calculadora de salário que permite aos usuários calcular seus ganhos diários, semanais e mensais em dólares americanos (USD) e convertê-los para reais (BRL) usando a cotação atual do dólar. Ele é útil para freelancers, trabalhadores remotos e qualquer pessoa que receba pagamentos em dólares e queira saber o valor equivalente em reais.

## 🚀 Funcionalidades
* Cálculo de salário diário, semanal e mensal com base no valor da hora trabalhada.
* Consumo de API REST (`requests`) para obter a cotação atualizada do Dólar.
* Conversão automática de todos os montantes para Real (BRL).

## 🧠 Lógica Utilizada
O sistema coleta dados fundamentais do utilizador: valor da hora, horas trabalhadas por dia e dias trabalhados por semana. A partir disso, a lógica matemática calcula as proporções, utilizando a fórmula de precisão de semanas no ano `(52 / 12)` para garantir um resultado mensal realista.

## 🚀 Como Executar

**Pré-requisitos:** Certifique-se de ter o Python 3 instalado na sua máquina.

1. Clone este repositório ou baixe o ficheiro `conversor.py`.
2. Abra o terminal e instale a biblioteca de requisições web executando:
   ```bash
   pip install requests

1. Execute o script com o comando:
   ```bash
   python conversor.py

3. Siga as instruções no terminal informando os seus dados de trabalho.

👨‍💻 Autor

Léo Santos - Estudante de Engenharia de Software e Desenvolvedor Python.
