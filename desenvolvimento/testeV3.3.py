import numpy as np


print(25*'-', 'CIDADES', 25*'-')
print(f'1 - Valkaria{"33 - Montanhas Uivantes(leste)":>42}\n2 - Palthar{"34 - Montanhas Uivantes(oeste)":>43}'
      f'\n3 - Rhond{"35 - Montanhas Uivantes(sul)":>43}\n4 - Nova Malpetrim{"36 - Montanhas Uinvantes(norte)":>37}'
      f'\n5 - Barud{"37 - Montanhas Uivantes(centro)":>46}\n6 - Yuvalin{"38 - Grande Savana(oeste)":>38}\n7 - Zakharin'
      f'{"39 - Grande Savana(leste)":>37}\n8 - Villent{"40 - Grande Savana(centro)":>39}\n9 - Hippiontar'
      f'{"41 - Montanhas Sanguinarias(sul)":>42}\n10 - Altrim{"42 - Montanhas Sanguinarias(centro)":>48}'
      f'\n11 - Nimbarann{"43 - Montanhas Sanguinarias(norte)":>44}\n12 - Thartann'
      f'{"44 - Deserto da Perdição(leste)":>42}\n13 - Kannilar{"45 - Deserto da Perdição(centro)":>43}\n14 - Coridrian'
      f'{"46 - Deserto da Perdição(oeste)":>41}\n15 - Horeen{"47 - Ermos Púrpuras":>32}\n16 - Smokestone'
      f'{"48 - Floresta Tollon":>29}\n17 - Giluk{"49 - Floresta das Escamas Verdes":>46}\n18 - Fross'
      f'{"50 - A Cidade Normal dos Humanos":>46}\n19 - Yukadar{"51 - Khershandallas":>31}\n20 - Yuton'
      f'{"52 - Cidade no Deserto":>36}\n21 - Roschfallen{"53 - Ruinas de Tyrondir":>31}\n22 - Norm'
      f'{"54 - Imperio de Tauron(leste)":>44}\n23 - Milothiann{"55 - Imperio de Tauron(oeste)":>38}\n24 - Norba'
      f'{"56 - Imperio de Tauron(centro)":>44}\n25 - Coravandor{"57 - Imperio de Tauron(norte)":>38}\n26 - Adhurian'
      f'{"58 - Tiberus":>23}\n27 - Lannestul\n28 - Sternatchen\n29 - Khalifor\n30 - Lysianassa\n31 - Monte Palidor'
      f'\n32 - Ghallistryx')
print(59*'-')

cidade_destino = int(input('Informe qual cidade deseja que seja o destino: '))
cidade_origem = int(input('Informe qual cidade deseja que seja a origem: '))


class Vertice:

    def __init__(self, nome, distancia_objetivo):
        self.nome = nome
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.nome, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

        # Novo atributo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


def switch_dist_zero(selecao):
    if selecao == 1:
        lista_zero = (750, 1800, 1250, 1500, 1300, 2900, 2250, 2750, 3690, 4190, 5000, 3750, 3250, 3750, 1995, 3250,
                      2540, 2985, 2200, 1700, 1650, 800, 2600, 1950, 1650, 1525, 825, 855, 675, 550, 0, 510, 480, 1205,
                      950, 2135, 1625, 2525, 2045, 1640, 1090, 1490, 1490, 1765, 2200, 2120, 2690, 3120, 3450, 4190,
                      3790, 3300, 4750, 340, 700, 1050, 1325, 2750)
    return lista_zero


