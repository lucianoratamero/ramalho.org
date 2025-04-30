

with open('lista_de_palavras.txt') as fp:
    for lin in fp:
        if lin.startswith('===== Prefixo'):
            break
        print(lin.strip())
    for prefixo in (f'{a}{b}' for a in range(1, 7) for b in range(1, 7)):
        pre_atual = lin.split()[2]
        assert pre_atual == prefixo
        print(f'## Prefixo', prefixo)
        print()
        assert next(fp).strip() == ''
        for i in range(1, 7):
            print(f'| **{prefixo}{i}...** ', end=' ')
        print()
        for i in range(1, 7):
            print(f'|-----', end='')
        print()
        for lin in fp:
            if not lin.startswith(f'| **{prefixo}'):
                break
            print(lin.strip())
        assert lin.strip() == ''
        assert next(fp).startswith('[[#lista')
        print('\n<!--LINKTOPO-->\n')
        assert next(fp).strip() == ''
        try:
            lin = next(fp)
        except StopIteration:
            break
