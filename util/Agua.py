nome = input("Olá, qual é o seu nome:")
peso =float(input(f'{nome}, quanto você pesa:'))
min = int(input(f'{nome}, durante quantas horas por dia você tem disponibilidade '
            f'para beber água:'))
copo = 180
min *= 60
ml = 35

agua_ideal = peso * ml
copos = round(agua_ideal / copo)
tempo = round(min/copos)

print(f'\n{nome}, você deve tomar {copos} copos durante o dia a cada {tempo} minutos. Boa Sorte!') #printar quantidade de copos










