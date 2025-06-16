nome1=input("Digite o nome do player 1 (que vai começar): ")
nome2=input("Digite o nome do player 2: ")

from random import randint

ListaMapas=['Alfheim','Savana','Marsh','Elysium','Blue Lagoon','Giza','Tundra','Anatolia','Ghost Lake','Nilo','Buraco','Midgard','Oasis','Megalopolis','Steppe','Bamboo']
ListaGods=['Zeus','Hades','Poseidon','Ra','Isis','Set','Thor','Odin','Loki','Freyr','Kronos','Urano','Gaia','Fu Xi','Nu Wa','Shennong']
a2=int(input('Digite 3 para Bo3 ou 5 para Bo5, se digitar outra coisa n vai funcionar'))

#Admin Map
a1=ListaMapas[randint(0,15)]
ListaMapas.remove(a1)
print('\n\n\n')
print('O mapa escolhido aleatoriamente é ' +a1)
print('\n\n\n')
MapasEscolhidos=[a1]
#Bans
for i in ListaMapas:
    print(str(ListaMapas.index(i))+" - "+i)
print('\n\n\n')
Ban1=int(input(f'Qual o numero do primeiro map ban por {nome1}?'))
print("\n"+ListaMapas[Ban1]+"\n")
ListaMapas.remove(ListaMapas[Ban1])
for i in ListaMapas:
    print(str(ListaMapas.index(i))+" - "+i)
print('\n')
Ban2=int(input(f'Qual o numero do segundo map ban por {nome2}?'))
print("\n"+ListaMapas[Ban2]+"\n")
ListaMapas.remove(ListaMapas[Ban2])
print('\n\n\n')
print('Sobraram as seguintes para escolher: \n')

for i in ListaMapas:
    print(str(ListaMapas.index(i))+" - "+i)
print('\n')
#Primeiro Pick
PrimeiroMapa=int(input(f'Qual o numero do primeiro mapa a ser escolhido por {nome1}?'))
print("\n"+ListaMapas[PrimeiroMapa]+"\n")
MapasEscolhidos.append(ListaMapas[PrimeiroMapa])
ListaMapas.remove(ListaMapas[PrimeiroMapa])

for i in ListaMapas:
    print(str(ListaMapas.index(i))+" - "+i)
print('\n')
#Segundo Pick

SegundoMapa=int(input(f'Qual o numero do segundo mapa a ser escolhido por {nome2}?'))
print("\n"+ListaMapas[SegundoMapa]+"\n")
MapasEscolhidos.append(ListaMapas[SegundoMapa])
ListaMapas.remove(ListaMapas[SegundoMapa])
print('\n\n\n')

print('\nLista Atual de mapas escolhidos:\n')
for i in MapasEscolhidos:
    print(i)
if a2==5:
    print('\n')
    print('Sobraram as seguintes para escolher: \n')

    for i in ListaMapas:
        print(str(ListaMapas.index(i))+" - "+i)

    print('\n')
    #Terceiro Pick
    TerceiroMapa=int(input(f'Qual o numero do terceiro mapa a ser escolhido por {nome1}?'))
    print("\n"+ListaMapas[TerceiroMapa]+"\n")
    MapasEscolhidos.append(ListaMapas[TerceiroMapa])
    ListaMapas.remove(ListaMapas[TerceiroMapa])

    for i in ListaMapas:
        print(str(ListaMapas.index(i))+" - "+i)
    print('\n')
    #Quarto Pick
    QuartoMapa=int(input(f'Qual o numero do quarto mapa a ser escolhido por {nome2}?'))
    print("\n"+ListaMapas[QuartoMapa]+"\n")
    MapasEscolhidos.append(ListaMapas[QuartoMapa])
    ListaMapas.remove(ListaMapas[QuartoMapa])
    print('\n\n\n')

    print('\nLista Atual de mapas escolhidos:\n')
    for i in MapasEscolhidos:
        if MapasEscolhidos.index(i) == 0:
            print("Mapa aleatório: "+i)
        elif MapasEscolhidos.index(i)%2!=0:
            print(f'{nome1} - '+i)
        else:
            print(f'{nome2} - '+i)


GodsEscolhidos=[]
#Bans
for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)
print('\n\n\n')
Ban1=int(input(f'Qual o numero do primeiro God ban por {nome1}?'))
print("\n"+ListaGods[Ban1]+"\n")
ListaGods.remove(ListaGods[Ban1])
for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)
print('\n')
Ban2=int(input(f'Qual o numero do segundo God ban por {nome2}?'))
print("\n"+ListaGods[Ban2]+"\n")
ListaGods.remove(ListaGods[Ban2])
print('\n\n\n')
print('Sobraram as seguintes para escolher: \n')

