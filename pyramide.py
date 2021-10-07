
blocks = int(input("Number of blocks: "))
height = 0
layerblocks = 0

while layerblocks <= blocks:
    height += 1
    blocks -= layerblocks
    layerblocks += 1

print("Layers: "+ str(layerblocks))