# AEDV
#listadouble


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
       

    def __str__(self):
        return str(self.value)


class DoubledList:

    def __init__(self, max_length=None, force_type=None):
        self.__begin = None
        self.__end = None
        self.__length = 0
        self.max_length = max_length
        self.force_type = force_type
        self.teste = 'teste'
      
    def validate(self, value=None, index=None):
        if self.max_length and self.__length >= self.max_length:
            raise Exception('O número máximo de elementos já foi atribuidos')
        if self.force_type and type(value) is not self.force_type:
            raise TypeError('O tipo não é válido')
        if index and index > self.__length - 1:
            raise IndexError('Index não existe na lista')

    

    def append(self, value):
        self.validate(value=value)
        no = Node(value)
        if self.__length == 0:         
          self.__begin = no
          self.__end = no
        else:
            self.__end.next = no
            no.previous = self.__end
            self.__end = self.__end.next
        self.__length += 1


    def insert(self, index, value):
        no = Node(value)
        if index >= self.__length:
            self.append(value)
        elif index == 0:
            no.next = self.__begin
            self.__begin.previous = no
            self.__begin = no
            self.__length += 1
        else:
            novo_perc = self.__get_perc(index)
            perc_previous = novo_perc.previous
            no.next = novo_perc
            no.previous = perc_previous
            novo_perc.previous = no
            perc_previous.next = no
            self.__length += 1


    def update_value(self, index, value):
        
        self.validate(index=index)
        perc = self.__get_perc(index)
        perc.value = value

    def get_index(self, index):
        if self.__begin== None:
            raise ValueError('Lista vazia')
        elif index > self.__length -1:
            raise ValueError('INDEX NÃO EXISTE')
        elif index ==0:
            return self.__begin.data
        elif index== self.__length -1:
            return self.__end.data
        a = self.__begin
        for i in range(index):
            a=a.next
        return a.data

        
    def clear(self):
        perc= self.__begin
        while perc:
            del_list=perc.next
            perc.later=perc.next= None
            perc.data=None
            perc=del_list
        self.__begin=self.__end=None
        print('Lista deletada')


    def remove(self, index):
        if index <= self.__length-1:
            if index == 0:
                self.__begin = self._begin.next
                self.__begin.previous = None
            elif index == self.__length-1:
                self.__end = self._end.previous
                self.__end.next = None
            else:
                perc = self.__get_perc(index)
                antecessor = perc.previous
                sucessor = perc.next
                print(perc)
                antecessor.next = sucessor
                sucessor.previus = antecessor
                perc.next = None
                perc.previous = None
       


    def append_extend(self, value):
        self.validate(value=value)
        n_node= DoubledList(value)
        n_node.next= None

        if self.__begin==None:
            n_node.previous=None
            self.__begin=n_node
            return
        l_node= self.__begin
        while l_node.next:
            l_node=l_node.next
        l_node.next=n_node
        n_node.previous=l_node
        return

        

    def extend(self, other_list):
        if not other_list:
            return
        for value in other_list:
            self.append_extend(value)

    def __get_perc(self, index: object) -> object:
        self.validate(index=index)
        point_index = self.__length - 1
        if index == 0:
            return self.__begin
        elif index == point_index:
            return self.__end
        else:
            point = 0
            next = True
            if index < (self.__length / 2):
                perc = self.__begin
                point = index
            else:
                perc = self.__end
                point = point_index - index
                next = False

            for i in range(point):
                if next:
                    perc = perc.next
                else:
                    perc = perc.previous

            return perc
    

    def get_item(self, index):
        perc = self.__get_perc(index)
        return perc.value


    def get_length(self) -> int:
         return self.__length

    def __print(self, reverse=False):
        if self.__begin is None:
            return '[]'
        value = ''
        perc = self.__begin if not reverse else self.__end
        apont = 'next' if not reverse else 'previous'
        while getattr(perc, apont):
            value += f'{perc.value}, '
            perc = getattr(perc, apont)
        else:
            value += f'{perc.value}'
        return f'[{value}]'

    def __str__(self):
        if self.__begin is None:
            return '[]'
        value = ''
        perc = self.__begin
        while perc.next:
            value += f'{perc.value}, '
            perc = perc.next
        else:
            value += f'{perc.value}'
        return f'[{value}]'
      
    def __str__(self):
        return self.__print()
      
    def print_reverse(self):
        return self.__print(True)

    def __len__(self):
         return self.get_length()

    def __getitem__(self, index):
        return self.get_item(index)

    def __setitem__(self, key, value):
        self.update_value(key, value)



lista = DoubledList()
lista.append(50)
lista.append(60)
lista.append(70)
lista.append(30)
lista.insert(0, 3)
lista.insert(20, 10)
lista.insert(2, 25)
lista.insert(1, 4)
print(lista[-1])
list1 = [1, 2, 3]
list1.reverse()
print(list1)
lista.update_value(4, 100)
print(lista)
print(lista.print_reverse())
lista.extend([6])
print(lista)
#lista.remove(25)
lista.remove(3) #informar dentro dos "()" o INDEX, (INDEX), posição dentro da lista q vc quer remover
print(lista)
lista.clear()
