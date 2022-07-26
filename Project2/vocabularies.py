from traceback import print_tb
from bst import BST
import sys

'''

for each unit:
print the unit name
add each translation of that unit to our bst. make the the value a list. if the key is already in the bst, append to it's value
print the translations
repeat for each unit

'''


def print_unit(vocab, keys):
    for i in keys:
        vals = vocab.get(i)
        if len(vals) > 0:
            vals.sort()
        sys.stdout.write(i + ": ")
        for j in range(len(vals)):
            if j != len(vals) - 1:
                sys.stdout.write(vals[j] + ", ")
            else:
                sys.stdout.write(vals[j] + '\n')


def vocabularies(filename):

    # Open file
    f = open(filename, 'r')
    vocab = BST()

    for i in f.readlines():
        # process each line of the file, skip empty lines
        line = " ".join(i.split())

        if line != "":
            # split translation into two parts
            line = line.split(":")

            # everytime we reach a new unit, print the previous unit followed by the unit title. Clear the tree for the next unit
            if line[0][0] == '%':
                if not vocab.is_empty():
                    print_unit(vocab, vocab.keys())
                    sys.stdout.write('\n')
                print(line[0])
                vocab.clear()
            else:
                # get all of the english words as an array
                english_words = line[1].split(',')
                for word in english_words:
                    stripped_word = word.replace(',', '').strip()
                    # if the key already exists, add to its array
                    if vocab.contains(stripped_word):
                        vocab.get(stripped_word).append(line[0].strip())

                    # otherwise insert a new BST node
                    else:
                        vocab.put(stripped_word, [line[0].strip()])
    if not vocab.is_empty():
        print_unit(vocab, vocab.keys())


# pass command line arguments to function
if(len(sys.argv) < 2):
    print("Not enough arguments passed, please try again")
    exit(0)
vocabularies(str(sys.argv[1]))
