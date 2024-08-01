print("Olá, você quer calcular a área de alguma forma geométrica?")
r = int(input('Digite 1 para sim e 2 para não: '))
if r == 1:
    print('Qual área quer calcular? \n'
          'Círculo - 1 \n'
          'Quadrado - 2 \n'
          'Retângulo - 3 \n'
          'Triângulo - 4 \n')
    r2 = int(input('Digite: '))
    if r2 == 1:
        raio = int(input('Qual o valor do raio deste círculo? Digite: '))
        print('O resultado da área do círculo é:', (3.14*(raio**2)))
    elif r2 == 2:
        lado = int(input('Qual o valor do lado deste quadrado? Digite: '))
        print('O resultado da área deste quadrado é:', lado**2)
    elif r2 == 3:
        base_r = int(input('Qual o valor da base deste retângulo? Digite: '))
        altura_r = int(input('Qual o valor da altura deste retângulo? Digite: '))
        print('O resultado da área deste retângulo é:', base_r*altura_r)
    elif r2 == 4:
        base_t = int(input('Qual o valor da base deste triângulo? Digite: '))
        altura_t = int(input('Qual o valor da altura deste triângulo? Digite: '))
        print('O resultado da área deste triângulo é de:', base_t*altura_t/2)
    else:
        print('Tente novamente e escolha uma opção válida.')
else:
    print('Okay, bom dia.')