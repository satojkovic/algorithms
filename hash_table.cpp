#include <iostream>

class HashEntry {
    public:
    std::string key;
    int value;

    HashEntry* next;

    HashEntry() {
        key = "";
        value = -1;
        next = nullptr;
    }
    HashEntry(std::string key, int value) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
    }
};

class HashTable {
    public:
    HashEntry** bucket;
    int slots;
    int size;

    HashTable(int s) {
        bucket = new HashEntry*[s];
        for (int i = 0; i < s; i++) {
            bucket[i] = nullptr;
        }
        slots = s;
        size = 0;
    }

    int getSize() {
        return size;
    }

    bool isEmpty() {
        return getSize() == 0;
    }

    int getIndex(std::string key) {
        int Key = 0;
        for (int i = 0; i < key.length(); i++) {
            Key = 37 * Key + key[i];
        }
        if (Key < 0) {
            Key *= -1;
        }
        return Key % slots;
    }

    void insert(std::string key, int value) {
        int hash_index = getIndex(key);
        if (bucket[hash_index] == nullptr) {
            bucket[hash_index] = new HashEntry(key, value);
            size++;
        } else {
            // chaining strategy
            HashEntry* temp = bucket[hash_index];
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = new HashEntry(key, value);
            size++;
        }
    }

    void resize() {
        slots *= 2;
        HashEntry** to_bucket = new HashEntry*[slots];
        for (int i = 0; i < slots; i++) {
            to_bucket[i] = nullptr;
        }

        for (int i = 0; i < slots/2; i++) {
            if (bucket[i] != nullptr) {
                HashEntry* from_elem = bucket[i];
                while (from_elem != nullptr) {
                    int hash_index = getIndex(from_elem->key);
                    if (to_bucket[hash_index] == nullptr) {
                        to_bucket[hash_index] = new HashEntry(from_elem->key, from_elem->value);
                    } else {
                        // Find next free space
                        HashEntry* to_elem = to_bucket[hash_index];
                        while (to_elem->next != nullptr) {
                            to_elem = to_elem->next;
                        }
                        to_elem->next = new HashEntry(from_elem->key, from_elem->value);
                    }
                    // Next element in the bucket[i]
                    from_elem = from_elem->next;
                }
            }
        }
        bucket = to_bucket;
    }

    int search(std::string key) {
        int hash_index = getIndex(key);
        if (bucket[hash_index] == nullptr) {
            std::cout << "Not found: " << key << std::endl;
            return -1;
        }

        if (bucket[hash_index]->key == key) {
            return bucket[hash_index]->value;
        } else {
            // Find the value in the list
            HashEntry* elem = bucket[hash_index]->next;
            while (elem != nullptr) {
                if (elem->key == key) {
                    return elem->value;
                }
                elem = elem->next;
            }
        }

        std::cout << "Not found: " << key << std::endl;
        return -1;
    }

    void display() {
        HashEntry* temp;
        std::cout << "HT slots: " << slots << " , size: " << size << std::endl;
        for (int i = 0; i < slots; i++) {
            if (bucket[i] != nullptr) {
                std::cout << "HashTable index : " << i << " ";
                temp = bucket[i];
                while (temp != nullptr) {
                    std::cout << "(key = " << temp->key << ", value = " << temp->value << " )";
                    temp = temp->next;
                }
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    HashTable ht(4);
    ht.insert("London",2);
    ht.insert("London",10);
    ht.insert("New York",15);
    ht.insert("Tokyo",7);
    ht.insert("Bangkok",2);
    ht.display();

    std::cout << "Resize HT" << std::endl;
    ht.resize();   // increase slots to 8
    ht.insert("Beijing",6);
    ht.insert("Islamabad",9);
    ht.insert("New Delhi",17);
    ht.insert("Moscow",12);
    ht.insert("Amsterdam",5);
    ht.insert("Paris",13);
    ht.display();

    std::cout << "London => " << ht.search("London") << std::endl;
    std::cout << "Moscow => " << ht.search("Moscow") << std::endl;
    std::cout << "Islamabad => " << ht.search("Islamabad") << std::endl;

    return 0;
}