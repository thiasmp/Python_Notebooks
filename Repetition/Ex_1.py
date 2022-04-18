import math
# 1. Create 5 list comprehensions to solve the following 5 problems:
list_of_names = ["Andreas", "Kurt", "Henrik", "Søren", "Mathias", "Kasper", "Hans"] 

#   1. Iterate a list of names to return a list of the names starting with H
def list_names():
    h_names = [e for e in list_of_names if e[0]=='H']
        
    print(h_names)
        
#list_names()
        
#   2. In one line create a list of the numbers 1-100 to the power of 3       
def pwr_3():
    print([x**3 for x in range(101)])
    
#pwr_3()
    
#   3. Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name   
def tuple_hell(lst):
    new_lst = []
    for x in lst:
        new_lst.append((len(x),x))
    
    return new_lst
    
#print(tuple_hell(list_of_names))
        
#   4. Iterate over each character in a string and get only those that are nummeric
def get_numeric():
    str = "1 går g1k jeg mig 45 ture og spiste 8 kager"     
    numeric = [e for e in str if e.isnumeric()]
    print (numeric)
    
#get_numeric()        
 
 
 #   5. Using only a list comprehension wrapped in set() get all possible combinations from throwing 2 dice 
# (hint use 2 for loops in a single list comprehension). Result should look like: [2,3,4,5,6,7,8,...] or a more complex/accurate solution: [(1,1),(1,2)...] in a way that (1,2) is equal to (2,1).
def dice():
    dice_roll = set([(e,x) for e in range(1,7) for x in range(1,7)])
    
    print(sorted(dice_roll))
    
#dice()
    
# 2. Create 2 dictionary comprehensions to solve the following:

#   1. Iterate a list of names and create a dictionary where key is the name and value is the length of the name
def key_val():
    dct = {name: len(name) for name in list_of_names}
    print(dct)

key_val()

    
#   2. Iterate a list of numbers and create a dictionary with {key:value} being {number:squareroot_of_number}
def sqrt():
    number_list = [1,45,8,3,57,9,2345,9]
    dct = {e: math.sqrt(e) for e in number_list}
    print(dct)

#sqrt()        
    