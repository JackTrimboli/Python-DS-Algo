'''
Jack Trimboli
CS435-021
Dr. Itani
Due: July 18th, 2022: 2pm


Input:
- N, a positive number indicating the number of people
- M, a nonnegative number indicating the number of passes
- x, the starting point
- D, a case-insensitive letter indicating token passing direction 
('C' or 'A' for clockwise or anticlockwise, respectively)

Output: A list of numbers written to standard output indicating the order of elimination, 
one number per line, and a message indicating the winner.
'''

from cll import CircularLinkedList
import sys


def josephus(N: int, M: int, x: int, D: str) -> None:
    # Display Args:
    sys.stdout.write("N: " + str(N) + ", M: " + str(M) +
                     ", x: " + str(x) + ", D: " + D + "\n")

    # create our circle
    circle = CircularLinkedList()

    # fill circular with the correct number of people
    for i in range(1, N+1):
        circle.push_back(i)

    # move token to correct starting position
    token = circle.head
    while token.elm != x:
        token = token.nxt

    # Play game in the anticlockwise direction
    if D.upper() == 'A':
        while token.nxt != token and token.prv != token:
            for i in range(M):
                token = token.prv
            sys.stdout.write(str(token.elm) + "\n")
            token = token.prv
            circle.eliminate(token.nxt)
    # Play game in the clockwise direction
    elif D.upper() == 'C':
        while token.nxt != token and token.prv != token:
            for i in range(M):
                token = token.nxt
            sys.stdout.write(str(token.elm) + "\n")
            token = token.nxt
            circle.eliminate(token.prv)
    else:
        sys.stdout.write("invalid character\n")
        return
    # output winner
    sys.stdout.write(str(token.elm) + " Won\n")


# pass command line arguments to function
if(len(sys.argv) < 5):
    print("Not enough arguments passed, please try again")
    exit(0)
josephus(int(sys.argv[1]), int(sys.argv[2]),
         int(sys.argv[3]), str(sys.argv[4]))
