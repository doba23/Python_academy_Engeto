colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black' , 'red', 'green']
color_counts = {}

while colors:
    color = colors.pop()
    if color not in color_counts:
        color_counts[color]=0
    color_counts[color] = color_counts[color] + 1

print (color_counts)