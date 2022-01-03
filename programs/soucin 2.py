def soucin(a,b):
  v=0
  if a>0:
    while a>0:
      v=v+b
      a=a-1
  else:
    while a<0:
      v=v-b
      a=a+1
  return v

nasobitel=int(input('vloz prvni cislo',))
nasobitel2=int(input('vloz druhe cislo',))

print (soucin(nasobitel,nasobitel2))