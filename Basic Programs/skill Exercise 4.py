#3rd question

import pandas as pd
import matplotlib.pyplot as plt
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df
def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i,column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color = colors[i])
    # plt.plot(x_values, y_values, marker='o', linestyle='-', color=colors)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    plt.savefig("a1.png")
    plt.show()

if __name__== "__main__":
    file_path = "se4.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)

#1st question
'''
import random
import string

def generate_random_color_hex():
    color_hex = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color_hex

def generate_random_alphabetical_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_random_value_between(min_value, max_value):
    random_value = random.randint(min_value, max_value)
    return random_value

def generate_random_multiple_of_7():
    random_multiple_of_7 = random.randint(0, 10) * 7
    return random_multiple_of_7

# Example usage:
random_color = generate_random_color_hex()
random_string = generate_random_alphabetical_string(10)
random_value = generate_random_value_between(5, 15)
random_multiple_of_7 = generate_random_multiple_of_7()

print("Random Color Hex:", random_color)
print("Random Alphabetical String:", random_string)
print("Random Value Between 5 and 15:", random_value)
print("Random Multiple of 7 Between 0 and 70:", random_multiple_of_7)

'''
#2nd question
'''
import random
from datetime import datetime, timedelta

def generate_random_integer_excluding(max_value):
    random_int = random.randint(0, max_value - 1)
    return random_int

def generate_random_integer_range_excluding(min_value, max_value):
    random_int = random.randint(min_value, max_value - 1)
    return random_int

def generate_random_integer_with_step(min_value, max_value, step):
    random_int = random.randrange(min_value, max_value, step)
    return random_int

def generate_random_date(start_date, end_date):
    time_difference = end_date - start_date
    random_days = random.randint(0, time_difference.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

# Example usage:
random_int_0_to_5 = generate_random_integer_excluding(6)
random_int_5_to_9 = generate_random_integer_range_excluding(5, 10)
random_int_with_step = generate_random_integer_with_step(0, 10, 3)
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)
random_date_between_dates = generate_random_date(start_date, end_date)

print("Random Integer between 0 and 5 (excluding 6):", random_int_0_to_5)
print("Random Integer between 5 and 9 (excluding 10):", random_int_5_to_9)
print("Random Integer between 0 and 10 with a step of 3:", random_int_with_step)
print("Random Date between {} and {}:".format(start_date, end_date), random_date_between_dates)
'''