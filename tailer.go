package main

import (
    "fmt"
    "os/exec"
    "strings")

func my_tail(output chan string, filename string) {
    cmd := exec.Command("tail", "-f", filename)
    stdout, err := cmd.StdoutPipe()
    if ( err != nil ) {
        return
    }
    if err := cmd.Start(); err != nil {
        return
    }
    buf := make([]byte, 1024)
    for {
        n, err := stdout.Read(buf)
        s := []string{filename, string(buf[:n])}
        if n != 0 {
            output <- strings.Join(s, " | ")
        }
        if err != nil {
            break
        }
    }
}

func main() {
    ch := make(chan string)
    go my_tail(ch, "/var/log/apache2/error.log")
    go my_tail(ch, "/var/log/nginx/access.log")
    for {
        text := <- ch
        fmt.Print(text)
    }
}
