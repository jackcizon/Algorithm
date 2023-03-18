def GaleShapley(men, women, pref):
    
    rank = {}
    #rank[0]: col of rank{}
    
    for w in women:
        rank[w] = {}
        i = 1
        # women: 1, 2, ...

        for m in pref[w]:
            rank[w][m] = i
            i += 1
            # men: 1: 1, 2, ...
            #      2: 1, 2, ...
            #        ....

        prefptr = {}
    
    for m in men:
        prefptr[m] = 0
        
    freemen = list(men)
    numpartners = len(men)
    S = {}
    
    
    while freemen:
        m = freemen.pop()
    
        if prefptr[m] > numpartners: 
            continue 
    
        w = pref[m][prefptr[m]]
        prefptr[m] += 1
    
        if w not in S:
            S[w] = m
    
        else:
            mprime = S[w]
    
            if rank[w][m]< rank[w][mprime]:
                S[w] = m
                freemen.append(mprime)
    
            else:
                freemen.append(m)
    
    return S



thewomen = ["Amy", "Lacy" , "Katie", "Bertha"]


themen = ["John", "Peter", "Tyrion", "Max"]


thepref = {"John": ["Amy", "Lacy", "Katie", "Bertha"],
           "Peter":["Lacy", "Amy", "Katie", "Bertha"],
           "Tyrion":["Lacy", "Katie", "Amy","Bertha"],
           "Max": ["Lacy", "Katie", "Amy","Bertha"],
           "Amy": ["John", "Tyrion", "Peter", "Max"],
           "Lacy": ["Peter", "John", "Tyrion", "Max"],
           "Katie": ["Tyrion", "John", "Peter", "Max"],
           "Bertha": ["Tyrion", "John", "Peter", "Max"]}

eng = GaleShapley(themen, thewomen, thepref)

from pprint import pprint as pp

pp(eng)