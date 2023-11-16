import unittest
from unittest.mock import mock_open, patch

from balance_bots.src.factory.factory import check_outputs
from balance_bots.src.factory.factory import read_instructions


class TestProcessBotFlow(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='instruction1\ninstruction2\ninstruction3')
    def test_read_instructions(self, mock_file_open):
        file_path = 'dummy_path'
        instructions = read_instructions(file_path)

        mock_file_open.assert_called_once_with(file_path, 'r')

        self.assertEqual(instructions, ['instruction1\n', 'instruction2\n', 'instruction3'])

    @patch('balance_bots.src.factory.logging.info')
    def test_check_outputs(self, mock_logging_info):
        outputs = {0: 2, 1: 5, 2: 7}

        check_outputs(outputs)

        mock_logging_info.assert_called_once_with('The result of multiplying the values in outputs 0, 1, and 2 is: 70')


if __name__ == '__main__':
    unittest.main()
