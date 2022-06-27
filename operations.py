import pandas as pd

# Dictionary access guide
# # To get 'Rent'
# print(trans_dict['Housing'][0])
trans_dict = {'Housing': ['Rent', 'Property taxes', 'Household repairs', 'HOA fees', 'Renters insurance'],
              'Transportation': ['Car payment', 'Car warranty', 'Gas', 'Tires', 'Maintenance', 'oil changes',
                                 'Parking fees', 'Repairs', 'Registration'],
              'Food': ['Groceries', 'Restaurants', 'Pet food', ],
              'Utilities': ['Electricity', 'Water', 'Garbage', 'Phones', 'Internet'],
              'Clothing': ['Clothes'],
              'Medical': ['Primary care', 'Dental care', 'Specialty care', 'dermatologists', 'orthodontics',
                          'optometrists'],
              'Personal': ['Gym memberships', 'Haircuts', 'Subscriptions'],
              'Entertainment': ['Alcohol', 'bars', 'Games', 'Movies', 'Concerts', 'Vacations', 'Amazon purchase'],
              'Financial': ['Investing', 'Transfer']}
