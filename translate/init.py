from abs import find_abs_pair

def intchk(n):
    try:
        int(n)
        return True
    except:
        return False

def f(x):
    evaluated = x.replace("^", "**")
    for i in range(1, len(evaluated)):
        if evaluated[i] == 'x':
            if intchk(evaluated[i-1]):
                evaluated = evaluated[:i] + "*" + evaluated[i:]
    evaluated = find_abs_pair(evaluated)
    print(evaluated)
    return evaluated