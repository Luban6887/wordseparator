#functionByLuban

def SepWords(text,the_list_name_where_you_want_to_store_separeted_words):
    sepwords = the_list_name_where_you_want_to_store_separeted_words
    text1 = " "
    text = text+text1 #its cant separet the last word thats why i use it
    cnt = []
    x = 0
    for i in range(0,1):
        
        for i in range(0,len(text)): #detecting the position of " "
            textcnt = text[i]

            if " " in textcnt:
                cnt.append(int(i)) #append the position in cnt[]

        for i in range(0,len(cnt)):
            z = text[x:cnt[i]] #z is separeted words
            x = cnt[i]
            x+=1
            sepwords.append(z) # append z in a list
    #print(sepwords) #print the list of separeted words
