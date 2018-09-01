stuff={'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}

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
    item_tot1 = 0
    for idx in range(0,len(addedItems)):
        for addedItems[idx] in inventory.keys():
            item_tot1 += inventory[addedItems[idx]]

    print(str(inventory[addedItems[idx]]) + ' ' + addedItems[idx] )
#displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory( stuff, dragonLoot )
