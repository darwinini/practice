# Hash Map

class HashMap:
    # Constructor
    def __init__(self):
        # size of the array
        self.size = 6
        # array to store data in
        # use None to force python to construct a list of a fixed length
        self.map = [None] * self.size

    # My hash function
    # calculate the index for a key
    def hashFunction(self, key):
        hash = 0
        # why I'm I forcing the already string into a string
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        # storing the hash key into key_hash
        key_hash_indx = self.hashFunction(key)

        # key_value is an array of two elements with key, value pair
        # this helps us construct a cell
        key_value_pair = [key, value]

        # check if the map is empty (it was initialized to be empty)
        if self.map[key_hash_indx] is None:
            # if the map is empty, insert the list object along with its key value pair
            self.map[key_hash_indx] = list([key_value_pair])
            return True

        # if the map is not empty, then update the values in it
        else:
            # for the case where we have a key_value_pair there are two outcomes:
            # Outcome1 where the key exists
            # Outcome2 where the key doesn't exist

            # Outcome1: the key exists, then we update the corresponding value
            for pair in self.map[key_hash_indx]:
                # how is the value being updated here?
                # check if key is already existing to perhaps change the value
                if pair[0] == key:
                    pair[1] = value
                    return True
            # Outcome2: the key didnt' exist
            # if we didn't find the value for our key, then we append a new pair on that index
            self.map[key_hash_indx].append(key_value_pair)
            return True

    def get(self, key):
        # get the hash index
        key_hash_indx = self.hashFunction(key)
        # locate the cell
        if self.map[key_hash_indx] is not None:
            for pair in self.map[key_hash_indx]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash_indx = self.hashFunction(key)

        if self.map[key_hash_indx] is None:
            return False
        for i in range(0, len(self.map[key_hash_indx])):
            if self.map[key_hash_indx][i][0] == key:
                self.map[key_hash_indx].pop(i)
                return True
        return False

    def keys(self):

        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Ming: ' + h.get('Ming'))
print(h.keys())

# 888-237-82893