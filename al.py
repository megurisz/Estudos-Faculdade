novoArr = []
menor = 1
maior = 1000
escolha = int(input("Digite um número entre 1 e 1000: "))

for i in range (1, 1001):
    novoArr.append(i)

if escolha < menor or escolha > maior:
    print(f"Erro: O número {escolha} não está entre {menor} e {maior}.")
else:
  
    while menor <= maior:
        meio = (menor + maior) // 2  
        chute = meio
        
        print(f"Chute: {chute}") 

        if chute == escolha:
            print(f"O número {escolha} foi encontrado.")
            break  
        elif chute < escolha:
            menor = meio + 1 
        else:
            maior = meio - 1

    if menor > maior:
        print(f"O número {escolha} não está na lista.")
