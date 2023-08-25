l=['car','bike','bus']
# Define the loop function
def loop(x):
    print(x*4)

# Define the map_simple function
def map_simple(crazy,l):
    for items in l:
      crazy(items)

# Call map_simple function to apply loop to each item in the list
map_simple(loop,l)

#Learn about functions
