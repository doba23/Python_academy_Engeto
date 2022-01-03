# Greet the client
print('=' * 80)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 80)

# Offer destinations
print('We can offer you the following destinations:')
print('-' * 80)
print('''
                            1 - Prague | 1000
                            2 - Wien | 1100
                            3 - Brno | 2000
                            4 - Svitavy | 1500
                            5 - Zlin | 2300
                            6 - Ostrava | 3400
                            ''')
print('-' * 80)

# Get input from user about destination
selection = int(input('Please enter the destination number to select: '))

# Assign variables appropriate data
DESTINATIONS = ['Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Check, whether entered valid input

# Get data from variables based on user's input
destination = DESTINATIONS[selection - 1]

if destination in DISCOUNT_25:
    print('Lucky you! You have just earned 25% discount for your destination -', destination)

price = PRICES[selection - 1]

# Calculate the price and check whether discount applicable for the selected destination

# Introduce registration

# Get input from user about personal data
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth_year = input('YEAR of BIRTH: ')
print('=' * 40)
email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD: ')
print('=' * 80)

# if some of condition is not met, invalid variable is set to 1
invalid = 0

# Check if the user is older than 15 years old
birth_year = int(birth_year)
if birth_year > 2004:
    print('you are too young')
    invalid = 1
# Check if email contains @ symbol
if not '@' in email:
    print('e-mail address is invalid')
    invalid = 1

# Check if password
# - is at least 8 chars long,
# - doesn't begin and end with a number
# - and contains both letters and numbers

if len(password) < 8:
    print ('password must be at least 8 characters long')
    invalid = 1


# Thank user by the input name and inform him/her about the reservation made
