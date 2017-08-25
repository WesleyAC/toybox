package main

import "fmt"

func delta(a []int) []int {
	var output []int
	for i := 1; i < len(a); i++ {
		output = append(output, a[i-1])
		output = append(output, a[i]-a[i-1])
	}
	output = append(output, a[len(a)-1])
	return output
}

func main() {
	a := [3]int{3, 8, 15}
	fmt.Println(delta(a[:]))
}
