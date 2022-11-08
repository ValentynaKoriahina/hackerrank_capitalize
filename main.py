import re

def solve(s):
    
    splited_s = re.split(r' ', s)
    result = list(map(lambda x: x.capitalize(), splited_s))
    return ' '.join(result)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
