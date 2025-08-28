def ages():
    for i in range(4):
        age = int(input("Enter age: "))
    if age < 13:
        print("Child")
    elif age < 20:
        print("Tennager")
    elif age < 60:
        print("Adult")
    elif age >= 60:
        print("Senior")

if __name__ == "__main__":
    ages()