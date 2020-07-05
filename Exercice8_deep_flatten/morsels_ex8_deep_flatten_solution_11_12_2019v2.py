from pprint import pprint

def parse_ranges(tekst):

    rangess = tekst.split(",")
    for r in rangess:
        if "->" in r:
            (out, seper,prawa) = r.partition("->")    
            yield int(out)
        elif "-" in r:
            tablica = r.split("-")
            rang = range(int(tablica[0]),int(tablica[1])+1)
            for i in rang:
                yield i
        else:
            yield int(r)
            
        


if __name__ == "__main__":
    
    pprint(list(parse_ranges('1-2,4-4,8-10')))
    pprint(list(parse_ranges('0-0, 4-8, 20-20, 43-45')))
    pprint(list(parse_ranges('0,4-8,20,43-45')))
    pprint(list(parse_ranges('0, 4-8, 20->exit, 43-45')))