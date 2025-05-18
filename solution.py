import requests

# currency user is converting from, upper() accepts only uppercase inputs
from_currency = str(
    input("Enter in the currency you'd like to convert from: ")).upper()

# currency user is converting to, upper() accepts only uppercase inputs
to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(
    input("Enter in your monetary amount: ") )
 
#fetches api, is successful when status is 200
response = requests.get(
    f"https://v6.exchangerate-api.com/v6/9ddf48650227d232cc03556a/pair/{from_currency}/{to_currency}")

#extract conversion rate from api response
conversion_rate = response.json()['conversion_rate']

# calculates the converted amount
converted_amount = amount * conversion_rate

#prints the converted amount
print(
    f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
)