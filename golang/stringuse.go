package main

import (
	"fmt"
	"strings"
)

func main() {
	a := `println("hello \n word")`
	fmt.Println(a)
	b := "hello"
	fmt.Println(b)
	fmt.Println(strings.Contains(a, b))
	fmt.Println(strings.Index(a, b))
	fmt.Println(strings.HasPrefix(a, b))

}