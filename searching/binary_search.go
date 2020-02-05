package main

import "fmt"

func binarySearch(data []int, target int) bool {
	low := 0
	high := len(data) - 1

	for low <= high {
		mid := (low + high) / 2
		if data[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	if low == len(data) || data[low] != target {
		return false
	}

	return true
}

func main() {
	data := []int{1, 10, 11, 25, 33, 52, 74, 100}
	fmt.Println(binarySearch(data, 11))
	fmt.Println(binarySearch(data, 123))
}
