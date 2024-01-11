import phonenumbers
from phonenumbers import geocoder, carrier

# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+573053030176")

# Getting carrier of a phone number
Carrier = carrier.name_for_number(phoneNumber, 'es')

# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'es')

# Printing the carrier and region of a phone number
print(Carrier)
print(Region)
