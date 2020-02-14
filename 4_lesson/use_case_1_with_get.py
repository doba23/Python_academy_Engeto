colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black' , 'red', 'green']
color_counts = {}

while colors:
    color = colors.pop()
    color_counts[color] = color_counts.get(color,0) + 1