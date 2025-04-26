#START

#Adding Error Handling
try:
 #Getting Total Marks Input
 marks = int(input("Enter The Total Marks:"))

 #Getting Obtained Marks Input
 obtm = int(input("Enter Obtained Marks:"))

 #Calculating Percentage
 p = (obtm/marks)*100
 
 #Printing Percentage
 print(f"Your Percentage is: {p}%")
except Exception as e:
	print("Error! Please Enter A Valid Number (>0)")
#END

