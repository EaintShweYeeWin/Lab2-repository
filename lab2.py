import statistics

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("Get user input")
    user_input = input()
    str_list = user_input.split(",")
    float_list =[]
    for s in str_list:
        float_list.append(float(s))
    return float_list


def calc_average(temperature_list):
    print("calc_average")
    return sum(temperature_list) / len(temperature_list)

def find_min_max(temperature_list):
    print("find_min_max")
    return [min(temperature_list), max(temperature_list)]

def sort_temperature():
    print("Sort_temperature")

def calc_median_temperature():
    print("calc median temperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)

if __name__ == "__main__":
    main()