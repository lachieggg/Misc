package main

import "fmt"

type Celsius float64
type Fahrenheit float64

func main() {
	var c Celsius
	fmt.Println(c.String())

}

// Sprintf definition...
// func Sprintf(format string, a ...any) string
// Sprintf formats according to a format specifier and returns the resulting string. 
func (c Celsius) String() string { return fmt.Sprintf("%g°C", c)}