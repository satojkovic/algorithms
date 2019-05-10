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

        bool remove_leaf(TreeNode* parent, TreeNode* node) {
            // Delete the leaf node by making the leaf node's parent's left or right child is nullptr
            if (root->data == node->data) {
                delete root;
                root = nullptr;
                return true;
            } else if (node->data < parent->data) {
                delete parent->left;
                parent->left = nullptr;
                return true;
            } else {
                delete parent->right;
                parent->right = nullptr;
                return true;
            }
        }

        bool remove_node_with_left_only(TreeNode* parent, TreeNode* node) {
            // Delete the node by making the left child of that node the node's parent's right or left child
            if (root->data == node->data) {
                delete root;
                root = node->left;
                return true;
            } else if (node->data < parent->data) {
                delete parent->left;
                parent->left = node->left;
                return true;
            } else {
                delete parent->right;
                parent->right = node->left;
                return true;
            }
        }

        bool remove_node_with_right_only(TreeNode* parent, TreeNode* node) {
            // Similar to the above left only case
            if (root->data == node->data) {
                delete root;
                root = node->right;
                return true;
            } else if (node->data < parent->data) {
                delete parent->left;
                parent->left = node->right;
                return true;
            } else {
                delete parent->right;
                parent->right = node->right;
                return true;
            }
        }

        bool remove_node_with_two_children(TreeNode* parent, TreeNode* node) {
            // Find the smallest value node in the right subtree of the current node
            TreeNode* least_node = findLeastNode(node);
            int data = least_node->data;
            // Swap the current value with the samllest value
            bool is_deleted = remove(root, data);
            node->data = data;
            return is_deleted;
        }

        TreeNode* findLeastNode(TreeNode* node) {
            TreeNode* current = node;
            while (current->left != nullptr) {
                current = current->left;
            }
            return current;
        }

        bool remove(TreeNode* node, int elem) {
            if (root == nullptr) {
                return false;
            }

            // Search the elem
            TreeNode* parent;
            while (node != nullptr && node->data != elem) {
                parent = node;
                if (elem < node->data) {
                    node = node->left;
                } else {
                    node = node->right;
                }
            }

            if (node == nullptr) {
                // Return false when the elem is not found
                return false;
            } else if (node->left == nullptr and node->right == nullptr) {
                // Deleting a leaf node
                return remove_leaf(parent, node);
            } else if (node->right == nullptr) {
                // Deleting a node with a left child only
                return remove_node_with_left_only(parent, node);
            } else if (node->left == nullptr) {
                // Deleting a node with a right child only
                return remove_node_with_right_only(parent, node);
            } else {
                // Deleting a node with two children
                return remove_node_with_two_children(parent, node);
            }
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

        void preOrderPrint(TreeNode* node) {
            if (node != nullptr) {
                std::cout << node->data << std::endl;
                preOrderPrint(node->left);
                preOrderPrint(node->right);
            }
        }

        void postOrderPrint(TreeNode* node) {
            if (node != nullptr) {
                postOrderPrint(node->left);
                postOrderPrint(node->right);
                std::cout << node->data << std::endl;
            }
        }
};

int main() {
    BinarySearchTree bst(6);
    std::cout << "root value : " << bst.getRoot()->data << std::endl;
    bst.addNode(4);
    bst.addNode(9);
    bst.addNode(5);
    bst.addNode(2);
    bst.addNode(8);
    bst.addNode(12);
    std::cout << "inorder print" << std::endl;
    bst.inOrderPrint(bst.getRoot());
    std::cout << "preorder print" << std::endl;
    bst.preOrderPrint(bst.getRoot());
    std::cout << "postorder print" << std::endl;
    bst.postOrderPrint(bst.getRoot());

    BinarySearchTree bst2(6);
    std::cout << "root value : " << bst2.getRoot()->data << std::endl;
    bst2.addNode(4);
    bst2.addNode(9);
    bst2.addNode(5);
    bst2.addNode(2);
    bst2.addNode(8);
    bst2.addNode(12);
    std::cout << "inorder print" << std::endl;
    bst2.inOrderPrint(bst2.getRoot());
    std::cout << "preorder print" << std::endl;
    bst2.preOrderPrint(bst2.getRoot());
    std::cout << "post order print" << std::endl;
    bst2.postOrderPrint(bst2.getRoot());

    int target = 12;
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

    int delete_target = 5;
    if (bst.remove(bst.getRoot(), delete_target)) {
        printf("Delete %d\n", delete_target);
        bst.inOrderPrint(bst.getRoot());
    } else {
        printf("Not found %d\n", delete_target);
    }

    delete_target = -1;
    if (bst.remove(bst.getRoot(), delete_target)) {
        printf("Delete %d\n", delete_target);
        bst.inOrderPrint(bst.getRoot());
    } else {
        printf("Not found %d\n", delete_target);
    }

    return 0;
}
