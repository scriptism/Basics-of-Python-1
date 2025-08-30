x = 2
print(x)
print(type(x))
y = float(x)
print(y)
print(type(y))
a = 2.08
print(a)
print(type(a))
b = int(a)
print(b)
print('------------')
# Python does not have a random() function
import random
# there are several functions in the random module
print(random.random())  # random float between 0 and 1
print(random.randint(1, 10))  # random integer between 1 and 10 (inclusive)
print(random.randrange(1, 10))  # random integer between 1 and 9 (10 is excluded)
print(random.choice(['apple', 'banana', 'cherry']))  # random choice from a list
print(random.uniform(1.5, 10.5))  # random float between 1.5 and 10.5
print(random.shuffle([1, 2, 3, 4, 5]))  # shuffles a list in place

print(f'Your random numver is:  {random.randrange(1, 10)}')

# strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('------------')
b = 'Hello, World!'
print(b[3])

for x in 'banana':
    if x == 'n':
        print(f'Ba{x}a{x}a')    

print('------------')
c = 'Hello, World!'
print(len(c))

txt = "The best things in life are free!"
print("free" in txt) # returns True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")