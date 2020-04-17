film = { 'name':'Shawshank Redemption','rating':87,'year':1994,'director':'Frank Darabont'}

#update values in distionary
film['starring'] = ['Tim Robbins', 'Morgan Freeman']
film.update({'budget':200})

#remove key-value pair
film.pop('budget')

# print (film)

# create new dictionary
films = {}

#update values in distionary
films.update({'DRAMA': film})
print (films)

# -------------------------------------------
# user film program
#
# print ('We can currently offer:')
# # print distionary keys
# print(films.keys())
#
# # user chose genre, save the result
# user_input = input ('What genre are zou interested in?:')
# print (films.get(user_input))
# -------------------------------------------

# -------------------------------------------
# user film program v.2

print ('We can currently offer:')
# print distionary keys
print(films.keys())

# user chose genre, save the result
user_input = input ('What genre are zou interested in?:')
print (films.pop(user_input))
if not films:
    print ('DATABASE HAS BEEN ERASED:')
print (films)
# -------------------------------------------