package main

import "fmt"

type TreeNode struct {
	val   int
	left  *TreeNode
	right *TreeNode
}

func Preorder(root *TreeNode) {
	if root != nil {
		fmt.Printf("%d ", root.val)
		Preorder(root.left)
		Preorder(root.right)
	}
}

func Postorder(root *TreeNode) {
	if root != nil {
		Postorder(root.left)
		Postorder(root.right)
		fmt.Printf("%d ", root.val)
	}
}

func Inorder(root *TreeNode) {
	if root != nil {
		Inorder(root.left)
		fmt.Printf("%d ", root.val)
		Inorder(root.right)
	}
}

func main() {
	root := &TreeNode{1, nil, nil}
	root.left = &TreeNode{2, nil, nil}
	root.right = &TreeNode{3, nil, nil}
	root.left.left = &TreeNode{4, nil, nil}
	root.left.right = &TreeNode{5, nil, nil}

	fmt.Printf("preorder: ")
	Preorder(root)
	fmt.Println("")

	fmt.Printf("postorder: ")
	Postorder(root)
	fmt.Println("")

	fmt.Printf("inorder: ")
	Inorder(root)
	fmt.Println("")
}
