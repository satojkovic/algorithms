#include <iostream>

class HashEntry {
    public:
    std::string key;
    int value;

    HashEntry* next;

    HashEntry() {};
    HashEntry(std::string key, int value) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
    }
};

class HashTable {
    public:
    HashEntry* bucket;
    int slots;
    int size;

    HashTable() {
        bucket = new HashEntry();
        slots = 10;
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
};

int main() {
    HashTable ht;
    std::cout << "HashTable is initilized => " << ht.isEmpty() << std::endl;
    return 0;
}