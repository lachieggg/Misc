package main

import (
	"fmt"
	"time"
)

func count(name string) {
	for i := 0; i <= 5; i++ {
		fmt.Printf("%v:\t%v\n", name, i)
	}
}

func main() {
	// Demonstrate go-routines
	go count("first")
	go count("second")
	go count("third")
	time.Sleep(time.Second)

	// Create channels of type "string"
	messages := make(chan string)
	channel := make(chan string)

	// Invoke an inline (anonymous)
	// function in a goroutine
	//
	// Sends a value to each channel
	go func() { messages <- "message"; channel <- "variable!" }()

	// Pass back the results of each channel back into the main thread
	msg := <-messages
	variable := <-channel

	// Print out the result
	fmt.Println(msg)
	fmt.Println(variable)
	fmt.Println("Messages sent")
}
