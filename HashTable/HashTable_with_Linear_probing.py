class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 10  # Initial small size for demonstration
        self.slots = [None for _ in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65

    def _hash(self, key): 
        mult = 1 # use this or else the value of "ab"="ba"
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break  # Key exists, update value
            h = (h + 1) % self.size  # Linear probing

        if self.slots[h] is None:
            self.count += 1  # New key
        self.slots[h] = item

        self.check_growth()  # Check load factor and grow if needed

    def get(self, key):
        h = self._hash(key)
        start = h  # To prevent infinite loop in worst case

        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size
            if h == start:
                break
        return None

    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing:", round(loadfactor, 2))
            self.growth()
            print("Load factor after growing:", round(self.count / self.size, 2))

    def growth(self):
        new_table = HashTable()
        new_table.size = 2 * self.size
        new_table.slots = [None for _ in range(new_table.size)]
        new_table.MAXLOADFACTOR = self.MAXLOADFACTOR  # Keep same threshold

        for i in range(self.size):
            if self.slots[i] is not None:
                new_table.put(self.slots[i].key, self.slots[i].value)

        self.size = new_table.size
        self.slots = new_table.slots
        # count remains the same

    def display(self):
        for i, item in enumerate(self.slots):
            if item is not None:
                print(f"Slot {i}: {item.key} → {item.value}")
