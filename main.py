import random

# ---------- numeric conversions ----------
x = 2
print(x, type(x))

y = float(x)
print(y, type(y))

a = 2.08
print(a, type(a))

b = int(a)
print(b, type(b))

# ---------- random module ----------
print("\n--- random functions ---")
print(random.random())                      
print(random.randint(1, 10))                 
print(random.randrange(1, 10))               
print(random.choice(['apple', 'banana', 'cherry']))
print(random.uniform(1.5, 10.5))            
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                        
print(nums)

print(f'Your random number is: {random.randrange(1, 10)}')

# ---------- strings ----------
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("\n--- multi-line string ---")
print(a)

b = 'Hello, World!'
print("\n--- character access ---")
print(b[3])

print("\n--- loop & substring ---")
for x in 'banana':
    if x == 'n':
        print(f'Ba{x}a{x}a')

c = 'Hello, World!'
print("\n--- length ---")
print(len(c))

txt = "The best things in life are free!"
print("\n--- membership ---")
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

print("\n--- sorting ---")

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) 
print(sorted_numbers) 
numbers.reverse()
print(numbers) 
sorted_numbers.reverse()
print(sorted_numbers) 

print("\n--- index method ---")
programming_languages = ['Rust', 'Java', 'JavaScript', 'Python', 'C++']
print(programming_languages.index('Python')) 

print("\n--- Join two lists ---")
# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


