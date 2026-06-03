destination = input("what is your destination?")
distance = float(input("what is the distance in miles?"))
mpg = float(input("what is car's fuel efficiency in miles per gallon?"))
gaz_price = float(input("how much the gas price per gallon? "))
nights = float(input("how many nights the stay?"))
cost = float(input("what is the hotrl's cost per night?"))
food_budget = float(input("what is daily food budget?"))
gallons = distance / mpg
gaz_cost = gallons * gaz_price
hotel_cost = nights * cost
food_cost = (nights + 1) * food_budget
total = gaz_cost + hotel_cost + food_cost
print(f"=== Road Trip Budget Planner ===")
print(f"\nDestination: {destination}")
print(f"Distance: {distance}")
print(f"--- Cost Breakdown ---")
print(f"Gaz (f{gallons} @ ${gaz_price}): ${gaz_cost}")
print(f"Hotel({nights} nights  @ {cost}): {hotel_cost}")
print(f"Food ({nights} + 1 days @ {food_budget}) {food_cost}")
print("-" * 40)
print(f"Estimated Total:  ${total}")

                            
                       