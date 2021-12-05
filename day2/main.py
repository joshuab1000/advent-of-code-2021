#Part 1
horizontalPos = 0
depth = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        instruction = line.split()
        num = int(instruction[1])
        direction = instruction[0]

        if direction == 'forward':
            horizontalPos += num
        elif direction == 'up':
            depth -= num
        elif direction == 'down':
            depth += num

    print("Depth * Horizontal Position =", (depth * horizontalPos))
    
#Part 2
aim = 0
horizontalPos = 0
depth = 0

for line in lines:
    instruction = line.split()
    num = int(instruction[1])
    direction = instruction[0]

    if direction == 'forward':
        horizontalPos += num
        depth += num * aim
    elif direction == 'up':
        aim -= num
    elif direction == 'down':
        aim += num
    
print("Depth * Horizontal Position =", (depth * horizontalPos))
