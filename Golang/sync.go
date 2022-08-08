package main

import (
	"fmt"
	"time"
)

func f(done chan bool) {
	fmt.Println("Working...")
	time.Sleep(1 * time.Second)
	fmt.Println("Done!")

	// Send back a value of true
	done <- true
}

func main() {
	// Determines whether to "block" until the go-routine is complete
	var block = false
	
	// Make a buffered boolean channel with one send value
	done := make(chan bool, 1)

	go f(done)

	if(block) {
		<-done
	}

	fmt.Println("Exiting...")
}