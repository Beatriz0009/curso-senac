faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print("faturamento da empresa:R$, faturamento")
print(f"faturamento da empresa: R$ {faturamento:.2f} Custo: {custo:.2f} Lucro: {lucro:.2f}")

email_cliente = "emailcliente@gmail.com"
print(email_cliente)

# Maiusculas
email_cliente = email_cliente.upper()
print(email_cliente)

# Minusculas
email_cliente = email_cliente.lower()
print(email_cliente)

# Encontrar o @ ou outros caracteres quaisquer
print(email_cliente.find("@"))