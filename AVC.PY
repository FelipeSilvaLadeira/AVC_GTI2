print("Bem-vindo a TF Brinquedos!")
print("Temos os seguintes brinquedos disponíveis: bola - piao - pipa - carrinho")
precos = {
    'bola': 50,
    'piao': 20,
    'pipa': 15,
    'carrinho': 65
}
estoque = {
    'bola': 20,
    'piao': 20,
    'pipa': 105,
    'carrinho': 5
}
total = 0
itens_comprados = {} 
while True:
    calculo = input("Escolha os brinquedos que deseja comprar: ").lower()
    for brinquedo in calculo:
        brinquedo = brinquedo
        if brinquedo in precos:
            quantidade = int(input(f"Digite a quantidade desejada para {brinquedo}: "))
            if quantidade <= estoque[brinquedo]:
                total += precos[brinquedo] * quantidade
                estoque[brinquedo] -= quantidade 
                if brinquedo in itens_comprados:
                    itens_comprados[brinquedo] += quantidade
                else:
                    itens_comprados[brinquedo] = quantidade
            else:
                print(f"Desculpe, temos apenas {estoque[brinquedo]} unidades de {brinquedo} em estoque.")
        else:
            print(f"O item '{brinquedo}' é inválido.")
    continuar = input("Deseja adicionar mais algum produto? (s/n): ").lower()
    if continuar != 's':
        break
print(f"O valor total da sua compra é: R${total:.2f}")
remover = input("Deseja remover algum produto da sua compra? (s/n): ").lower()
if remover == 's':
    for produto, quantidade in itens_comprados.items():
        print(f"{produto.capitalize()}: {quantidade} unidades")
    produto_remover = input("Digite o nome do produto que deseja remover: ").lower()
    if produto_remover in itens_comprados:
        quantidade_remover = int(input(f"Quantas unidades de {produto_remover} deseja remover? "))
        if quantidade_remover <= itens_comprados[produto_remover]:
            total -= precos[produto_remover] * quantidade_remover
            itens_comprados[produto_remover] -= quantidade_remover
            estoque[produto_remover] += quantidade_remover
            if itens_comprados[produto_remover] == 0:
                del itens_comprados[produto_remover]
            print(f"Produto removido. O novo valor total da sua compra é: R${total:.2f}")
        else:
            print("Quantidade a remover é maior que a quantidade comprada.")
    else:
        print("Produto não encontrado na sua compra.")
if total > 500:
    desconto = total * 0.10
    total_com_desconto = total - desconto
    print(f"O valor total da sua compra com 10% de desconto é: R${total_com_desconto:.2f}")
else:
    print(f"O valor total final da sua compra é: R${total:.2f}")
