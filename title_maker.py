def make_title(title, symbol = '=', padding = 2, line_after = False):
    lines = []
    space_padding = []

    for letter in title:
        lines.append(str(symbol))

    for i in range(int(padding) * 2):
        lines.append(str(symbol))

    for i in range(int(padding)):
        space_padding.append(' ')
    
    lines = ''.join(lines)
    space_padding = ''.join(space_padding)

    print(lines)
    print(space_padding + title + space_padding)
    print(lines)
    if line_after == True:
        print()