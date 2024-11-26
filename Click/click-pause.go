package main

import (
	"fmt"
	"os"
	"time"

	"github.com/go-vgo/robotgo"
	"github.com/eiannone/keyboard"
)

var pause = 1000
var clicking = false // State variable to toggle clicking
var lastMouseX, lastMouseY int // To store the last mouse position

func main() {
	fmt.Println("Press 's' to start/stop auto-clicking.")
	fmt.Println("Press 'e' or 'Ctrl+C' to exit the program.")

	// Open the keyboard for input detection
	if err := keyboard.Open(); err != nil {
		fmt.Println("Error opening keyboard:", err)
		return
	}
	defer keyboard.Close()

	// Initialize the mouse position
	lastMouseX, lastMouseY = robotgo.GetMousePos()

	// Run a goroutine to monitor keypresses
	go monitorKeys()

	// Main loop for auto-clicking
	for {
		if clicking {
			// Check if mouse has moved
			currentMouseX, currentMouseY := robotgo.GetMousePos()
			if currentMouseX != lastMouseX || currentMouseY != lastMouseY {
				fmt.Printf("Pausing for %d milliseconds.\n", pause)
				time.Sleep(time.Duration(pause) * time.Millisecond)
				lastMouseX, lastMouseY = currentMouseX, currentMouseY
			} else {
				robotgo.Click("left") // Perform a mouse click
			}
		}
	}
}

// monitorKeys listens for key events to toggle clicking or exit
func monitorKeys() {
	for {
		char, key, err := keyboard.GetKey()
		if err != nil {
			fmt.Println("Error reading key:", err)
			return
		}

		// Toggle clicking on 's'
		if char == 's' {
			clicking = !clicking
			if clicking {
				fmt.Println("Auto-clicker started.")
			} else {
				fmt.Println("Auto-clicker stopped.")
			}
		}

		// Exit program on 'e'
		if char == 'e' {
			fmt.Println("Exiting program.")
			os.Exit(0)
		}

		// Exit program on Ctrl+C (keyboard.KeyCtrlC)
		if key == keyboard.KeyCtrlC {
			fmt.Println("Exiting program due to Ctrl+C.")
			os.Exit(0)
		}
	}
}

