from node import *

class MinMax:

    cont = None  #contador de nos

    def __init__(self):
        self.cont = 0  #inicializa a classe e seta o contador como 0

    def getCont(self):
        return self.cont

    def copyArray(self,arr):  # faz uma copia de um vetor
        res=[]
        for i in range(0,len(arr)):
            res.append(arr[i])
        return res

    # ESSA É A FUNAÇAO CHAMADA POR FORA, ela se responsabiliza por encapsular um vetor na estrutura Node
    #e retorna o vetor q corresponde ao movimento qua a IA escolheu
    def choose(self,arr):
        self.cont = 0   #reinicia o contador a cada movimento da IA
        node = Node(arr)   #encapsula
        node = self.buildTree(node,'max')   #entra na recursão para construir a arvore de movimentos da IA, começa como max pois a IA sempre quer o max
        print(self.cont)
        return node.choice.array    #o atributo choiseSon é o Node filho do Node atual que representa o movimento que a IA escolheu

    #essa função é usada na recursão para determinar se o Node enviado como paramatro é um Node final
    #precisamos dessa informaçao para nao construir Nodes desenecessarios durante a construçao da arvore
    # se for um Final onde o X ganha retorna 1
    # se for um Final onde o O ganha retorna 2
    # se for um Final onde ninguem ganha retorna 0
    # se nao for um Final retorna 4
    def isFinal(self,node):
        if (node.array[0]==1 and node.array[1]==1 and node.array[2]==1):
            return 1
        if (node.array[3]==1 and node.array[4]==1 and node.array[5]==1):
            return 1
        if (node.array[6]==1 and node.array[7]==1 and node.array[8]==1):
            return 1
        if (node.array[0]==1 and node.array[3]==1 and node.array[6]==1):
            return 1
        if (node.array[1]==1 and node.array[4]==1 and node.array[7]==1):
            return 1
        if (node.array[2]==1 and node.array[5]==1 and node.array[8]==1):
            return 1
        if (node.array[0]==1 and node.array[4]==1 and node.array[8]==1):
            return 1
        if (node.array[2]==1 and node.array[4]==1 and node.array[6]==1):
            return 1

        if (node.array[0]==2 and node.array[1]==2 and node.array[2]==2):
            return 2
        if (node.array[3]==2 and node.array[4]==2 and node.array[5]==2):
            return 2
        if (node.array[6]==2 and node.array[7]==2 and node.array[8]==2):
            return 2
        if (node.array[0]==2 and node.array[3]==2 and node.array[6]==2):
            return 2
        if (node.array[1]==2 and node.array[4]==2 and node.array[7]==2):
            return 2
        if (node.array[2]==2 and node.array[5]==2 and node.array[8]==2):
            return 2
        if (node.array[0]==2 and node.array[4]==2 and node.array[8]==2):
            return 2
        if (node.array[2]==2 and node.array[4]==2 and node.array[6]==2):
            return 2
        for i in range(0,len(node.array)):
            if (node.array[i] == 0):
                return 4
        return 0

    #funçao chamada pela classe de fora para verificar se o estado atual é Final
    def checkWin(self,arr):
        node = Node(arr)   #encapsula
        return self.isFinal(node)   #usa a msm funçao que é usada na hora da construçao da arvore

    #funçao que constroi a arvore a partir de um dado Node
    #essa funçao é recursiva
    #o Node q vem como parameto sera retornado no final com seus atributos VALUE, SONS e CHOISESON definidos
    #o parametro TYPE serve para informar se essa funçao foi chamada num nivel de min ou max na hora da construçao da arvore
    def buildTree(self,node,type):

        if (self.isFinal(node)==1):   #verifica se o Node enviado como parametro representa um Final onde o X(IA) ganhou
            node.choice = node  #esse Node nao possui filhos por ser final, logo o Node q representa o movimento a ser feito é manter ele mesmo
            node.value = 1   #define o valor do Node para 1, que é o valor de MAX
            return node
        if (self.isFinal(node)==2):
            node.choice = node
            node.value = -1
            return node
        if (self.isFinal(node)==0):
            node.choice=node
            node.value = 0
            return node
        else:

            if(type == 'min'):
                for i in range(0,len(node.array)):
                    if (node.array[i] == 0):
                        copiedArray = self.copyArray(node.array)
                        copiedArray[i] = 2
                        son = Node(copiedArray)
                        self.cont = self.cont + 1
                        son.father = node
                        son = self.buildTree(son, 'max')
                        if (node.value == None or son.value < node.value):
                            node.value = son.value
                            node.choice = son
                return node
            if (type == 'max'):
                for i in range(0,len(node.array)):
                    if (node.array[i] == 0):
                        copiedArray = self.copyArray(node.array)
                        copiedArray[i] = 1
                        son = Node(copiedArray)
                        self.cont = self.cont + 1
                        son.father = node
                        son = self.buildTree(son,'min')
                        if(node.value == None or son.value>node.value):
                            node.value = son.value
                            node.choice = son
                return node