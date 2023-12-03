my_list = ['apple', 'banana', 'orange']

def enumerate_list(my_list):
    results = []
    for index, value in enumerate(my_list):
        results.append(f"Index: {index}, Value: {value}\n")
    return results
    
results = enumerate_list(my_list)
print("".join(results))