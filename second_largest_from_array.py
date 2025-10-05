# Find second largest  element from array 

arr =  [3,2,7,4,9,5,8,1]

arr.sort(reverse=True)  # Sort from biggest to smallest: [9,8,7,5,4,3,2,1]

second_largest = arr[1]
print(f"Second largest element : {second_largest}")