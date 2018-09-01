def displayInventory(inventory):
    print("Inventory:")
    item_tot = 0
    
#    for k, v in inventory.items():
#        print(str(v) + ' ' + k )
#        item_tot += v

    for k in inventory.keys():
        print(str(inventory[k]) + ' ' + k )
        item_tot += inventory[k]

    print("\nTot number of items: " + str(item_tot))

def addToInventory(inventory, addedItems):
    for key in addedItems:
        if key not in inventory.keys():
            inventory.setdefault(key, 1 )
            continue
        else:
            inventory[key] += 1


#stuff={'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}
stuff = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dagger', 'ruby', 'dagger']
addToInventory( stuff, dragonLoot )
#print(stuff)
displayInventory( stuff )
