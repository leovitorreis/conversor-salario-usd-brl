import requests

# Função para obter a cotação atual do dólar
def obter_cotacao_dolar():
    url = "https://v6.exchangerate-api.com/v6/76240b1f93be691b30c53dc4/latest/USD"
    response = requests.get(url)
    dados = response.json()
    return dados['conversion_rates']['BRL']

# Solicita os dados do usuário
salario_por_hora = float(input("Informe o seu salário por hora: "))
horas_trabalhadas = float(input("Informe as horas trabalhadas: "))
dias_por_semana = float(input("Informe os dias trabalhadas por semana: "))

# Calcula os salários
salario_diaria_usd = salario_por_hora * horas_trabalhadas
salario_semanal_usd = salario_diaria_usd * dias_por_semana
salario_mensal_usd = salario_semanal_usd * (52 / 12)

# Obtém a cotação do dólar e converte os valores para reais
cotacao_dolar = obter_cotacao_dolar()
salario_diaria_brl = salario_diaria_usd * cotacao_dolar
salario_semanal_brl = salario_semanal_usd * cotacao_dolar
salario_mensal_brl = salario_mensal_usd * cotacao_dolar

# Exibe os resultados
print(f"Seu salário por dia é de ${salario_diaria_usd:.2f} USD ou R${salario_diaria_brl:.2f} BRL")
print(f"Seu salário semanal é de ${salario_semanal_usd:.2f} USD ou R${salario_semanal_brl:.2f} BRL")
print(f"Seu salário mensal é de ${salario_mensal_usd:.2f} USD ou R${salario_mensal_brl:.2f} BRL")