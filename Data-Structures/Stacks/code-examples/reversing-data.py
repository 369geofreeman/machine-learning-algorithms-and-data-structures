# Reversing the data from one text file and writing it to naother

from Stack import Stack


def reverseFile(file1, file2):
    """
    Write contents of a text file in reverse
    order, line by line to a new file
    """
    S = Stack()
    original = open(file1)
    for line in original:
        S.push(line.strip('\n'))
    original.close()

    # Now we push to a new file in reverse order
    output = open(file2, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


reverseFile('file1.txt', 'file2.txt')







