package main

import "fmt"

func merge(left []int, right []int) []int {
	merged := make([]int, 0)
	left_idx := 0
	right_idx := 0
	for left_idx < len(left) && right_idx < len(right) {
		if left[left_idx] <= right[right_idx] {
			merged = append(merged, left[left_idx])
			left_idx += 1
		} else {
			merged = append(merged, right[right_idx])
			right_idx += 1
		}
	}
	merged = append(merged, left[left_idx:]...)
	merged = append(merged, right[right_idx:]...)
	return merged
}
func mergesort(data []int) []int {
	if len(data) <= 1 {
		return data
	}
	mid := len(data) / 2
	left := mergesort(data[0:mid])
	right := mergesort(data[mid:])
	merged := merge(left, right)
	return merged
}

func main() {
	data := []int{3, 1, 10, 8, 9, 22}
	fmt.Println(mergesort(data))
}
