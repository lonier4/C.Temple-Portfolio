pizzas = ["cheese", "pineapple", "margherita", "chicken"]
#dont forget the colon and the indentation
for pizza in pizzas:
    print(pizza.title() + " pizzas are the dankest!\n")
#no indentation will exit the loop and only print once
print("All pizzas are welcomed in my book")

#prints range as a list
numbers = list(range(1,21))
print(numbers)

#prints numbers as a column
for number in range(1,21):
    print(number)

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
    print(odd_numbers)

#prints every multiple of 3 until 30
threes = list(range(3,31, 3))
for value in threes:
    print(threes)

#prints cube value of each number in a range
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

cubes = [cube**3 for cube in range(1, 11)]
print(cubes)