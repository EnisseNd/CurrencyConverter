import requests

# currency user is converting from, upper() accepts only uppercase inputs
from_currency = str(
    input("Enter in the currency you'd like to convert from: ")).upper()

# currency user is converting to, upper() accepts only uppercase inputs
to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(
    input("Enter in your monetary amount: ") )

