# Fazendo a importação do projeto da 1 VA
import va1

class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.nivel = 0
       

    def __str__(self):
          return f'{self.value}'

    def is_leaf(self):
        return self.right is None and self.left is None

class Tree:
    
    def __init__(self, raiz=None):
        self.raiz = raiz
        self.__total_nodes = 0

    def add(self, value):
        no = No(value)
        self.__total_nodes += 1
        if not self.raiz:
            self.raiz = no
            return
        perc = self.raiz
        while True:
            no.nivel += 1
            if value > perc.value:
                if not perc.right:
                    perc.right = no
                    break
                perc = perc.right
            else:
                if not perc.left:
                    perc.left = no
                    break
                perc = perc.left

    def length(self):
          return self.__total_nodes

    def pre_ordem(self):
        self._print(self.raiz, 'pre')

    def in_ordem(self):
        self._print(self.raiz, 'in')

    def pos_ordem(self):
        self._print(self.raiz, 'pos')

    def _print(self, perc, type):
        if not perc:
            return
        if type == 'pre':
            print(perc.value)
        self._print(perc.left, type)
        if type == 'in':
            print(perc.value)
        self._print(perc.right, type)
        if type == 'pos':
            print(perc.value)

    def __str__(self):
        print(self.raiz.value)
        print(self.raiz.left.value)
        print(self.raiz.right.value)

    def _get_perc(self, perc, value, ant=None):
        if not perc or perc.value == value:
            return perc, ant
        elif value > perc.value:
            return self._get_perc(perc.right, value, perc)
        else:
            return self._get_perc(perc.left, value, perc)

    def get(self, value):
        perc = self.raiz
        if not perc:
            return None
        while perc is not None and perc.value != value:
            if value > perc.value:
                perc = perc.right
            else:
                perc = perc.left
        return perc


    def _get_min(self, no):
        perc = no
        while perc.left:
            perc = perc.left
        return perc

    def _get_max(self, no):
        pred = no
        while pred.right:
            pred = pred.right
        return pred

    def _get_sucessor(self, no):
        sucessor = self._get_min(no.right)
        return sucessor

    def _get_predecessor(self, no):
        perc = self._get_max(no.left)
        return perc

    def altura(self, valor):
        # começa a busca a partir da raiz da árvore
        no_atual = self.raiz

    # percorre a árvore enquanto não chegar a um nó vazio
        while no_atual is not None:
        # compara o valor buscado com o valor do nó atual
            if valor == no_atual.valor:
                # se encontrou o nó, retorna-o
                return no_atual
            elif valor < no_atual.valor:
                # se o valor buscado for menor que o valor do nó atual,
                # continua a busca na subárvore esquerda
                no_atual = no_atual.esquerda
            else:
                # se o valor buscado for maior que o valor do nó atual,
                # continua a busca na subárvore direita
                no_atual = no_atual.direita

        # se não encontrou o nó, retorna None
        return None

    def fator(self, valor):
        # buscar um no pelo valor, se exitir, verificar o fator de balanceamento
        # usado na função de balancar
        no = self.buscar(valor)
        if no is None:
            return None
        return self.fator(no)

    def remove(self, value):
        perc, ant = self._get_perc(self.raiz, value)
        if perc:
            # 1 - saber se o No é uma folha
            if perc.is_leaf():
                if ant.value > perc.value:
                    ant.left = None
                else:
                    ant.right = None
                return True
            sucessor = self._get_sucessor(perc)
            ant_sucessor = self._get_perc(perc, sucessor.value)[1]
            
            perc.value = sucessor.value
            if ant_sucessor.value>sucessor.value:
                ant_sucessor.left = sucessor.right
                sucessor.right = None
            else:
                ant_sucessor.right = sucessor.left
                sucessor.left = None
            return True
            

    def rotacao(self, atual):
        
        # 1 - pega o nó
        # 2 - verifica o fator de balanceamento (Pega o fator da esquerda e o da direita e subtrai e verifica)
        # 3 rotaciona para esqueda ou direita, antes de rotacionar verificar se é rotação simples ou duplas
        fator = self.fator(atual)
        if fator == 2:
            if self.altura(atual.esquerda.esquerda) >= self.altura(atual.esquerda.direita):
                atual = self.rotacao_direita(atual)
            else:
                atual = self.rotacao_esquerda_direita(atual)
        elif fator == -2:
            if self.altura(atual.direita.direita) >= self.altura(atual.direita.esquerda):
                    atual = self.rotacao_esquerda(atual)
            else:
                atual = self.rotacao_direita_esquerda(atual)
            return atual

    def rotacao_direita(self, atual):
        novo_pai = atual.esquerda
        atual.esquerda = novo_pai.direita
        if atual.esquerda:
            atual.esquerda.pai = atual
        novo_pai.direita = atual
        novo_pai.pai = atual.pai
        atual.pai = novo_pai
        # Atualiza o fator de balanceamento
        atual.fator_bal = self.altura(atual.direita) - self.altura(atual.esquerda)
        novo_pai.fator_bal = self.altura(novo_pai.direita) - self.altura(novo_pai.esquerda)
        if novo_pai.pai:
            novo_pai.pai.fator_bal = self.altura(novo_pai.pai.direita) - self.altura(novo_pai.pai.esquerda)
        return novo_pai

    def rotacionar_esquerda(self, atual):
        # Salva a subárvore direita do nó atual
        nova_raiz = atual.direita
        # Define a nova subárvore direita do nó atual como a antiga subárvore esquerda da nova raiz
        atual.direita = nova_raiz.esquerda
        if atual.direita:
            atual.direita.pai = atual
        # Define a nova subárvore esquerda da nova raiz como o nó atual
        nova_raiz.esquerda = atual
        nova_raiz.pai = atual.pai
        atual.pai = nova_raiz
        # Atualiza o fator de balanceamento
        atual.fator_bal = self.altura(atual.direita) - self.altura(atual.esquerda)
        nova_raiz.fator_bal = self.altura(nova_raiz.direita) - self.altura(nova_raiz.esquerda)
        if nova_raiz.pai:
            nova_raiz.pai.fator_bal = self.altura(nova_raiz.pai.direita) - self.altura(nova_raiz.pai.esquerda)
        return nova_raiz

   
    ##Conversões

    ## Lista para Arvore

    #Criei um vetor iteravel([]) da lista do projeto, mesma ideia do metodo print no projeto da lista
    def lista_to_arvore(self,lista):
       
        
        arvore.lista_to_arvore(lista)
        #Percorrendo o iteravel criado e adicionando
        for i in va1.lista.create_iterable():
            self.add(i)
       
        
        # 2 - Fazer um for nela e chama a função add
        #for valor in lista:
        #    self.add(valor)

    def arvore_to_lista(self, type):
        

        #lista = va1.DoubledList()
        #lista = arvore.arvore_to_lista()
        # 1 - Vai receber um type, pre|in|pos/
        
        # 2 - Vai retornar a lista dupla, criado na 1v com a lista de acordo com o type.
      
        # 3 - Tentar usar algo parecido com pre_ordem| pos_ordem| in_ordem
        
      
        pass


# 50,60,72,65,30,25
#lista = va1.DoubledList()
arvore = Tree()
arvore.add(50)
arvore.add(30)
arvore.add(25)
arvore.add(69)
arvore.add(60)
arvore.add(75)


#lista.add(1)
#lista.add(33)

print('PRE----')
arvore.pre_ordem()
print('IN----')
arvore.in_ordem()
print('POS----')
arvore.pos_ordem()

no = arvore.get(60)
print(arvore.remove(25))
#print(arvore.remove(69))
print(arvore.remove(30))
print(arvore.remove(50))
print(arvore.remove(60))
print('=-=-=-=-')
print(arvore.in_ordem())

arvore2 = Tree()
arvore2.lista_to_arvore()
print('PREOrdem---')
arvore2.pre_ordem()

