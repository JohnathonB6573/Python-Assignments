# this can throw an exception
def get_numbers_from_file(file_name):
    numbers = []
    # with open(file_name) as file: automatically closes the file when leaving the block
    with open(file_name, 'r') as file:

        # Read the file's contents as a list of strings.
        unconverted_numbers = file.readlines()

         # Convert the strings to integers and store them in numbers list
        for number in unconverted_numbers:
                numbers.append(int(number))

    return numbers

def display_summary_statistics_for_values_in_file(file_name):
    # Initialize variables
    number_sum = 0
    number_count = 0
    number_average = 0
    number_maximum = 0
    number_minimum = 0
    number_range = 0
    number_median = 0
    number_mode = 0
    numbers = []

    try:
        numbers = get_numbers_from_file(file_name)
    except Exception as error:
        print(error)
        return

    # Determine the sum
    number_sum = sum(numbers)
    # Determine the count
    number_count = len(numbers)
    # Determine the max
    number_maximum = max(numbers)
    # Determine the minimum
    number_minimum = min(numbers)
    
    # Determine the median
    numbers.sort()
    count = int(len(numbers))
    middle = int(count / 2)
    if count %2 == 0:
        number_median = (numbers[middle] + numbers[middle + 1])/2
    else:
        number_median = numbers[middle]

    # Determine the mode
    numbers_count = {}
    for number in numbers:
        if number in numbers_count:
            numbers_count[number] += 1
        if not number in numbers_count:
            numbers_count[number] = 1
    count = numbers_count[number]
    for number in numbers:
        if numbers_count[number] == count:
            number_mode = numbers_count[number]
        
    # Calculate the average
    number_average = number_sum / number_count
    # Calculate the range
    number_range = number_maximum - number_minimum

    # Print the calculated statistics
    print("File name:", file_name)
    print("Sum:", number_sum)
    print("Count:", number_count)
    print("Average:", number_average)
    print("Maximum:", number_maximum)
    print("Minimum:", number_minimum)
    print("Range:", number_range)
    print("Median:", number_median)
    print("Mode:", number_mode)
   
def main():
    while (True):
        file_name = input("Enter the path of the file you would like to process: ")
        try:
            display_summary_statistics_for_values_in_file(file_name)
        except Exception as error:
            print("There are no numbers in", file_name)
            return
        calculate_again = input("Would you like to evaluate another file? (y/n) ")
        if (calculate_again != "y"):
            break  
        else:
            print('') # separator between inputs

main()
