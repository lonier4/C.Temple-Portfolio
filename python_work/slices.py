cars = ["chevy", "audi", "ford", "lambo", "benz", "bmw"]
print("These are my favorite cars:")

#prints the first 3
print(cars[:3])

#prints the last 3
print(cars[-3:])

#prints the 4 total starting at index 1
print(cars[1:4])

#copies cars list into friend_cars
friend_cars = cars[:]
cars.append("honda")
friend_cars.append("tesla")

for car in cars:
    print(cars[:2])

for friend in friend_cars:
    print(friend)