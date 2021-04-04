from Jacobi import IterasiJacobi3
from Jacobi import IterasiJacobi4
from GaussSeidel import IterasiGaussSeidel3
from GaussSeidel import IterasiGaussSeidel4

demoArr3 = " [A11, A12, A13]  [B1]\n [A21, A22, A23]  [B2]\n [A31, A32, A33]  [B3]"
demoArr4 = " [A11, A12, A13, A14]  [B1]\n [A21, A22, A23, A24]  [B2]\n [A31, A32, A33, A34]  [B3]\n [A41, A42, A43, A44]  [B4]"

print("\n=== Program untuk menghitung Solusi SPL menggunakan Lelaran Jacobi dan Gauss-Seidel ===")
print("===                   By Xave Senduk https://github.com/xavesenduk                  ===")

matriks = ""
while matriks != "3" or matriks != "4":
    matriks = str(input("Pilih ordo matriks: \n3 = 3x3\n4 = 4x4\nOrdo = "))
    if matriks == "3" or matriks == "4":
        break
    else:
        print("Pilihan tidak valid!\n")

if matriks == "3":
    print(" Untuk Matriks 3x3\n" + demoArr3)

    print("\nMasukkan nilai A:")
    A11 = float(input("A11:  "))
    A12 = float(input("A12:  "))
    A13 = float(input("A13:  "))
    A21 = float(input("A21:  "))
    A22 = float(input("A22:  "))
    A23 = float(input("A23:  "))
    A31 = float(input("A31:  "))
    A32 = float(input("A32:  "))
    A33 = float(input("A33:  "))

    print("\nMasukkan nilai b:")
    B1 = float(input("B1:  "))
    B2 = float(input("B2:  "))
    B3 = float(input("B3:  "))

    print(f'\n Menghitung Solusi SPL:\n [{A11}, {A12}, {A13}]  [{B1}]\n [{A21}, {A22}, {A23}]  [{B2}]\n [{A31}, {A32}, {A33}]  [{B3}]\n')
    IterasiJacobi3(A11, A12, A13, B1, A21, A22, A23, B2, A31, A32, A33, B3)
    print("\n")
    IterasiGaussSeidel3(A11, A12, A13, B1, A21, A22, A23, B2, A31, A32, A33, B3)

elif matriks == "4":
    print(" Untuk Matriks 4x4\n" + demoArr4)

    print("\nMasukkan nilai A:")
    A11 = float(input("A11:  "))
    A12 = float(input("A12:  "))
    A13 = float(input("A13:  "))
    A14 = float(input("A14:  "))
    A21 = float(input("A21:  "))
    A22 = float(input("A22:  "))
    A23 = float(input("A23:  "))
    A24 = float(input("A24:  "))
    A31 = float(input("A31:  "))
    A32 = float(input("A32:  "))
    A33 = float(input("A33:  "))
    A34 = float(input("A34:  "))
    A41 = float(input("A41:  "))
    A42 = float(input("A42:  "))
    A43 = float(input("A43:  "))
    A44 = float(input("A44:  "))

    print("\nMasukkan nilai b:")
    B1 = float(input("B1:  "))
    B2 = float(input("B2:  "))
    B3 = float(input("B3:  "))
    B4 = float(input("B4:  "))

    print(f'\n Menghitung Solusi SPL:\n [{A11}, {A12}, {A13}, {A14}]  [{B1}]\n [{A21}, {A22}, {A23}, {A24}]  [{B2}]\n [{A31}, {A32}, {A33}, {A34}]  [{B3}]\n [{A41}, {A42}, {A43}, {A44}]  [{B4}]\n')
    IterasiJacobi4(A11, A12, A13, A14, B1, A21, A22, A23, A24, B2, A31, A32, A33, A34, B3, A41, A42, A43, A44, B4)
    print("\n")
    IterasiGaussSeidel4(A11, A12, A13, A14, B1, A21, A22, A23, A24, B2, A31, A32, A33, A34, B3, A41, A42, A43, A44, B4)

print("\n===                   By Xave Senduk https://github.com/xavesenduk                  ===")
print("=== Program untuk menghitung Solusi SPL menggunakan Lelaran Jacobi dan Gauss-Seidel ===")
