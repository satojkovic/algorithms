#include <iostream>

class HashTable {
    public:
    std::string key;
    int value;

    HashTable* next;

    HashTable(std::string key, int value) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
    }
};

int main() {
    HashTable ht("TEST", 100);
    std::cout << ht.key << " => " << ht.value << std::endl;
    return 0;
}