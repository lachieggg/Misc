package main

import "fmt"

func main() {
	// Unbuffered
	var c chan string = make(chan string)

	go func() { c <-"test" }()

	// Can store two strings in the buffer at any given time
	var x chan string = make(chan string, 2)

	x <- "hello"
	x <- "world"

	fmt.Println(<-x)
	fmt.Println(<-x)

	x <- "let's"
	x <- "go"

	fmt.Println(<-x)
	fmt.Println(<-x)

	msg := <-c

	fmt.Println(msg)

}