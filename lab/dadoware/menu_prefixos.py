for a in (str(n) for n in range(1, 7)):
    print('|:---:' * 6)
    for b in (str(n) for n in range(1, 7)):
        prefixo = f'{a}{b}'
        link = f'**[{prefixo}](#prefixo-{prefixo})**'
        print(f'| {link}', end=' ')
    print()