#include <iostream>
#include <vector>

template<typename T>
class MaxHeap {
public:
    MaxHeap() {};
    void Insert(const T& value);
    T GetMax();
    void RemoveMax();
    void Build(const std::vector<T>& values);

private:
    void Heapify();
    std::vector<T> h_;
};

int main() {
    MaxHeap<int> max_heap;
    return 0;
}