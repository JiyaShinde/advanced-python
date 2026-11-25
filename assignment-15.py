import gc
import sys

# Function to create some objects
def create_objects():
    objects = []
    for i in range(1000):
        objects.append([i] * 100)
    return objects

# Function to display memory usage
def display_memory():
    print("Memory usage:", 
          sum(sys.getsizeof(obj) for obj in gc.get_objects()), "bytes")

# Display initial memory usage
print("Initial memory usage:")
display_memory()

# Create objects and display memory usage
objects = create_objects()
print("\nMemory usage after creating objects:")
display_memory()

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Collect garbage and display memory usage
del objects
gc.collect()

print("\nMemory usage after garbage collection:")
display_memory()

# Disable garbage collection debugging
gc.set_debug(0)
