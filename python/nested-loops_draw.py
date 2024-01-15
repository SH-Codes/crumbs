def draw():
    numbers = [5, 2, 5, 2, 2]
    x_count = ''

    for x_count in numbers:
        output = ''
        for count in range(x_count):
            output += 'X'
        print(output)
draw()
