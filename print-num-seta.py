num = int(input('Digite um número: '))
lista = []
for i in range(1):
    for x in range(1,num+1):
        lista.append(x)
        print('  ' * lista[-1], *lista,sep='   ')
        if lista[-1] == num:
            for y in range(num-1,0,-1):
                del lista[-1]
                print('  ' * lista[-1],*lista,sep='   ')
