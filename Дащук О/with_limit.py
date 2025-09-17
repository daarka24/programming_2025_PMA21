def fibonaci(array, limit):
    if array[-1] > limit:
        return array[:-1]
    else:
        array.append(array[-1] + array[-2])
        return fibonaci(array, limit)

with open("limit_file.txt", "r") as file:
   line_one=file.readline()
   limit=file.readline()
array=[]
line_one=line_one.split()
for i in line_one:
    array.append(i)
    array=[float(i) for i in array]
for i in limit:
    limit=float(limit)

with open("limit_result.txt", "w") as file:
    file.write(str(fibonaci( array,limit)))
    file.write("\n")
