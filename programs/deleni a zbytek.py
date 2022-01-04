def deleni(a,b):
  p=0
  while a>=b:
    a=a-b
    p=p+1
  return p,a

print(deleni(4,2))