# Balance Bot program

Python script to manage bots and their movement based on instructions provided.
It allows to follow which bot is handling 2 specific microchips in the process.
In this case, we are interested in finding the bot that handles microchip 17 and 61.

The script starts by reading the instructions as input from file and then sets the initial state of the bots.
When the state is set, the script starts checking which bot needs to be in action and execute their instruction.

Finally, once all the instructions are done, we can check the values in each output and do some calculations with it.

Some files explained: 
- in factory.py is the main proces. It reads the file, and starts of the process
- In bot.py - the executing object in the factory - is declared with some methods to interact with it.
- In instructions_processor.py is the main logic and responsible to set the initial state and to let the bots move
- In microchip.py you can adjust the specific microchip values that you are interested in
