blocks = int(input("Enter the number of blocks: "))

height = 0
current_layer = 1
while blocks >= current_layer:
    blocks -= current_layer
    height += 1
    current_layer += 1

print("The height of the pyramid:", height)
