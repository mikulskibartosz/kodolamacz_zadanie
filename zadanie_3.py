from read_file import read_file


def licz_produkty_w_sklepach(sprzedaz):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> sprzedaz = [('sklep_1', '3'), ('sklep_1', ''), ('sklep_2', '5'), ('', '100')]
    >>> oczekiwany_wynik = [('sklep_2', 5), ('sklep_1', 4)]

    >>> wynik = licz_produkty_w_sklepach(sprzedaz)
    >>> assert wynik == oczekiwany_wynik, wynik
    """
    sprzedane_produkty = {}

    for sklep, liczba_produktow in sprzedaz:
        if not sklep:  # pusta nazwa sklepu
            continue
        liczba_produktow = int(liczba_produktow) if liczba_produktow else 1
        # drugim parametrem metody get jest wartość domyślna zwracana gdy klucz nie istnieje w słowniku
        policzona_sprzedaz = sprzedane_produkty.get(sklep, 0)
        sprzedane_produkty[sklep] = policzona_sprzedaz + liczba_produktow

    lista_sklepow = sprzedane_produkty.items()  # items zwraca listę krotek: (klucz, wartość)
    return sorted(lista_sklepow, key=lambda x: x[1], reverse=True)  # key wskazuje po której wartości sortować listę, x[1] zwraca drugi element krotki (liczbę sprzedanych produktów)


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    sprzedaz = zip(zawartosc_pliku.shop_id, zawartosc_pliku.pieces_sold)

    print(licz_produkty_w_sklepach(sprzedaz))
