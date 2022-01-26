#Unit converter

user_name = input("Please tell me your name: ")
greeting = "Hello, " + user_name + ", I'm Converter! Nice to meet you. I'm here to help you convert units of distance, mainly kilometers to miles. Let's get started"

print(user_name)
print(greeting)

km = int(input("Please write the number of kilometers: "))
print("You want to know how many miles are",km,"kilometers. Let's convert this!")

m = km * 0.62
print(km,"kilometers are",m, "miles!")

repeat = user_name + ", do you want to do another conversion?"
print(repeat)

answer = input("What is your answer? Select Yes or No. ")
print(answer)

while answer == "Yes":
        km = int(input("Please write the number of kilometers: "))
        print("You want to know how many miles are", km, "kilometers. Let's convert this!")
        m = km * 0.62
        print(km, "kilometers are", m, "miles!")
        repeat = user_name + ", do you want to do another conversion?"
        print(repeat)
        answer = input("What is your answer? Select Yes or No. ")
        print(answer)
        if answer != "Yes":
            print("Enough for today, bye bye!")
