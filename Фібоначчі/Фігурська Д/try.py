

def fib(step, starters):
    if step==0:
        return None # рекомендує return NONE

    elif step>0:
        starters.append(starters[-2]+starters[-1])
        step-=1

        return fib(step, starters)



with open("starter. txt", "r") as file1:
    step=int(file1.readline().strip())
    starters= [int(x) for x in file1.readlines()]
    print(starters)
    print(step)

    result = fib(step, starters)

    with open("result.txt", "w") as file2:
        file2.write('Result: ')
        file2.write(' '.join([str(x) for x in starters]))




with open("limit.txt", "r") as file1:
    limit=int(file1.readline().strip())

fibo= [0,1]
def withlimits(limit, fibo):
    next = fibo[-1]+fibo[-2]
    if next>=limit:
        return fibo
    fibo.append(next)
    return withlimits(limit, fibo)


fibo = withlimits(limit, fibo)

with open("limitresult.txt", "w") as file2:
    file2.write("Result: ")
    file2.write(" ".join([str(x) for x in fibo]))