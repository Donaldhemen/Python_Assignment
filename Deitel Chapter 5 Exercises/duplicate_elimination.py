
def eliminate_duplicate(items):

    new_items = []
    for item in items:
        if item not in new_items:
            new_items.append(item)
    return sorted(new_items)

items = [1,2,1,2,4,4,5,3]
print(eliminate_duplicate(items))

name = 'hembafanchorob'
print(eliminate_duplicate(name))