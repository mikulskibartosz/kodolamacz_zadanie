from read_file import read_file
from datetime import datetime


def rok_i_kwartal(data: datetime):
    """
    >>> assert rok_i_kwartal(datetime(2021, 1, 4)) == (2021, 1)
    >>> assert rok_i_kwartal(datetime(2021, 4, 15)) == (2021, 2)
    >>> assert rok_i_kwartal(datetime(2021, 6, 30)) == (2021, 2)
    >>> assert rok_i_kwartal(datetime(2020, 7, 9)) == (2020, 3)
    >>> assert rok_i_kwartal(datetime(2020, 11, 1)) == (2020, 4)
    """
    q = (data.month-1) // 3 + 1
    return (data.year, q)


def licz_ceny_w_kwartalach(dane):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> date = ['2020-01-05', '2020-03-14', '2020-07-08', '2020-09-30', '2021-01-02']
    >>> pieces_sold = ['6', '4', '2', '', '5']
    >>> price_per_item = ['10.0', '10.0', '10.0', '10.0', '5.0']

    >>> oczekiwany_wynik = [(2020, 1, 100.0), (2020, 3, 30.0), (2021, 1, 25.0)]
    >>> dane = zip(date, pieces_sold, price_per_item)

    >>> wynik = licz_ceny_w_kwartalach(dane)
    >>> assert wynik == oczekiwany_wynik, wynik
    """
    sumy = {}
    for data, liczba_produktow, cena_za_produkt in dane:
        liczba_produktow = int(liczba_produktow) if liczba_produktow else 1
        cena = liczba_produktow * float(cena_za_produkt)

        data = datetime.fromisoformat(data)
        rok_i_kw = rok_i_kwartal(data)

        policzona_sprzedaz = sumy.get(rok_i_kw, 0)
        sumy[rok_i_kw] = policzona_sprzedaz + cena

    # sumy.items() zwraca krotki zagnieżdżone: ((rok, kwartał), sprzedaż), więc przepakowujemy wartości
    # dla czytelności możemy też zaokrąglić wynik
    wynik = [(rok, kwartal, round(sprzedaz, 2)) for ((rok, kwartal), sprzedaz) in sumy.items()]
    return sorted(wynik)  # sorted w przypadku listy krotek najpierw porównuje pierwszy element, jeśli są identyczne to drugi element, itd.


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    dane = zip(zawartosc_pliku.order_date, zawartosc_pliku.pieces_sold, zawartosc_pliku.price_per_item)
    print(licz_ceny_w_kwartalach(dane))
