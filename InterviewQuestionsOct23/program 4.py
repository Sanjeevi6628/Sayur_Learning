"""
4. Encode the user input using the following alg, using the encode Key (a number)

For each word in the odd position, move each letter in the word by the number of positions mentioned in the key.
For words in the even position, reverse the word and then do the same as the odd position

Eg - Key 2, Input sentence "I am the King"
Output K oc vjg ipkM
"""

word_list = input("Enter the Sentence Here: ").split(" ")


while True:
    try:
        key = int(input("Key : "))
        break
    except:
        print("Please Check your Input !")
        continue

lower_alpha = 'abcdefghijklmnopqrstuvwxyz'*key
upper_alpha = lower_alpha.upper()

words = []
for word in word_list:
    if ((word_list.index(word)) + 1) % 2 == 0:
        word = word[::-1]

    str_ = ""
    for ch in word:
        if ch in lower_alpha:
            str_ += lower_alpha[(lower_alpha.index(ch)) + key]
        elif ch in upper_alpha:
            str_ += upper_alpha[(upper_alpha.index(ch)) + key]
        else:
            str_ += ch
    words.append(str_)


for i in words:
    print(i, end=" ")

"""
Output 1:
Enter the Sentence Here: I am the King
Key : 2
K oc vjg ipkM 
Process finished with exit code 0

Output 2:
Enter the Sentence Here: I am the King of My World
Key : 15
X bp iwt vcxZ du nB Ldgas 
Process finished with exit code 0
"""
