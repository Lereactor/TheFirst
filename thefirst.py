name = input('inser one: ')
print('your number is ', name)
print(f"you nunmer {name}!")
num_0 = int(input('one: '))
num_1 = int(input('two: '))
result = num_0 >= num_1
print(result)

#async function
def pc(x):
    for num in range(x):
        print(num)
def start(x):
    for num in range(x):
        pc(x)
start(3)
