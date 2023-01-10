r = []

def print_odd_desc(*a):
    
    

    for n1 in a:
        if n1%2==0:
            pass
        else:
            #print(n1)
            r.append(n1)
            
    r.sort()
    r.reverse()
    print(r)
#

print_odd_desc(11,22,33,44,55)