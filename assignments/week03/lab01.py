# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:


age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Tennager")
elif age < 60:
    print("Adult")
elif age >= 60:
    print("Senior")