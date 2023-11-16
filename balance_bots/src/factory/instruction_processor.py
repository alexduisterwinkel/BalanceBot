import logging
from balance_bots.src.constants.instruction_type import InstructionType
from balance_bots.src.constants.microchip import Microchip

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


# This method handles the initial state by going over the instructions and setting the variables per bot
def process_initial_state(instructions, bots):
    for instruction in instructions:
        words = instruction.split()

        if words[0] == InstructionType.VALUE.value:
            microchip_value = int(words[1])
            bot_number = int(words[5])

            bots[bot_number].add_value(microchip_value)
        elif words[0] == InstructionType.BOT.value:
            bot_number = int(words[1])

            bots[bot_number].low_to = (words[5], int(words[6]))
            bots[bot_number].high_to = (words[10], int(words[11]))

    return bots


# This method is used in a loop, checking each time if a bot has 2 microchips in hand and if so,
# to execute the instruction by giving the microchip either to another bot or an output.
# Because we are interested in the bot who handles 2 specific microchips, we give notice of that in here.
def process_instruction(bot, bot_number, bots, outputs):
    if bot.has_two_values():
        low_value, high_value = bot.give_values()

        if bot.low_to:
            low_dest, low_dest_num = bot.low_to
            if low_dest == InstructionType.BOT.value:
                bots[low_dest_num].add_value(low_value)
            else:
                outputs[low_dest_num] = low_value

        if bot.high_to:
            high_dest, high_dest_num = bot.high_to
            if high_dest == InstructionType.BOT.value:
                bots[high_dest_num].add_value(high_value)
            else:
                outputs[high_dest_num] = high_value

        if low_value == Microchip.ONE.value and high_value == Microchip.TWO.value:
            logging.info(f'Bot number: {bot_number} is responsible for handling microchip {Microchip.ONE.value} and {Microchip.TWO.value}')
