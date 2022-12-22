def numJewelIsStones(J: str, S: str) -> int:
    mymap = {}
    for ch in J:
        if ch not in mymap:
            mymap[ch] = 0
        mymap[ch] += 1
    
    count = 0
    for ch in S:
        if ch in mymap:
            count += 1
    
    return count