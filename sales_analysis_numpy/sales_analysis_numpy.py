import numpy as np
data = np.genfromtxt(
    "sales_analysis_numpy/sales_data.csv",
    delimiter=",",
    skip_header=1,
    usecols = (4,5,6,7,8,9)                             #new array containing only numerical columns
)
print("shape : ",data.shape)
print("no. of dimensions : ",data.ndim)
print("size : ",data.size)
print("Data type:", data.dtype)

##Extract every second transaction from the dataset
print(data[::2]) 
##Extract revenue column                   
print(data[:,3])  
##Extracting multiple columns                  
print(data[:,[0,1,2]])  
##Extract the Unit_Price values for the first 15 transactions          
print(data[:15,1])                  
#what is total revenue:
revenue = data[:,3]
total_revenue = np.sum(revenue)
print("Total revenue : ",total_revenue)      
#find average revenue:
avg_revenue = np.mean(revenue)
print("Average revenue : ",avg_revenue)
#Calculate the median Revenue.
median_revenue = np.median(revenue)
print(median_revenue)
#find out minimum and maximum Revenue:
print(np.min(revenue))
print(np.max(revenue))
# Calculate total Quantity sold,ignoring missing values.
quantity = data[:,0]
total_quantity = np.nansum(quantity)
print("Total quantity : ",total_quantity)
#Find all transactions where Revenue is greater than 100000.
revenue = data[:,3]
transactions = data[revenue>100000]
print(transactions)
#Find all transactions where Customer_Rating is 4.5 or higher.
customer_rating = data[:,5]
transactions = data[customer_rating >= 4.5]
print(transactions)
#Find transactions where Revenue is above average Revenue.
avg_revenue = np.mean(revenue)
print("Average revenue : ",avg_revenue)
transactions = data[revenue>avg_revenue]
print(transactions)
#Find transactions where Quantity is between 3 and 7.
transactions = data[((quantity >= 3) & (quantity <= 7))]
print(transactions)
#Find transactions where Revenue is above 100000 AND Customer_Rating is at least 4.
transactions = data[(revenue>100000) & (customer_rating == 4)]
print(transactions)
#Use np.where() to classify discounts as "Discounted" or "No Discount".
discount = data[:,2]
classification = np.where(discount<1,"no discount","discount")
print(classification)
#Use np.where() to give a 5% bonus adjustment to Revenue values above average Revenue.
revenue = data[:,3]
avg_revenue = np.mean(revenue)
bonus = np.where(revenue>avg_revenue,revenue*1.05,revenue)
print(bonus)
#Find the index of the transaction with the highest Unit_Price.
unit_price = data[:,1]
transactions = np.argmax(unit_price)
print(transactions)
#Find the index of the transaction with the lowest Customer_Rating, ignoring NaN values.
customer_rating = data[:,5]
transactions = np.nanargmin(customer_rating)
print(transactions)
#Sort Revenue from smallest to largest.
sorted_revenue = np.sort(revenue)
print(sorted_revenue)
#Sort Revenue from largest to smallest,ignoring missing values.
sorted_revenue = np.sort(revenue[~np.isnan(revenue)])[::-1]
print(sorted_revenue)
#Find the five lowest Revenue values.
sorted_revenue = np.sort(revenue)[:5]
print(sorted_revenue)
#Create a simple 1D NumPy array containing the first 12 Revenue values.
revenue = data[:12,3]
print(revenue)
#Reshape it into a 3 × 4 array.
new_revenue = revenue.reshape(3,4)
print(new_revenue)
#Reshape the same values into a 2 × 6 array.
reshaped_revenue = new_revenue.reshape(2,6)
print(reshaped_revenue)
#Flatten a 2D array back into 1D.
flat = reshaped_revenue.flatten()
print(flat)
#Create a small array of three additional revenue values and append them to an existing Revenue array.
arr = np.array([1500.0,6700.0,7650.0,13400.0])
print(np.append(revenue,arr))
#Insert a value into a chosen position of a Revenue array.
print(np.insert(revenue,4,178))
#Delete a chosen value from a Revenue array.
print(np.delete(revenue,1,axis = 0))
#Increase every Unit_Price by 10% using broadcasting.
unit_price = data[:, 1]
increased_price = unit_price * 1.10
print(increased_price)
#Apply a 5% reduction to all Revenue.
revenue = data[:, 3]
reduced_revenue = revenue * 0.95
print(reduced_revenue)
#Add a fixed delivery charge of 500 to every transaction.
delivery_charge = 500
revenue_with_delivery = revenue + delivery_charge
print(revenue_with_delivery)

#**************************************************************************************************