package main

import "fmt"

func quicksort(data []int) []int {
	if len(data) <= 1 {
		return data
	}

	pivot := len(data) / 2
	left := make([]int, 0)
	right := make([]int, 0)
	equal := make([]int, 0)
	for _, d := range data {
		if d < data[pivot] {
			left = append(left, d)
		} else if d > data[pivot] {
			right = append(right, d)
		} else {
			equal = append(equal, d)
		}
	}
	ret := append(quicksort(left), append(equal, quicksort(right)...)...)
	return ret
}

func main() {
	data := []int{10, 3, 9, 4, 5}
	ret := quicksort(data)
	fmt.Println(ret)
}
