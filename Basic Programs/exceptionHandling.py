'''
while True:
    try:
        n=int(input("Enter an integer"))
        m=int(input("Enter an integer"))
        z=n/m
        break

    except Exception as e:
        print("Not an integer , please again 123")
        print(e)
    except ValueError:
        print("Not an integer !! please again 456")
    finally:
        print("You successfully entered an integer!!")

'''

try:
    klu1=open("file.txt","w+")
    try:
        klu1.write("Thia is PFSD Class")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    klu1.close()