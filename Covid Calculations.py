import math
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------Eu sou muito louco em listar 200 países----------------------------------------------------
paises = {'Brasil': 211049519, 'Estados Unidos': 329064917, 'China': 1433783692, 'Índia': 1366417756,
          'Indonésia': 270625567, 'Paquistão': 216565317, 'Nigéria': 200963603, 'Bangladesh': 163046173,
          'Rússia': 145872260, 'México': 127575529, 'Japão': 126860299, 'Etiópia': 112078727, 'Filipinas': 108116622,
          'Egito': 100388076, 'Vietnã': 96462105, 'RDCongo': 86790568, 'Alemanha': 83517046, 'Turquia': 83429607,
          'Irã': 82913893, 'Tailândia': 69625581, 'Reino Unido': 67530161, 'França': 65129731, 'Itália': 60550092,
          'África do Sul': 58558267, 'Tanzânia': 58005461, 'Myanmar': 54045422, 'Quénia': 52573967,
          'Coréia do Sul': 51225321, 'Colômbia': 50339443, 'Espanha': 46736782, 'Argentina': 44780675,
          'Uganda': 44269587, 'Ucrânia': 43993643, 'Argélia': 43053054, 'Sudão': 42813237, 'Iraque': 39309789,
          'Afeganistão': 38041757, 'Polônia': 37887771, 'Canadá': 37411038, 'Marrocos': 36471766,
          'Arábia Saudita': 34268529, 'Uzbequistão': 32981715, 'Peru': 32510462, 'Malásia': 31949789,
          'Angola': 31825299, 'Gana': 30417858, 'Moçambique': 30366043, 'Iêmen': 29161922, 'Nepal': 28608715,
          'Venezuela': 28515829, 'Madagascar': 26969306, 'Camarões': 25876387, 'Costa do Marfim': 25716554,
          'Coreia do Norte': 25666158, 'Austrália': 25203200, 'Níger': 23310719, 'Sri Lanka': 21323734,
          'Burkina Faso': 20321383, 'Mali': 19658023, 'Roménia': 19364558, 'Chile': 18628749, 'Malawi': 18628749,
          'Cazaquistão': 18551428, 'Zâmbia': 17861034, 'Guatemala': 17581476, 'Equador': 17373657,
          'Países Baixos': 17097123, 'Síria': 17070132, 'Camboja': 16486542, 'Senegal': 16296362, 'Chade': 15946882,
          'Somália': 15442906, 'Zimbabwe': 14645473, 'Guiné': 12771246, 'Ruanda': 12626938, 'Benim': 11801151,
          'Tunísia': 11694721, 'Bélgica': 11539326, 'Burundi': 11530577, 'Bolívia': 11513102, 'Cuba': 11333484,
          'Haiti': 11263079, 'Sudão do Sul': 11062114, 'República Dominicana': 10738957, 'República Checa': 10689213,
          'Grécia': 10473452, 'Portugal': 10226178, 'Jordânia': 10101697, 'Azerbaijão': 10047719, 'Suécia': 10036391,
          'Emirados Árabes Unidos': 9770526, 'Honduras': 9746115, 'Hungria': 9684680, 'Bielorrússia': 9452409,
          'Tajiquistão': 9321023, 'Áustria': 8955108, 'Nova Guiné': 8776119, 'Sérvia': 8772228, 'Suíça': 8591361,
          'Israel': 8519373, 'Togo': 8082359, 'Serra Leoa': 7813207, 'Hong Kong': 7436157, 'Laos': 7169456,
          'Paraguai': 7044639, 'Bulgária': 7000117, 'Líbano': 6855709, 'Líbia': 6777453, 'Nicarágua': 6545503,
          'El Salvador': 6453550, 'Quirguistão': 6415851, 'Turquemenistão': 5942094, 'Singapura': 5804343,
          'Dinamarca': 5771877, 'Finlândia': 5532159, 'Eslováquia': 5457012, 'Congo': 5380504, 'Noruega': 5378859,
          'Costa Rica': 5047561, 'Estado da Palestina': 4981422, 'Omã': 4974992, 'Libéria': 4937374, 'Irlanda': 4882498,
          'Nova Zelândia': 4783062, 'República Centro-Africana': 4745179, 'Mauritânia': 4525698, 'Panamá': 4246440,
          'Kuwait': 4207077, 'Croácia': 4130299, 'Moldávia': 4043258, 'Geórgia': 3996762, 'Eritreia': 3497117,
          'Uruguai': 3461731, 'Bósnia': 3300998, 'Mongólia': 3225166, 'Armênia': 2957728, 'Jamaica': 2948277,
          'Porto Rico': 2933404, 'Albânia': 2880913, 'Catar': 2832071, 'Lituânia': 2759631, 'Namíbia': 2494524,
          'Gâmbia': 2347696, 'Botswana': 2303703, 'Gabão': 2172578, 'Lesoto': 2125267,
          'República da Macedônia': 2083458, 'Eslovênia': 2078654, 'Guiné-Bissau': 1920917, 'Letônia': 1906740,
          'Bahrein': 1641164, 'Trindade e Tobago': 1394969, 'Guiné Equatorial': 1355982, 'Estônia': 132649,
          'Timor-Leste': 1293120, 'Maurícia': 1269670, 'Chipre': 1198574, 'Suazilândia': 1148133, 'Djibouti': 973557,
          'Fiji': 889955, 'Reunião': 888932, 'Comores': 850891, 'Guiana': 782775, 'Butão': 763094,
          'Ilhas Salomão': 669821, 'Macau': 640446, 'Montenegro': 627988, 'Luxemburgo': 615730,
          'Saara Ocidental': 582458, 'Suriname': 581363, 'Cabo Verde': 549936, 'Maldivas': 530957, 'Malta': 440377,
          'Brunei': 433296, 'Guadalupe': 400048, 'Belize': 390351, 'Bahamas': 389486, 'Martinica': 375557,
          'Islândia': 339037, 'Vanuatu': 299882, 'Guiana Francesa': 290823, 'Barbados': 287021,
          'Nova Caledônia': 282757, 'Polinésia Francesa': 279285, 'Mayotte': 266153, 'São Tomé e Príncipe': 215048,
          'Samoa': 197093, 'Santa Lúcia': 182795, 'Ilhas do Canal': 172264, 'Guam': 167295, 'Curaçao': 163423,
          'Kiribati': 117608, 'Micronésia': 113811, 'Granada': 112002, 'São Vicente de Granadinas': 110593,
          'Aruba': 106310, 'Ilhas Virgens Americanas': 104497, 'Tonga': 104497, 'Seychelles': 97741,
          'Antígua e Barbuda': 97115}
