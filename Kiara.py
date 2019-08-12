print('Olá, me chamo Kiara, eu sou uma pequena robô projetada pelo Sandro.')

from  time import sleep 

for contagem in range(0,1):
    sleep(1)
    nome = str(input('Como você se chama? '))

if nome.upper() == 'SANDRO':
  print('Muito prazer em conhecê-lo Criador!')
else:
  print ('Muito prazer',nome)

tudobem = str(input('Como você está? '))

if tudobem.upper() == 'BEM E VOCÊ?':
    print('Eu estou bem, muito obrigada por perguntar.')
elif tudobem.upper() == 'NÃO':
    print('Poxa, espero que tudo melhore para você!')

aniver = str(input(''))

if aniver.upper() == 'QUANDO VOCÊ NASCEU?':
 print('Eu nasci no dia 09 de agosto de 2019 as ‏‎17:45:10.')
  
  sario = str(input('Gostaria de saber mais alguma coisa? '))
    if sario.upper == 'SIM'
     conta = str(input('Eu sei fazer somas gostaria de ver? '))
    elif sario.upper == 'NÃO'
      print('Tudo bem, estarei sempre aqui a dispocição.')

elif aniver.upper() == 'O QUE VOCÊ SABE FAZER?': 
  conta = str(input('Eu sei fazer somas gostaria de ver? '))

if conta.upper() == 'SIM':
  print('Ok, vamos começar')
  N1 = int(input('Escolha um numero: '))
  N2 = int(input('Escolha outro numero: '))
  resultado = N1 + N2

  print ('A soma entre', N1, 'e', N2, 'é igual a', resultado)

  final = str(input('Esse foi a sua conta, gostou? '))

  if final.upper() == 'GOSTEI':
    print('Muito obrigada. Me esforcei bastante, foi um prazer somar para você! Até mais')
  elif final.upper() == 'NÃO':
    print('Me desculpa, me esforçarei mais da proxima vez!')
elif conta.upper() == 'NÃO GOSTEI':
  print('Me desculpa, farei meu melhor na proxima vez.')