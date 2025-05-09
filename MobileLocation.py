import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

# enter phone number along with country
number = input("Enter phone number with country code : ")

# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)

# printing the timezone using the timezone module
timeZone = timezone.time_zones_for_number(phoneNumber)
print("timezone : " + str(timeZone))

# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber, "en")
print("location : " + geolocation)

# printing the service provider
service = carrier.name_for_number(phoneNumber, "en")
print("service provider : " + service)
