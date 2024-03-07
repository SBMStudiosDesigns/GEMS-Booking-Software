from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich.console import Console
from rich.style import Style
from rich import print, pretty 
from time import sleep
import sys
import locale
import typer


## -- Styles ---------------------------------------------------------------------------------------------------------------------------------
styleTitle = Style(color='magenta', bgcolor='grey85', bold=True, italic=False, underline=True, underline2=False, frame=False)
styleHeading = Style(color='plum4', bgcolor='grey85', bold=True, italic=False, underline=True, underline2=False, frame=False)
styleSubheading = Style(color='plum4', bgcolor='grey85', bold=True, italic=True, underline=False, underline2=False, frame=False)
styleBody = Style(color='plum4', bgcolor='grey85', bold=False, italic=False, underline=False, underline2=False, frame=False)  ## [plum4 on grey85]
styleInput = Style(color='plum4', bgcolor='grey69', bold=False, italic=False, underline=False, underline2=False, frame=False) ## [plum4 on grey69]
styleOutput = Style(color='grey85', bgcolor='plum4', bold=False, italic=True, underline=False, underline2=False, frame=False)

styleSelection = Style(color='deep_pink4', bgcolor='grey69', bold=True, italic=False, underline=False, underline2=False, frame=False)
styleSuccess = Style(color='magenta', bgcolor='grey85', bold=True, italic=False, underline=False, underline2=False, frame=False)
styleClose = Style(color='grey85', bgcolor='plum4', bold=True, italic=False, underline=False, underline2=False, frame=False)
styleError = Style(color='grey85', bgcolor='red3', bold=True, italic=False, underline=False, underline2=False, frame=False)





