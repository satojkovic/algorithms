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
    int num_nodes;

    public:
        BinarySearchTree(int elem) {
            root = new TreeNode(elem);
            num_nodes = 1;
        }

        TreeNode* getRoot() {
            return root;
        }

        TreeNode* search(int elem) {
            TreeNode* current_node = root;
            while (current_node && current_node->data != elem) {
                if (elem < current_node->data) {
                    current_node = current_node->left;
                } else {
                    current_node = current_node->right;
                }
            }
            // after the loop, we'll have either the searched value
            // or nullptr in case the value was not found
            return current_node;
        }

        TreeNode* search(TreeNode* node, int elem) {
            if (node == nullptr) {
                return nullptr;
            } else if (node->data == elem) {
                return node;
            } else if (elem < node->data) {
                return search(node->left, elem);
            } else {
                return search(node->right, elem);
            }
        }

        bool contains(int elem) {
            return contains_r(root, elem);
        }

        bool contains_r(TreeNode* node, int elem) {
            if (node == nullptr) {
                return false;
            }

            if (elem < node->data) {
                return contains_r(node->left, elem);
            } else if (elem > node->data)
            {
                return contains_r(node->right, elem);
            } else {
                return true;
            }
        }

        bool addNode(int elem) {
            if (contains(elem)) {
                return false;
            } else {
                root = addNode_r(root, elem);
                num_nodes++;
                return true;
            }
        }

        TreeNode* addNode_r(TreeNode* node, int elem) {
            // base case
            // create new node and return it to the previous leaf(null) node.
            if (node == nullptr) {
                node = new TreeNode(elem);
            } else if (elem < node->data) {
                node->left = addNode_r(node->left, elem);
            } else {
                node->right = addNode_r(node->right, elem);
            }
            return node;
        }

        bool addNode_i(int elem) {
            if (contains(elem)) {
                return false;
            }

            if (getRoot() == nullptr) {
                root = new TreeNode(elem);
                num_nodes++;
                return true;
            }

            // Starting from the root
            TreeNode* node = root;
            TreeNode* parent;
            while (node) {
                parent = node;
                if (elem < node->data) {
                    node = node->left;
                } else {
                    node = node->right;
                }
            }
            // When the current node becomes nullptr, it inserts the value to its parent.
            if (elem < parent->data) {
                parent->left = new TreeNode(elem);
            } else {
                parent->right = new TreeNode(elem);
            }

            num_nodes++;
            return true;
        }

        void inOrderPrint(TreeNode* node) {
            if (node != nullptr) {
                inOrderPrint(node->left);
                std::cout << node->data << std::endl;
                inOrderPrint(node->right);
            }
        }
};

int main() {
    BinarySearchTree bst(3);
    std::cout << "root value : " << bst.getRoot()->data << std::endl;
    bst.addNode(2);
    bst.addNode(5);
    bst.addNode(-1);
    bst.addNode(0);
    bst.addNode(10);
    bst.addNode(0);
    bst.inOrderPrint(bst.getRoot());

    BinarySearchTree bst2(3);
    std::cout << "root value : " << bst2.getRoot()->data << std::endl;
    bst2.addNode(2);
    bst2.addNode(5);
    bst2.addNode(-1);
    bst2.addNode(0);
    bst2.addNode(10);
    bst2.addNode(0);
    bst2.inOrderPrint(bst2.getRoot());

    int target = 10;
    if (bst.search(target)) {
        printf("Recursive search %d -> Found\n", target);
    } else {
        printf("Recursive search %d -> Not found\n", target);
    }

    if (bst.search(bst.getRoot(), target)) {
        printf("Iterative search %d -> Found\n", target);
    } else {
        printf("Iterative search %d -> Not found\n", target);
    }

    return 0;
}
