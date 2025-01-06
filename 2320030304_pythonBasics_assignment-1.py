2320030304 - K.Santhoshini

python basic assignment1

ORIGINAL FILE IS LOCATED  https://colab.research.google.com/drive/18VtlRa2viQDNvSVf37UMqnRastINniYQ#scrollTo=6Ueuj9W2KKSV

#Task1
n=input("Enter Name:")
age=int(input("Enter Age:"))
f=int(input("Enter Favorite Number:"))
print("Hello",n)
c=2024
a=100-age
print("Year to be 100 years old is",c+a)
result=f*2;
print("Double of Favorite Number:",result)

#Task2
num=int(input("Enter a Number:"))
if num%2==0:
  print(num,"is a Even Number")
else:
  print(num,"is a Odd Number")

#Task3
print("For Loop")
for i in range(1,51):
  if i%2==0:
    print(i,end=" ")
print("\n")
print("While Loop")
# While Loop
num=1
while num<=50:
  if num%2==0:
    print(num,end=" ")
  num+=1;

#Task4
food=["Pizza","Chips","Panner","Biryani","Cake"]
print(food)
food_length={}
for f in food:
  food_length[f]=len(f)
  print(food_length)

  #Task5
  def calculate_area(shape,dimension1,dimension2=None):
  if shape.lower()=="circle":
    result=3.14*dimension1
    print(result)
  elif shape.lower()=="rectangle":
    result=dimension1*dimension2
    print(result)
  elif shape.lower()=="triangle":
    result=0.5*dimension1*dimension2
    print(result)
  else:
    print("Invalid Shape")
calculate_area("circle",5)
calculate_area("rectangle",4,7)
calculate_area("triangle",6,8)

#Task6
s=input("Enter a Sentence:")
v=0;
for i in s.lower():
  if i in "aeiou":
    v+=1;
    print("Number of Vowels:",v)
    rs=s[::-1]
    print("Reversed Sentence:",rs)
    us=s.upper()
    print("UpperCse:",us)

#Task7
with open("data.txt","w") as file:
  file.write("Hello,Python\n")
  file.write("Learning File Handling\n")
  file.write("Python is Fun\n")
with open("data.txt","r") as file:
    print(file.read())

#Task8
try:
  num1=int(input("Enter Number 1:"))
  num2=int(input("Enter Number 2:"))
  result=num1/num2
  print("Result:",result)
except ZeroDivisionError:
  print("Cnnot be divided by Zero")

except ValueError:
  print("Invalid Input")    