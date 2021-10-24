from read_file import read_file  # funkcja wczytująca plik jest w module (pliku) read_file


def sortuj_nazwy_zwroc_dziesiec(nazwy):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> oczekiwany_wynik = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    >>> dane_testowe = ['A', 'Z', 'B', 'X', 'C', 'P', 'D', 'R', 'E', 'F', 'G', 'H', 'I', 'J']
    >>> wynik = sortuj_nazwy_zwroc_dziesiec(dane_testowe)

    >>> assert wynik == oczekiwany_wynik, f'Otrzymany wynik: {wynik}'
    """
    return sorted(nazwy)[0:10]


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    print(sortuj_nazwy_zwroc_dziesiec(zawartosc_pliku.product_name))
