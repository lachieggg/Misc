package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var sep = ""
	var s = ""
	for index, arg := range os.Args[1:] {
		s += sep + arg + " " + strconv.Itoa(index)
		sep = " "
	}
	fmt.Println(s)
}
