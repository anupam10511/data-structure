def search(lst, item, l, r):
    status = {
        "found": False,
        "index": None
    }
    if l <= r:
        mid = (r + l)/2
        if lst[mid] == item:
            status["found"] = True
            status["index"] = mid
            return {"found": True, "index": mid}
        elif item > lst[mid]:
            l = mid + 1
            search(lst, item, l, r)
        else:
            r = mid - 1
            search(lst, item, l, r)
    else:
        return status
lst = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = input("Please Enter the item to be searched:")

print(search(lst, item, 0, len(lst)-1))


