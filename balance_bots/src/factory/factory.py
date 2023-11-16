import logging

from collections import defaultdict
from balance_bots.src.model.bot import Bot
from balance_bots.src.factory.instruction_processor import process_initial_state
from balance_bots.src.factory.instruction_processor import process_instruction

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def process_bot_flow(bots):
    outputs = {}

    # Part 1
    # Iterate over the bots and check which bot needs to execute their instruction
    # in process_instruction(), outputs is updated if necessary
    while any(bot.has_two_values() for bot in bots.values() if bot.has_two_values()):
        for bot_number, bot in bots.items():
            process_instruction(bot, bot_number, bots, outputs)

    # Because we are in a factory, we want to know for sure each output has the correct microchip.
    for idx, (output, value) in enumerate(sorted(outputs.items())):
        logging.info(f'Output no:{output}: with value: {value}')

    # Part 2
    # Now that we processed all the bots and their instructions, we know the values in each output
    check_outputs(outputs)


def check_outputs(outputs):
    multiplying_values = [outputs[0], outputs[1], outputs[2]]
    result = multiplying_values[0] * multiplying_values[1] * multiplying_values[2]
    logging.info(f'The result of multiplying the values in outputs 0, 1, and 2 is: {result}')


# Read the instructions from the given resource file
def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


instructions = read_instructions('../../resources/instructions.txt')
bots = defaultdict(Bot)

bots = process_initial_state(instructions, bots)
process_bot_flow(bots)
