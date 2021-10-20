# P1


def read_list():
    lista = []
    n = int(input("Numar de elemente"))
    for i in range(n):
        lista.append(int(input("lista[" + str(i) + "]=")))
    return lista


# P2


def number_in_list(lst: list[int], numar: int, pozitie: int):
    """
    Verifica daca un numar citit de la tastatura se regaseste in lista incepand de la o anumita pozitie
    :param lst: lista de numere intregi
    :param numar: numar intreg
    :param pozitie: numar intreg
    :return: 'DA' daca numarul se gaseste in lista de la o anumita pozitie
    """
    for i in range(pozitie, len(lst)):
        if lst[i] == numar:
            return 'DA'
    return 'NU'


def test_number_in_list():
    assert number_in_list([2, 32, 122, 12, 1456], 12, 3) == 'DA'
    assert number_in_list([2, 32, 122, 1456, 12], 12, 3) == 'DA'
    assert number_in_list([2, 32, 122, 12, 1456], 12, 4) == 'NU'


# P3


def sum_of_even_int(lst: list[int]) -> int:
    """
    Afiseaza suma tuturor numerelor intregi pare din lista
    :param lst: lista de numere intregi
    :return: suma tuturor numerelor intregi pare
    """
    sumapare = 0
    for x in lst:
        if x % 2 == 0:
            sumapare += x
    return sumapare


def test_sum_of_even_int():
    assert sum_of_even_int([2, 3, 12, 5, 9]) == 14
    assert sum_of_even_int([1, 15, 5, 9]) == 0

def test_all():
    test_number_in_list()
    test_sum_of_even_int()

def main():
    test_all()
    lst = []
    while True:
        print("1. Citire lista de numere intregi")
        print("2. Verificati daca un numar se regaseste in lista incepand de la o anumita pozitie")
        print("3. Calculeaza suma tuturor numerelor intregi pare din lista")
        print("x. Iesire")
        optiune = input(" Alegeti optiunea din meniu: ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            numar = int(input("Dati un numar"))
            pozitie = int(input("Dati o pozitie"))
            print(number_in_list(lst, numar, pozitie))
        elif optiune == '3':
            print(sum_of_even_int(lst))
        elif optiune == '4':
            pass
        elif optiune == 'x':
            break
        else:
            print(" Optiune gresita!!")


if __name__ == '__main__':
    main()
