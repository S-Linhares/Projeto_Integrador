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
    Montanhas_uivantes = Vertice('Montanhas Uivantes', 366)
    Palthar = Vertice('Palthar', 374)
    Hippiontar = Vertice('Hippiontar', 380)
    Rhond = Vertice('Rhond', 253)
    Altrim = Vertice('Altrim', 329)
    Nova_malpetrim = Vertice('Nova Malpetrim', 244)
    Nimbarann = Vertice('Nimbarann', 241)
    Barud = Vertice('Barud', 242)
    Thartann = Vertice('Thartann', 160)
    Yuvalin = Vertice('Yuvalin', 193)
    Kannilar = Vertice('Kannilar', 178)
    Zakharin = Vertice('Zakharin', 98)
    Valkaria = Vertice('Valkaria', 0)
    giurgiu = Vertice('Giurgiu', 77)

    Montanhas_uivantes.adiciona_adjacente(Adjacente(Palthar, 75))
    Montanhas_uivantes.adiciona_adjacente(Adjacente(Rhond, 140))
    Montanhas_uivantes.adiciona_adjacente(Adjacente(Altrim, 118))

    Palthar.adiciona_adjacente(Adjacente(Montanhas_uivantes, 75))
    Palthar.adiciona_adjacente(Adjacente(Hippiontar, 71))

    Hippiontar.adiciona_adjacente(Adjacente(Palthar, 71))
    Hippiontar.adiciona_adjacente(Adjacente(Rhond, 151))

    Rhond.adiciona_adjacente(Adjacente(Hippiontar, 151))
    Rhond.adiciona_adjacente(Adjacente(Montanhas_uivantes, 140))
    Rhond.adiciona_adjacente(Adjacente(Kannilar, 99))
    Rhond.adiciona_adjacente(Adjacente(Yuvalin, 80))

    Altrim.adiciona_adjacente(Adjacente(Montanhas_uivantes, 118))
    Altrim.adiciona_adjacente(Adjacente(Nova_malpetrim, 111))

    Nova_malpetrim.adiciona_adjacente(Adjacente(Altrim, 111))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Nimbarann, 70))

    Nimbarann.adiciona_adjacente(Adjacente(Nova_malpetrim, 70))
    Nimbarann.adiciona_adjacente(Adjacente(Barud, 75))

    Barud.adiciona_adjacente(Adjacente(Nimbarann, 75))
    Barud.adiciona_adjacente(Adjacente(Thartann, 120))

    Thartann.adiciona_adjacente(Adjacente(Barud, 120))
    Thartann.adiciona_adjacente(Adjacente(Zakharin, 138))
    Thartann.adiciona_adjacente(Adjacente(Yuvalin, 146))

    Yuvalin.adiciona_adjacente(Adjacente(Thartann, 146))
    Yuvalin.adiciona_adjacente(Adjacente(Rhond, 80))
    Yuvalin.adiciona_adjacente(Adjacente(Zakharin, 97))

    Kannilar.adiciona_adjacente(Adjacente(Rhond, 99))
    Kannilar.adiciona_adjacente(Adjacente(Valkaria, 211))

    Zakharin.adiciona_adjacente(Adjacente(Yuvalin, 97))
    Zakharin.adiciona_adjacente(Adjacente(Thartann, 138))
    Zakharin.adiciona_adjacente(Adjacente(Valkaria, 101))

    Valkaria.adiciona_adjacente(Adjacente(Kannilar, 211))
    Valkaria.adiciona_adjacente(Adjacente(Zakharin, 101))
    Valkaria.adiciona_adjacente(Adjacente(giurgiu, 90))


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


vetor = VetorOrdenado(20)
vetor.insere(grafo.Montanhas_uivantes.adjacentes[0])
vetor.insere(grafo.Montanhas_uivantes.adjacentes[1])
vetor.insere(grafo.Montanhas_uivantes.adjacentes[2])

vetor.imprime()


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('------------------')
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


busca_aestrela = AEstrela(grafo.Valkaria)
busca_aestrela.buscar(grafo.Montanhas_uivantes)
