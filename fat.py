def func_fat(num):
  if num < 0:
    return "Fatorial não pode ser número negativo"

  elif num == 0 or num == 1:
    return 1

  else:
    return num*func_fat(num - 1)


num = input("Digite um número inteiro").replace(',', '.')
num_float = float(num)

if not num_float.is_integer():
  print("Erro: Digite apenas números inteiros, sem vírgulas ou casas decimais.")
else:
  fat = func_fat(int(num_float))
  print(f"O número {num} fatorial é: {fat}")