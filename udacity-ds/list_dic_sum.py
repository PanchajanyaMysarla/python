stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(stuff,dragonLoot):
    for loot in dragonLoot:
        stuff.setdefault(loot, 0)
        stuff[loot] += 1
    print(stuff)
    
    
addToInventory(stuff,dragonLoot)