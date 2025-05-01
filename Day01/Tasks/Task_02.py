#Simple Grocery Bill
#input number of items 
total_items= int(input("Enter The Number Of Total Items You Purchased "))
total_bill =0
#Input Details of each Item
while(total_items) :
     name = input(f"Enter The Name Of The Item :")
     quantity = int(input(f"Enter The Number Of Units You Purchased  :" ))
     price = int(input(f"Enter The Price Of One {name} :"))
     total_item_price = quantity*price
     print(f"Total {name} Price = {total_item_price}\n")
     gst = total_item_price*0.18
     final_price = total_item_price+gst
     total_bill += final_price
     total_items -= 1
     
  #printing the final payable bill
print(f"Your Total Bill (incl GST) = {round(total_bill, 2)} Rs")   
      