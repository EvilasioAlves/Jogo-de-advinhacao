import random
print ("*************************************")
print ("Seja bem vindo ao jogo de advinhação!")
print ("*************************************")

numero_secretro = random.randrange(1,26)
numero_secretro = round(numero_secretro)

tentativa = 0
rodada = 1

print ("Nível do jogo")
print ("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Digite o nível desejado: "))

if nivel == 1:
  tentativa = 15
elif nivel == 2: 
  tentativa = 10
else:
  tentativa = 3
  
for rodada in range (1, tentativa + 1):
  print ("Rodada {} de {}".format(rodada,tentativa))
  chute = int(input("Digite seu número entre 1 e 25: "))
  rodada = rodada + 1

  if chute <1 or chute>25:
    print ("É necessário digitar um número entre 1 e 25")
    continue
    
  acertou = chute == numero_secretro
  maior   = chute > numero_secretro
  menor   = chute < numero_secretro
  
  if acertou:
    print ("Você descobriu o número secreto. Parabéns!")
    break
  else:
    if maior:
      print ("O número digitado é maior que o número secreto ")
    if menor:
      print ("O número digitado menor que o número secreto ")
      
print ("Fim do jogo!")
print ("O número secreto era {}".format(numero_secretro))