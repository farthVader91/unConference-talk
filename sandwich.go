package main

import (
    "fmt"
)

func bread(fn func(string)) (func(string)){
    return func(s string) {
        fmt.Println("</''''''\\>")
        fn(s)
        fmt.Println("<\\______/>")
    }
}

func layers(number int, fn func(string)) (func(string)) {
    return func(s string) {
        for i := 0; i < number; i++ {
            fn(s)
        }
    }
}

func ingredients(with_cheese bool, fn func(string)) (func(string)) {
    return func(s string) {
        fmt.Println()
        fmt.Println("#tomatoes#")
        fn(s)
        fmt.Println("~salad~")
        if with_cheese {
            fmt.Println("*cheese*")
        }
        fmt.Println()
    }
}

func sandwich(food string) {
    fmt.Println(food)
}

func main() {
    // create filling with ingredients first
    filling := ingredients(true, sandwich)
    // create layers of filling
    layered_filling := layers(2, filling)
    // add the bread
    full_sandwich := bread(layered_filling)
    full_sandwich("--ham--")
}