# Different ways to use index numbers in for loops

# Method 1: Using enumerate()
fruits = ['apple', 'banana', 'orange', 'mango']
print("Method 1: Using enumerate()")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Method 2: Using range() with len()
print("\nMethod 2: Using range() with len()")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Method 3: Starting index from 1
print("\nMethod 3: Starting index from 1")
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")

# Method 4: Using enumerate with custom step
print("\nMethod 4: Using enumerate with custom step")
for index, fruit in enumerate(fruits):
    if index % 2 == 0:  # Only print even indices
        print(f"Even Index {index}: {fruit}")

# Method 5: Using enumerate with unpacking
print("\nMethod 5: Using enumerate with unpacking")
for index, (fruit, length) in enumerate(zip(fruits, [len(f) for f in fruits])):
    print(f"Index {index}: {fruit} has {length} letters") 