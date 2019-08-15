print('\nOlá, me chamo Kiara, eu sou uma pequena robô projetada pelo Sandro.')

from time import sleep 
sleep(1)
nome = str(input('\nComo você se chama? '))
if nome.upper() == 'SANDRO':
  print('\nMuito prazer em conhecê-lo Criador!')
else:
  print ('\nMuito prazer',nome)

tudobem = str(input('\nComo você está? '))
if tudobem.upper() == 'BEM E VOCÊ?':
  print('\nEu estou bem, muito obrigada por perguntar!')
elif tudobem.upper() == 'MAL':
  print('\nPor que? o que houve?')
  resposta = str(input('\n'))
  print('\nPoxa, espero que tudo melhore para você!')
elif tudobem.upper() == 'BEM':
  print('\nQue bom que você está bem', nome)
else:
  print('\nDesculpa, eu ainda não aprendi a responder a isso!')

pergunta2 = str(input('\nGostaria de saber algo sobre mim? '))
if pergunta2.upper() == 'SIM':
  print('\nEu nasci no dia 09 de agosto de 2019 as 17:45:10')
elif pergunta2.upper() == 'NÃO':
  print('\nTudo bem')
else:
    print('\nDesculpa, eu ainda não aprendi a responder a isso!')

pediraju = str(input('\n'))
if pediraju.upper() == 'PODE ME AJUDAR?':
  print('\nPosso sim, qual materia?')
else:
  print('\nDesculpa, eu ainda não aprendi a responder a isso!')
  
ajuda = str(input('\n'))
if ajuda.upper() == 'PRECISO DE AJUDA EM MATEMATICA':
  conta = str(input('\nA conta é de adição, subtração, multiplicação ou divisão? '))
  if conta.upper() == 'ADIÇÃO':
    A1 = int(input('\nQual é o primeiro valor? '))
    A2 = int(input('\nQual é o segundo valor? '))
    resultadoa = A1 + A2
    print('\nA soma entre', A1, 'e', A2, 'é igual a', resultadoa)
  elif conta.upper() == 'SUBTRAÇÃO':
    S1 = int(input('\nQual é o primeiro valor? '))
    S2 = int(input('\nQual é o segundo valor? '))
    resultados = S1 - S2
    print('\nA subtração entre', S1, 'e', S2, 'é igual a', resultados)
  elif conta.upper() == 'MULTIPLICAÇÃO':
    M1 = int(input('\nQual é o primeiro valor? '))
    M2 = int(input('\nQual é o segundo valor? '))
    resultadom = M1 * M2
    print('\nA multiplicação entre', M1, 'e', M2, 'é igual a', resultadom)
  elif conta.upper() == 'DIVISÃO':
    D1 = int(input('\nQual é o primeiro valor? '))
    D2 = int(input('\nQual é o segundo valor? '))
    resultadod = D1 / D2
    print('\nA divisão entre', D1, 'e', D2, 'é igual a', resultadod)

elif ajuda.upper() == 'PRECISO DE AJUDA EM PORTUGUÊS':
  print('\nDesculpe eu ainda não aprendi sobre Português')

elif ajuda.upper() == 'PRECISO DE AJUDA EM INGLÊS':
  print('\nDesculpe eu ainda não aprendi sobre Inglês')

elif ajuda.upper() == 'PRECISO DE AJUDA EM FÍSICA':
  print('\nDesculpe eu ainda não aprendi sobre Física')

elif ajuda.upper() == 'PRECISO DE AJUDA EM QUÍMICA':
  print('\nDesculpe eu ainda não aprendi sobre Química')

elif ajuda.upper() == 'PRECISO DE AJUDA EM ARTES':
  print('\nDesculpe eu ainda não aprendi sobre Artes')

elif ajuda.upper() == 'PRECISO DE AJUDA EM HISTORIA':
  print('\nDesculpe eu ainda não aprendi sobre Historia')

elif ajuda.upper() == 'PRECISO DE AJUDA EM SOCIOLOGIA':
  print('\nDesculpe eu ainda não aprendi sobre Sociologia')

elif ajuda.upper() == 'PRECISO DE AJUDA EM FILOSOFIA':
  print('\nDesculpe eu ainda não aprendi sobre Filosofia')

elif ajuda.upper() == 'PRECISO DE AJUDA EM EDUCAÇÃO FISICA':
  print('\nDesculpe eu ainda não aprendi sobre Educação Fisica')

elif ajuda.upper() == 'PRECISO DE AJUDA EM GEOGRAFIA':
  print('\nDesculpe eu ainda não aprendi sobre Geografia')

pergunta3 = str(input('\nPrecisa de ajuda em mais alguma coisa? '))
if pergunta3.upper() == 'SIM':
  ajuda2 = str(input('\n'))
  if ajuda2.upper() == 'PRECISO DE AJUDA EM MATEMATICA':
    conta2 = str(input('\nA conta é de adição, subtração, multiplicação ou divisão? '))
    if conta2.upper() == 'ADIÇÃO':
      A1 = int(input('\nQual é o primeiro valor? '))
      A2 = int(input('\nQual é o segundo valor? '))
      resultadoa = A1 + A2
      print('\nA soma entre', A1, 'e', A2, 'é igual a', resultadoa)
    elif conta2.upper() == 'SUBTRAÇÃO':
      S1 = int(input('\nQual é o primeiro valor? '))
      S2 = int(input('\nQual é o segundo valor? '))
      resultados = S1 - S2
      print('\nA subtração entre', S1, 'e', S2, 'é igual a', resultados)
    elif conta2.upper() == 'MULTIPLICAÇÃO':
      M1 = int(input('\nQual é o primeiro valor? '))
      M2 = int(input('\nQual é o segundo valor? '))
      resultadom = M1 * M2
      print('\nA multiplicação entre', M1, 'e', M2, 'é igual a', resultadom)
    elif conta2.upper() == 'DIVISÃO':
      D1 = int(input('\nQual é o primeiro valor? '))
      D2 = int(input('\nQual é o segundo valor? '))
      resultadod = D1 / D2
      print('\nA divisão entre', D1, 'e', D2, 'é igual a', resultadod)

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM PORTUGUÊS':
    print('\nDesculpe eu ainda não aprendi sobre Português')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM INGLÊS':
    print('\nDesculpe eu ainda não aprendi sobre Inglês')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM FÍSICA':
    print('\nDesculpe eu ainda não aprendi sobre Física')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM QUÍMICA':
    print('\nDesculpe eu ainda não aprendi sobre Química')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM ARTES':
    print('\nDesculpe eu ainda não aprendi sobre Artes')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM HISTORIA':
    print('\nDesculpe eu ainda não aprendi sobre Historia')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM SOCIOLOGIA':
    print('\nDesculpe eu ainda não aprendi sobre Sociologia')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM FILOSOFIA':
    print('\nDesculpe eu ainda não aprendi sobre Filosofia')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM EDUCAÇÃO FISICA':
    print('\nDesculpe eu ainda não aprendi sobre Educação Fisica')

  elif ajuda2.upper() == 'PRECISO DE AJUDA EM GEOGRAFIA':
    print('\nDesculpe eu ainda não aprendi sobre Geografia')

elif pergunta3.upper() == 'NÃO':
  print('\nTudo bem, estarei a disposição')

from time import sleep 
sleep(5)