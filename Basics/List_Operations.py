# #  Understanding List Methods
# groceryList = ["Apples","Milk","Chicken Breasts","Bread","Avacado"];
# groceryList.append("Bananas")
# groceryList.insert(4, "Wine")
# print(groceryList.index("Wine"))
# print(groceryList);
# print(groceryList[0]);
# print(groceryList[-1]);
# print(groceryList[2-4]);
# print(groceryList[2:5])

#  Find the largest number fro mth list
# numberList = [45, 67, 23, 947, 267, 40];
# largestNumber = numberList[0];
#
# for number in numberList:
#     if number > largestNumber:
#         largestNumber = numberList;
#
# print(largestNumber);

# Remove the duplicates from the list
# Approch 1 removes the number if duplicated:
# numbersList = [65, 10, 20, 30, 10, 20, 40, 50, 65]
# print(numbersList);
# for number in numbersList:
#     numberCount = numbersList.count(number);
#     i = 0;
#     while i < numberCount:
#         numbersList.remove(number);
#         i += 1;
# print(numbersList);

# Approch 2 keeps one instance and removes the duplicate instances:
# numbersList = [65, 10, 20, 30, 10, 20, 40, 50, 65]
# print(numbersList);
# uniques = [];
# for number in numbersList:
#     if number not in uniques:
#         uniques.append(number);
# print(uniques);