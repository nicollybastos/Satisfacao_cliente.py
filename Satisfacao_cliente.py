# Contador

excelente = 0
bom = 0
ruim = 0

for i in range(50):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  print()
  print("Opnião de Atendimento:")
  print(" 1 - EXCELENTE | 2 - BOM | 3 - RUIM ")
  opniao = int(input("Digite um número: "))
  
  if opniao == 1:
    excelente = excelente + 1
  elif opniao == 2:
    bom = bom + 1
  elif opniao == 3:
    ruim = ruim + 1
  else:
    print("opcao inválida")

print("Quantidade de Respostas")
print()
print("EXCELENTE: ", excelente)
print("BOM: ", bom)
print("RUIM: ", ruim)
  
