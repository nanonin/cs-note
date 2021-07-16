package main

import "fmt"

const a = 1 << 4
const b = "one-str"
const mutilinenum = 0.1354654457658769879

const (
	boy = 0
	girl = 1
)

const (
    id1 = iota
    jd2
    jd3
)

func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(mutilinenum)
}