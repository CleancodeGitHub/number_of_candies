#=========================================================
'''
   Python program that calculates the number of boxes, bags, and
   remaining.candies given the total number of candies produced.

'''

candies = int(input("Enter the number of candies produced:  "));

boxes = candies /15//24;
bags = candies//15%24;
remaining_candies = candies % 15;

print("The number of packed boxes is" , boxes , " .");
print("There are "  ,bags,   " bags and "  ,remaining_candies,  "candies.");
