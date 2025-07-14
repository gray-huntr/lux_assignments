for i in range(11):
    print(i)


y = 0
while True:
    word = input('Type stop to quit: ')
    if word == 'stop':
        break
    else:
        y += 1
        print(y)

for i in range(21):
    if i % 2 == 0:
        print(i)

# Explanation of break and continue
# Break - this reserved word tells the loop to stop at the current iteration
# continue - this reserved word tell the loop to skip the current iteration
