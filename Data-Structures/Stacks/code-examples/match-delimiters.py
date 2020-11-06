# Importing the Stack class we use it to check if the 
# delimiters of a math expression is balanced


from Stack import Stack


def is_matched(exp):
    """
    Return True if all the delimiters are
    properly matched; False otherwise
    """

    lefty = '({['
    righty = ')}]'
    S = Stack()

    for c in exp:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


# Tests

tests = ['[(5+x)-(y+z)]', '((()(()){([()])}))', ')(()){([()])}', '(']
# >>> Returns True, True, False, False

if __name__ == "__main__":

    res = []

    for i in tests:
        res.append(is_matched(i))

    ans = 'correct' if res == [True, True, False, False] else 'Incorrect'
    print('-'*20)
    print('Correct results are: True, True, False, False')
    print('Your results: {}'.format(res))
    print('\n')
    print('Your results are {}.'.format(ans))
    print('-'*20)