## -- Class: App -----------------------------------------------------------------------------------------------------------------------------
class ConsoleApp():
    def __init__(self):
        self.title = f'\n***************************************\nWelcome to GEMS Booking Software       \n***************************************\n'
        self.console = Console()
        self.booking_sheet = {101: [], 102: [], 103: [], 201: [], 202: [], 203: [], 301: [], 302: [], 303: [], '[blue]401 (Penthouse)[blue]': []}  ## booking_list = {'room_no': [fname, lname, price, checkin]}

    def __str__(self):
        return self.title
    
    def __main__(self):
        options = ['• A: Enter a new booking', '• B: Remove a booking', '• C: Dump booking list', '• E: Exit program']
        user_option = "[plum4 on grey69 bold]\nSelect task [plum4 on grey69 bold]"
        
        menu_heading = '  Main Menu  '
        console.print(menu_heading, style=styleHeading)

        menu_blurp = 'Select an option from the following task list:'
        console.print(menu_blurp, style=styleSubheading)

        for option in options:
            console.print(option, style=styleBody)

        # user_input = Style(user_option, style=styleInput)
        # console.print(user_option)
        # user_input = console.input(user_option,style=styleInput)
        # user_input = typer.prompt(user_option,style=styleInput)
        user_input = Prompt.ask(user_option)

        self.menu_options(user_input)

    def exit_program(self):
        sleep(01.10)
        console.clear()
        sys.exit(0)

    def menu_options(self, entry):
        option = entry.upper()
        attempt = 1
        
        while attempt <= 2:
            if option == 'A':
                msg = '\nOption [A] selected\n'
                console.print(msg, style=styleOutput)
                self.optionA_new_booking()
                break

            elif option == 'B':
                msg = '\nOption [B] selected\n'
                console.print(msg, style=styleOutput)
                self.optionB_remove_booking()
                break

            elif option == 'C':
                msg = '\nOption [C] selected\n'
                console.print(msg, style=styleOutput)
                self.optionC_dump_table()
                break
                
            elif option == 'E':
                msg = '\n\n**************************************************\n   Option [E] selected. Program will now close.   \n   Goodbye!   \n**************************************************\n'
                console.print(msg, style=styleClose)
                # console.clear()
                self.exit_program()

            else:
                errormsg = '[deep_pink4 on grey69 bold]Please input the letter representing a task option[deep_pink4 on grey69 bold]'
                
                option = Prompt.ask(errormsg).upper()
                attempt +=1
        else:
            err_msg = "***************************************\n      3 attempts have been made.       \n      Program will now close.              \n***************************************\n"
            console.print(err_msg, style=styleError)
            self.exit_program()
            return err_msg
            
    def optionA_new_booking(self):

        a_title = "   Option A: Enter New Booking   "
        a_heading = "[plum4 on grey69]Wish to proceed with task?[plum4 on grey69]"

        console.print(a_title, style=styleHeading)

        question =  Confirm.ask(a_heading, default=True)

        if question == True:
            
            while True:                

                global counter
                counter = 0

                room_msg = "[plum4 on grey85]• Room # [plum4 on grey85]"
                fname_msg = "[plum4 on grey85]• First Name [plum4 on grey85]"
                lname_msg = "[plum4 on grey85]• Last Name [plum4 on grey85]"
                price_msg = "[plum4 on grey85]• Price [plum4 on grey85]"
                checkin_msg = "[plum4 on grey85]• Checkin Date (formatted yyyy-mm-dd) [plum4 on grey85]"
                
                while counter <= 2: 

                    room_entry = IntPrompt.ask(room_msg)

                    if room_entry in self.booking_sheet:

                        global interested_room                            
                        interested_room = self.booking_sheet[room_entry]

                        if len(interested_room) == 0:

                            fname = Prompt.ask(fname_msg)
                            lname = Prompt.ask(lname_msg)
                            price = IntPrompt.ask(price_msg)
                            checkin  = Prompt.ask(checkin_msg)

                            client_info = f"Name {fname} {lname} | Paid: ${price} | Checkin (YYYY-MM-DD): {checkin}"
                            self.booking_sheet[room_entry] = client_info

                            print(f'\nNew booking has been entered for room:\n{interested_room}')
                            print(f'\nUpdated Booking sheet...')
                            print(self.booking_sheet)

                            complete_msg = "\n***************************************\nNew Booking has been entered!\nGoing back to the main menu...\n***************************************\n"
                            console.print(complete_msg, style=styleSuccess)
                        
                            self.__main__()

                        else:
                            err2 = "Room is booked.\nPlease select another room"
                            console.print(err2, style=styleError)
                            counter += 1

                    else:
                        err_msg = '\nRoom number out of range.\nPlease enter a number from the following list:'

                        console.print(err_msg, style=styleError)

                        for item in (self.booking_sheet.keys()):
                            console.print(item, style=styleInput)
                        
                        counter += 1

                else:
                    err_msg = "\n***************************************\n3 attempts have been made.       \nProgram will now return back to the main menu.              \n***************************************\n"
                    print('Attempts out of range.\nBack to main menu...')
                    console.print(err_msg, style=styleError)
                    question = False
                    self.__main__()
        else:
            err3 = 'Attempts out of range.\nBack to main menu...'
            console.print(err3, style=styleError)
            question = False
            self.__main__()

    def optionB_remove_booking(self):
        
        b_title = "   Option B: Enter New Booking   "
        b_heading = "[plum4 on grey69]Wish to proceed with task?[plum4 on grey69]"

        console.print(b_title, style=styleHeading)

        question =  Confirm.ask(b_heading, default=True)

        if question == True:
            
            while True:                

                global counter
                counter = 0

                room_msg = "[plum4 on grey85]• Enter the room number[plum4 on grey85]"

                while counter <= 2: 

                    room_no = IntPrompt.ask(room_msg)

                    if room_no in self.booking_sheet:
                        
                        global remove_room
                        remove_room = self.booking_sheet[room_no]

                        if len(remove_room) == 0:

                            err2 = "Room is empty.\nPlease select another room"
                            console.print(err2, style=styleError)
                            counter += 1
                        else:
                            fname = remove_room[0]
                            checkin = remove_room[3]
                            msg1 = f"Room is currently being occupied by {fname} since {checkin}"

                            console.print(msg1, style=styleOutput)

                            msg2 = "[bold plum4 on grey85]Are you sure you want to remove booking?[bold plum4 on grey85]"
                            
                            confirm_removal = Prompt.ask(msg2)

                            if confirm_removal == True:

                                self.booking_sheet[room_no] = []

                                msg3 = f'\nRoom #{room_no} is now empty\nBooking removal process now completed!\nNow returning back to the main menu...'
                                console.print(msg3, style=styleSuccess)   
                                self.__main__() 

                            else:    
                                err4 = 'Booking removal process cancelled.\nNow returning back to the main menu...'
                                console.print(err4, style=styleError)   
                                self.__main__() 

                    else:

                        err_msg = '\nRoom number out of range.\nPlease enter a number from the following list:'

                        console.print(err_msg, style=styleError)

                        for item in (self.booking_sheet.keys()):
                            console.print(item, style=styleInput)
                        
                        counter += 1

                    
                else:
                    err_msg = "\n***************************************\n3 attempts have been made.       \nProgram will now return back to the main menu.              \n***************************************\n"
                    print('Attempts out of range.\nBack to main menu...')
                    console.print(err_msg, style=styleError)
                    question = False
                    self.__main__()

        else:
            err3 = 'Attempts out of range.\nBack to main menu...'
            console.print(err3, style=styleError)
            question = False
            self.__main__()

    def optionC_dump_table(self):

        c_title = "   Option B: Enter New Booking   "
        c_heading = "[plum4 on grey69]Wish to proceed with task?[plum4 on grey69]"

        console.print(c_title, style=styleHeading)

        question =  Confirm.ask(c_heading, default=True)

        if question == True:
                
                for key, value in self.booking_sheet.items():
                    formatstring = f'Room #{key} || Client {value}'
                    console.print(formatstring, style=styleOutput)
                
                # for booking in self.booking_sheet:
                #     room = self.booking_sheet[booking]
                #     # key = self.booking_sheet[room]
                #     formatstring = f'Room #{room}'
                #     console.print(room, style=styleOutput)

                global counter
                counter = 0
                msg5 = "[plum4 on grey69]Ready to return back to the main menu?[plum4 on grey69]"
                end_task = Prompt.ask(msg5)

                if end_task == True:
                    self.__main__()
                else:
                    msg6 = "\nThere's no where else to go silly goose!\n:P\n"
                    console.print(msg6, style=styleSuccess)
                    sleep(00.20)
                    self.__main__()

        else:
            err3 = 'Back to main menu...'
            console.print(err3, style=styleSuccess)
            question = False
            self.__main__()
         

## -- Main Console ---------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # locale.setlocale(locale.LC_ALL, '')
    console = Console()
    console.clear()

    startup_msg = "*------------------------------------*\n           Starting app...            \n*------------------------------------*"

    app = ConsoleApp()

    console.print(startup_msg, style=styleSuccess)
    console.print(app, style=styleClose)
    sleep(0.5)
    app.__main__()
    sleep(0.5)
    console.clear()
    
