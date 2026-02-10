lista_produto= []
lista_pagamento= []
lista_total_geral= []
subtotal= 0.0
total_geral= 0.0

print("Bem-Vindo!")

while True:
    try:
        registro= int(input("Digite a quantidade de registro utilizando números:"))      
        break
    
    except ValueError:
        print("Por favor, utilize apenas números inteiros")       # Mensagem de erro caso o usuário escreva algum texto ou números decimais no registro


while registro <0:
    print("Por favor, utilize números positivos:")          # Caso o usuário escreva algum número negativo no registro, vai aparecer uma mensagem
    registro= int(input("Digite a quantidade de registro em números:"))
    


for reg in range(registro):                     # Vai repetir de acordo com o número de registro feito pelo usuário
    print("Número do produto:", reg + 1)        # Vai enumerar os registros de forma crescente

    
    nome_produto= input("Digite o nome do produto utilizando apenas letras:").lower()         # lower garante que qualquer letra atribuída se transforme em uma letra minúscula
             
    
    while True:                                                    # Vai repetir até o usuário escrever utilizando apenas números e o ponto no lugar da vírgula
        try:
            preco_unitario= float(input("Digite o preço unitário:"))
            if preco_unitario >0:
                break                         # Se o usuário escrever certo, o laço para
            
            else:
                print("Por favor, digite apenas números positivos")

        except ValueError:                                                             # Se ele escrever colocando vírgula, vai aparecer a mensagem
            print("Por favor, utilize apenas números com o . no lugar da vírgula")


    while True:
        try:                                                                   # Vai repetir até o usuário escrever utilizando apenas números inteiros
            quantidade_produto= int(input("Digite a quantidade de produtos:"))     
            if quantidade_produto >0: 
                break                              # Quando o usuário escrever a quantidade da forma certa, o laço para

            else:
                print("Por favor, utilize apenas números positivos")
        
        except ValueError:
            print("Digite apenas números inteiros e positivos")
    

    subtotal = preco_unitario * quantidade_produto

    lista_produto.append({"Nome":nome_produto ,"preço unitário": preco_unitario , "Quantidade":quantidade_produto , "subtotal": round(subtotal,2)})

    lista_total_geral.append(subtotal)   # Vai introduzir o subtotal dentro de uma lista para na linha 64 fazer a soma de todos os elementos 


print("Forma de pagamento")
print("1- À vista")
print("2- Cartão de Crédito")

pagamento= int(input("Digite sua forma de pagamento (1 ou 2):"))


while pagamento !=1 and pagamento !=2:                   # Condição para o usuário escrever apenas os números 1 e 2
    print("Opção inválida, por favor, digite 1 ou 2:")
    print("Forma de pagamento")
    print("1- À vista")
    print("2- Cartão de crédito")

    pagamento= int(input("Digite sua forma de pagamento (1 ou 2):"))
    
if pagamento == 1:
    print("Você selecionou À vista")          # Condições para informar o usuário qual tipo de pagamento ele escolheu

elif pagamento == 2:
    print ("Você selecionou Cartão de Crédito")
        

def calculo_desconto(pagamento,total):               #Função que vai armazenar os cálculos de desconto de acordo com algumas condições
    if pagamento == 1:                                           
        if total > 200:
            return total * 0.15  # à vista com desconto de 15%
        elif total >= 100:
            return total * 0.10  # à vista com desconto de 10% 
        else:
            return 0              # Se o total for menor que 100, vai retornar 0
    else:
        return 0                    # Se o pagamento for diferente que 1, vai retornar 0
    

for t in lista_total_geral:        # Laço que vai somar todos os elementos (subtotais) da lista total geral
    total_geral += t            # A soma do total antes do desconto

desconto = calculo_desconto(pagamento,total_geral)    # Desconto aplicado utilizando a função def feita na linha 54

total_final = total_geral - desconto      # Total após o desconto

lista_pagamento.append({"Total": round(total_geral,2) ,"Desconto": round(desconto,2)})  # Armazenou todas as informações finais 

#Saída Formatada

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