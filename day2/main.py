horizontalPos = 0
depth = 0

#Part 1
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
