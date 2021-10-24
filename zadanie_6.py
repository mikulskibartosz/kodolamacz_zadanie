from read_file import read_file
from datetime import datetime


def liczba_dni(dane):
    """
    >>> import sys; sys.tracebacklimit = 0

    >>> sklepy = ['sklep_1', 'sklep_2', 'sklep_1', '', 'sklep_2', '']
    >>> daty = ['2021-10-01', '2021-04-15', '2021-10-15', '2021-01-01', '2021-03-20', '2021-12-31']
    >>> dane = zip(sklepy, daty)

    >>> oczekiwany_wynik = [('sklep_1', 14), ('sklep_2', 26)]

    >>> wynik = liczba_dni(dane)
    >>> assert wynik == oczekiwany_wynik, wynik
    """
    pierwsza = {}
    ostatnia = {}

    for sklep, data in dane:
        if not sklep:
            continue
        data = datetime.fromisoformat(data)

        if sklep not in pierwsza:  # ten sklep jeszcze nie ma pierwszej daty zakupu, wstawiamy bieżącą wartość
            pierwsza[sklep] = data
        if sklep not in ostatnia:
            ostatnia[sklep] = data

        poprzednia_pierwsza = pierwsza[sklep]
        if poprzednia_pierwsza > data:  # aktualnie przetwarzana data jest wcześniejsza
            pierwsza[sklep] = data

        poprzednia_ostatnia = ostatnia[sklep]
        if poprzednia_ostatnia < data:  # aktualnie przetwarzana data jest późniejsza
            ostatnia[sklep] = data

    wynik = []
    sklepy = sorted(pierwsza.keys())
    for sklep in sklepy:
        pierwszy_zakup = pierwsza[sklep]
        ostatni_zakup = ostatnia[sklep]

        delta = ostatni_zakup - pierwszy_zakup
        wynik.append((sklep, delta.days))

    return wynik


if __name__ == '__main__':
    zawartosc_pliku = read_file()
    dane = zip(zawartosc_pliku.shop_id, zawartosc_pliku.order_date)
    print(liczba_dni(dane))
