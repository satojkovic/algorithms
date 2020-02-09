package main

import "fmt"

type TreeNode struct {
	val   int
	left  *TreeNode
	right *TreeNode
}

func Preorder(root *TreeNode) {
	if root != nil {
		fmt.Printf("%d\n", root.val)
		Preorder(root.left)
		Preorder(root.right)
	}
}

func main() {
	root := &TreeNode{1, nil, nil}
	root.left = &TreeNode{2, nil, nil}
	root.right = &TreeNode{3, nil, nil}
	root.left.left = &TreeNode{4, nil, nil}
	Preorder(root)
}
