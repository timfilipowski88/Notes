            ### #2 Python Fundamentals

        ## Functions
    # Objectives
# Syntax
# The def keword signifies the declaration of a function and assigns a name so we can call it later. 
def add(a, b):  # function name: 'add', parameters: a and b
    x = a + b  # process
    return x  # return value: x


def values_greater_than_second(input_list):
    new_list = []
    second_num = input_list[1]
    for y in range(len(input_list)):
        if input_list[y] > second_num:
            new_list.append(input_list[y])
    print(len(new_list))
    return new_list


values_greater_than_second([5, 2, 3, 2, 1, 4])
values_greater_than_second([3])
