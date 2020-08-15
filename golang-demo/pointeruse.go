package main

import (
	"fmt"
)

func main() {
	a := `println("hello \n word")`
	fmt.Println(a)
	b := "hello"
	fmt.Println(b)
	fmt.Println(&b)
	var pa *string = &a
	fmt.Println(pa)
	*pa = "new str"
	fmt.Println(*pa)
	fmt.Println(a)

}