#include <iostream>

class HashEntry {
    public:
    std::string key;
    int value;

    HashEntry* next;

    HashEntry(std::string key, int value) {
        this->key = key;
        this->value = value;
        this->next = nullptr;
    }
};

int main() {
    HashEntry he("TEST", 100);
    std::cout << he.key << " => " << he.value << std::endl;
    return 0;
}