from ast import Index
import numpy as np
import pandas as pd

if __name__ == '__main__':


    data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])
    #2a
    our_data = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
    Index(['Row1', 'Row2', 'Row3'], dtype='object')
    Index(['Col1', 'Col2', 'col3'], dtype='object')
    #print(our_data['Col2'])

    #2b
    third_row = our_data.iloc[0:3,2]
    #print(third_row)
    
    #2c
    third_second = our_data.iloc[2,1]
    print(third_second)

