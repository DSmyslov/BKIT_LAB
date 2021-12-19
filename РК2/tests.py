from main import *
import unittest


class RKTest(unittest.TestCase):

    def setUp(self) -> None:
        # Производители
        self.manufacturers = [
            Manufacturer(1, 'Производитель деталей и запчастей для роботов'),
            Manufacturer(2, 'Детали студентам на ИнжГрафе'),
            Manufacturer(3, 'Современный производитель надежных деталей'),

            Manufacturer(11, 'Производитель (другой) деталей и запчастей для роботов'),
            Manufacturer(22, 'Детали (другие) студентам на ИнжГрафе'),
            Manufacturer(33, 'Современный производитель (другой) надежных деталей'),
        ]

        # Детали
        self.details = [
            Detail(1, 'Механическая рука', 24999, 1),
            Detail(2, 'Фланец', 1000, 2),
            Detail(3, 'Вал', 2500, 2),
            Detail(4, 'Гайка', 100, 3),
            Detail(5, 'Коленчатый вал', 5000, 3)
        ]

        # Производители и их детали
        self.manufacturer_detail = [
            Detail_Manufacturer(1, 1),
            Detail_Manufacturer(2, 2),
            Detail_Manufacturer(2, 3),
            Detail_Manufacturer(3, 4),
            Detail_Manufacturer(3, 5),

            Detail_Manufacturer(11, 1),
            Detail_Manufacturer(22, 2),
            Detail_Manufacturer(22, 3),
            Detail_Manufacturer(33, 4),
            Detail_Manufacturer(33, 5),
        ]

        self.one_to_many = bound_otm(self.manufacturers, self.details)
        self.many_to_many = bound_mtm(self.manufacturers, self.details, self.manufacturer_detail)

    def test_taskA1(self):
        result = taskA1(self.one_to_many)
        needed_res = [('Фланец', 1000, 'Детали студентам на ИнжГрафе'),
                      ('Вал', 2500, 'Детали студентам на ИнжГрафе'),
                      ('Механическая рука', 24999, 'Производитель деталей и запчастей для роботов'),
                      ('Гайка', 100, 'Современный производитель надежных деталей'),
                      ('Коленчатый вал', 5000, 'Современный производитель надежных деталей')]
        self.assertEqual(result, needed_res)

    def test_taskA2(self):
        result = taskA2(self.manufacturers, self.one_to_many)
        needed_res = [('Производитель деталей и запчастей для роботов', 24999),
                      ('Современный производитель надежных деталей', 5100),
                      ('Детали студентам на ИнжГрафе', 3500)]
        self.assertEqual(result, needed_res)

    def test_taskA3(self):
        result = taskA3(self.manufacturers, self.many_to_many)
        needed_res = {'Производитель деталей и запчастей для роботов': ['Механическая рука'],
                      'Современный производитель надежных деталей': ['Гайка', 'Коленчатый вал'],
                      'Производитель (другой) деталей и запчастей для роботов': ['Механическая рука'],
                      'Современный производитель (другой) надежных деталей': ['Гайка', 'Коленчатый вал']}
        self.assertEqual(result, needed_res)


if __name__ == '__main__':
    unittest.main()
