# ------import modules ------
import random

text = "I am a student of Python in the university."
print(text)
text = 'You are' + text[4:]
print(text)


x = "Hallo "
print(x * 5)
print(x.upper())
print(x.lower())
print(len(x))
print(x.split("l"))

text1 = "I"
text2 = "love"
text3 = "Python"
print(text1 + " " + text2 + " " + text3)


# ---------- numeric conversions ----------
x = 2
print(x, type(x))

y = float(x)
print(y, type(y))

a = 2.08
print(a, type(a))

b = int(a)
print(b, type(b))


# find()
# matches the first occurrence of the specified value
print(text.find("y"))
portion = text.find("Python")
# print(portion)
print(text[portion:])
print(text[portion:portion + 17])


# ---------- random module ----------
print("\n--- random functions ---")
print(random.random())                       # 0.0 ≤ float < 1.0
print(random.randint(1, 10))                 # int 1-10 inclusive
print(random.randrange(1, 10))               # int 1-9
print(random.choice(['apple', 'banana', 'cherry']))
print(random.uniform(1.5, 10.5))             # float 1.5-10.5

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                         
print(nums)

print(f'Your random number is: {random.randrange(1, 10)}')

# ---------- strings ----------
a = """Lorem ipsum dolor sit amet,
consectetur elit,
sed do eiusmod incididunt
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

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]
numbers.reverse()
print(numbers) # [41, 67, 1, 35, 2, 19]
sorted_numbers.reverse()
print(sorted_numbers) # [67, 41, 35, 19, 2, 1]

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

