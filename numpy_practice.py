#Create a NumPy array containing the marks of 5 students in a test. Print the array, its data type, number of elements, and dimensions.
import numpy as np
students_marks = np.array([89,77,100,69,97])
print(students_marks)
print(students_marks.dtype)
print(students_marks.size)
print(students_marks.ndim)
#----------------------------------------------------------------------------------------------------
#Create an array containing the sales amounts of 8 products. Display the first, third, and last sales values.
sale_amount = np.array([500,680,340,550,120,1000,300,800])
print("first sale value : ",sale_amount[0])
print("third sale value : ",sale_amount[2])
print("last sale value : ",sale_amount[-1])
#----------------------------------------------------------------------------------------------
#Create an array containing temperatures recorded during 7 days. Find the maximum and minimum temperature.
temp = np.array([54,23,40,36,12,50,66])
print("maximum temperature is : ",temp.max())
print("minimum temperature is : ",temp.min())
#------------------------------------------------------------------------------------------------
#Create an array containing expenses for 12 months. Calculate the total yearly expense and average monthly expense.
expenses = np.array([1000,2000,1000,5000,7000,5000,6000,3000,7000,9000,1000,8000])
print("total yearly expense is : ",np.sum(expenses))
print("average monthly expense is : ",np.mean(expenses))
#------------------------------------------------------------------------------------------------
#Create an array containing salaries of 5 employees. Calculate the average salary.
salaries = np.array([30000,25000,60000,40000,15000])
print("average salaries of employees is : ",np.mean(salaries))
#-------------------------------------------------------------------------------------------------
#Create an array of product prices and increase every price by 10%.
prices =  np.array([100,300,450,1000.690,500])
new_price = prices*1.10                                  # 100% = original price = 1.00
print(new_price)                                         # 10% = increase = 0.10
print(new_price)                                         # 110% = new price = 1.10
#------------------------------------------------------------------------------------------------
#Create an array of marks for 10 students. Change the marks of the fourth student to a new value.
marks = np.array([500,550,489,506,478,499,506,400,234,523])
marks[3] = 515
print(marks)
#------------------------------------------------------------------------------------------
#Create an array containing sales for 10 days and display it in reverse order using NumPy slicing.
sales = np.array([500,550,489,506,478,499,506,400,234,523])
print(sales[: : -1])
#-----------------------------------------------------------------------------------------
#Create an array containing 10 numbers and extract every second value.
marks = np.array([500,550,489,506,478,499,506,400,234,523])
print(marks[0:10:2])
#-------------------------------------------------------------------------------------
#Create an array containing revenue for 20 days.
#Calculate:
#total revenue
#average daily revenue
#highest daily revenue
#lowest daily revenue
revenue =  np.array([
    12000, 14500, 13200, 15800, 17100,
    14900, 16500, 18200, 17600, 19300,
    20100, 18700, 21500, 22400, 20800,
    23100, 24500, 21800, 25200, 26300,])
print("total revenue : ",np.sum(revenue))
print("average daily revenue : ",np.mean(revenue))
print("highest daily revenue : ",np.max(revenue))
print("lowest daily revenue : ",np.min(revenue))
#---------------------------------------------------------------------------------------------
#Create an array containing marks of 10 students.
#Use NumPy to extract only students who scored 500 or above.
marks = np.array([500,550,489,506,478,499,506,400,234,523])
result = marks[marks>=500]
print(result)
#------------------------------------------------------------------------------------------------
#Create an array containing employee salaries.
#Find:
#salaries greater than the average salary
#salaries below the average salary
salaries = np.array([30000,25000,60000,40000,15000])
average_salaries = np.mean(salaries)
above = salaries[salaries>average_salaries]
print("salaries greater than average salary : ",above)
below = salaries[salaries<average_salaries]
print("salaries below the average salary : ",below)
#-----------------------------------------------------------------------------------------------
#Create a 2D array representing inventory of 4 products across 3 warehouses.
#Find the total inventory available for each product.
inventory = np.array([[1000,4000,10000],[2000,2000,5000],[6000,1000,3000],[9000,2000,7000]])
print(np.sum(inventory,axis = 1))
#-----------------------------------------------------------------------------------
#Create an array containing sales for 12 months and reshape it into a 3 × 4 array.
sales = np.array([120,400,230,200,550,670,490,100,830,1000,470,300])
new_array = sales.reshape(3,4)
print(new_array)
#-----------------------------------------------------------------------------------------
#Create a 2D array containing student marks and convert it into a 1D array.
marks = np.array([[500,550,489,506,478,499,506,400,234,523]])
new = marks.flatten()
print(new)
#------------------------------------------------------------------------------------------
#Create two arrays containing the number of products sold by Store A and Store B for 5 days.
#Concatenate the arrays and calculate the total products sold.
store_A = np.array([15,23,2,40,34])
store_B = np.array([5,17,23,60,5])
store = np.concatenate([store_A,store_B])
print("Total products sold : ",np.sum(store))

#-------------------------------------------------------------------------------------------
#Create an array containing marks of 20 students.
#Split it into 4 groups of 5 students.
students = np.array([67,56,90,88,15,60,45,86,70,100,0,66,50,100,89,93,18,85,77,69])
print(np.array_split(students,4))
#------------------------------------------------------------------------------------------
#Increase the brightness of every pixel by 50.
image = np.array([[200,150],[100,250]])
brightness = image+50
print(brightness)
#-----------------------------------------------------------------------------------------
#Calculate the average of the values while ignoring NaN.
sales = np.array([100, 200, np.nan, 400, 500])
average = np.nanmean(sales)
print(average)
#-----------------------------------------------------------------------------------------
#Count how many NaN values are present in the array.
data = np.array([10, np.nan, 20, np.nan, 30, 40, np.nan])
nan_count = np.sum(np.isnan(data))
print(nan_count)
#----------------------------------------------------------------------------------------
