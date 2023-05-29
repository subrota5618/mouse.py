import phonenumbers 
from test import number 
from phonenumbers import geocoder
# get country name 
ch_phone = phonenumbers.parse(number , "CH")
print("Country name for number => ", geocoder.description_for_number(ch_phone , "en"))
# get sim server  
from phonenumbers import carrier
sim_server = phonenumbers.parse(number, "RO")
print("Service name for number => ", carrier.name_for_number(sim_server , "en"))
