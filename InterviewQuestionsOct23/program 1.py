"""
1. Write a program for the following.
start with the input number n.
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the resulting number until the answer is 1.

Eg: input is 8
output 8, 4,2, 1

input is 9
output 9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1
Get two numbers as input. Print the number that has less number of steps to reach 1.
"""

print("1 - For printing numbers in the collatz conjecture\n2- For printing the numbers which have minimum number of \
iterations over the Collatz Conjecture Sequence")
mode = input(">> ")


def collatz_conjecture(n, mode_=1):
    list_ = []
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n //= 2
            list_.append(n)
        else:
            n = (3*n) + 1
            list_.append(n)
    no_of_iterations = len(list_)
    if mode_ == 1:
        return list_
    elif mode_ == 2:
        return no_of_iterations


if mode == "1":
    try:
        num = int(input("Enter the number here : "))
        print(num, end=" ")
        for i in collatz_conjecture(num):
            print(i, end=" ")
    except Exception as e:
        print(f"Error Message : {e}")

elif mode == "2":
    try:
        starting_number = int(input("Enter the Starting Number: "))
        ending_number = int(input("Enter the Ending Number: ")) + 1
        iterations = {}
        for i in range(starting_number, ending_number):
            iterations[i] = collatz_conjecture(i, 2)

        print("The Numbers with the greatest number of iterations over Collatz Conjecture is/are", end=" ")
        smallest_number_iterations = min(list(iterations[x] for x in iterations))
        for i in iterations:
            if iterations[i] == smallest_number_iterations:
                print(i, end=", ")
        print(f" with {smallest_number_iterations} Iteration(s)")
    except:
        print("Sorry! Unable to Process your Request")


else:
    print("Sorry ! Unable to Understand\nExiting the Code...")

"""
Output 1:
1 - For printing numbers in the collatz conjecture
2- For printing the numbers which have minimum number of iterations over the Collatz Conjecture Sequence
>> 1
Enter the number here : 945
945 2836 1418 709 2128 1064 532 266 133 400 200 100 50 25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

Process finished with exit code 0


Output 2:
1 - For printing numbers in the collatz conjecture
2- For printing the numbers which have minimum number of iterations over the Collatz Conjecture Sequence
>> 2
Enter the Starting Number: 236
Enter the Ending Number: 786
The Numbers with the greatest number of iterations over Collatz Conjecture is/are 256 , with 8 Iteration(s)

Process finished with exit code 0
"""