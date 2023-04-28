package main

import "fmt"

func main() {
	x := 1
	p := &x

	fmt.Printf("Address of x: %v\n", &x)
	fmt.Printf("Value of x: %d\n", x)
	fmt.Printf("Changing the value of x using pointer\n")

	*p = 2

	fmt.Printf("Address of x: %v\n", &x)
	fmt.Printf("Value of x: %d\n", x)

	// Can return a variable's memory address from
	// functions and assign to pointer.
	// They are still accessible!
	p = f()
	fmt.Println(p)
	fmt.Println(*p)
}

func f() *int {
	v := 1
	return &v
}
