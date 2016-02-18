package main

import (
    "os"
    "io"
    "fmt"
    "log"
    "hash"
    "crypto/sha1"
)

const SIZE_128_MB = 128<<10
const BIG_FILE_PATH = "big_file"

var c chan string
var flag chan bool
var h hash.Hash
var wf *os.File

func file_chunker(file *os.File, chunk_size int){
    chunk := make([]byte, chunk_size)
    for {
        chunk = chunk[:cap(chunk)]
        n, err := file.Read(chunk)
        chunk = chunk[:n]
        if err == io.EOF {
            break
        }
        if err != nil {
            panic(err)   
        }
        c <- string(chunk)
    }
    close(c)
    return
}

func hasher() {
    h = sha1.New()
    for str := range c {
        h.Write([]byte(str))
    }
    flag <- true
    return
}

func main() {
    big_f, err := os.Open(BIG_FILE_PATH)
    if err != nil {
        log.Fatal(err)
    }
    defer big_f.Close()

    c = make(chan string, 20)
    flag = make(chan bool)

    go file_chunker(big_f, SIZE_128_MB)
    go hasher()
    <-flag
    fmt.Printf("%x\n", h.Sum(nil))
}