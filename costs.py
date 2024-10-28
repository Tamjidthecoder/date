import datetime
import calendar
nights=datetime.time(12)
hotel_cost=int(input("enter your nights stayed in hotel: "))
if hotel_cost>nights:
    print("Your cost is $180")
days=datetime.time()
plane_cost=int(input("enter your days stayed in hotel: "))
if plane_cost>days:
    print("Your cost is $180")
hours=datetime.time(1)
rental_cost=int(input("enter your hours useed car: "))
if rental_cost>hours:
    print("Your cost is $180")