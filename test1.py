


#create and call a function that prints your name
#execute script


def print_name():
    print("Mike Mckitrick")



def list1():
    print("working with lists (arrays)")

    names = ['John','Juan']
    #add values to the list
    names.append("Carlos")
    names.append("Charles")

    #get the values
    print(names[0])
    print(names[3])

    print(names)

    #for loop
    for x in names:
        print(x)

print_name()


def list2():
    print("-" * 30)

    # 1 - print the sum of all numbers
    nums=[123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]
    
    total= 0
    for n in nums:
        total += n

    print(total)

    # 2 - print numbers lower than 50
    # 2b - count how many number are lower than 50
    count = 0
    for num in nums:
       if(num < 50):
           print(num)
           count += 1


    print(f"There are: {count} nums lower than 50")

    # 3 - find the smallest number in the list
    # varible that starts with any number from the list(first)
    #for
    #compare if the num is lower than the smallest number,

    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    print(f"the smallest number in the list is: {smallest}")

def dict1():
    print("Dictionary tests 1 --------")

    me = {
        "name": "Mike",
        "last": "Mckitrick",
        "age": "37",
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city":"Springfield"
        }
    }
    print(me["name"])

    print(me["name"] + " " + me["last"])



    me["age"] = 99
    me["email"]= "mr.mckitrick.mm@gmail.com"



    print(me)

    address=me["address"]
    print(f"{address['number']} {address['street']} {address['city']}")

    

list1()
list2()
dict1()