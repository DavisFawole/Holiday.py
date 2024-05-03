# Here I will be creating a function plane cost, I ask that the user choose a city fly to
# The user can choose from three cities listed - Paris, Frankfurt or Milan

def plane_cost():
    while True:
        city_flight = input("Please enter city you are flying to. Enter Paris, Frankfurt or Milan: ").lower()
        
        if city_flight == "paris":
            paris = 180
            return city_flight, paris
        elif city_flight == "frankfurt":
            frankfurt = 175
            return city_flight, frankfurt
        elif city_flight == "milan":
            milan = 220
            return city_flight, milan
        else:
            print("Please enter a valid city, Paris, Frankfurt or Milan")

# Here I will be creating a hotel cost function, asking the user to choose a number of nights for their stay
# Calculating costs is depedant on the number of nights and city chosen by the user


def hotel_cost(city_flight):
    while True:
        travel_num_nights = input("Please enter the number of nights for your stay: ")
        try:
            travel_num_nights = int(travel_num_nights)

            par_cost_per_night = 80
            frank_cost_per_night = 65
            mil_cost_per_night = 72

            if city_flight == "paris":
                paris = travel_num_nights * par_cost_per_night
                return paris
            elif city_flight == "frankfurt":
                frankfurt = travel_num_nights * frank_cost_per_night
                return frankfurt
            elif city_flight == "milan":
                milan = travel_num_nights * mil_cost_per_night
                return milan
        except:
            print("Please enter a number only ")

# Creating car cost function
# Asking user to choose a number of days
# Passing through city_flight in the parentheses 
# Using while True try to handle user input errors
# Calculating costs depending on the number of days and city chosen by the user


def car_cost(city_flight):
    while True:
        car_rental_num_days = input("Please enter car rental number of days: ")
        try:
            car_rental_num_days = int(car_rental_num_days)

            par_rent_cost_per_day = 15
            frank_rent_cost_per_day = 27
            mil_rent_cost_per_day = 22

            if city_flight == "paris":
                paris = car_rental_num_days * par_rent_cost_per_day
                return paris
            elif city_flight == "frankfurt":
                frankfurt = car_rental_num_days * frank_rent_cost_per_day
                return frankfurt
            elif city_flight == "milan":
                milan = car_rental_num_days * mil_rent_cost_per_day
                return milan
        except:
            print("Please enter a number only ")

# Creating holiday cost function
# Calculating grand total for the total cost of the holiday by adding hotel_total, plane_total and rental_total

def holiday_cost():
    city_flight, plane_total = plane_cost()
    hotel_total = hotel_cost(city_flight)
    rental_total = car_cost(city_flight)
    grand_total = plane_total + hotel_total + rental_total
    return f'''Your plane cost to {city_flight.capitalize()} is: £{plane_total}
Your total hotel cost is: £{hotel_total}
Your total car rental cost is: £{rental_total}
Your total holiday total is: £{grand_total}'''

total = holiday_cost()
print(total)







