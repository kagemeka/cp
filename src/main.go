package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type BufStdScanner struct {
	scanner *bufio.Scanner
}

func NewBufStdScanner() *BufStdScanner {
	const maxBuffer = 1 << 20
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer([]byte{}, maxBuffer)
	scanner.Split(bufio.ScanWords)
	return &BufStdScanner{scanner}
}

func (sc *BufStdScanner) Str() string {
	sc.scanner.Scan()
	return sc.scanner.Text()
}

func (sc *BufStdScanner) Int() int {
	v, _ := strconv.Atoi(sc.Str())
	return v
}

type BufStdWriter struct {
	writer *bufio.Writer
}

// defer writer.Flush()
func NewBufStdWriter() *BufStdWriter {
	return &BufStdWriter{bufio.NewWriter(os.Stdout)}
}

func (writer *BufStdWriter) Write(a ...any) {
	fmt.Fprintln(writer.writer, a...)
}

func (writer *BufStdWriter) Flush() { writer.writer.Flush() }

func Assert(ok bool) {
	if !ok {
		panic("assertion failed")
	}
}

func ToAnySlice[T any](a []T) []any {
	b := make([]any, len(a))
	for i, x := range a {
		b[i] = x
	}
	return b
}

func ZAlgorithm[T comparable](a []T) []int {
	n := len(a)
	lcp := make([]int, n)
	for i, l := 1, 0; i < n; i++ {
		r := l + lcp[l]
		d := 0
		if r > i {
			d = lcp[i-l]
			if r-i < d {
				d = r - i
			}
		}
		for i+d < n && a[i+d] == a[d] {
			d++
		}
		lcp[i] = d
		if r < i+d {
			l = i
		}
	}
	lcp[0] = n
	return lcp
}

func main() {
	reader := NewBufStdScanner()
	writer := NewBufStdWriter()
	defer writer.Flush()

	s := []rune(reader.Str())
	lcp := ZAlgorithm(s)

	writer.Write(ToAnySlice(lcp)...)

}
