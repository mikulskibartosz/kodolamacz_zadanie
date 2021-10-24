from read_file import read_file


def cena_zakupu(pieces_sold, price_per_item):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> wynik_z_pustym_pieces_sold = cena_zakupu("", "13")
    >>> assert wynik_z_pustym_pieces_sold == 13, wynik_z_pustym_pieces_sold

    >>> pieces_sold_1 = cena_zakupu("1", "4.2")
    >>> assert pieces_sold_1 == 4.2, pieces_sold_1

    >>> pieces_sold_5 = cena_zakupu("5", "5")
    >>> assert pieces_sold_5 == 25, pieces_sold_5
    """
    # gdy użyjemy pustego tekstu w warunku if, otrzymamy wartość false. Niepusty tekst = True
    # bool("") == False    bool("tekst") == True
    pieces_sold = int(pieces_sold) if pieces_sold else 1
    price_per_item = float(price_per_item)
    return pieces_sold * price_per_item


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    # uzywamy zip aby otrzymać krotkę z obiema wartościami z wiersza
    for pieces_sold, price_per_item in zip(zawartosc_pliku.pieces_sold, zawartosc_pliku.price_per_item):
        cena = cena_zakupu(pieces_sold, price_per_item)
        # nie było wymagane w zadaniu, ale możemy też zaokrąglić cenę do 2 miejsc po przecinku
        cena = round(cena, 2)
        print(f'Pieces sold: {pieces_sold} price: {price_per_item} = {cena}')
