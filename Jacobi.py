from prettytable import PrettyTable

def IterasiJacobi3(A11, A12, A13, B1, A21, A22, A23, B2, A31, A32, A33, B3):
    tabel_jacobi = PrettyTable()
    tabel_jacobi.field_names = ["Iterasi", "X1", "X2", "X3", "Galat X1", "Galat X2", "Galat X3"]
    tabel_jacobi.add_row([0, 1, 1, 1, 0, 0, 0])
    X1old = 1
    X2old = 1
    X3old = 1
    #X1errold = 1
    #X2errold = 1
    #X3errold = 1
    m = 1

    print(":::Menggunakan Lelaran Jacobi:::")
    #print(f' Iterasi ke-{0} : [{X1old}, {X2old}, {X3old}]')
    while True:
        X1new = (B1 - (A12*X2old) - (A13*X3old))/A11
        X2new = (B2 - (A21*X1old) - (A23*X3old))/A22
        X3new = (B3 - (A31*X1old) - (A32*X2old))/A33

        X1errnew = (X1new - X1old)/X1new * 100
        X2errnew = (X2new - X2old)/X2new * 100
        X3errnew = (X3new - X3old)/X3new * 100

        X1old = X1new
        X2old = X2new
        X3old = X3new

        X1errold = X1errnew
        X2errold = X2errnew
        X3errold = X3errnew

        #print(f' Iterasi ke-{m} : [{X1new}, {X2new}, {X3new}] | Galat : [{X1errnew}, {X2errnew}, {X3errnew}]')
        tabel_jacobi.add_row([m, X1new, X2new, X3new, X1errnew, X2errnew, X3errnew])
        if (abs(X1errold) == 0 and abs(X2errold) == 0 and abs(X3errold) == 0) or (m == 200):
            print(tabel_jacobi)
            print(f'\n Hasil Iterasi Jacobi -->     X1 = {int(X1new)}, X2 = {int(X2new)}, X3 = {int(X3new)}')
            print(f' Didapatkan setelah {m}x iterasi')
            if m == 200:
                print(" (MAKSIMAL)")
            break
        m += 1

def IterasiJacobi4(A11, A12, A13, A14, B1, A21, A22, A23, A24, B2, A31, A32, A33, A34, B3, A41, A42, A43, A44, B4):
    tabel_jacobi = PrettyTable()
    tabel_jacobi.field_names = ["Iterasi", "X1", "X2", "X3", "X4", "Galat X1", "Galat X2", "Galat X3", "Galat X4"]
    tabel_jacobi.add_row([0, 1, 1, 1, 1, 0, 0, 0, 0])
    X1old = 1
    X2old = 1
    X3old = 1
    X4old = 1
    #X1errold = 1
    #X2errold = 1
    #X3errold = 1
    #X4errold = 1
    m = 1

    print(":::Menggunakan Lelaran Jacobi:::")
    #print(f' Iterasi ke-{0} : [{X1old}, {X2old}, {X3old}]')
    while True:
        X1new = (B1 - (A12*X2old) - (A13*X3old) - (A14*X4old))/A11
        X2new = (B2 - (A21*X1old) - (A23*X3old) - (A24*X4old))/A22
        X3new = (B3 - (A31*X1old) - (A32*X2old) - (A34*X4old))/A33
        X4new = (B4 - (A41*X1old) - (A42*X2old) - (A43*X3old))/A44

        X1errnew = (X1new - X1old)/X1new * 100
        X2errnew = (X2new - X2old)/X2new * 100
        X3errnew = (X3new - X3old)/X3new * 100
        X4errnew = (X4new - X4old)/X4new * 100

        X1old = X1new
        X2old = X2new
        X3old = X3new
        X4old = X4new

        X1errold = X1errnew
        X2errold = X2errnew
        X3errold = X3errnew
        X4errold = X4errnew

        #print(f' Iterasi ke-{m} : [{X1new}, {X2new}, {X3new}] | Galat : [{X1errnew}, {X2errnew}, {X3errnew}]')
        tabel_jacobi.add_row([m, X1new, X2new, X3new, X4new, X1errnew, X2errnew, X3errnew, X4errnew])
        if (abs(X1errold) == 0 and abs(X2errold) == 0 and abs(X3errold) == 0 and abs(X4errold) == 0) or (m == 200):
            print(tabel_jacobi)
            print(f'\n Hasil Iterasi Jacobi -->     X1 = {int(X1new)}, X2 = {int(X2new)}, X3 = {int(X3new)}, X4 = {int(X4new)}')
            print(f' Didapatkan setelah {m}x iterasi')
            if m == 200:
                print(" (MAKSIMAL)")
            break
        m += 1