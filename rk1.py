from operator import itemgetter


class Detail:
    """Деталь"""

    def __init__(self, id, name, price, manufacturer_id):
        self.id = id
        self.name = name
        self.price = price  # Стоимость детали
        self.manufacturer_id = manufacturer_id


class Manufacturer:
    """Производитель"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Detail_Manufacturer:
    """
    'Детали производителя' для реализации
    связи многие-ко-многим
    """

    def __init__(self, manufacturer_id, detail_id):
        self.manufacturer_id = manufacturer_id
        self.detail_id = detail_id


# Производители
manufacturers = [
    Manufacturer(1, 'Надёжный производитель'),
    Manufacturer(2, 'Производитель деталей машин'),
    Manufacturer(3, 'Детали будущего для конструкторов и инженеров настоящего'),

    Manufacturer(11, 'Надёжный (другой) производитель'),
    Manufacturer(22, 'Производитель (другой) деталей машин'),
    Manufacturer(33, '(другие) детали будущего для конструкторов и инженеров настоящего'),
]

# Детали
details = [
    Detail(1, 'Штуцер', 1000, 1),
    Detail(2, 'Маховик', 5500, 2),
    Detail(3, 'Вал', 15750, 2),
    Detail(4, 'Поршень', 12250, 3),
    Detail(5, 'Фланец', 2000, 3),
    Detail(6, 'Демпфер', 8999, 3),
]

manufacturer_detail = [
    Detail_Manufacturer(1, 1),
    Detail_Manufacturer(2, 2),
    Detail_Manufacturer(2, 3),
    Detail_Manufacturer(3, 4),
    Detail_Manufacturer(3, 5),
    Detail_Manufacturer(3, 6),

    Detail_Manufacturer(11, 1),
    Detail_Manufacturer(22, 2),
    Detail_Manufacturer(22, 3),
    Detail_Manufacturer(33, 4),
    Detail_Manufacturer(33, 5),
    Detail_Manufacturer(33, 6),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(d.name, d.price, m.name)
                   for m in manufacturers
                   for d in details
                   if d.manufacturer_id == m.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(m.name, md.manufacturer_id, md.detail_id)
                         for m in manufacturers
                         for md in manufacturer_detail
                         if m.id == md.manufacturer_id]

    many_to_many = [(d.name, d.price, m_name)
                    for m_name, m_id, d_id in many_to_many_temp
                    for d in details if d.id == d_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for m in manufacturers:
        m_details = list(filter(lambda i: i[2] == m.name, one_to_many))
        if len(m_details) > 0:
            m_price = [price for _, price, _ in m_details]
            m_price_sum = sum(m_price)
            res_12_unsorted.append((m.name, m_price_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    for m in manufacturers:
        if 'производитель' in m.name.lower():
            m_details = list(filter(lambda i: i[2] == m.name, many_to_many))
            m_details_names = [x for x, _, _ in m_details]
            res_13[m.name] = m_details_names

    print(res_13)


if __name__ == '__main__':
    main()
