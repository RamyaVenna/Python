#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

previous_num = 0

for i in range(1,11):
    i_sum=previous_num+i
    print("Current number", i, "previous number", previous_num, "Sum:", i_sum)
    previous_num=i
