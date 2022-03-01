#Create a Python module, which consists of a class TextContainer. The class must have a constructor 
#which allow objects to be initialized with a text ala: tc = TextContainer(my_text). 
#The class must implement the following methods for computing statistics on texts.
from cgitb import text
from itertools import count
import string


class TextContainer():
 
    def __init__(self,my_text,tc):
        my_text = "jeg er 1 bjørn!"  
        tc = TextContainer(my_text)
        

    def count_words(self,tc):
        result = len(self.tc.split())
        print(result) 

    def count_chars(self,tc):
        result = len(self.text)
        print(result)

    def count_ascii(self,tc):
        ascii_string = string.ascii_letters
        ascii_count = sum(c in ascii_string for c in self.text)
        print(ascii_count)


    def contains_punctuation(self,tc):
        strings = string.punctuation

        for i in self.text:
            if i in strings:
                self.text = self.text.replace(i,"")
        print(self.text)
         
    


    count_words(tc) 
#tc.count_chars(text)
#tc.count_ascii(text)
#tc.contains_punctuation(text)


