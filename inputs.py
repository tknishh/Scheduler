def selectYear():
    year = ['1st','2nd','3rd','4th']
    y = input('Year: ')
    year.remove(y)

def selectBranch():
    year = ['CSE','ECE','MEC','CE','CIV']
    y = input('Branch: ')
    year.remove(y)

def dividing_batches():
    total_students = int(input('Total students: '))
    total_batches = int(input('Total batches: '))
    a = split(total_students, total_batches)
    groupBatches(a)

def split(x, n):
    a=[]
    if(x < n):
        a.append(-1)
    elif (x % n == 0):
        for i in range(n):
            a.append(x//n)
    else:
        zp = n - (x % n)
        pp = x//n
        for i in range(n):
            if(i>= zp):
                a.append(pp + 1)
            else:
                a.append(pp)
    return a

def groupBatches(a):
    n = int(input('Number of batches together: '))
    comb_batches = len(a)//n
    print('No. of Combined Batches: ',comb_batches)
