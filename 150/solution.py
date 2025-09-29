def solve(tokens: list) -> int:
    s = []
    ops = { "+", "*", "-", "/" }
    for el in tokens:
        if el not in ops:
            s.append(int(el))
        else:
            b = s.pop()
            a = s.pop()
            match el:
                case "+":
                    s.append(a+b)
                case "-":
                    s.append(a-b)
                case "*":
                    s.append(a*b)
                case "/":
                    s.append(int(a/b))
    return s.pop()

print(solve(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

