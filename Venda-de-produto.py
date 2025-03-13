def venda_de_produto():
    print('**********Venda de Produto**********')
nome = input("Escreva o nome do produto: ")
while True:
    try:
        preco = float(input("Escreva o preço R$: "))
        quantidade = int(input("Escreva a quantidade de produtos: "))
        valor_total = preco * quantidade
        print(f"Valor a pagar R$: {valor_total:.2f}")
        break # Sai do loop se tudo estiver correto
    except ValueError:
        print("Atenção! Os campos 'quantidade' e 'preço' devem conter apenas valores númericos. Tente novamente!")
print("Escolha a forma de pagamento: ")
print("1. Dinheiro")
print("2. Pix")
print("3. Cartão (crédito/débito)")
while True:
    forma = input("Digite o número correspondente a forma de pagamento: ")
    if forma == "1":
        print("-> Você escolheu dinheiro. Pagamento realizado em dinheiro.")
        break
    elif forma == "2":
        print("Você escolheu Pix. Pagamento realizado via Pix.")
        break
    elif forma == "3":
        print("Você escolheu cartão. Pagamento realizado no cartão (crédito/débito).")
        break
    else:
        print("->Forma de pagamento inválido, por favor, escolha outra opção.")
                
print("Adoramos te atender! Volte logo, Esperamos por você!")

# Chamando a função
venda_de_produto()

    
