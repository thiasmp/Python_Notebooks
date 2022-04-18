def title_splitter(year1, year2):
    df = data['Title'].where(data['License']=='PG')
    clearnedList = [x for x in df if str(x) != 'nan']
    counter = 0
    for value in clearnedList:
        tmp1 = value.split('(')
        newtmp = [x[:-1] for x in tmp1]
        only_years = newtmp[-1]
        #print(only_years)
        tmp = only_years.split('\n')
        #print(tmp)
        new_list = ([])
        
        for x in range(len(tmp)):
            new_list.append(int(tmp[x])) 
            
        
        
        for x in range(len(new_list)):    
            if year1 <= new_list[x] <= year2:
                counter += 1
                #print(new_list[x])
            else:
                pass
            #print(tmp[x])
        
        
    print(counter)
    percent = (counter/917)*100
    print(percent)
    print (data)
            
        
            
        #print(f"Index : {index}, Value : {value}")


title_splitter(2001, 2015)
#converter("December 16, 2015")
#def pg_procent(year):
    
#pg_procent = data['License'].where(data['Release Date']== converter("2015"))
                                   
#print(pg_procent)