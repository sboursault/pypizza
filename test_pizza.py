import unittest

from pizza import Pizza


# quatro_fromagi = Pizza("Quattro formaggi", ["Mozzarella", "Gorgonzola", "Fontina", "Parmigiano-Reggiano"])

class TestSum(unittest.TestCase):

    def test_equals(self):
        p1 = Pizza("Regina", ["Ham", "Mushrooms", "Mozzarella", "Tomato purée"])
        p2 = Pizza("Regina", ["Ham", "Mushrooms", "Mozzarella", "Tomato purée"])
        self.assertEqual(p1, p2)

    def test_missing_ingredient(self):
        p1 = Pizza("Regina", ["Ham", "Mushrooms", "Mozzarella", "Tomato purée"])
        p2 = Pizza("Regina", ["Ham", "Mozzarella", "Tomato purée"])
        self.assertNotEqual(p1, p2)


if __name__ == '__main__':
    unittest.main()
