package main

import "fmt"

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func splice(a []int, b []int) []int {
	var output []int
	out_size := max(len(a), len(b))
	for i := 0; i < out_size; i++ {
		if len(a) > i {
			output = append(output, a[i])
		}
		if len(b) > i {
			output = append(output, b[i])
		}
	}
	return output
}

func main() {
	a := [5]int{1, 2, 3, 4, 5}
	b := [7]int{6, 7, 8, 9, 10, 11, 12}
	fmt.Println(splice(a[:], b[:]))
}
