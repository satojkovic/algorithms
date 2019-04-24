#include <iostream>

class TreeNode {
    public:
        int data;
        TreeNode* left;
        TreeNode* right;

    TreeNode() {
        data = 0;
        left = nullptr;
        right = nullptr;
    }

    TreeNode(int elem) {
        data = elem;
        left = nullptr;
        right = nullptr;
    }
};

class BinarySearchTree {
    TreeNode* root;

    public:
        BinarySearchTree(int elem) {
            root = new TreeNode(elem);
        }

        TreeNode* getRoot() {
            return root;
        }
};

int main() {
    BinarySearchTree bst(3);
    std::cout << "root value : " << bst.getRoot()->data << std::endl;
    return 0;
}
