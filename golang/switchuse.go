package main

import "fmt"

func main() {
	var str = "book"
	switch str {
		case "book":
			fmt.Println("yes")
		case "ok":
			fmt.Println("ok")
		default:
			fmt.Println("others")

	}
}