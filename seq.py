#!python

sequence = (-4,-2,-1,0,2,3,4,5,6,7,8,9,10,12,14,15,17)

def find_gap(sequence):
    indexes = set()
    for idx, num in enumerate(sequence):
        try:
            old_num
        except NameError:
            old_num = num
            continue
        if num - old_num > 1:
            indexes.add(idx)
        old_num = num
    return indexes

gaps = find_gap(sequence)
print(f"Sequence is {sequence} [0 indexed]")
if len(gaps) > 0:
    for gap in gaps:
        print(f"Found gap at index {gap-1}")