class Grafo:

    lista = switch_dist_zero(cidade_destino)

    Montanhas_uivantes_leste = Vertice('Montanhas Uivantes(leste)', lista[0])
    Montanhas_uivantes_oeste = Vertice('Montanhas Uivantes(oeste)', lista[1])
    Montanhas_uivantes_sul = Vertice('Montanhas Uivantes(sul)', lista[2])
    Montanhas_uivantes_norte = Vertice('Montanhas Uivantes(norte)', lista[3])
    Montanhas_uivantes_centro = Vertice('Montanhas Uivantes(centro)', lista[4])
    Savana_oeste = Vertice('Grande Savana(oeste)', lista[5])
    Savana_centro = Vertice('Grande Savana(centro)', lista[6])
    Savana_leste = Vertice('Grande Savana(leste)', lista[7])
    Sanguinarias_sul = Vertice('Montanhas Sanguinarias(sul)', lista[8])
    Sanguinarias_centro = Vertice('Montanhas Sanguinarias(centro)', lista[9])
    Sanguinarias_norte = Vertice('Montanhas Sanguinarias(norte)', lista[10])
    Deserto_leste = Vertice('Deserto da Perdição(leste)', lista[11])
    Deserto_centro = Vertice('Deserto da Perdição(centro)', lista[12])
    Deserto_oeste = Vertice('Deserto da Perdição(oeste)', lista[13])
    Tauron_leste = Vertice('Imperio de Tauron(leste)', lista[14])
    Tauron_oeste = Vertice('Imperio de Tauron(oeste)', lista[15])
    Tauron_centro = Vertice('Imperio de Tauron(centro)', lista[16])
    Tauron_norte = Vertice('Impero de Tauron(norte)', lista[17])
    Tiberus = Vertice('Tiberus', lista[18])
    Palthar = Vertice('Palthar', lista[19])
    Hippiontar = Vertice('Hippiontar', lista[20])
    Rhond = Vertice('Rhond', lista[21])
    Altrim = Vertice('Altrim', lista[22])
    Nova_malpetrim = Vertice('Nova Malpetrim', lista[23])
    Nimbarann = Vertice('Nimbarann', lista[24])
    Barud = Vertice('Barud', lista[25])
    Thartann = Vertice('Thartann', lista[26])
    Yuvalin = Vertice('Yuvalin', lista[27])
    Kannilar = Vertice('Kannilar', lista[28])
    Zakharin = Vertice('Zakharin', lista[29])
    Valkaria = Vertice('Valkaria', lista[30])
    Coridrian = Vertice('Coridrian', lista[31])
    Villent = Vertice('Villent', lista[32])
    Floresta_Tollon = Vertice('Floresta de Tollon', lista[33])
    Horeen = Vertice('Horeen', lista[34])
    Smokestone = Vertice('Smokestone', lista[35])
    Giluk = Vertice('Giluk', lista[36])
    Fross = Vertice('Fross', lista[37])
    Yukadar = Vertice('Yukadar', lista[38])
    Yuton = Vertice('Yuton', lista[39])
    Roschfallen = Vertice('Roschfallen', lista[40])
    Norm = Vertice('Norm', lista[41])
    Ermos = Vertice('Ermos Púrpuras', lista[42])
    Milothiann = Vertice('Milothiann', lista[43])
    Floresta_Verde = Vertice('Floresta das Escamas Verdes', lista[44])
    Norba = Vertice('Norba', lista[45])
    Cidade_humanos = Vertice('A Cidade Normal dos Humanos', lista[46])
    Coravandor = Vertice('Coravandor', lista[47])
    Adhurian = Vertice('Adhurian', lista[48])
    Ghallistryx = Vertice('Ghallistryx', lista[49])
    Khershandallas = Vertice('Khershandallas', lista[50])
    Cidade_deserto = Vertice('Cidade no Deserto', lista[51])
    Lannestul = Vertice('Lannestul', lista[52])
    Monte_palidor = Vertice('Monte Palidor', lista[53])
    Ruinas = Vertice('Ruinas de Tyrondir', lista[54])
    Sternatchen = Vertice('Sternatchen', lista[55])
    Khalifor = Vertice('Khalifor', lista[56])
    Lysianassa = Vertice('Lysianassa', lista[57])

    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Yuvalin, 140))
    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 710))
    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 730))

    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 500))
    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Giluk, 290))
    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Tiberus, 525))
    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Tauron_centro, 850))

    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 710))
    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 485))
    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Barud, 350))
    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Giluk, 390))

    Montanhas_uivantes_norte.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 420))
    Montanhas_uivantes_norte.adiciona_adjacente(Adjacente(Tauron_leste, 755))

    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 730))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 485))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_norte, 420))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 500))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Giluk, 300))

    Savana_oeste.adiciona_adjacente(Adjacente(Tauron_norte, 860))
    Savana_oeste.adiciona_adjacente(Adjacente(Savana_centro, 1250))
    Savana_oeste.adiciona_adjacente(Adjacente(Cidade_deserto, 760))

    Savana_centro.adiciona_adjacente(Adjacente(Savana_oeste, 1250))
    Savana_centro.adiciona_adjacente(Adjacente(Savana_leste, 1380))
    Savana_centro.adiciona_adjacente(Adjacente(Palthar, 755))
    Savana_centro.adiciona_adjacente(Adjacente(Deserto_centro, 810))

    Savana_leste.adiciona_adjacente(Adjacente(Savana_centro, 1380))
    Savana_leste.adiciona_adjacente(Adjacente(Fross, 340))
    Savana_leste.adiciona_adjacente(Adjacente(Deserto_leste, 1000))

    Sanguinarias_sul.adiciona_adjacente(Adjacente(Adhurian, 330))
    Sanguinarias_sul.adiciona_adjacente(Adjacente(Sanguinarias_centro, 1000))

    Sanguinarias_centro.adiciona_adjacente(Adjacente(Sanguinarias_sul, 1000))
    Sanguinarias_centro.adiciona_adjacente(Adjacente(Coravandor, 1100))
    Sanguinarias_centro.adiciona_adjacente(Adjacente(Sanguinarias_norte, 840))
    Sanguinarias_centro.adiciona_adjacente(Adjacente(Khershandallas, 750))

    Sanguinarias_norte.adiciona_adjacente(Adjacente(Sanguinarias_centro, 840))
    Sanguinarias_norte.adiciona_adjacente(Adjacente(Ghallistryx, 350))

    Deserto_leste.adiciona_adjacente(Adjacente(Khershandallas, 1350))
    Deserto_leste.adiciona_adjacente(Adjacente(Savana_leste, 1000))
    Deserto_leste.adiciona_adjacente(Adjacente(Deserto_centro, 1390))

    Deserto_centro.adiciona_adjacente(Adjacente(Deserto_leste, 1390))
    Deserto_centro.adiciona_adjacente(Adjacente(Savana_centro, 810))
    Deserto_centro.adiciona_adjacente(Adjacente(Deserto_oeste, 1325))

    Deserto_oeste.adiciona_adjacente(Adjacente(Deserto_centro, 1325))
    Deserto_oeste.adiciona_adjacente(Adjacente(Cidade_deserto, 200))
    Deserto_oeste.adiciona_adjacente(Adjacente(Lannestul, 1300))

    Tauron_leste.adiciona_adjacente(Adjacente(Montanhas_uivantes_norte, 755))
    Tauron_leste.adiciona_adjacente(Adjacente(Tauron_centro, 1300))

    Tauron_oeste.adiciona_adjacente(Adjacente(Tiberus, 1100))
    Tauron_oeste.adiciona_adjacente(Adjacente(Tauron_centro, 965))

    Tauron_centro.adiciona_adjacente(Adjacente(Tauron_leste, 1300))
    Tauron_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 850))
    Tauron_centro.adiciona_adjacente(Adjacente(Tiberus, 850))
    Tauron_centro.adiciona_adjacente(Adjacente(Tauron_oeste, 965))
    Tauron_centro.adiciona_adjacente(Adjacente(Tauron_norte, 600))

    Tauron_norte.adiciona_adjacente(Adjacente(Tauron_centro, 600))
    Tauron_norte.adiciona_adjacente(Adjacente(Savana_oeste, 860))

    Tiberus.adiciona_adjacente(Adjacente(Altrim, 525))
    Tiberus.adiciona_adjacente(Adjacente(Tauron_oeste, 1100))
    Tiberus.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 430))
    Tiberus.adiciona_adjacente(Adjacente(Tauron_centro, 850))

    Palthar.adiciona_adjacente(Adjacente(Hippiontar, 300))
    Palthar.adiciona_adjacente(Adjacente(Savana_centro, 755))
    Palthar.adiciona_adjacente(Adjacente(Fross, 905))
    Palthar.adiciona_adjacente(Adjacente(Yukadar, 735))

    Hippiontar.adiciona_adjacente(Adjacente(Kannilar, 995))
    Hippiontar.adiciona_adjacente(Adjacente(Palthar, 300))
    Hippiontar.adiciona_adjacente(Adjacente(Yuton, 495))

    Rhond.adiciona_adjacente(Adjacente(Zakharin, 205))

    Altrim.adiciona_adjacente(Adjacente(Nimbarann, 865))
    Altrim.adiciona_adjacente(Adjacente(Nova_malpetrim, 740))
    Altrim.adiciona_adjacente(Adjacente(Smokestone, 360))
    Altrim.adiciona_adjacente(Adjacente(Tiberus, 525))

    Nova_malpetrim.adiciona_adjacente(Adjacente(Altrim, 740))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Nimbarann, 300))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Smokestone, 430))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Lysianassa, 850))

    Nimbarann.adiciona_adjacente(Adjacente(Nova_malpetrim, 300))
    Nimbarann.adiciona_adjacente(Adjacente(Barud, 215))
    Nimbarann.adiciona_adjacente(Adjacente(Altrim, 865))
    Nimbarann.adiciona_adjacente(Adjacente(Smokestone, 550))
    Nimbarann.adiciona_adjacente(Adjacente(Giluk, 600))

    Barud.adiciona_adjacente(Adjacente(Nimbarann, 215))
    Barud.adiciona_adjacente(Adjacente(Floresta_Tollon, 335))
    Barud.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 350))

    Thartann.adiciona_adjacente(Adjacente(Valkaria, 825))
    Thartann.adiciona_adjacente(Adjacente(Floresta_Tollon, 460))
    Thartann.adiciona_adjacente(Adjacente(Ruinas, 845))
    Thartann.adiciona_adjacente(Adjacente(Horeen, 190))

    Yuvalin.adiciona_adjacente(Adjacente(Zakharin, 350))
    Yuvalin.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 140))

    Kannilar.adiciona_adjacente(Adjacente(Hippiontar, 995))
    Kannilar.adiciona_adjacente(Adjacente(Villent, 200))
    Kannilar.adiciona_adjacente(Adjacente(Roschfallen, 700))

    Zakharin.adiciona_adjacente(Adjacente(Yuvalin, 350))
    Zakharin.adiciona_adjacente(Adjacente(Rhond, 205))
    Zakharin.adiciona_adjacente(Adjacente(Villent, 300))

    Valkaria.adiciona_adjacente(Adjacente(Coridrian, 510))
    Valkaria.adiciona_adjacente(Adjacente(Thartann, 825))
    Valkaria.adiciona_adjacente(Adjacente(Villent, 480))
    Valkaria.adiciona_adjacente(Adjacente(Monte_palidor, 340))

    Coridrian.adiciona_adjacente(Adjacente(Valkaria, 510))

    Villent.adiciona_adjacente(Adjacente(Valkaria, 480))
    Villent.adiciona_adjacente(Adjacente(Kannilar, 200))
    Villent.adiciona_adjacente(Adjacente(Zakharin, 300))

    Floresta_Tollon.adiciona_adjacente(Adjacente(Thartann, 460))
    Floresta_Tollon.adiciona_adjacente(Adjacente(Barud, 335))

    Horeen.adiciona_adjacente(Adjacente(Thartann, 190))

    Smokestone.adiciona_adjacente(Adjacente(Nimbarann, 550))
    Smokestone.adiciona_adjacente(Adjacente(Nova_malpetrim, 430))
    Smokestone.adiciona_adjacente(Adjacente(Altrim, 360))

    Giluk.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 390))
    Giluk.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 300))
    Giluk.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 290))
    Giluk.adiciona_adjacente(Adjacente(Nimbarann, 600))

    Fross.adiciona_adjacente(Adjacente(Savana_leste, 340))
    Fross.adiciona_adjacente(Adjacente(Palthar, 905))
    Fross.adiciona_adjacente(Adjacente(Yukadar, 500))

    Yukadar.adiciona_adjacente(Adjacente(Fross, 500))
    Yukadar.adiciona_adjacente(Adjacente(Palthar, 735))
    Yukadar.adiciona_adjacente(Adjacente(Norba, 300))

    Yuton.adiciona_adjacente(Adjacente(Hippiontar, 495))
    Yuton.adiciona_adjacente(Adjacente(Ermos, 550))

    Roschfallen.adiciona_adjacente(Adjacente(Kannilar, 700))
    Roschfallen.adiciona_adjacente(Adjacente(Norm, 235))
    Roschfallen.adiciona_adjacente(Adjacente(Ermos, 400))

    Norm.adiciona_adjacente(Adjacente(Roschfallen, 235))

    Ermos.adiciona_adjacente(Adjacente(Yuton, 550))
    Ermos.adiciona_adjacente(Adjacente(Roschfallen, 400))
    Ermos.adiciona_adjacente(Adjacente(Milothiann, 385))

    Milothiann.adiciona_adjacente(Adjacente(Ermos, 385))
    Milothiann.adiciona_adjacente(Adjacente(Floresta_Verde, 600))

    Floresta_Verde.adiciona_adjacente(Adjacente(Milothiann, 600))
    Floresta_Verde.adiciona_adjacente(Adjacente(Norba, 590))
    Floresta_Verde.adiciona_adjacente(Adjacente(Adhurian, 1290))

    Norba.adiciona_adjacente(Adjacente(Yukadar, 300))
    Norba.adiciona_adjacente(Adjacente(Floresta_Verde, 590))
    Norba.adiciona_adjacente(Adjacente(Cidade_humanos, 980))

    Cidade_humanos.adiciona_adjacente(Adjacente(Norba, 980))
    Cidade_humanos.adiciona_adjacente(Adjacente(Coravandor, 475))

    Coravandor.adiciona_adjacente(Adjacente(Cidade_humanos, 475))
    Coravandor.adiciona_adjacente(Adjacente(Sanguinarias_centro, 1100))

    Adhurian.adiciona_adjacente(Adjacente(Floresta_Verde, 1290))
    Adhurian.adiciona_adjacente(Adjacente(Sanguinarias_sul, 330))

    Ghallistryx.adiciona_adjacente(Adjacente(Sanguinarias_norte, 350))
    Ghallistryx.adiciona_adjacente(Adjacente(Khershandallas, 400))

    Khershandallas.adiciona_adjacente(Adjacente(Ghallistryx, 400))
    Khershandallas.adiciona_adjacente(Adjacente(Sanguinarias_centro, 750))
    Khershandallas.adiciona_adjacente(Adjacente(Deserto_leste, 1350))

    Cidade_deserto.adiciona_adjacente(Adjacente(Deserto_oeste, 200))
    Cidade_deserto.adiciona_adjacente(Adjacente(Savana_oeste, 760))

    Lannestul.adiciona_adjacente(Adjacente(Deserto_oeste, 1300))

    Monte_palidor.adiciona_adjacente(Adjacente(Valkaria, 340))
    Monte_palidor.adiciona_adjacente(Adjacente(Ruinas, 325))

    Ruinas.adiciona_adjacente(Adjacente(Monte_palidor, 325))
    Ruinas.adiciona_adjacente(Adjacente(Thartann, 845))
    Ruinas.adiciona_adjacente(Adjacente(Sternatchen, 500))

    Sternatchen.adiciona_adjacente(Adjacente(Ruinas, 500))
    Sternatchen.adiciona_adjacente(Adjacente(Khalifor, 800))

    Khalifor.adiciona_adjacente(Adjacente(Sternatchen, 800))

    Lysianassa.adiciona_adjacente(Adjacente(Nova_malpetrim, 850))


