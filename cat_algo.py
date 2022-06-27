# This file contains 'home' function and its subordinates which are used to categorize transaction and add to categorization to categories table
from sql_connection import create_con, execute_query

my_con = create_con("192.168.0.50", "root", "admin", "default")

trans_dict = {'Housing': ['Rent', 'Property taxes', 'Household repairs', 'HOA fees', 'Renters insurance'],
              'Transportation': ['Car payment', 'Car warranty', 'Gas', 'Tires', 'Maintenance', 'Oil changes',
                                 'Parking fees', 'Repairs', 'Registration'],
              'Food': ['Groceries', 'Restaurants', 'Pet food', ],
              'Utilities': ['Electricity', 'Water', 'Garbage', 'Phones', 'Internet'],
              'Clothing': ['Clothes'],
              'Medical': ['Primary care', 'Dental care', 'Specialty care', 'Dermatologists', 'Orthodontics',
                          'Optometrists'],
              'Personal': ['Gym memberships', 'Haircuts', 'Subscriptions'],
              'Entertainment': ['Alcohol', 'Bars', 'Games', 'Movies', 'Concerts', 'Vacations', 'Amazon purchase'],
              'Financial': ['Investing', 'Transfer']}

new_dict = {0: ('Housing', 'Rent'), 1: ('Housing', 'Property taxes'), 2: ('Housing', 'Household repairs'),
            3: ('Housing', 'HOA fees'), 4: ('Housing', 'Renters insurance'),
            5: ('Transportation', 'Car payment'), 6: ('Transportation', 'Car warranty'), 7: ('Transportation', 'Gas'),
            8: ('Transportation', 'Tires'), 9: ('Transportation', 'Maintenance'), 10: ('Transportation', 'Oil changes'),
            11: ('Transportation', 'Parking fees'), 12: ('Transportation', 'Repairs'),
            13: ('Transportation', 'Registration'),
            14: ('Food', 'Groceries'), 15: ('Food', 'Restaurants'), 16: ('Food', 'Pet food'),
            17: ('Utilities', 'Electricity'), 18: ('Utilities', 'Water'), 19: ('Utilities', 'Garbage'),
            20: ('Utilities', 'Phones'), 21: ('Utilities', 'Internet'),
            22: ('Clothing', 'Clothes'),
            23: ('Medical', 'Primary care'), 24: ('Medical', 'Dental care'), 25: ('Medical', 'Specialty care'),
            26: ('Medical', 'Dermatologists'), 27: ('Medical', 'Orthodontics'), 28: ('Medical', 'Optometrists'),
            29: ('Personal', 'Gym memberships'), 30: ('Personal', 'Haircuts'), 31: ('Personal', 'Subscriptions'),
            32: ('Entertainment', 'Alcohol'), 33: ('Entertainment', 'Bars'), 34: ('Entertainment', 'Games'),
            35: ('Entertainment', 'Movies'), 36: ('Entertainment', 'Concerts'), 37: ('Entertainment', 'Vacations'),
            38: ('Entertainment', 'Amazon purchase'),
            39: ('Financial', 'Investing'), 40: ('Financial', 'Transfer'),
            41: ('Transportation', 'Travel'), 42: ('Uncategorized', 'Uncategorized'),
            43: ('Miscellaneous', 'Miscellaneous'), 44: ('Education', 'Education'), 45: ('Transportation', 'Uber')}


# Function to remove apostrophe from word to avoid word processing error
def crem(word):
    word = word.replace("'", "")
    return word


# Function to test categorization dictionary
def cat():
    new_dict = {}
    count = 0
    for x, y in trans_dict.items():
        # print(x)

        for i in y:
            print(x, i)
            new_dict[count] = (x, i)
            count += 1

    print(new_dict)


def get_cat(p):
    ans = p
    if p == 'n':
        z = False
    else:
        ans = int(ans)
        print(new_dict[ans])


# cat()
z = True
# while z:
#     ans = input()
#     get_cat(ans)
# List of problem phrases
words = ['Debit Card Purchase - ', 'Digital Card Purchase - ']


# function breaks down transaction name and removes problem phrases. It leaves most relevant name.
def short(y):
    # Loop over problem phrases
    for i in words:
        # Search for problem phrase in string, if found index is -1, triggering if conditional.
        a = y.find(i)
        if a != -1:
            # split both problem phrase and transaction description into words
            res = y.split()
            res1 = i.split()
            # Create new list to represented new string with problem phrase
            list_difference = []
            # Use loop to populate new list with no problem phrase
            for element in res:
                if element not in res1:
                    list_difference.append(element)
            # Creation of new word
            final = list_difference[0] + ' ' + list_difference[1]
            # reassign new word for the remaining of function
            y = final

    # Split word into parts
    res = y.split()
    # If category is only one word, return
    if len(res) == 1:
        return y
    # Take first two words and return
    else:
        final = res[0] + ' ' + res[1]
        return final

# main function
def home(y):
    # Use short function to reduce name of category
    x = short(y)
    # remove apostrophe
    x = crem(x)
    # Print RResult
    print(x)
    # Intialize cursor for sql
    mycursor = my_con.cursor()
    # Convert to string
    x = str(x)
    # SQL Query to find if name has association in db
    sql = "SELECT * FROM categories WHERE name = '%s'" % x
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    # If entry is not in database.
    if not myresult:
        # add record to db
        print(new_dict)
        print(y)
        # Select Category assignment
        ans = input('Please select primary and secondary categories for \n')
        ans = int(ans)

        cat1 = new_dict[ans][0]
        cat2 = new_dict[ans][1]
        # Confirmation message.
        confirm = input(f'Are you sure you want to assign {y} as {new_dict[ans]}')
        if confirm == 'y':
            query = "INSERT INTO categories (name, category1, category2) VALUES ('%s', '%s', '%s')" % (
                x, cat1, cat2)
            execute_query(my_con, query)
        else:
            home(y)

    else:
        return
        # return cat 1 and cat as list