# ----------------------------------------------------------------------------------------------------------------------
print('-----------------------------------------------------------------------------------------------------------')
print('Este é um algorítmo que mostra como o Covid-19 se comporta!')
print('No banco de dados, há 200 países com seus respectivos números de habitantes. Digite corretamente o nome do'
      ' país.')
# ----------------------------------------------------------------------------------------------------------------------
v = 3
print('-----------------------------------------------------------------------------------------------------------')
pais = input('Escreva o nome do país: ')
pais = pais.title()
while pais not in paises:
    pais = input('Digitação incorreta. Verifique a digitação e tente novamente: ')
    pais = pais.title()
# ----------------------------------------------------------------------------------------------------------------------
else:
    if pais in paises:
        populacao = paises[pais]
# ----------------------------------------------------------------------------------------------------------------------
        print('--------------------------------------------------------------------------------------------------------'
              '---')
        print(f'Segundo o banco de dados, a população do país: {pais}, é de: {populacao}. (Dados de 2019)')
        opcao = input('Você deseja usar estes dados(S/N)?: ')
        opcao = opcao.title()
# ----------------------------------------------------------------------------------------------------------------------
        while opcao != 'Sim' and opcao != 'Não' and opcao != 'Nao' and opcao != 'S' and opcao != 'N':
            opcao = input('Resposta esperada: Sim ou Não. Você deseja usar estes dados?: ')
            opcao = opcao.title()
# ----------------------------------------------------------------------------------------------------------------------
        else:
            if opcao == 'Sim' or opcao == 'S':
                print('------------------------------------------------------------------------------------------------'
                      '-----------')
                casos = float(input(f'Digite o número de casos confirmados de Covid-19 no(a) {pais}: '))
                while casos <= 0:
                    casos = float(input(f'O número de casos não pode ser menor ou igual a 0! Digite novamente o número'
                                        f'de casos confirmados de Covid-19 no(a) {pais}: '))
# ----------------------------------------------------------------------------------------------------------------------
                else:
                    print('--------------------------------------------------------------------------------------------'
                          '---------------')
                    mortes = float(input(f'Agora digite quantos casos de mortes pela Covid-19 no(a) {pais}: '))
                    while casos < mortes:
                        mortes = float(input(f'O número de casos tem que ser maior que o número de mortos. Digite '
                                             f'novamente o número de mortes pela Covid-19 no(a) {pais}: '))
                        while mortes < 0:
                            mortes = float(input(f'O número de mortes não pode ser negativo! Ingresse novamente'
                                                 f'o número de mortes pela Covid-19 no(a) {pais}: '))
# -----------------------Multiplica-se o número de casos por 9 para obter o número de casos reais-----------------------
                    else:
                        mortes = mortes * 1.2
                        casosr = casos * 9
                        contagior = float(casosr / populacao)
# -------------------------------------------------------------------------------------------------------------------
                        contagio = float(casos / populacao)
                        letalidade = float(mortes / casos)
