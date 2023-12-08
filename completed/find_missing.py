def findMissingNumbers(n):
    #create unique set - faster membership checking
    numbers = set(n)
    output = []
    # range creates object of nums from 1 to last num in set -1 (bc if last num missing, set ends earlier)
    for i in range(1, n[-1]):
        # if i from range not in set, add to output arr
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1,3,4,5]
print(findMissingNumbers(listOfNumbers))

# output: [2]