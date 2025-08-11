#palindrome
def palindrome(string):
    str=string[::-1]
    if string==ticket:
        print("Lucky Ticket")
    else:
        print("Not Ticket")

ticket=input("enter ticket=")
palindrome(ticket)

#A wizard is teaching you a math spell to calculate the *magic sum* of square numbers.
# Given a number n, you must find the sum of the squares of all numbers from 1 to n.
# For example, if n = 3, the result is 1² + 2² + 3² = 14.

num=int(input("enter a number:"))
sum_of_squares=0
for i in range(1,num+1):
    sum_of_squares+=i**2
print(sum_of_squares)

#Write a program to display all perfect square numbers between 1 and 500 so players can see which numbers will win.
limit=500
i=1
while i*i<=limit:
       print(i*i)
       i+=1

#Given a number n, print the cube of every number from 1 to n so the player knows the sizes of cubes they can collect.
num1=int(input("enter a number:"))
for i in range(1,num1+1):
    cube=i**3
    print(cube)