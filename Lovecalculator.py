print("Hello This is love calculator score checking program")
name1=input()
name2=input()
combined_names=name1+name2
lower_names=combined_names.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
first_digit=t+r+u+e

l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit=l+o+v+e

score=int(str(first_digit) + str(second_digit))
if (score<10) or (score>90):
    print(f"Your score is {score},You are good to go together")
elif (score>=40) or (score<=50):
    print(f"Your score is {score},You have a perfect match")
else:
    print(f"Your score is {score}.")