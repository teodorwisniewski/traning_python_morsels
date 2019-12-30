from collections.abc import Set




class OrderedSet(Set):

    def __init__(self,iteratorek):


        self.orderde_pojemniszek = dict.fromkeys(iteratorek,None)
        
    def __iter__(self):
        return iter(self.orderde_pojemniszek)
    
    def __contains__(self, element):
        return element in self.orderde_pojemniszek
    
    def __len__(self):
        return len(self.orderde_pojemniszek.keys())


    def add(self,new_el):
        if not new_el in self.orderde_pojemniszek:
            self.orderde_pojemniszek[new_el] = None
        return self.orderde_pojemniszek

    def discard(self,el_to_delete):

        if el_to_delete in self.orderde_pojemniszek:
            tab_kopia = list(self.orderde_pojemniszek.keys())
            tablica_uporzadkowana = [el for el in tab_kopia if el_to_delete !=el]
            self.orderde_pojemniszek = dict.fromkeys(tablica_uporzadkowana,None)
        return self.orderde_pojemniszek

    def __eq__(self,other):
        if isinstance(other, set):
            return len(other) == len(self.orderde_pojemniszek) and all(el in other for el in self.orderde_pojemniszek)    
        if isinstance(other, OrderedSet):
            return list(other.orderde_pojemniszek.keys()) ==  list(self.orderde_pojemniszek.keys())
        return False

    def __getitem__(self,indice):
        tablica = list(self.orderde_pojemniszek.keys())
        return tablica[indice]


if __name__ == "__main__":

    ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
    print(*set(ordered_words))
    print(*OrderedSet(ordered_words))
    print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))

    words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    print(len(words))
    print('hello' in words)

    print(words.add("ello"))
    print(words.add("siemano"))
    print(words.add("hello"))
    print(words.discard("ello"))
    print(words.discard("siemano"))
    print(words.discard("hello"))
    print(words.discard("hello"))
    print(words.discard("hello"))
    print(OrderedSet(['how', 'are', 'you']) == OrderedSet(['how', 'you', 'are']))
    print(OrderedSet(['how', 'are', 'you']) == {'how', 'you', 'are'})
    print(OrderedSet(['how', 'are', 'you']) == ['how', 'are', 'you'])
    print(words.add("ello"))
    print(words.add("siemano"))
    print(words.add("hello"))

    print(words[0])
    print(words[-1])