import numpy as np


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


class Grafo:
    Montanhas_uivantes_leste = Vertice('Montanhas Uivantes(leste)', 750)
    Montanhas_uivantes_oeste = Vertice('Montanhas Uivantes(oeste)', 1800)
    Montanhas_uivantes_sul = Vertice('Montanhas Uivantes(sul)', 1250)
    Montanhas_uivantes_norte = Vertice('Montanhas Uivantes(norte)', 1500)
    Montanhas_uivantes_centro = Vertice('Montanhas Uivantes(centro)', 1300)
    Savana_oeste = Vertice('Grande Savana(oeste)', 2900)
    Savana_centro = Vertice('Grande Savana(centro)', 2250)
    Savana_leste = Vertice('Grande Savana(leste)', 2750)
    Sanguinarias_sul = Vertice('Montanhas Sanguinarias(sul)', 3690)
    Sanguinarias_centro = Vertice('Montanhas Sanguinarias(centro)', 4190)
    Sanguinarias_norte = Vertice('Montanhas Sanguinarias(norte)', 5000)
    Deserto_leste = Vertice('Deserto da Perdição(leste)', 3750)
    Deserto_centro = Vertice('Deserto da Perdição(centro)', 3250)
    Deserto_oeste = Vertice('Deserto da Perdição(oeste)', 3750)
    Tauron_leste = Vertice('Imperio de Tauron(leste)', 1995)
    Tauron_oeste = Vertice('Imperio de Tauron(oeste)', 3250)
    Tauron_centro = Vertice('Imperio de Tauron(centro)', 2540)
    Tauron_norte = Vertice('Impero de Tauron(norte)', 2985)
    Tiberus = Vertice('Tiberus', 2200)
    Palthar = Vertice('Palthar', 1700)
    Hippiontar = Vertice('Hippiontar', 1650)
    Rhond = Vertice('Rhond', 800)
    Altrim = Vertice('Altrim', 2600)
    Nova_malpetrim = Vertice('Nova Malpetrim', 1950)
    Nimbarann = Vertice('Nimbarann', 1650)
    Barud = Vertice('Barud', 1525)
    Thartann = Vertice('Thartann', 825)
    Yuvalin = Vertice('Yuvalin', 855)
    Kannilar = Vertice('Kannilar', 675)
    Zakharin = Vertice('Zakharin', 550)
    Valkaria = Vertice('Valkaria', 0)
    Coridrian = Vertice('Coridrian', 510)
    Villent = Vertice('Villent', 480)
    Floresta_Tollon = Vertice('Floresta de Tollon', 1205)
    Horeen = Vertice('Horeen', 950)
    Smokestone = Vertice('Smokestone', 2135)
    Giluk = Vertice('Giluk', 1625)
    Fross = Vertice('Fross', 2525)
    Yukadar = Vertice('Yukadar', 2045)
    Yuton = Vertice('Yuton', 1640)
    Roschfallen = Vertice('Roschfallen', 1090)
    Norm = Vertice('Norm', 1490)
    Ermos = Vertice('Ermos Púrpuras', 1490)
    Milothiann = Vertice('Milothiann', 1765)
    Floresta_Verde = Vertice('Floresta das Escamas Verdes', 2200)
    Norba = Vertice('Norba', 2120)
    Cidade_humanos = Vertice('A Cidade Normal dos Humanos', 2690)
    Coravandor = Vertice('Coravandor', 3120)
    Adhurian = Vertice('Adhurian', 3450)
    Ghallistryx = Vertice('Ghallistryx', 4190)
    Khershandallas = Vertice('Khershandallas', 3790)
    Cidade_deserto = Vertice('Cidade no Deserto', 3300)
    Lannestul = Vertice('Lannestul', 4750)
    Monte_palidor = Vertice('Monte Palidor', 340)
    Ruinas = Vertice('Ruinas de Tyrondir', 700)
    Sternatchen = Vertice('Sternatchen', 1050)
    Khalifor = Vertice('Khalifor', 1325)
    Lysianassa = Vertice('Lysianassa', 2750)

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


def switch(opcao):
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
        return grafo.Montanhas_uivantes_leste
    elif opcao == 10:
        return grafo.Hippiontar
    elif opcao == 11:
        return grafo.Altrim
    elif opcao == 12:
        return grafo.Nimbarann
    elif opcao == 13:
        return grafo.Thartann
    elif opcao == 14:
        return grafo.Kannilar
    elif opcao == 15:
        return grafo.Coridrian
    elif opcao == 16:
        return grafo.Floresta_Tollon


print(21*'-', 'CIDADES', 21*'-')
print(f'1 - Valkaria{"9 - Montanhas uivantes(leste)":>39}\n2 - Palthar{"10 - Hippiontar":>26}\n'
      f'3 - Rhond{"11 - Altrim":>24}\n4 - Nova Malpetrim{"12 - Nimbarann":>18}\n5 - Barud{"13 - Thartann":>26}\n'
      f'6 - Yuvalin{"14 - Kannilar":>24}\n7 - Zakharin{"15 - Coridrian":>24}\n8 - Villent{"16 - Floresta Tollon":>31}')
print(51*'-')
busca_aestrela = AEstrela(switch(int(input('Informe qual cidade deseja que seja o destino: '))))
busca_aestrela.buscar(switch(int(input('Informe qual cidade deseja que seja a origem: '))))
