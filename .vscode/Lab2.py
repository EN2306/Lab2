print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def get_user_input():
    user_input = input("Give me numbers separated by commas: ")

    values = user_input.split(",")
    numbers = [float(value.strip()) for value in values]

    print("get_user_input")
    print(numbers)

    return numbers

numbers = get_user_input()


def calc_average(temperatures):
    average = sum(temperatures) / len(temperatures)
    return average

def find_min_max(temperatures):
    return [min(temperatures), max(temperatures)]

def sort_temperature(temperatures):
    return sorted(temperatures)
    
def calc_median_temperature(temperatures):
    sorted_temperatures = sorted(temperatures)
    length = len(sorted_temperatures)
    middle = length // 2

    if length % 2 == 1:
        return sorted_temperatures[middle]
    else:
        return (
            sorted_temperatures[middle - 1]
            + sorted_temperatures[middle]
        ) / 2