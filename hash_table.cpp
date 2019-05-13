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

    void display() {
        HashEntry* temp;
        std::cout << "HashTable size : " << size << std::endl;
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
    HashTable ht(3);
    ht.insert("London",2);
    ht.insert("London",10);
    ht.insert("New York",15);
    ht.insert("Tokyo",7);
    ht.insert("Bangkok",2);
    ht.insert("Beijing",6);
    ht.insert("Islamabad",9);
    ht.display();
    return 0;
}