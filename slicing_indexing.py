def match(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word) and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print(lst)
    return ctr
counter=match(['aga', 'sud', '329723', 'aeytyiqgbxqzna', '1424', 'geil'])
print("the amount of some end and start letters are : ",counter)