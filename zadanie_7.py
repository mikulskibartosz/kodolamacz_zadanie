from read_file import read_file


def kategoria_i_nazwa(nazwa):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> assert kategoria_i_nazwa('Nazwa Bez Kategorii') == (None, 'Nazwa Bez Kategorii')
    >>> assert kategoria_i_nazwa('Kategoria - Nazwa') == ('Kategoria', 'Nazwa')
    >>> assert kategoria_i_nazwa('Kategoria - Nazwa Z Dodatkowym - Myślnikiem') == ('Kategoria', 'Nazwa Z Dodatkowym - Myślnikiem')
    """
    if '-' in nazwa:
        kategoria, nazwa_produktu = nazwa.split('-', maxsplit=1)  # maxsplit ogranicza liczbę wyszukiwanych myślników
        return (kategoria.strip(), nazwa_produktu.strip())
    else:
        return (None, nazwa)


def unikalne_produkty_w_kategoriach(produkty):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> produkty = ['Kategoria 1 - Nazwa 1', 'Kategoria 1 - Nazwa 2 - Z Myślnikiem', 'Kategoria 2 - Nazwa 1', 'Kategoria 2 - Nazwa 1', 'Nazwa bez kategorii']
    >>> oczekiwany_wynik = [('Kategoria 1', 2), ('Kategoria 2', 1)]

    >>> wynik = unikalne_produkty_w_kategoriach(produkty)
    >>> assert wynik == oczekiwany_wynik, wynik
    """
    produkty_w_kategoriach = {}

    for produkt in produkty:
        kategoria, nazwa = kategoria_i_nazwa(produkt)
        if not kategoria:  # brak kategorii
            continue

        lista_produktow = produkty_w_kategoriach.get(kategoria, [])
        lista_produktow.append(nazwa)
        produkty_w_kategoriach[kategoria] = lista_produktow

    liczba_produktow = [
        (kategoria, len(set(produkty_w_kategorii)))
            for kategoria, produkty_w_kategorii in produkty_w_kategoriach.items()
    ]

    return sorted(liczba_produktow, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    for policzone_produkty in unikalne_produkty_w_kategoriach(zawartosc_pliku.product_name):
        print(policzone_produkty)
