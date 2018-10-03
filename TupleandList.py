def main():
    #truples immutable
    tupels = (15,20,45,75)
    print (tupels)
    print(tupels[0:1])# show slaice system

    #List mutable
    list = [15,20,45,75]
    list.append(25)#insert in final position
    list.insert(2,28)#first one position and scend one value
    print (list[1:3])
    print (list[0])
    print(list)

    #the slaice system works the same in string
    str = "benlaiter djamel"
    print (str[1:5])
if __name__ == '__main__':main()