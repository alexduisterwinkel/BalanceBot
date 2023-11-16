import unittest
from collections import defaultdict
from balance_bots.src.model.bot import Bot
from balance_bots.src.factory.instruction_processor import process_initial_state, process_instruction


class TestInstructionProcessing(unittest.TestCase):
    def test_process_initial_state(self):
        instructions = [
            'value 5 goes to bot 2',
            'bot 2 gives low to bot 1 and high to bot 3'
        ]
        bots = defaultdict(Bot)
        processed_bots = process_initial_state(instructions, bots)

        self.assertEqual(processed_bots[2].values, [5])
        self.assertEqual(processed_bots[2].low_to, ('bot', 1))
        self.assertEqual(processed_bots[2].high_to, ('bot', 3))

    def test_1_value_not_processed(self):
        bot = Bot()
        bot.bot_number = 1
        bot.add_value(5)

        bots = {1: bot}
        outputs = {}

        process_instruction(bot, 1, bots, outputs)

        # Check that the value is not moved
        self.assertEqual(bots[1].values, [5])
        self.assertEqual(outputs, {})

    def test_processed_and_moved(self):
        bot = Bot()
        bot.bot_number = 2
        bot.add_value(12)
        bot.add_value(17)

        bots = {2: bot}
        outputs = {}

        process_instruction(bot, 2, bots, outputs)

        # Check that the values were correctly moved
        self.assertEqual(bots[2].values, [])
        self.assertEqual(outputs, {})


if __name__ == '__main__':
    unittest.main()
