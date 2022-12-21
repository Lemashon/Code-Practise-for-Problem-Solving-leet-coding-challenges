def minimumAbsDifference(arr):
    arr.sort() #Sorting the array in ascending order
    min_diff = float('inf') #initialize minimum difference to infinity
    pairs = [] #Initializing empty list of pairs
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1] # Calculate difference between current and previous element
        if diff < min_diff:
            #Updating the minimum difference between
            
            min_diff = diff
            #Updating list of pairs to current pairs
            
            pairs = [[arr[i - 1], arr[i]]]
            
        elif diff == min_diff:
            pairs.append[arr[i-1], arr[i]]
            
        return pairs
            