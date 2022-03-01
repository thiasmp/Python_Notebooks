import argparse
import csv

if __name__ == '__main__':
#2. Add a functionality so that the file can be called from cli with 2 arguments:
    parser = argparse.ArgumentParser(description='A program that reads from one file and writes to another')
    parser.add_argument('path', help='The path to process')
    parser.add_argument('-d','--file file_name', help='The name of the file to store the content in', default='default.csv')

    args = parser.parse_args()
    print('Path:', args.path)
    print('File:', args.file_name)


    #2.a path to csv file
    #2.b an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.