def calcular_digito_verificador(numero_conta):
    soma = sum(int(digito) for digito in str(numero_conta))
    digito_verificador = soma % 10
    return digito_verificador

def numero_conta_completo(numero_conta):
    digito_verificador = calcular_digito_verificador(numero_conta)
    return f"00{numero_conta}-{digito_verificador}"

numero_conta = 7314
numero_completo = numero_conta_completo(numero_conta)
print(numero_completo)
