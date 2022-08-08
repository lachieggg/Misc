package main

import "fmt"

func main() {
	fmt.Println("Hello, world")
	var sum = add(1,2)
	fmt.Println(sum)
}

func add(x int, y int) int {
	return x + y
}

