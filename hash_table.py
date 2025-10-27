class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        contact = Contact(key, number)
        node = Node(key, contact)

        if self.data[index] is None:
            self.data[index] = node
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    current.value = contact
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.data[i]
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Test your hash table implementation here.   
if __name__ == "__main__":
    table = HashTable(10)
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.insert("Rebecca", "999-444-9999")

    table.print_table()
    print("\nSearch result:", table.search("John"))
    print("Search result:", table.search("Chris"))


"""
Design Memo

Hash table is the right structure for this contact management system because it
allows very fast lookups, insertions, and updates compared to lists or other data
structures. Whenever someone searches for a contact by name, the hash function can
quickly convert the name into an index number and jump directly to that spot in
memory. This makes the program works well, even when there are hundreds of contacts
stored.

In my implementation, I used separate chaining to handle collisions. This means
that if two names produce the same hash index, they are linked together in a short
chain using nodes. Each node holds a contact and a pointer to the next one. When
searching, the system only goes through that small linked list instead of the
entire table, which keeps it fast. Also, I made sure that if the same name is added
again, the system updates the contact's number instead of adding a duplicate.

An engineer would choose a hash table over a list or tree when quick access by
unique keys is more important than sorting or ordering data. Lists require checking
each item one by one, and trees can be more complex to maintain. Hash tables are
simple, lightweight, and ideal for limited-memory devices that still need quick
access to stored information, like contact managers or caches.
"""