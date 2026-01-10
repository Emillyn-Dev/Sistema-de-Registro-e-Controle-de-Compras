lista_produto= []
lista_pagamento= []
lista_total_geral= []
subtotal= 0
total_geral= 0

registro= int(input("Digite a quantidade de registro:"))


for reg in range(registro):       #repete de acordo com a quantidade do registro
    print("Número do produto:", reg + 1)

    nome_produto= input("Digite o nome do produto:").lower()
    preco_unitario= float(input("Digite o preço unitário:"))
    quantidade_produto= int(input("Digite a quantidade de produtos:"))

    subtotal = preco_unitario * quantidade_produto
    lista_produto.append({"Nome":nome_produto,"preço unitário": preco_unitario, "Quantidade":quantidade_produto, "subtotal": subtotal})
    lista_total_geral.append(subtotal)

print("Forma de pagamento")
print("1- Cartão de Crédito")
print("2- à vista")
pagamento= int(input("Digite sua forma de pagamento (1 ou 2):"))



while pagamento !=1 and pagamento !=2:
    print("Opção inválida, por favor, digite 1 ou 2:")
    print("Forma de pagamento")
    print("1- Cartão de Crédito")
    print("2- à vista")

    pagamento= int(input("Digite sua forma de pagamento (1 ou 2):"))

    if pagamento == 1:
        print("Você selecionou crédito")
    elif pagamento == 2:
        print ("Você selecionou à vista")
        

def calculo_desconto(pagamento,total):
    if pagamento == 2:
        if total > 200:
            return total * 0.15  # à vista com desconto de 15%
        elif total >= 100:
            return total * 0.10  # à vista com desconto de 10% dentro de um intervalo
    else:
        return 0
    

for t in lista_total_geral:
     total_geral += t        #A soma do subtotal de todo os registros (Valor antes do desconto)


desconto = calculo_desconto(pagamento,total_geral) #Desconto aplicado
total_final = total_geral - desconto  #Total após o desconto

lista_pagamento.append({"Total":total_geral,"Desconto":desconto,"Total a pagar":total_final})

print("\n" + "="*40)
print("        RELATÓRIO DA COMPRA")
print("="*40)

for produto in lista_produto:
    print(f"Produto: {produto['Nome'].title()}")
    print(f"Preço unitário: R$ {produto['preço unitário']:.2f}")
    print(f"Quantidade: {produto['Quantidade']}")
    print(f"Subtotal: R$ {produto['subtotal']:.2f}")
    print("-"*40)

print("\nRESUMO DO PAGAMENTO")
print("-"*40)

if pagamento == 1:
    forma = "Cartão de Crédito"
else:
    forma = "à Vista"

print(f"Forma de pagamento: {forma}")
print(f"Total sem desconto: R$ {total_geral:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print("="*40)
print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
print("="*40)



