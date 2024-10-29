count = 0
dict= {}
while True:
    try:
        saying = input("grocery: ")
        if saying in dict:
            #dict{saying}
            dict.update({saying:count})
        else:
            dict.update({saying:count+1})
            count += 1
    except EOFError:
        break


dict.sorted()
print(dict)

#if saying in list:
#count += 1

#print(f"{count} {list[0]}")