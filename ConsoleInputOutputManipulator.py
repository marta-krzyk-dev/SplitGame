from termcolor import colored, COLORS
from os import system, get_terminal_size
from Project4_Split.instructions import getInstructions
from Project4_Split.helpers import getFirst


class ConsoleInputOutputManipulator:
    def __init__(self, font_color="white"):
        self.font_color = font_color if font_color in COLORS.keys() else "white"
        try:
            self.console_width = get_terminal_size().columns
        except OSError:
            self.console_width = 40

    def ClearConsole(self):
        system('cls')

    # region Print methods
    def Print(self, text, color=None, attributes=["bold"]):
        if not isinstance(text, str):
            return
        else:
            if color is None:
                color = self.font_color
            print(colored(text, color, attrs=attributes))

    def PrintCentered(self, text, font_color=None, attributes=["bold"]):
        if font_color is None:
            font_color = self.font_color

        print(colored(text.center(self.console_width), font_color, attrs=attributes))

    def PrintReverse(self, text):
        self.Print(text, self.font_color, ["bold", "reverse"])

    def PrintOnBackground(self, text):
        if not isinstance(text, str):
            return

        print(colored(text, self.font_color, attrs=["bold", "reverse"]))

    def PrintInstructions(self):
        # self.ClearScreen()
        self.PrintParagraphs(getInstructions())

    def PrintParagraphs(self, paragraphDict):
        if not isinstance(paragraphDict, dict):
            return

        for p in paragraphDict:
            self.Print(f"\n*** {p.upper()} ***\n", "blue", ['bold','reverse'])
            print(colored(paragraphDict[p], "white", attrs=['bold']))

        if len(paragraphDict) > 0:
            print()

    def PrintCommands(self):
        print("Available commands:")
        print("--help       Print instructions")
        print("--resume     Resume the game")

    def PrintStacks(self, card_piles, arrow_color1, arrow_color2, print_size_above_cards=False, print_size_below_cards=False):

            row_arrow_above = "  V    "
            row1 = ""
            row2 = ""
            row3 = ""
            row_arrow_below = "  X    "
            pile_sizes_row = ""

            for pile in card_piles:
                row1 += "┌──┐  " if len(pile) < 2 else "╔══╗  "
                character = getFirst(pile, '░')
                row2 += f"│{character.ljust(2)}│  " if len(pile) < 2 else f"║{character.ljust(2)}║  "
                row3 += "└──┘  " if len(pile) < 2 else "╚══╝  "
                pile_sizes_row += f"[{str(len(pile))}]".rjust(4) + "  "

            if print_size_above_cards:
                self.Print(pile_sizes_row.center(50))

            self.Print(row_arrow_above.center(50), arrow_color1)
            self.Print(row1.center(50))
            self.Print(row2.center(50))
            self.Print(row3.center(50))
            self.Print(row_arrow_below.center(50), arrow_color2)

            if not print_size_below_cards:
                self.Print(pile_sizes_row.center(50))

    # endregion

    # region Input methods
        #TODO REmove
    def IsCommand(self, input):
        input = input.replace(" ", "").lower()
        return input == "--help" or input == "--resume"

    def GetInput(self, message="", allowed_answers=[]):

        allowed_answers = [str(x).lower() for x in allowed_answers]

        while True:
            answer = input(colored(message, self.font_color, attrs=["bold", "reverse"]))  # Remove whitespaces
            formatted_answer = answer.replace(" ", "").lower()

            if formatted_answer in allowed_answers:
                return answer
            elif formatted_answer == "--help":
                self.PrintInstructions()
                while True:
                    answer_ = input(colored("Type --resume to get back to the game", self.font_color, attrs=["bold", "reverse"])).replace(" ", "").lower()
                    if answer_ == '--resume':
                        break
                    elif answer_ == '--help':
                        self.PrintInstructions()
                    else:
                        self.PrintCommands()
            elif formatted_answer == "--resume":
                continue
            elif formatted_answer.startswith("--"):
                self.PrintCommands()
            elif not allowed_answers:
                return answer

    def Command(self, input):
        if False == input is str:
            raise TypeError

        answer = input.replace(" ", "").lower()  # Remove whitespaces

        if answer == "--help":
            self.PrintInstructions()
        elif answer == "--resume":
            return
        else:
            print("Available commands:")
            print("--help       Print instructions")
            print("--resume     Resumes the game")

        return answer
    # endregion