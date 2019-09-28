
"""
Function  to perform sequential search.
"""
def search(lst,item):
    status = {
            "found": False,
            "index": None,
            }
    i = 0;
    for current in lst:
        if current == item:
            status["found"] = True
            status["index"] = i
            break
        i += 1
    return status
lst = [10, 20, 30, 40, 50]
item = input("Please Enter an item to be searched in the list:")
print(search(lst,item))
        

