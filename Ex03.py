import json

# Carregar o arquivo JSON com os dados do faturamento
with open('faturamento.json') as f:
    dados = json.load(f)

# Ignorar dias com faturamento zerado
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular menor, maior e média
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_faturamento = sum(faturamentos) / len(faturamentos)

# Contar os dias com faturamento acima da média
dias_acima_media = len([f for f in faturamentos if f > media_faturamento])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