for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)
print('\n')
#Primeiro Pick
PrimeiroGod=int(input(f'Qual o numero do god a ser escolhido por {nome1}?'))
print("\n"+ListaGods[PrimeiroGod]+"\n")
GodsEscolhidos.append(ListaGods[PrimeiroGod])
ListaGods.remove(ListaGods[PrimeiroGod])

for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)
print('\n')
#Segundo Pick

SegundoGod=int(input(f'Qual o numero do segundo god a ser escolhido por {nome2}?'))
print("\n"+ListaGods[SegundoGod]+"\n")
GodsEscolhidos.append(ListaGods[SegundoGod])
ListaGods.remove(ListaGods[SegundoGod])
print('\n\n\n')

print('\nLista Atual de gods escolhidos:\n')
for i in GodsEscolhidos:
    print(i)

print('\n')
print('Sobraram as seguintes para escolher: \n')

for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)

print('\n')
#Terceiro Pick
TerceiroGod=int(input(f'Qual o numero do terceiro god a ser escolhido por {nome1}?'))
print("\n"+ListaGods[TerceiroGod]+"\n")
GodsEscolhidos.append(ListaGods[TerceiroGod])
ListaGods.remove(ListaGods[TerceiroGod])

for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)
print('\n')
#Quarto Pick
QuartoMapa=int(input(f'Qual o numero do quarto god a ser escolhido por {nome2}?'))
print("\n"+ListaGods[QuartoMapa]+"\n")
GodsEscolhidos.append(ListaGods[QuartoMapa])
ListaGods.remove(ListaGods[QuartoMapa])
for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)

#Quinto Pick
QuintoGod=int(input(f'Qual o numero do Quinto god a ser escolhido por {nome1}?'))
print("\n"+ListaGods[QuintoGod]+"\n")
GodsEscolhidos.append(ListaGods[QuintoGod])
ListaGods.remove(ListaGods[QuintoGod])

for i in ListaGods:
    print(str(ListaGods.index(i))+" - "+i)
print('\n')
#Sexto Pick
SextoGod=int(input(f'Qual o numero do Sexto god a ser escolhido por {nome2}?'))
print("\n"+ListaGods[SextoGod]+"\n")
GodsEscolhidos.append(ListaGods[SextoGod])
ListaGods.remove(ListaGods[SextoGod])
#     print('\nLista Atual de gods escolhidos:\n')
#     for i in GodsEscolhidos:
#         print(i)
if a2==5:
    for i in ListaGods:
        print(str(ListaGods.index(i))+" - "+i)
    SetimoGod=int(input(f'Qual o numero do Setimo god a ser escolhido por {nome1}?'))
    print("\n"+ListaGods[SetimoGod]+"\n")
    GodsEscolhidos.append(ListaGods[SetimoGod])
    ListaGods.remove(ListaGods[SetimoGod])

    for i in ListaGods:
        print(str(ListaGods.index(i))+" - "+i)
    print('\n')
    #Oitavo Pick
    OitavoGod=int(input(f'Qual o numero do Oitavo god a ser escolhido por {nome2}?'))
    print("\n"+ListaGods[OitavoGod]+"\n")
    GodsEscolhidos.append(ListaGods[OitavoGod])
    ListaGods.remove(ListaGods[OitavoGod])
    #     print('\nLista Atual de gods escolhidos:\n')
    #     for i in GodsEscolhidos:
    #         print(i)
    for i in ListaGods:
        print(str(ListaGods.index(i))+" - "+i)
    NonoGod=int(input(f'Qual o numero do Nono god a ser escolhido por {nome1}?'))
    print("\n"+ListaGods[NonoGod]+"\n")
    GodsEscolhidos.append(ListaGods[NonoGod])
    ListaGods.remove(ListaGods[NonoGod])

    for i in ListaGods:
        print(str(ListaGods.index(i))+" - "+i)
    print('\n')
    #Decimo Pick
    DecimoGod=int(input(f'Qual o numero do Decimo god a ser escolhido por {nome2}?'))
    print("\n"+ListaGods[DecimoGod]+"\n")
    GodsEscolhidos.append(ListaGods[DecimoGod])
    ListaGods.remove(ListaGods[DecimoGod])
    #     print('\nLista Atual de gods escolhidos:\n')
    #     for i in GodsEscolhidos:
    #         print(i)

# for i in GodsEscolhidos:
#     if GodsEscolhidos.index(i)%2==0:
#         print(f'{nome1} - '+i)
#     else:
#         print(f'{nome2} - '+i)

        
print("MAPAS: \n\n")
for i in MapasEscolhidos:
    if MapasEscolhidos.index(i) == 0:
        print("Mapa aleatório: "+i)
    elif MapasEscolhidos.index(i)%2!=0:
        print(f'{nome1} - '+i)
    else:
        print(f'{nome2} - '+i)
print("\n\nGODS: \n\n")
for i in GodsEscolhidos:
    if GodsEscolhidos.index(i)%2==0:
        print(f'{nome1} - '+i)
    else:
        print(f'{nome2} - '+i)


