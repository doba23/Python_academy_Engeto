 from requests import get, post, head
 import csv
# seznam = get ('http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/')
# print (seznam.text)
# ['lovely puppy', 'cute kitty', 'yumy food', 'sweet baby' ]
#
#
# machine_answer =
#
# get('http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/', answer+)


a = get ('http://api.github.com/search/repositories', params={'q':'requests+language:python'})
text_from_webvprint (a.text)
writer = csv.writer(csvfile, delimiter=' ', quotechar='”')
