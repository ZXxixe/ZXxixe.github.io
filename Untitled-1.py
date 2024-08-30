print('hello')
name = input("what is your name ")
print('nice to meet you ' + name)
print("in order to continuo you must be 18+" )
age = input("how old are you ")
if age > str(18):
    print("congrats, you meet the requirement")
elif age < str(18):
    print("sorry but you do NOT mneet the requirement")
