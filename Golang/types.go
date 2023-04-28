package main

import "fmt"

type Celsius float64
type Fahrenheit float64

func main() {
	var c Celsius
	fmt.Println(c.String())

}

// String
func (c Celsius) String() string {
	return fmt.Sprintf("%g°C", c)
}
