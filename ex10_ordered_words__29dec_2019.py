


class OrderedSet:

    def __init__(self,iteratorek):


        self.orderde_pojemniszek = dict.fromkeys(iteratorek,None)
        
    def __iter__(self):
        return iter(self.orderde_pojemniszek)
    
    def __contains__(self, element):
        return element in self.orderde_pojemniszek
    
    def __len__(self):
        return len(self.orderde_pojemniszek.keys())



if __name__ == "__main__":

    ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
    print(*set(ordered_words))
    print(*OrderedSet(ordered_words))
    print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))

    words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    print(len(words))
    print('hello' in words)