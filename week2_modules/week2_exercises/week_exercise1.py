import argparse
import csv
import platform

if __name__ == '__main__':

    #1. Create a python file with 3 functions:
    #1a. def print_file_content(file) that can print content of a csv file to the console
    
    
    def print_file_content(f):
        with open(f) as file:  
            reader = csv.reader(file)
            for row in reader:
                print(row)

    #print_file_content('default.csv')

    #1.b def write_list_to_file(output_file, lst) that can take a list or tuple of strings and write each element to a new line in file rewrite the function so that it gets an arbitrary number of strings instead of a list
    my_lst = ['Roman1', 'Modern1', 'Country1', 'Year1', 'Length1']
    def write_list_to_file(output_file, lst):
        if platform.system() == 'Windows':
            newline=''
        else:
            newline=None  
        with open(output_file, 'w', newline=newline) as output_file:
            output_writer = csv.writer(output_file)
            output_writer.writerow(lst)
            output_writer.writerow(['2015', '1', '0', '5104', '2,3'])
            output_writer.writerow(['2015', '1', '0', '5106', '1'])
            output_writer.writerow(['2015', '1', '0', '5110', '1'])     

    #write_list_to_file('default.csv',my_lst)                

    #1.c def read_csv(input_file) that take a csv file and read each row into a list. Print the list.
    def read_csv(input_file):
        with open(input_file) as file:  
            reader = csv.reader(file)
            new_lst = []
            for row in reader:
                new_lst.append(row)
            print(new_lst)    
    #read_csv('default.csv')        

    