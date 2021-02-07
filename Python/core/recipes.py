порвать внешний цикл
    for i in range(3):
        print('hi')
        for j in range(3):
            if i == 1:break
        else:
            continue
        break