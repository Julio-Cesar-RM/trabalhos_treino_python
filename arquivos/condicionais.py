n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media >= 7:
    print(f'O aluno foi aprovado, com nota de {media}')
elif 5 <= media < 7:
    print(f'O aluno está de recuperação, com nota de {media}')
else:
    print(f'O aluno foi reprovado, com nota de {media}')