"""To install Windows 11, a computer must have 8GB of memory and 64GB of free storage space, and be running Windows
10. (Source, Microsoft)

All three requirements must be met.

Write a windows_11_compatible function that takes three arguments, the amount of memory, the free storage space,
and current operating system.

In the windows_11_compatible function use conditions to figure out if the user's computer can be upgraded to Windows
11 or not.

You'll need to check that the memory is at least 8, the free storage space is at least 64, and the name of the
current operating system equals 'Windows 10'

Your windows_11_compatible function should return one of the Boolean values True (if the computer can be upgraded) or
False (if it can't be upgraded).  The can_upgrade function will not print anything.

Create a main function.  In the main function, ask the user for

The current memory in their computer, in GB.  (For example, a user with 8GB of memory would enter 8) The amount of
free storage space, in GB. (For example, a user with a 500GB of free space should enter 500) The name of their
current operating system. (For example, a user could enter Windows 10 or Windows 8 or Windows 7 or Windows XP or
Linux or MacOS...)
Call your windows_11_compatible function from main(), and use the return value to print a message
to the user telling them if they can, or can't, upgrade."""

print('Here we will enter some of your computer specifications to see if Windows 11 can be installed.')


def main():
    memory = int(input('Please enter the amount of memory your computer has, in GB: '))
    free_space = int(input('How much free space does your computer have, in GB: '))
    operating_system = input('What is your current operating system? ')
    compatible = can_upgrade(memory, free_space, operating_system)
    status_message = windows_11_compatible(memory, free_space, operating_system)
    print(f'Your computer {status_message} be upgraded.')


def can_upgrade(memory, free_space, operating_system):
    if memory >= 8:
        return True
    elif memory < 8:
        return False
    elif free_space >= 64:
        return True
    elif free_space < 64:
        return False
    elif operating_system == 'Windows 10':
        return True
    elif operating_system != ' Windows 10':
        return False


def windows_11_compatible(memory, free_space, operating_system):
    if memory >= 8 and free_space >= 64 and operating_system.lower() == 'windows 10':
        return 'can'
    else:
        return 'cannot'


main()

# THIS one took a lot of trial and error. I took a few days to complete, mainly to re-read and try and re-wrapy my
# head around the concepts. I tried calling functions that werent there, with values that were not defined globally.
# after some rearranging i realized i forgot to set a function for the main to call after setting Bool values. Cannot
# call those in a str message. I had to tell the program what to say when the value returned True or False. Also,
# i keep forgetting to include '()' after certain things (like lower() or upper() ) which, caused a lot of issues.
# need to remind myself to slow down and take breaks when i feel stuck!!
