def fibonaci(steps, array):
    if steps==0:
        return array
    array.append(array[-1]+ array[-2])
    steps-=1
    return fibonaci(steps, array)

with open("file.txt", "r") as file:
   line_one=file.readline()
   steps=file.readline()
array=[]

line_one=line_one.split()
for i in line_one:
    array.append(i)
    array=[float(i) for i in array]
for i in steps:
    steps=float(steps)
with open("result.txt", "w") as file:
        file.write(str(fibonaci(steps, array)))
        file.write("\n")
