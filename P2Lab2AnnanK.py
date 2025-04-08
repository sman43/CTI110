#Kenneth Annan
#2/21/25
#P2Lab2
#Using a dictionary and F strings

cars = {'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26}
#Get keys from dictionary
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep= ", ")

#Get a car from user
car_name= input("Enter a car: ")
#Get MPG for given car
car_mpg = cars[car_name]
print(f" The {car_name} gets {car_mpg} miles per gallon.")

#get miles from user. 
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#calculate
gallons_needed =  miles_driven/car_mpg

print(f"If you're driving the {car_name}, you need {gallons_needed:.1f} gallon(s) of gas to drive {miles_driven:.0f} miles.")