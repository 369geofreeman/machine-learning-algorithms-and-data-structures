# Importing the Stack class we use it to check if the
# delimiters of a math expression is balanced


from collections import deque


def is_matched(s):
    """
    Return True if all the delimiters are
    properly matched; False otherwise
    """

    d = {"(": ")", "[": "]", "{": "}"}
    check = '(){}[]'

    stack = deque()

    for bracket in s:
        if bracket in check:
            if bracket in d:
                stack.append(d[bracket])
            else:
                if not stack or bracket != stack.pop():
                    return False

    return True if not stack else False


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
