import time

def fast_exponentiation(y):
    x=time.time()
    z=pow(y,16741517871409143969046143790568590742046827347168578727343902113955048060929,66222722236519953653620750244932514345027291799515061275764866828038389148929)
    return (time.time()-x," sec taken", z)
print("fast exponentiation of big numbers using pow function", fast_exponentiation(2**127))

def slow_exponentiation(y):
    x=time.time()
    z=(y**167415)%66222
    return (time.time()-x," sec taken ", z)

print("Usual slower exponentiation of relatively smaller numbers using pow function", slow_exponentiation(2**127))