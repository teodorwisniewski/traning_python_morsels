# from pprint import pprint
from timeit import default_timer


class OrderedSet:

    def __init__(self, iteratorek):
        self.tablica_uporzadkowana = []
        self.set_nieuporzadkowany = set()
        for i in iteratorek:
            if not i in self.set_nieuporzadkowany:
                self.set_nieuporzadkowany.add(i)
                self.tablica_uporzadkowana.append(i)
        
        self.wielkosc = len(self.set_nieuporzadkowany)

    def __iter__(self):
        out = tuple(self.tablica_uporzadkowana)
        for el in out:
            yield el

    def __len__(self):
        return self.wielkosc
    
    def __contains__(self, key):
        return key in self.tablica_uporzadkowana

    def add(self,new_el):
        if not new_el in self.tablica_uporzadkowana:
            self.tablica_uporzadkowana.append(new_el)
        self.set_nieuporzadkowany = set(self.tablica_uporzadkowana)
        self.wielkosc = len(self.set_nieuporzadkowany)
        return self.tablica_uporzadkowana

    def discard(self,el_to_delete):

        if el_to_delete in self.tablica_uporzadkowana:
            tab_kopia = list(self.tablica_uporzadkowana)
            self.tablica_uporzadkowana = [el for el in tab_kopia if el_to_delete !=el]
        self.set_nieuporzadkowany = set(self.tablica_uporzadkowana)
        self.wielkosc = len(self.set_nieuporzadkowany)
        return self.tablica_uporzadkowana

    def __eq__(self,other):
        if isinstance(other, set):
            return len(other) == len(self.tablica_uporzadkowana) and all(el in other for el in self.tablica_uporzadkowana)    
        if isinstance(other, OrderedSet):
            return other.tablica_uporzadkowana == self.tablica_uporzadkowana
        return False

    def __getitem__(self,indice):
        return self.tablica_uporzadkowana[indice]
        

    # def __repr__(self):
    #     return self.tablica_uporzadkowana

# if __name__=="__main__":
#     ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
#     print(*set(ordered_words))
#     print(*OrderedSet(ordered_words))
#     numbers = OrderedSet([1, 3, 2, 4, 2, 1, 4, 5])
#     print(sorted(numbers)== [1, 2, 3, 4, 5])
#     words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
#     print(len(words))
#     print("hello" in words)

#     print(words.add("ello"))
#     print(words.add("siemano"))
#     print(words.add("hello"))
#     print(words.discard("ello"))
#     print(words.discard("siemano"))
#     print(words.discard("hello"))
#     print(words.discard("hello"))
#     print(words.discard("hello"))
#     print(OrderedSet(['how', 'are', 'you']) == OrderedSet(['how', 'you', 'are']))
#     print(OrderedSet(['how', 'are', 'you']) == {'how', 'you', 'are'})
#     print(OrderedSet(['how', 'are', 'you']) == ['how', 'are', 'you'])
#     print(words.add("ello"))
#     print(words.add("siemano"))
#     print(words.add("hello"))

#     print(words[0])
#     print(words[-1])
#     print(words[2])