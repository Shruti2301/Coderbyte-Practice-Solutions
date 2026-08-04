# Design an Least Frequently Used (LFU) cache.
# An LFU cache is like a smart storage shelf with limited space. 
# When it gets full and you want to add something new, it kicks out the item that you have used the least amount of times. 
# If two items are tied for the lowest usage, it kicks out the oldest one (Least Recently Used).

# Step 1 : Initialization

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        # Save the maximum number of iterms the cache can hold
        self.capacity = capacity
         
        # Keep track of the lowest frequency currently in cache.
        # Helps us know which group to delete from when the cache is full.
        self.min_freq = 0
        
        # Store items in dictionary, using key as the index and the value as the item.
        self.vals = {}   # key -> value
        
        # A dictionary to track how many times each key has been used. (key -> frequency
        self.counts = {}  # key -> frequency
        
        # Group keys by how often they are used.
        self.freq_map = defaultdict(dict)   # defaultdict(dict) creates a dictionary that defaults to an empty dictionary if a key is not found.
        
        # Step 2 : Frequency Updater
        # This is a helper function to increment the frequency of a key and move it to the next frequency group.
        
        def _update(self, key: int) -> None:
            """ Helper function to increment the frequency of a key"""
            freq = self.counts[key]
            
            # 1. Remove the key