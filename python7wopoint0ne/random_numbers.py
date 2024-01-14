import random

n = int(input("Enter number of integers to be generated: "))


random_number_list = []

my_string = "Generated values: "
for i in range(n):
    random_number = random.randint(1,101)
    my_string += str(random_number) + ' '
    random_number_list.append(random_number)

max = max(random_number_list)
min = min(random_number_list)
average = round(sum(random_number_list)/n, 1) 
print(random_number_list)

print(f"Average, min, and max are {average}, {min}, and {max}")

    