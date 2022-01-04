package main

import "fmt"


func printAnything[T any] (thing T) {
	fmt.Println(thing)
}


type Adder interface {
	add(b Adder) Adder
}

func Add[T Adder] (a, b T) T {
	return a.add(b).(T)
}

type Int int

func (a Int) add(b Adder) Adder {
	return a + b.(Int)
} 


func main() {
	var a Int = 1
	var b Int = 2
	printAnything(Add(a, b))
}