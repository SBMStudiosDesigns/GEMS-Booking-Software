from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich.console import Console
from rich.style import Style
from rich import print, pretty 
import copy as c
import sys
import locale
import typer


# def get_number(self, prompt):
#     num = int(prompt)
#     # print(num)
#     return num


room_list = {101: ['john', 'doe', 20, '2024-04-15'], 102: ['tea', 'duncan', 20, '2024-04-15'], 103: ['angella', 'pitter', 20, '2024-04-15'], 104: []}
cliententryinfo = {101: ['john', 'doe', 20, '2024-04-15'], 102: ['tea', 'duncan', 20, '2024-04-15'], 103: ['angella', 'pitter', 20, '2024-04-15'], 104: []}
booking_sheet = {101: [], 102: [], 103: [], 104: []}


# print('## test 1 - using variable as a key to grab value')
# # num = 101
# # new = room_list[num]
# print(new)
# print()

print("Testing 1...")
names = ['David', 'Peter', 'Michael', 'John', 'Bob']
for i in range (len (names)):
    print("{}.{}".format(i + 1, names[i]))

print("\nTesting 2...") ## i like 
for key, value in room_list.items():
    print(f'{key} {value}')

print("\nTesting 3...") ## i like
for value in room_list.items():
    print(f'{value}')

print("\nTesting 4...")
while i in range(len(room_list)):
    roomkey = room_list[2]
    clientinfo = room_list[roomkey]
    print(f'{roomkey} {clientinfo}')

# print("\nTesting 5...") 
# for val in room_list.items():
#     formatstring = "Name {} {} Paid ${} Checkin: {}" 
#     # client_info2 = val.format(formatstring)
#     client_info2 = val.__format__("Name {} {} Paid ${} Checkin: {}")
#     # client_info2 = formatstring.format(*val)
#     # client_info2 = list(map(formatstring, val))
#     print(f'{client_info2}')


# print('## Test 2 - format dict value to string')
# num = 101
# room_entered = room_list[num]
# for unit in room_entered:
#     #room = room_list[unit]
#     formatstring = "Name {} {} Paid ${} Checkin: {}"                    
#     client_info = formatstring.format(**unit)
#     print(client_info)
# print()

# print('## test 3 - check if dict key has values')
# check2 = room_list[101]
# if len(check2) == 0:
#     print("The dictionary is empty")
# else:
#     print("The dictionary is not empty")
#     client_info = formatstring.format(*check2)
#     print(client_info)
# print()


# print('## test 4 - check if dict key has values')
# check2 = room_list[104]
# if len(check2) == 0:
#     print("The dictionary is empty")
# else:
#     print("The dictionary is not empty")
#     client_info = formatstring.format(*check2)
#     print(client_info)
# print()


# print('## test 5 - add room to booking sheet')
# num = 104                                                                  ## room num variable
# interestedroom = booking_sheet[num]                                        ## grabbing booksheet key using variable

# if len(interestedroom) == 0:                                               ## if key is empty
#     print("The room is empty\nNow entering booking...") 

#     booking_sheet[num] = client_info                                       ## add client info as key values

#     print(f'Room client info before booking:{interestedroom}')
#     print(f'Room info after booking{booking_sheet}')
# else:
#     print("The room is booked. Sorry...goodbye now.")
# print()


# print("Test 6: Get user name")
# # new = room_list[num]
# print(new)
# print(f"First Name: {new[0]}")
# print(client_info)



# print("Test 7: Update user name")
# # new = room_list[num]
# print(new)

# print(f"First Name before update: {new[0]}\n")

# new[0] = 'Sara'

# print(f"First Name after update: {new[0]}\n")

# print("Print room list")
# print(room_list)

# room_list[101] = []
# print("Print updated room list")
# print(room_list)


# print()