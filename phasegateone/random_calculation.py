import time
from random import random, Random

def get_random_calculation():
    random = Random()
    first_number = random.randint(20,50)
    second_number = random.randint(10, 20)
    print(f"{first_number} - {second_number}")
    final_score = first_number - second_number
    return final_score

def get_time_spent(start_time):
    end_time = time.time()
    time_spent = end_time - start_time
    return time_spent


score = 0
start_time_display = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Your start time is {start_time_display}")
start_time = time.time()
for i in range(0,10):
    final_score = get_random_calculation()
    response = int(input(f"Enter the correct answer: "))
    if response == final_score:
        score += 1
    if i == 9:
        time_spent = get_time_spent(start_time)
        print("You got " + str(score ) + " points in " + str(time_spent) + " seconds.")



