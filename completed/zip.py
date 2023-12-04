list1 = [1,2,3,4]
list2 = ["a", "b", "c", "d"]

def do_zip(list1, list2):
    combined = zip(list1, list2)
    return list(combined)

result = do_zip(list1, list2)
print(result)