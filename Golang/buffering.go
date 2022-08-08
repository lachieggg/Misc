package main

import "fmt"

func main() {
	messages := make(chan string, 2)

	// Inline go-routine that sends messages to the channel
	go func() {
			messages <-"2!4c9WuyF.6x4Y*"
			messages <-"V6@Ly87L82sBjrN"
	}()

	// Receive the two messages into the main thread
	msg := <-messages
	msg2 := <-messages

	// Pretty print out
	fmt.Printf("%v\t%v\n", msg, msg2)
}
