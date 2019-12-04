import unittest
from hot_dog_stand import calculate_day_total, calculate_total_profit, add_sale, calculate_total_profit


class TestingValues(unittest.TestCase):
    ########## Testing Input Variables #############
    numb_of_hotdogs = int(5)  # number of hot dogs sold in a transaction
    price = 5.00           # price of each hot dog sold in transaction

    ### Test 1 ###
    def test_numb_of_hotdogs_is_an_integer(self):
        # Verify number of hotdogs is an integer
        self.assertIsInstance(self.numb_of_hotdogs, int)

    ### Test 2 ###
    def test_numb_of_hotdogs_is_positive(self):
        # Verify number of hotdogs is positive
        self.assertTrue(self.numb_of_hotdogs > 0)

    ### Test 3 ###
    def test_price_is_a_number(self):
        # Verify price is a number
        self.assertIsInstance(self.price, float)

    ### Test 4 ###
    def test_price_is_positive(self):
        # Verify price is positive
        self.assertTrue(self.price > 0)

    ### Test 5 ###
    def test_price_is_two_decimal_places(self):
        self.assertEqual(self.price, round(self.price,2))

    ### Test 6 ###
    def test_total_of_transaction(self):
        self.assertEqual(311.32, calculate_total_profit())


if __name__ == '__main__':
    unittest.main(verbosity=2)
