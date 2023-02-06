import unittest

from onlinesimru import Driver


class TestSum(unittest.TestCase):
    def test_free(self):
        driver = Driver("90b7beba2e36054e19ec87ec1855ca46")
        data = driver.free().get_countries()
        self.assertIsNotNone(data)

    def test_numbers(self):
        driver = Driver("90b7beba2e36054e19ec87ec1855ca46")
        data = driver.numbers().tariffs()
        self.assertIsNotNone(data)
        self.assertTrue('7' in data)

        data = driver.numbers().tariffsOne(7)
        self.assertIsNotNone(data)
        self.assertEqual(data['code'], 7)

    def test_proxy(self):
        driver = Driver("90b7beba2e36054e19ec87ec1855ca46")
        data = driver.proxy().tariffs()
        self.assertIsNotNone(data)
        self.assertEqual(data['response'], '1')

    def test_rent(self):
        driver = Driver("90b7beba2e36054e19ec87ec1855ca46")
        data = driver.rent().get_tariff()
        self.assertIsNotNone(data)
        self.assertTrue(data.code == 7)

    def test_user(self):
        driver = Driver("90b7beba2e36054e19ec87ec1855ca46")
        data = driver.user().balance()
        self.assertIsNotNone(data)
        self.assertEqual(data['response'], '1')
        self.assertTrue('response' in data)
        self.assertTrue('balance' in data)
        self.assertTrue('income' in data)


if __name__ == '__main__':
    unittest.main()