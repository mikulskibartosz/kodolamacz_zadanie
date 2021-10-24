from dataclasses import dataclass


FILE_NAME = 'MOCK_DATA.csv'


@dataclass
class ZawartoscPliku:
    order_id: list
    product_name: list
    pieces_sold: list
    price_per_item: list
    order_date: list
    shop_id: list


def read_file():
    order_id_list = []
    product_name_list = []
    pieces_sold_list = []
    price_per_item_list = []
    order_date_list = []
    shop_id_list = []

    with open(FILE_NAME) as file:
        file.readline() # ignorujemy nagłówek

        for line in file:
            if '"' not in line: # ignorujemy linie zawierające cudzysłów
                order_id, product_name, pieces_sold, price_per_item, order_date, shop_id = line.strip().split(',')
                order_id_list.append(order_id)
                product_name_list.append(product_name)
                pieces_sold_list.append(pieces_sold)
                price_per_item_list.append(price_per_item)
                order_date_list.append(order_date)
                shop_id_list.append(shop_id)

    return ZawartoscPliku(
        order_id=order_date_list,
        product_name=product_name_list,
        pieces_sold=pieces_sold_list,
        price_per_item=price_per_item_list,
        order_date=order_date_list,
        shop_id=shop_id_list
    )


# poniższy kod zostanie uruchomiony tylko jeśli uruchomimy ten plik python, a nie jeśli go zaimportujemy w innym pliku
if __name__ == '__main__':
    plik = read_file()
    print(len(plik.order_id))
    print(len(plik.product_name))
    print(len(plik.pieces_sold))
    print(len(plik.price_per_item))
    print(len(plik.order_date))
    print(len(plik.shop_id))

