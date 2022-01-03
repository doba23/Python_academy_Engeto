def nejdelsi_slovo (a):
    max = 'j'
    for i in a.split():
        if len(a) > max:
            max = i
    return max

a = str('se dodo, dodose')
nejdelsi_slovo(a.split(' '))

