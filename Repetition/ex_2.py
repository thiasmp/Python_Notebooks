import webget
import csv
import platform
import argparse

#  Exercise 1
# 1. Create a python file with 3 functions:
#   1. `def print_file_content(file)` that can print content of a csv file to the console


def print_file_content(file):
    with open(file) as file_object:
        reader = csv.reader(file_object)
        for row in reader:
            print(row)

# print_file_content('science.csv')


#   2. `def write_list_to_file(output_file, lst)` that can take a list or tuple of strings and write each element to a new line in file
#     1. rewrite the function so that it gets an arbitrary number of strings instead of a list
str = 'Year1', 'US science spending1', 'Suicides1'


def write_list_to_file(output_file, lst):

    with open('science.csv', 'a', newline='') as output_file:
        output_writer = csv.writer(output_file)

# output_writer.writerow(lst)

#   3. `def read_csv(input_file)` that take a csv file and read each row into a list. Print the list.


def write_list_to_file(input_file):
    with open(input_file) as file:
        reader = csv.reader(file)
        lst = []
        for row in reader:
            lst.append(row)
        print(lst)


# write_list_to_file('science.csv')

# 2. Add a functionality so that the file can be called from cli with 2 arguments:
    #   1. path to csv file!
    #   2. an argument `--file file_name` that if given will write the content to file_name or otherwise will print it to the console.

def call_from_cli():
    parser = argparse.ArgumentParser(description='A program that reads CSV')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('-d', '--destination', default='default-file.csv')
    args = parser.parse_args()
    print(args.file.readlines())


call_from_cli()
