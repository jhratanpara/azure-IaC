import sys
import operator

list_of_price = list(input('Please enter price: ').split(','))
qty = list(input('Please enter qty: ').split(','))
total_qty =sum([float(i) for i in qty])
percentage_qty = []
float_price = [float(i) for i in list_of_price]
price_percentage = []

for y in qty:11
     percentage_qty.append((float(y)*100)/total_qty)  

for x,y in zip(float_price,percentage_qty):
       price_percentage.append((x*y)/100)

# print(list_of_price)
# print('Total buy coin: ',total_qty)
# print('Percentage : ',percentage_qty)
# print(float_price)
# print('average by buying price: ',price_percentage)

print("Average buying price: ",sum(price_percentage))

