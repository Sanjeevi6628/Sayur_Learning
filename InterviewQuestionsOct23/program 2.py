"""
2. You are writing an essay. You don't want any word to appear very frequently. Write a program that will take your
essay as input (maybe from a file) and print the number of times each unique word appears in your Essay.
"""

file_ = open("file1", "r")

frequency = {}
file = []
for line in file_:
    line_ = []
    for word in line.split():
        line_.append(word)
    file.append(line_)

for line in file:
    formal_variable = None
    for i in range(len(line) - 1):
        if (line[i] == line[i + 1]) and (formal_variable != line[i]):
            print(f"The Word '{line[i]}' appeared again and again in the line :")
            print(" ".join(line))
            formal_variable = line[i]
            print("\n")
        if line[i] not in frequency:
            frequency[line[i]] = 1
        else:
            frequency[line[i]] += 1

maximum = 0
for key, value in frequency.items():
    print(f"The Word '{key}' appeared frequently, that is almost {value} times")
    if maximum < value:
        maximum = value

print("\n")

print("Most Frequently appeared word is/are", end=" ")
for key, value in frequency.items():
    if value == maximum:
        print(f"'{key}'", end=" ")

file_.close()

"""
Output:

The Word 'searching' appeared again and again in the line :
The crow then started searching searching searching for a few pebbles.


The Word 'the' appeared again and again in the line :
He returned to the pot and dropped it in the the pot.


The Word 'Once' appeared frequently, that is almost 1 times
The Word 'Upon' appeared frequently, that is almost 1 times
The Word 'a' appeared frequently, that is almost 11 times
The Word 'Time,' appeared frequently, that is almost 1 times
The Word 'There' appeared frequently, that is almost 1 times
The Word 'was' appeared frequently, that is almost 13 times
The Word 'crow' appeared frequently, that is almost 12 times
The Word 'who' appeared frequently, that is almost 1 times
The Word 'lived' appeared frequently, that is almost 1 times
The Word 'in' appeared frequently, that is almost 10 times
The Word 'forest' appeared frequently, that is almost 1 times
The Word 'close' appeared frequently, that is almost 1 times
The Word 'to' appeared frequently, that is almost 13 times
The Word 'The' appeared frequently, that is almost 9 times
The Word 'travelling' appeared frequently, that is almost 2 times
The Word 'for' appeared frequently, that is almost 6 times
The Word 'long' appeared frequently, that is almost 1 times
The Word 'time' appeared frequently, that is almost 1 times
The Word 'so' appeared frequently, that is almost 1 times
The Word 'he' appeared frequently, that is almost 8 times
The Word 'very' appeared frequently, that is almost 4 times
The Word 'He' appeared frequently, that is almost 8 times
The Word 'looked' appeared frequently, that is almost 1 times
The Word 'around' appeared frequently, that is almost 3 times
The Word 'water' appeared frequently, that is almost 15 times
The Word 'drink,' appeared frequently, that is almost 1 times
The Word 'but' appeared frequently, that is almost 4 times
The Word 'unable' appeared frequently, that is almost 3 times
The Word 'find' appeared frequently, that is almost 1 times
The Word 'any' appeared frequently, that is almost 1 times
The Word 'started' appeared frequently, that is almost 5 times
The Word 'feeling' appeared frequently, that is almost 2 times
The Word 'weak' appeared frequently, that is almost 2 times
The Word 'because' appeared frequently, that is almost 1 times
The Word 'there' appeared frequently, that is almost 2 times
The Word 'no' appeared frequently, that is almost 1 times
The Word 'searching' appeared frequently, that is almost 4 times
The Word 'water.' appeared frequently, that is almost 1 times
The Word 'flew' appeared frequently, that is almost 3 times
The Word 'all' appeared frequently, that is almost 2 times
The Word 'the' appeared frequently, that is almost 37 times
The Word 'jungle' appeared frequently, that is almost 1 times
The Word 'and' appeared frequently, that is almost 14 times
The Word 'nearby' appeared frequently, that is almost 1 times
The Word 'After' appeared frequently, that is almost 3 times
The Word 'town,' appeared frequently, that is almost 1 times
The Word 'saw' appeared frequently, that is almost 3 times
The Word 'house' appeared frequently, that is almost 1 times
The Word 'thought' appeared frequently, that is almost 2 times
The Word 'must' appeared frequently, that is almost 1 times
The Word 'be' appeared frequently, that is almost 2 times
The Word 'reaching' appeared frequently, that is almost 1 times
The Word 'house,' appeared frequently, that is almost 1 times
The Word 'pot' appeared frequently, that is almost 7 times
The Word 'full' appeared frequently, that is almost 1 times
The Word 'of' appeared frequently, that is almost 11 times
The Word 'became' appeared frequently, that is almost 1 times
The Word 'But,' appeared frequently, that is almost 1 times
The Word 'now' appeared frequently, that is almost 1 times
The Word 'problem' appeared frequently, that is almost 1 times
The Word 'that' appeared frequently, that is almost 1 times
The Word 'level' appeared frequently, that is almost 4 times
The Word 'low' appeared frequently, that is almost 1 times
The Word 'drink' appeared frequently, that is almost 5 times
The Word 'from' appeared frequently, that is almost 3 times
The Word 'lot' appeared frequently, that is almost 1 times
The Word 'an' appeared frequently, that is almost 1 times
The Word 'idea' appeared frequently, that is almost 1 times
The Word 'came' appeared frequently, that is almost 2 times
The Word 'across' appeared frequently, that is almost 1 times
The Word 'his' appeared frequently, that is almost 5 times
The Word 'thought,' appeared frequently, that is almost 1 times
The Word '"If' appeared frequently, that is almost 1 times
The Word 'I' appeared frequently, that is almost 2 times
The Word 'throw' appeared frequently, that is almost 1 times
The Word 'some' appeared frequently, that is almost 2 times
The Word 'pebbles' appeared frequently, that is almost 3 times
The Word 'then' appeared frequently, that is almost 3 times
The Word 'present' appeared frequently, that is almost 1 times
The Word 'will' appeared frequently, that is almost 2 times
The Word 'go' appeared frequently, that is almost 1 times
The Word 'up' appeared frequently, that is almost 1 times
The Word 'able' appeared frequently, that is almost 1 times
The Word 'few' appeared frequently, that is almost 1 times
The Word 'lying' appeared frequently, that is almost 1 times
The Word 'on' appeared frequently, that is almost 1 times
The Word 'ground' appeared frequently, that is almost 1 times
The Word 'towards' appeared frequently, that is almost 1 times
The Word 'put' appeared frequently, that is almost 1 times
The Word 'one' appeared frequently, that is almost 5 times
The Word 'returned' appeared frequently, that is almost 1 times
The Word 'dropped' appeared frequently, that is almost 1 times
The Word 'it' appeared frequently, that is almost 1 times
The Word 'Gradually,' appeared frequently, that is almost 1 times
The Word 'by' appeared frequently, that is almost 2 times
The Word 'dropping' appeared frequently, that is almost 2 times
The Word 'pebble' appeared frequently, that is almost 1 times
The Word 'at' appeared frequently, that is almost 1 times
The Word 'time,' appeared frequently, that is almost 1 times
The Word 'rose' appeared frequently, that is almost 1 times
The Word 'little' appeared frequently, that is almost 1 times
The Word 'beak' appeared frequently, that is almost 2 times
The Word 'still' appeared frequently, that is almost 2 times
The Word 'not' appeared frequently, that is almost 1 times
The Word 'capable' appeared frequently, that is almost 1 times
The Word 'drinking' appeared frequently, that is almost 3 times
The Word 'repeated' appeared frequently, that is almost 1 times
The Word 'process' appeared frequently, that is almost 2 times
The Word 'flying' appeared frequently, that is almost 2 times
The Word 'pebbles,' appeared frequently, that is almost 1 times
The Word 'picking' appeared frequently, that is almost 1 times
The Word 'them,' appeared frequently, that is almost 1 times
The Word 'back' appeared frequently, that is almost 1 times
The Word 'them' appeared frequently, that is almost 1 times
The Word 'Then' appeared frequently, that is almost 2 times
The Word 'tried' appeared frequently, that is almost 1 times
The Word 'do' appeared frequently, that is almost 1 times
The Word 'Now,' appeared frequently, that is almost 1 times
The Word 'even' appeared frequently, that is almost 1 times
The Word 'more' appeared frequently, that is almost 1 times
The Word 'thirsty' appeared frequently, that is almost 2 times
The Word 'never' appeared frequently, that is almost 1 times
The Word 'stopped.' appeared frequently, that is almost 1 times
The Word 'doing' appeared frequently, that is almost 1 times
The Word 'same' appeared frequently, that is almost 1 times
The Word 'again' appeared frequently, that is almost 2 times
The Word 'almost' appeared frequently, that is almost 1 times
The Word 'hour' appeared frequently, that is almost 1 times
The Word 'finally' appeared frequently, that is almost 2 times
The Word 'succeeded' appeared frequently, that is almost 1 times
The Word 'had' appeared frequently, that is almost 1 times
The Word 'risen' appeared frequently, that is almost 1 times
The Word 'rim' appeared frequently, that is almost 1 times
The Word 'pot,' appeared frequently, that is almost 1 times
The Word 'which' appeared frequently, that is almost 1 times
The Word 'easily' appeared frequently, that is almost 1 times
The Word 'accessible' appeared frequently, that is almost 1 times
The Word 'much' appeared frequently, that is almost 1 times
The Word 'happy' appeared frequently, that is almost 1 times
The Word 'rapidly' appeared frequently, that is almost 1 times
The Word 'dipped' appeared frequently, that is almost 1 times
The Word 'drank' appeared frequently, that is almost 2 times
The Word 'until' appeared frequently, that is almost 1 times
The Word 'incapable' appeared frequently, that is almost 1 times
The Word 'kind-hearted' appeared frequently, that is almost 2 times
The Word 'also' appeared frequently, that is almost 1 times
The Word 'invited' appeared frequently, that is almost 1 times
The Word 'other' appeared frequently, that is almost 1 times
The Word 'birds' appeared frequently, that is almost 2 times
The Word 'with' appeared frequently, that is almost 1 times
The Word 'Lots' appeared frequently, that is almost 1 times
The Word 'They' appeared frequently, that is almost 1 times
The Word 'thanked' appeared frequently, that is almost 1 times


Most Frequently appeared word is/are 'the' 

Process finished with exit code 0
"""