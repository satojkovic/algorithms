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

func binarySearchR(data []int, target int, low int, high int) bool {
	if low > high {
		return false
	}
	mid := (low + high) / 2
	if data[mid] == target {
		return true
	} else if data[mid] > target {
		return binarySearchR(data, target, low, mid-1)
	} else {
		return binarySearchR(data, target, mid+1, high)
	}
}

func main() {
	data := []int{1, 10, 11, 25, 33, 52, 74, 100}
	fmt.Println(binarySearch(data, 11))
	fmt.Println(binarySearch(data, 123))
	fmt.Println(binarySearchR(data, 11, 0, len(data)-1))
	fmt.Println(binarySearchR(data, 123, 0, len(data)-1))
}
