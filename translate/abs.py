def find_abs_pair(eq):
    l = len(eq)
    find = '+-*/^'
    findopen = '([{'
    stack = []
    head = []
    tail = []
    for i in range(len(eq)):
        if eq[i] == '|':
            stack.append(i)
    if not stack:
        return eq
    cnt = 0
    calib = 0
    tocnt = len(stack) // 2
    print(stack, tocnt)
    endfind = False
    for i in stack:
        if endfind:
            tail.append(i)
            continue
        if cnt == 0:
            head.append(i)
            cnt += 1
            if cnt == tocnt:
                endfind = True
            continue
        if i == l-1:
            tail.append(i)
            continue
        if eq[i-1] in findopen or eq[i-1] in find:
            head.append(i)
            cnt += 1
        # elif eq[i+1] in findclose or eq[i+1] in find:
        #     tail.append(i)
        # else:
        #     tail.append(i)
        if cnt == tocnt:
            endfind = True
    # print(head, tail)
    for i in head:
        eq = eq[:i+calib]+'abs('+eq[i+calib+1:]
        calib += 3
    # print(eq)
    for i in tail:
        if i == l-1:
            eq = eq[:i+calib]+')'
        else:
            eq = eq[:i+calib]+')'+eq[i+calib+1:]
        # print(eq)
    # print(eq)
    if not endfind:
        eq = find_abs_pair(eq)
    return eq

# print(find_abs_pair(input()))
