myNumberAr = set({'0'+str(x) for x in range(100)}).union(set({x for x in range(100) if x > 10}))
numRand = int(tuple(myNumberAr)[0].replace('0',''))
print("Number: "+str(numRand)+" type: "+str(type(numRand)))
