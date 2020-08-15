package  main

import "fmt"

func main() {
	a := 1
	if a == 1 {
		fmt.Println("a equals 1")
	} else {		
		fmt.Println("a equals 1")
	}

	b := "b"

	if b == "b" {
		fmt.Println("b equals b")
	} else if b == "c" {
		fmt.Println("b equals c")
	}
}