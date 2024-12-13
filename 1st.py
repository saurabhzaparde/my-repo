#Python Program to check if no. exists in fibonacci series or not.


'''
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
#Python Program to check if no. exists in fibonacci series or not.

num = int(input('Enter No U want to check.:-'))
fibo_series = [0,1]
i = -1
temp = 0
while temp < num+1:
    i+=1
    temp = fibo_series[i]+fibo_series[i+1]
    if temp > num+1:
        break
    fibo_series.append(temp)

if num in fibo_series:
    print('Enter No.:-%d is from fibonacci series.' % num)
else:
    print('Enter No.:-%d is Not from fibonacci series.' % num)
    
---------------------------------------------------------------------------------------------------------
#Python Program to get fibonacci series upto entered no.


fibo_series = [0,1]
num = int(input('Enter No upto U want series.:-'))
i = -1
temp = 0
while temp < num:
    i+=1
    temp = fibo_series[i]+fibo_series[i+1]
    if temp > num:
        break
    fibo_series.append(temp)

print('Fibonacci Series of n Numbers.:-',fibo_series)

---------------------------------------------------------------------------------------------------------
#Python Program to get fibonacci series of n numbers

---approach_1

fibo_series = [0,1]
num = int(input('Enter How Many fibonacci No.:-'))
for i in range(num-2):
    temp = fibo_series[i]+fibo_series[i+1]
    fibo_series.append(temp)

print('Fibonacci Series of n Numbers.:-',fibo_series)

---approach_2

lst=[]
i, j = 0, 1
num = int(input('Enter the no.:-'))
for _ in range(num):
    lst.append(i)
    i ,j = j ,i+j
        
print('Fibonacci Series of n Numbers.:-',lst)

---------------------------------------------------------------------------------------------------------
#Python Program Database Connectivity (python database connectivity)pdbc.

from pymysql import *

try:
    cnct = connect(user='root',password='sql_me',host='127.0.0.1',database='sample')
    csr = cnct.cursor()
    print(cnct)

except Exception :
    print(Exception,"???")
---------------------------------------------------------------------------------------------------------
#Python Program Database Connectivity (python database connectivity)pdbc.

from pymysql import *

#passing connection parameters to connect function of pymysql class
cnct = connect(user='root', password='sql_me',host='127.0.0.1',database='sample')

csr = cnct.cursor()                 #creating the cursor object to use its function

print(cnct)                         #to check if got the connection or not if its nono then connect failed 

csr.execute('select *from employee')#to execute sql query using curser object

rows = csr.fetchall()               #to read actual data from sql and storing it in sql

print('id name dept_id dept sal')
for i in rows:
    print(i)                        #to iterate the tuple we got as result
    
csr.close()                         #closing the curser object
cnct.close()                        #closing th connection object
---------------------------------05/12/2024------------------------------------------------------------------------
#Python Program to sorting in 3D Array 

from numpy import*

arr1 = array([[[3,5,6],[9,6,4]],
              [[5,8,9],[1,2,0]],
              [[5,2,8],[1,4,3]]])

print("3D Array before sorting.")
print(arr1)

for i in range(1,3):
    arr1[::,i-1:i:,::] = sort(arr1[::,i-1:i:,::])
    
print("3D Array after sorting rows and columns in ascending order.")
print(arr1)
---------------------------------------------------------------------------------------------------------
#Take birth date of a person and tell on which day of week was he born.
from datetime import *

user_input = input('Enter the Birth date(dd-mm-yyyy hh-mm-ss).:-').split('-')

d,mon,y,h,m,s = [int(i) for i in user_input]

g_date = datetime(y,m,d,h,m,s)

duration = timedelta(weeks,days,hours,mins,sec)

print(duration)
---------------------------------------------------------------------------------------------------------
#Take birth date of a person and tell on which day of week was he born.
from datetime import *

user_input = input('Enter the Birth date(dd/mm/yyyy).:-').split('/')

d,m,y = [int(i) for i in user_input]

b_date = date(y,m,d)

day = b_date.strftime('Your Were born on %A')
print(day)

---------------------------------------------------------------------------------------------------------

#find out epoch it means starting point of current year 1 midnight till now (01/01/2024 00:00)

from time import*


ep = time()
print(ep)


dt = ctime(ep)
print(dt)

n=datetime.datetime.today()
m=datetime.datetime.now()
print(n)
print(m)
---------------------------------------------------------------------------------------------------------
#Write list comprension to get 1st letter of each String in list.

lst1 = ['Delhi','Mumbai','Kolkata','Jaisalmer']

lst3 = [i[0] for i in lst1 ]

print('1st List.:-',lst1)
print('List of 1st letter of elements.:-',lst3)

---------------------------------------------------------------------------------------------------------

#Write list comprension to add corresponding elements in two list and store in another list

lst1 = [10,20,-5,0,44,99]

lst2 = [10,44,5,11,22,0]

lst3 = []

lst3 = [int(i) for i in lst1 for j in lst2 if i == j]

print('1st List.:-',lst1)
print('2nd List.:-',lst2)
print('List of Common elements.:-',lst3)

---------------------------------------------------------------------------------------------------------

#Write list comprension to add corresponding elements in two list and store in another list

lst0 = [int(i) for i in range(1,10+1)]

lst1 = [int(i) for i in range(11,20+1)]

if len(lst0) == len(lst1):
    lst2=[lst0[i]+lst1[i] for i in range(0,len(lst0),1)]
    
elif len(lst0) > len(lst1):
    for i in range(len(lst1),len(lst0)):
        lst1.append(0)
    lst2=[lst0[i]+lst1[i] for i in range(0,len(lst0),1)]
    
elif len(lst0) < len(lst1):
    for i in range(len(lst0),len(lst1)):
            lst0.append(0)
    lst2=[lst0[i]+lst1[i] for i in range(0,len(lst0),1)]
    
print('1st List .:-',lst0)
print('2nd List .:-',lst1)
print('Addition of list.:-',lst2)
---------------------------------------------------------------------------------------------------------
#Write list comprension to find the squares of no. from 1 to 10.

lst = [int(i) for i in range(10+1)]
print(lst)
lst = [i*i for i in lst]   # List comprension
print(lst)

#Write list comprension to get even no. upto to 10

lst0 = [int(i) for i in range(10+1)]

lst1 = [int(i) for i in range(2,10+1,2)]

lst2 = [int(i) for i in range(10+1) if i%2 == 0]

print(lst0,lst1,lst2)
-----------------------------------04/12/2024------------------------------------------------------------
#Accept a matrix from keyboard and sort its elements into descending order on
#rows and columns separately.Display the sorted matrices.

from numpy import array
from array_creation import*

print('Enter Array Size.')
num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))
arr1 = get_2d_array(num1,num2)

arr1 = sort(arr1)
arr1 = arr1.flatten()
arr1 = arr1[arr1.size-1//2::-1]
arr1 = arr1.reshape(num1,num2)

print("Matrix after sorting rows and columns in descending order:")
print(arr1)

-------approach_2

from numpy import array
from array_creation import*

print('Enter Array Size.')
num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))
arr1 = get_2d_array(num1,num2)

# Sorting the rows in descending order
for i in range(arr1.shape[0]):
    arr1[i] = sorted(arr1[i], reverse=True)

# Sorting the columns in descending order
for j in range(arr1.shape[1]):
    arr1[:, j] = sorted(arr1[:, j], reverse=True)

# Print the sorted matrix
print("Matrix after sorting rows and columns in descending order:")
print(arr1)
--------------------------------------------------------------------------------------------------------
#Python Program to do Addition of Array

from numpy import* 
from array_creation import*

print('Enter 1st Array Size.')
num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))
arr1 = get_2d_array(num1,num2)

print('Enter 2nd Array Size.')
num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))
arr2 = get_2d_array(num1,num2)

arr3 = zeros((num1,num2),dtype=int)

for i in range(2):
    for j in range(2):
        arr3[i][j] = arr1[i][j]+arr2[i][j]
        if i>j:
            print()
        print(arr3[i][j],end=' ')

-----------------------------------Assignment_5--------------------------------------------------------------------
#Python Program to do multiplication of matrix

from numpy import* 
from array_creation import*

num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))

arr1 = get_2d_array(num1,num2)

num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))

arr2 = get_2d_array(num1,num2)

mat1 = matrix(arr1)
mat2 = matrix(arr2)

mul_mat = mat1*mat2

print('1st Matrix')
print(mat1)
print('2nd Matrix')
print(mat2)
print('multiplication of Matrices.')
print(mul_mat)

--------------------------------------------------------------------------------------------------------
#Python Program to do addition of matrix

from numpy import* 
from array_creation import*

num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))

arr1 = get_2d_array(num1,num2)

num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))

arr2 = get_2d_array(num1,num2)

mat1 = matrix(arr1)
mat2 = matrix(arr2)

add_mat = mat1+mat2

print('1st Matrix')
print(mat1)
print('2nd Matrix')
print(mat2)
print('addition of Matrices.')
print(add_mat)

----------------------------------------------------------------------------------------------------
#Python Program to do transpose of matrix

from numpy import* 

def get_2d_array(num1,num2):

    #to create array of given size filled with zeros
    arr = zeros((num1,num2),dtype=int)

    #to get array element
    print('Enter array elements row by row(seperated by single space).')

    for i in range(num1):
        arr[i] = array([input().split()])

    #to print the array taken from user
    return arr
    
def get_1d_array(num):
    #to create array of given size filled with zeros
    arr = zeros(num,dtype=int)
    print('Enter array elements in a row(seperated by single space).')
    user_input = input().split()
    
    for i in range(num):
        arr[i] = int(user_input[i])

    #to print the array taken from user
    return arr

num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))

arr = get_2d_array(num1,num2)

mat = matrix(arr)

trans_mat = mat.transpose()

print('1st Matrix.')
print(mat)
print('Transpose of Matrix.')
print(trans_mat)

----------------------------------------------------------------------------------------------------
#Python Program  to take 2d array from user

from numpy import* 

num1=int(input('Enter no. of Rows.:-'))
num2=int(input('Enter no. of Columns.:-'))

#to create array of given size filled with zeros
arr = zeros((num1,num2),dtype=int)

#to get array element
print('Enter array elements row by row(seperated by single space).')

for i in range(num1):
    arr[i] = array([input().split()])

#to print the array taken from user
print(arr)
----------------------------------------------------------------------------------------------------
#Python program to get 1d,2d,3d Array

arr_1d = array([0,1,2,3,4,5,6,7,8,9])
arr_2d = array([[0,1,2,3,4],[5,6,7,8,9]])
arr_3d = array([[[0,1]],[[2,3]],[[4,5]],[[6,7]]])
new_lst1 = []
new_lst2 = []
new_lst3 = []

print('1D.:-',arr_1d,sep='\n')
print('2D.:-',arr_2d,sep='\n')
print('3D.:-',arr_3d,sep='\n')

for i in arr_1d:
    if i%2 == 0 and i != 0:
        new_lst1.append(arr_1d[i])
    elif i%2 != 0:
        new_lst2.append(arr_1d[i])
    else: new_lst3.append(arr_1d[i])

even_arr = array(new_lst1)
odd_arr = array(new_lst2)
neut_arr = array(new_lst3)

print(neut_arr)
print(odd_arr)
print(even_arr)


---------------------------------------------------------------------------------------------------------
#Python Program to get 1D array from user

from array_creation import*
from numpy import*

num=int(input('Enter Size of array.:-'))
arr = get_1d_array(num)

print(arr)

-----------------------------------03/12/2024-----------------------------------------------------------------
#Python Program  to take 1D array

import numpy as np 

arr1=np.array([66,58,36,-65,45])
x=np.array(sorted(arr1))
print('1D Int Array orignal,orignal_reversed,sorted ,reversed_of_sorted=',arr1,arr1[::-1],x,x[::-1],sep='\n')
#simple 1D Int Array orignal,orignal_reversed,sorted ,reversed_of_sorted.
z=arr1

----------------------------------------------------------------------------------------------------
#Python Program  to take 1D array

import numpy as np 

arr1=np.array([66,58,36,65,45])
arr2=np.array(['saurabh','akhil','hritik','uddhav'])
arr3=np.arange(0,10,1)
arr4=np.linspace(0,10,5)
arr5=np.logspace(0,10,5)
arr6=np.zeros(5)
arr7=np.ones(10)

print('1D Int Array=',arr1) #simple 1D Int Array creation.
print('1D str Array=',arr2) #simple 1D String Array creation.
print('1D range Array=',arr3) #simple 1D Int Array in the Given range excluding last_limit creation.
print('1D LineSpace Array=',arr4) #simple 1D Array by dividing the line into equal parts.
print('1D LogSpace Array=',arr5) #simple 1D Arrayby dividing the line into equal logarithmic parts.
print('1D Zeros Array=',arr6) #simple 1D Array of Zeros only.
print('1D Ones Array=',arr7) #simple 1D Array of Ones only.

----------------------------------02/12/2024--------------------------------------------------------
#Write a lambda that returns only negative numbers from a tuple.

from functools import*

mytpl=(-5,-4,-3,-2,-1,0,1,2,3,4,5)

res=filter(lambda i : i<0, mytpl)

print(mytpl)
print('Negative Elements From Tuple.')
for i in res:print(i,end=' ')

----------------------------------------------------------------------------------------------------
#Write a Lambda to Find Cumulitive Sum of a List.

from functools import*

mylst=[1,2,3,4,5]

res=reduce(lambda i,j: i+j, mylst)

print(mylst)
print('Cumulitive Sum of List=',res)

-------------------------------Assignment_4-----------------------------------------------------------

#Write a lambda to find square value of no.

sqrt=lambda num: num*num

res=sqrt(4)
print(res)

#Write a lambda to find sum of two no.

sum_no=lambda num1,num2: num1+num2

res=sum_no(5,6)
print(res)

#Write a lambda functions to (filter)filteration ,(map)modifiy sequence and (reduce).

from functools import*

mylst=[1,0,2,3,52,7,36]

res=filter(lambda i:i%2 == 0,mylst)

for i in res:
    print(i)
#-----------------------------
mylst=[1,0,2,3,52,7,36]

res=map(lambda i:i+2,mylst)

for i in res:
    print(i)
#-----------------------------
mylst=[1,2,3,4,5]

res=reduce(lambda i,j: i*j, mylst)

print(mylst)
print('Cumulitive multiplication of List=',res)


------------------------------------------------------------------------------------------

#Ways to import module in python

import arith
import arith.py
from arith import*
from arith import add_no,sub_no

add_no(10,20)
result=sub_no(10,20)
print('Subtraction=',result)

------------------------------------------------------------------------------------------
#Python function to Create new range_function.

def new_range(starting_limit,ending_limit,step=1):
    result=[]
    if starting_limit > ending_limit:
       while ending_limit < starting_limit:
        result.append(starting_limit)
        starting_limit+=step
        
    else:
        while starting_limit < ending_limit:
            result.append(starting_limit)
            starting_limit+=step
            
    return result

lst=new_range(10,20)
print(lst)

--------------------------01/12/2024------------------------------------------------------

#Python function that accepts a string and returns
#the number of chars in the string.

def char_count(string):
    count=0
    for i in range(0,len(string),1):
        count+=1
    result=count
    return result

string=input('Enter The String.:-')
res1=char_count(string)   #Function call
print('Character Count of',string,'.:-',res1)

------------------------------------------------------------------------------------------
#Python function to calculate factorial value of a
#given number without using recursion

--approach_1

def fact_recur(num):        
    if num == 0: 
        result=1 
    else: 
        result=num*fact_recur(num-1)  # Function Calling Itself fact_recur() is calling itself 
    return result 
 
num = int(input('Enter No.:-'))
res = fact_recur(num)
print('Factorial of %d! is.:-%d' % (num,res))

--approach_2

def factorial(num):
    result=1
    if num == 0:
        result=1
    for i in range(1,num,1):
        result=result*i
    return result

num=int(input('Enter The No.:-'))
res1=factorial(num)   #Function call
print('Factorial of %d! No.:-%d' % (num,res1))

--------------------------------------------------------------------------------

#Python Function to return yearly salary by
#taking monthly salary And provident fund Based on yearly salary.

def annual_sal(monthly_salary):
    result=monthly_salary*12
    return result

def provident_fund(annual_salary):
    result=annual_salary*0.125
    return result

monthly_salary=float(input('Enter Monthly Salary.:-'))
res1=annual_sal(monthly_salary)   #Function call
res2=provident_fund(res1)
print('Annual Salary.:-',res1)
print('Provident Fund.:-',res2)

-------------------------Assignment_3-------------------------------------------------------

#Python Function variable length args


def fact(num):
    if num == 0:
        res=1
    else:
        res=num*fact(num-1)
    return res

factorial=fact(4)
print('Factorial.:-',factorial)

#Python Function variable length args

def add_all(n,*x): # *->(Symbol represent variable length args)
    total= n+sum(x)
    print(total)
     
add_all(0,1,2,0,3,4,5,6,7,8,9)#Function Call

#Python Function default args

def grocery(item,price=45.3):
    print('Price= Rs%.2f' % price)
    print('item= %s' % item)
     
grocery('Salt')#Function Call
grocery('Salt',63.2)#Function Call(if we give value then it won't take default value)

#Python Function keyword args

def join(s1,s2):
    st=s1+s2
    print(st)
    
join(s1='Bl',s2='ues') #Function Call(changing position won't affect result)


#Python Function position args

def join(s1,s2):
    st=s1+s2
    print(st)
    
join('Bl','ues') #Function Call(changing position will affect result)

---------------------------30/11/2024-----------------------------------------------------

#Python Function to return sqrt values from 1 to 10

def sqrt_no():
    result=[]
    for i in range(1,10+1,1):
        res=i**(1/2)
        result.append(res)
    return result


res=sqrt_no()        #Function call
print('Result(Square Root of 1 to 10).')
for i in range(0,len(res),1):
    print('Square Root of ',1+i,'=%.2f' % res[i])
--------------------------------------------------------------------------------

#Python Function to return monthly salary by
#taking yearly salary And TDS Based on monthly salary.

def month_sal_tds(num):
    monthly_salary=num/12
    tds=monthly_salary*0.1
    result={'monthly_salary':monthly_salary,'(Tax Deduction)TDS':tds}
    return result


num=float(input('Enter Yearly Salary.:-'))
res=month_sal_tds(num)        #Function call
print('Result.:-',end='')

for i,j in res.items():
    print(i,'=%.2d'% j,end=' ')
--------------------------------------------------------------------------------

#Python Function to find Arithmatic of numbers.

def arithmatic_operation(num1,num2):    
    res1=num1+num2
    res2=num1-num2
    res3=num1*num2
    res4=num1//num2
    result={'Sum':res1,'Subtraction':res2,'Multiplication':res3,'Division':res4}
    return result


num1=int(input('Enter 1st No.:-'))
num2=int(input('Enter 2nd No.:-'))
res=arithmatic_operation(num1,num2)        #Function call
print('Result.:-',end='')

for i in res.items():
    print(i)

--------------------------------------------------------------------------------

#Python Function to find cube & square of number.

def cube_square_no(num):    
    res1=num*num*num # num**3 Slower Then num*num*num
    res2=num*num
    return res1,res2


num=int(input('Enter No.:-'))
res=cube_square_no(num)        #Function call
print('Result(Cube of no.).:-',res[0])
print('Result(Square of no.).:-',res[1])
--------------------------------------------------------------------------------

#Python Function to find cube of number.

def cube_no(num):    
    res=num*num*num # num**3 Slower Then num*num*num
    return res


num=int(input('Enter No.:-'))
res=cube_no(num)        #Function call
print('Result(Cube of no.).:-',res)
--------------------------------------------------------------------------------

#Python Function to find two numbers.

def add_two_no(num1,num2):    
    res=num1+num2
    print('Result.:-',res)
    return res

#call the function inside the class
class tempo:
    num1=float(input('Enter 1st No.:-'))
    num2=float(input('Enter 2st No.:-'))
    res=add_two_no(num1,num2)
    print('Result.:-',res)

#Python Function to find two numbers.

def add_two_no(num1,num2):    
    res=num1+num2
    print('Result.:-',res)

#call the function
    num1=float(input('Enter 1st No.:-'))
    num2=float(input('Enter 2st No.:-'))
    add_two_no(num1,num2)
---------------------------29/11/2024---------------------------------------------------------

#Python program to generate prime number series.

--approach 1

num=int(input('Enter The No.:-'))
print('Prime Number Series.:-',end='')
for i in range(2,num+1,1):
    for j in range(2,i//2,1):
        if(i%j == 0):
            break
    else:
        if (i%2 != 0 or i == 2):
            print(i,end=' ')
print(end='.')

--approach 1

num=int(input('Enter The No.:-'))
print('Prime Number Series.:-',end='')
lst=[]
count=0
i=2
while count < num:
    for j in range(2,i//2,1):
        if(i%j == 0):
            break
    else:
        if (i%2 != 0 or i == 2):
            lst.append(i)
            count+=1
    i+=1
print(lst)
-------------------------------------------------------------------------------------

#Python program to check if a given number is prime or not.

--approach 1

num=int(input('Enter The No. Want to Verify:-'))

temp=False
for i in range(2,num//2,1):
    if(num%i == 0):
        temp=True
        break

if temp == False and num != 0:
    print('Entered No. is Prime.')
else:
    print('Entered No. is Not Prime.')

--approach 2

num=int(input('Enter The No. Want to Verify:-'))

for i in range(2,num//2,1):
    if(num%i == 0):
        print('Entered No. is Not Prime.')
        break
else:
    print('Entered No. is Prime.')
    
if num == 0:
    print('Entered No. is Not Prime.')
--------------------------------------------------------------------------------------

#Python program to reverse a list of numbers given without using slicing and reverse() methods.

--approach_1

lst=[10, 20, 5, 4, 33, 22]
print('Original List.:-',lst)
rev=[]
for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])
print('Reverse of List.:-',rev)

--approach_2

lst=[10, 20, 5, 4, 33, 22]
temp=0
print('Original List.:-',lst)
for i in range(0,int(len(lst)/2),1):

    for j in range(len(lst)-1-i,int(len(lst)/2),-1):
        temp=lst[i]
        lst[i]=lst[j]
        lst[j]=temp
        break
print('Reverse of List.:-',lst)

--------------------------------------------------------------------------------------

#Python program to check if a given character is a vowel or consonant.

--approach 1
vef=('a','e','i','o','u','A','E','I','O','U')

new_string=input('Enter Character From Keyboard.:-')
for i in vef:
    if new_string == i:
        print('Given Character is a Vowel.')
        break
else:
    print('Given Character is a Consonant.')

--approach 2

vef=('a','e','i','o','u','A','E','I','O','U')

new_string=input('Enter Character From Keyboard.:-')
if new_string in vef: print('Given Character is a Vowel.')
else: print('Given Character is a Consonant.')

--------------------------Assignment_02--------------------------------------------------------------

#Python program to check if user input is between 100 to 200.
try:   
    num=int(input('Enter the No(100-200).:-'))
    assert 100<num<200 , 'Wrong Input Entered'
    print('Square of Number.:-',num*num)
except Exception and AssertionError as ex:
    print(ex)
-----------------------------------------------------------------------------------------

#Python program to take list of No. count -ve no.
mylst=[0,-1,33,65,75,-6,0,-9,8,-5]
count=0
for i in mylst:
    if i<0:
        count+=1
    else:
        continue #Anything works same here pass/continue/variable-variable
        pass
        count=count
print('Orignal List.:-',mylst)
print('Count of -ve No.:-',count)
---------------------------------------------------------------------

#Python program to check if given no.is in a list or not
lst=[10,20,-44,55,0,21,33]
num=float(input('Which No. You Want to Search.:-'))
b=False

for i in lst:
    if num == i:
        b=True
        
if b == True:
    print('The No. is Found in the List.')
else:
    print('The No. Not Found in the List.')

#Python program to check if given no.is in a list or not
lst=[10,20,-44,55,0,21,33]
num=float(input('Which No. You Want to Search.:-'))

for i in lst:
    if num == i:
        print('The No. is Found in the List.')
        break
else:
    print('The No. Not Found in the List.')
---------------------------------------------------------------------

#Python program to display multiplication table
i=1
j=1
while j<=20:
    while i<=20:
        print(i,'x',j,'=',j*i)
        i+=1
    print('---------------------------------------')
    i=1
    j+=1
----------------------------------------------------------------------

#Python program to display multiplication table
num=int(input('Enter The No.:-'))
i=1
while i<=20:
        print(i,'x',num,'=',num*i)
        print('%d X %d = %d'%(i,num,i*num))
        i+=1
----------------------------------------------------------------------
        
#Python program to extract -ve numbers from a tuple
mytpl=(22,-1,33,65,75,-6,0,-9,8,-5)
lst1=[]
lst2=[]
lst3=[]
for i in mytpl:
    if i<0:
        lst1.append(i)
    elif i>0:
        lst2.append(i)
    else:
        lst3.append(i)
print('Orignal tuple.:-',mytpl)
print()
print('List of -ve Element from tuple.:-',lst1)
print()
print('List of +ve Element from tuple.:-',lst2)
print()
print('List of Not -ve or +ve Element from tuple.:-',lst3)

-------------------------------28/11/2024------------------------------------------------

#Python program to know if a given string is palindrome or not. 
s='malayalam'
rev=s[::-1]

if rev == s: print("Given String is Palindrom")
else: print("Given String is Not Palindrom")

print("Given String.:-",s)
print("Reversed of String.:-",rev)
-------------------------------------------------------------------------------

#Python program to count the number of zeros in a given number.
num=10203

zero_count=str(num).count('0')
print("Given No.:-",num)
print("Number of Zero`s in the No.:-",zero_count)
-------------------------------------------------------------------------------

#Python program to find out how many strings are there in the given list.
lst=[10, 20, 'aaa', 'bbb', 33.5, 'ccc', 88, 'bbb', 25]
string_count=0
for i in lst:
    if type(i)==str:
       string_count+=1
print("The Given List.:-",lst)
print("Number of Strings in The List.-:", string_count)
-------------------------------------------------------------------------------------------------------

#Python program to reverse a list of numbers given

lst=[10, 20, 5, 4, 33, 22]
print('Original List.:-',lst)
lst=lst[::-1]   
print('Reverse List.:-',lst)

#Python program to reverse a list of numbers given without using slicing and reverse() methods.

lst=[10, 20, 5, 4, 33, 22]
temp=0
print('Original List.:-',lst)
for i in range(0,int(len(lst)/2),1):

    for j in range(len(lst)-1-i,int(len(lst)/2),-1):
        temp=lst[i]
        lst[i]=lst[j]
        lst[j]=temp
        break
print('Reverse of List.:-',lst)
------------------------------Assignment_1--------------------------------------------------------------------------

#Python program to display list using while loop

mylst=[int(i) for i in input('Enter List Elements(comma separated).:-').split(',')]
sum = 0
for i in mylst:
    if i%2 == 0 and i != 0:
        sum += i
        print(i) 
print('Sum of Even No.:-',sum)
---------------------------------------------------------------------------------------------------------

#Python program to display even No. from 10 to 20 using while loop

num1=int(input('Enter The Starting Limit No.:-'))
num2=int(input('Enter The Ending Limit No.:-'))
    
while(num1<=num2):     
    print(num1)
    num1+=2
    
-------------------------------------------------------------------------------------------------------- 

#Python program to display No. from 1 to 10 using while loop

num1=int(input('Enter The Starting Limit No.:-'))
num2=int(input('Enter The Ending Limit No.:-'))
    
while(num1<=num2):     
    print(num1)
    num1+=1
--------------------------------------------------------------------------------------------------------    

#Python program to known no. is divisible by another no. or not

while(1==1):
    num1=int(input('Enter The 1st No.:-'))
    num2=int(input('Enter The 2nd No.:-'))
    if num2 == 0:
        print('The Divisor is Zero Answer is INFINITY')
        print('If You Want Valid Answer Enter Divisor Anything Other than Zero')
    else:
        if num1 % num2 == 0:
            print('The 1st No. is Divisible by 2nd.')
            break
        else:
            print('The 1st No. is Not Divisible by 2nd.')
            break
-------------------------------------------------------------------------------------------------------

#Python program to accept day no. and display day of week

while(1==1):
            day=int(input('Enter The Day No.:-'))
            if day == 1:
                print('It`s Sunday')
                break
            elif day == 2:
                print('It`s Munday')
                break
            elif day == 3:
                print('It`s Tuesday')
                break
            elif day == 4:
                print('It`s Wednsday')
                break
            elif day == 5:
                print('It`s Thuesday')
                break
            elif day == 6:
                print('It`s Friday')
                break
            elif day == 7:
                print('It`s Saturday')
                break
            else:
                print('Please Enter Valid day No.')
                print('Try Again There Only 7 DAYS in Week')
--------------------------------------------------------------------------------------------------------

#Python program to check the given no. even or not

num=int(input('Enter The No.:-'))

if num == 0:
    print('Given No. is Zero.',num)
else:
    if num%2==0:
        print('Given No. is Even.',num)
    else:
        print('Given No. is Odd.',num)
--------------------------------------------------------------------------------------------------------

#Python program to check if password is correct or not.
ORG_PASS = 'saura12'
usr_pass = input('Enter the Password.:-')
if ORG_PASS == usr_pass:
    print('Entered Password is Correct.')
else:
    print('Entered Password is Wrong.')
print('Password Verification is Done.')
--------------------------------------------------------------------------------------------------------

#Python program to get group of strings.

lst=[i.strip() for i in input('Enter The Strings.:-').split(',')]
print('Original List=',lst)

lt=lst.sort()
print('Sorted List=',lt)
--------------------------------------------------------------------------------------------------------

#Python program to get and print the date.
d,m,y=[int(i) for i in input('Enter The Date(dd/mm/yyyy).:-').split('/')]

print('Date=%i-%i-%i' %(d,m,y))


#Python program to add three no.

a,b,c=[float(i) for i in input('Enter nos.:-').split(',')]
total=a+b+c
print('Result=%.3f',%total)

a,b,c=float(input('Enter No.:-')),float(input('Enter No.:-')),float(input('Enter No.:-'))
print('Result=',a+b+c)

print('Result=',float(input('Enter No.:-'))+float(input('Enter No.:-'))+float(input('Enter No.:-')))
--------------------------------------------------------------------------------------------------------

#Python program to sum list and average of list.

l=[float(i) for i in input('Enter No.:-').split(',')]
                total +=i
                avg=total/len(lst);
print('total=',total,end='\n','average=',avg)
--------------------------------------------------------------------------------------------------------

#Python program to find output no. to the power.

n=float(input('Enter No.:-'))
p=float(input('Enter Power of No.:'))
result=(n**p)
print('Result=',result)

n,p=[float(i) for i in input('Enter No.:-').split(',')]
result=n**p
print('Result=',result)
-------------------------------27/11/2024-------------------------------------------------------------------------

'''
