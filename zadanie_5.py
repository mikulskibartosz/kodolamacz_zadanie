from read_file import read_file
from datetime import datetime


def produkty_sprzedane_w_weekendy(dane):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> date = ['2021-10-24', '2021-10-23', '2021-10-22']
    >>> pieces_sold = ['20', '', '300']
    >>> dane = zip(date, pieces_sold)

    >>> assert produkty_sprzedane_w_weekendy(dane) == 21
    """
    suma = 0
    for data, liczba_produktow in dane:
        liczba_produktow = int(liczba_produktow) if liczba_produktow else 1
        data = datetime.fromisoformat(data)
        weekend = data.isoweekday() in [6, 7]
        if weekend:
            suma += liczba_produktow
    return suma


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    dane = zip(zawartosc_pliku.order_date, zawartosc_pliku.pieces_sold)
    print(produkty_sprzedane_w_weekendy(dane))