grafo = Grafo()


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.nome, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print(45*'-')
        print('Atual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)


def switch_cities(opcao):
    if opcao == 1:
        return grafo.Valkaria
    elif opcao == 2:
        return grafo.Palthar
    elif opcao == 3:
        return grafo.Rhond
    elif opcao == 4:
        return grafo.Nova_malpetrim
    elif opcao == 5:
        return grafo.Barud
    elif opcao == 6:
        return grafo.Yuvalin
    elif opcao == 7:
        return grafo.Zakharin
    elif opcao == 8:
        return grafo.Villent
    elif opcao == 9:
        return grafo.Hippiontar
    elif opcao == 10:
        return grafo.Altrim
    elif opcao == 11:
        return grafo.Nimbarann
    elif opcao == 12:
        return grafo.Thartann
    elif opcao == 13:
        return grafo.Kannilar
    elif opcao == 14:
        return grafo.Coridrian
    elif opcao == 15:
        return grafo.Horeen
    elif opcao == 16:
        return grafo.Smokestone
    elif opcao == 17:
        return grafo.Giluk
    elif opcao == 18:
        return grafo.Fross
    elif opcao == 19:
        return grafo.Yukadar
    elif opcao == 20:
        return grafo.Yuton
    elif opcao == 21:
        return grafo.Roschfallen
    elif opcao == 22:
        return grafo.Norm
    elif opcao == 23:
        return grafo.Milothiann
    elif opcao == 24:
        return grafo.Norba
    elif opcao == 25:
        return grafo.Coravandor
    elif opcao == 26:
        return grafo.Adhurian
    elif opcao == 27:
        return grafo.Lannestul
    elif opcao == 28:
        return grafo.Sternatchen
    elif opcao == 29:
        return grafo.Khalifor
    elif opcao == 30:
        return grafo.Lysianassa
    elif opcao == 31:
        return grafo.Monte_palidor
    elif opcao == 32:
        return grafo.Ghallistryx
    elif opcao == 33:
        return grafo.Montanhas_uivantes_leste
    elif opcao == 34:
        return grafo.Montanhas_uivantes_oeste
    elif opcao == 35:
        return grafo.Montanhas_uivantes_sul
    elif opcao == 36:
        return grafo.Montanhas_uivantes_norte
    elif opcao == 37:
        return grafo.Montanhas_uivantes_centro
    elif opcao == 38:
        return grafo.Savana_oeste
    elif opcao == 39:
        return grafo.Savana_leste
    elif opcao == 40:
        return grafo.Savana_centro
    elif opcao == 41:
        return grafo.Sanguinarias_sul
    elif opcao == 42:
        return grafo.Sanguinarias_centro
    elif opcao == 43:
        return grafo.Sanguinarias_norte
    elif opcao == 44:
        return grafo.Deserto_leste
    elif opcao == 45:
        return grafo.Deserto_centro
    elif opcao == 46:
        return grafo.Deserto_oeste
    elif opcao == 47:
        return grafo.Ermos
    elif opcao == 48:
        return grafo.Floresta_Tollon
    elif opcao == 49:
        return grafo.Floresta_Verde
    elif opcao == 50:
        return grafo.Cidade_humanos
    elif opcao == 51:
        return grafo.Khershandallas
    elif opcao == 52:
        return grafo.Cidade_deserto
    elif opcao == 53:
        return grafo.Ruinas
    elif opcao == 54:
        return grafo.Tauron_leste
    elif opcao == 55:
        return grafo.Tauron_oeste
    elif opcao == 56:
        return grafo.Tauron_centro
    elif opcao == 57:
        return grafo.Tauron_norte
    elif opcao == 58:
        return grafo.Tiberus


busca_aestrela = AEstrela(switch_cities(cidade_destino))
busca_aestrela.buscar(switch_cities(cidade_origem))
print('\n')