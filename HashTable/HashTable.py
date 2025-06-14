class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # create list of empty buckets

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if key already exists and update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key not found, insert new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i] # deleteing the pair in the inner chain
                return True
        return False  # Key not found

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:", bucket)

# Example usage
ht = HashTable(10)
ht.insert("apple", 3)
ht.insert("banana", 5)
ht.insert("grape", 7)
ht.insert("apple", 10)  # update value
ht.display()

print("Search 'banana':", ht.search("banana"))
ht.delete("banana")
ht.display()