# -------------------------------------------------------------------------------------------------------------------
                        print('----------------------------------------------------------------------------------------'
                              '-------------------')
                        print('>O número de contaminados, de acordo com o número de casos confirmados, é de: {:.2f}%'
                              .format(contagio * 100))
                        print('>De acordo com estudos feitos na Inglaterra, o número REAL de contaminados é de: {:.2f}%'
                              .format(contagior * 100))
                        print('>A taxa de letalidade é de: {:.2f}%'.format(letalidade * 100))
                        print('>E, segundo os estudos feitos na Inglaterra, a REAL taxa de letalidade é de: {:.2f}%'
                              .format(mortes / casosr * 100))
                        print('----------------------------------------------------------------------------------------'
                              '-------------------')
                        print('Gerou-se um gráfico para este país!')
# -------------------------------------------------------------------------------------------------------------------
                        f = lambda x: v * 100 * math.pow(contagior * 100, x)
# -------------------------------------------------------------------------------------------------------------------
                        x = np.array(np.linspace(0, 8, 200))
                        y1 = np.array([f(i) for i in x])
# -------------------------------------------------------------------------------------------------------------------
                        plt.plot(x, y1)
# -------------------------------------------------------------------------------------------------------------------
                        plt.title('Gráfico de crescimento. Azul = Contaminados')
                        plt.grid()
                        plt.show()
# ----------------------------------------------------------------------------------------------------------------------
            elif opcao == 'Não' or opcao == 'Nao' or opcao == 'N':
                print('------------------------------------------------------------------------------------------------'
                      '-----------')
                pop = float(input('Digite o número de pessoas que deseja analisar: '))
                while pop <= 0:
                    pop = float(input('O número de pessoas não pode ser menor ou igual a 0. Digite novamente o '
                                      'número de pessoas que desrja analisar: '))
# ----------------------------------------------------------------------------------------------------------------------
                else:
                    print('--------------------------------------------------------------------------------------------'
                          '---------------')
                    casos = float(input(f'Digite o número de casos confirmados de Covid-19 neste grupo: '))
                    while casos <= 0:
                        casos = float(input('O número de casos não pode ser menor ou igual a 0! Digite novamente o '
                                            'número de casos confirmados de Covid-19 neste grupo: '))
# ----------------------------------------------------------------------------------------------------------------------
                    else:
                        print('----------------------------------------------------------------------------------------'
                              '-------------------')
                        mortes = float(input('Agora digite quantos casos de mortes pela Covid-19 neste grupo: '))
                        while casos < mortes:
                            mortes = float(input('O número de casos não pode ser maior que o número de mortes! '
                                                 'Digite novamente o número de moretes pela Covid-19 neste grupo: '))
                            while mortes < 0:
                                mortes = float(input(f'O número de mortes não pode ser negativo! Ingresse novamente'
                                                     f'o número de mortes pela Covid-19 neste grupo: '))
# -----------------------Multiplica-se o número de casos por 9 para obter o número de casos reais-----------------------
                        else:
                            casosr = casos * 9
                            contagior = float(casosr / pop)
# ----------------------------------------------------------------------------------------------------------------------
                            contagio = float(casos / pop)
                            letalidade = float(mortes / casos)
# ----------------------------------------------------------------------------------------------------------------------
                            print('------------------------------------------------------------------------------------'
                                  '-----------------------')
                            print('>O número de contaminados, de acordo com o número de casos confirmados, é de:'
                                  ' {:.2f}%'.format(contagio * 100))
# ----------------------------------------------------------------------------------------------------------------------
                    if pop >= 100000:
                        print('>Se este grupo for uma sociedade, de acordo com estudos feitos na Inglaterra, o número'
                              ' REAL de contamidados seria de: {:.2f}%'.format(contagior * 100))
                        print('>A taxa de letalidade é de: {:.2f}%'.format(letalidade * 100))
                        print('>E, segundo os estudos feitos na Inglaterra, a REAL taxa de letalidade é de: {:.2f}%'
                              .format(mortes / casosr * 100))
                        print('----------------------------------------------------------------------------------------'
                              '-------------------')
                        print('Gerou-se um gráfico para este grupo!')
# ----------------------------------------------------------------------------------------------------------------------
                    else:
                        print('>A taxa de letalidade é de: {:.2f}%'.format(letalidade * 100))
                        print('----------------------------------------------------------------------------------------'
                              '-------------------')
                        print('Gerou-se um gráfico para este grupo!')
# ----------------------------------------------------------------------------------------------------------------------
                    f = lambda x: v * math.pow(contagior * 100, x)
# ----------------------------------------------------------------------------------------------------------------------
                    x = np.array(np.linspace(0, 8, 1000))
                    y1 = np.array([f(i) for i in x])
# ----------------------------------------------------------------------------------------------------------------------
                    plt.plot(x, y1)
# ----------------------------------------------------------------------------------------------------------------------
                    plt.title('Gráfico de crescimento. Azul = Contaminados')
                    plt.grid()
                    plt.show()
# ----------------------------------------------------------------------------------------------------------------------
