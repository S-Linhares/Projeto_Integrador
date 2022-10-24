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

    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Yuvalin, 140))

    Palthar.adiciona_adjacente(Adjacente(Hippiontar, 300))

    Hippiontar.adiciona_adjacente(Adjacente(Kannilar, 995))

    Rhond.adiciona_adjacente(Adjacente(Zakharin, 205))

    Altrim.adiciona_adjacente(Adjacente(Nimbarann, 865))
    Altrim.adiciona_adjacente(Adjacente(Nova_malpetrim, 740))

    Nova_malpetrim.adiciona_adjacente(Adjacente(Altrim, 740))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Nimbarann, 300))

    Nimbarann.adiciona_adjacente(Adjacente(Nova_malpetrim, 300))
    Nimbarann.adiciona_adjacente(Adjacente(Barud, 215))
    Nimbarann.adiciona_adjacente(Adjacente(Altrim, 865))

    Barud.adiciona_adjacente(Adjacente(Nimbarann, 215))
    Barud.adiciona_adjacente(Adjacente(Floresta_Tollon, 335))

    Thartann.adiciona_adjacente(Adjacente(Valkaria, 825))
    Thartann.adiciona_adjacente(Adjacente(Floresta_Tollon, 460))

    Yuvalin.adiciona_adjacente(Adjacente(Zakharin, 350))
    Yuvalin.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 140))

    Kannilar.adiciona_adjacente(Adjacente(Hippiontar, 995))
    Kannilar.adiciona_adjacente(Adjacente(Villent, 200))

    Zakharin.adiciona_adjacente(Adjacente(Yuvalin, 350))
    Zakharin.adiciona_adjacente(Adjacente(Rhond, 205))
    Zakharin.adiciona_adjacente(Adjacente(Villent, 300))

    Valkaria.adiciona_adjacente(Adjacente(Coridrian, 510))
    Valkaria.adiciona_adjacente(Adjacente(Thartann, 825))
    Valkaria.adiciona_adjacente(Adjacente(Villent, 480))

    Coridrian.adiciona_adjacente(Adjacente(Valkaria, 510))

    Villent.adiciona_adjacente(Adjacente(Valkaria, 480))
    Villent.adiciona_adjacente(Adjacente(Kannilar, 200))
    Villent.adiciona_adjacente(Adjacente(Zakharin, 300))

    Floresta_Tollon.adiciona_adjacente(Adjacente(Thartann, 460))
    Floresta_Tollon.adiciona_adjacente(Adjacente(Barud, 335))


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
