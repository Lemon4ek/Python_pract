import random

random_list = [random.randrange(-100,100) for i in range(30)]

print("\nRandom list of numbers from -100 to 100 is: ", random_list)

maxNumber = max(random_list)

maxNumberId = 1 + random_list.index(maxNumber)

print("\nMax number:", maxNumber, "\nMax number id:", maxNumberId, "\n\n")

for i in range(29):
    if random_list[i] < 0 and random_list[i+1] < 0:
        print(random_list[i], random_list[i+1], "\n")
