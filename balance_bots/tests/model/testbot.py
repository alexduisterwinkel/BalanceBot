import unittest
from balance_bots.src.model.bot import Bot


class TestBot(unittest.TestCase):
    def test_add_value(self):
        bot = Bot()
        bot.add_value(5)
        self.assertEqual(bot.values, [5])

        bot.add_value(3)
        self.assertEqual(bot.values, [3, 5])

    def test_max_2_values(self):
        bot = Bot()
        bot.add_value(12)
        bot.add_value(14)
        self.assertEqual(bot.values, [12, 14])

        bot.add_value(20)
        self.assertFalse(len(bot.values) > 2, "Bot has more than 2 values")

    def test_has_two_values(self):
        bot = Bot()
        self.assertFalse(bot.has_two_values())

        bot.add_value(5)
        self.assertFalse(bot.has_two_values())

        bot.add_value(3)
        self.assertTrue(bot.has_two_values())

        bot.add_value(8)
        self.assertTrue(bot.has_two_values())

    def test_give_values(self):
        bot = Bot()
        bot.add_value(5)
        bot.add_value(3)

        low, high = bot.give_values()
        self.assertEqual(low, 3)
        self.assertEqual(high, 5)
        self.assertEqual(bot.values, [])

    def test_give_values_empty_bot(self):
        bot = Bot()

        with self.assertRaises(ValueError):
            bot.give_values()


if __name__ == '__main__':
    unittest.main()
