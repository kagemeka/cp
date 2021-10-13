package main 


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Modular struct {
	value int 
	mod int
}


func (
	x Modular,
) Add(
	y interface{},
) (
	interface{},
) {
	x.value += y.(Modular).value
	x.init()
	return x
}


func (
	x Modular,
) AddIdentity() (
	interface{},
) {
	return Modular{0, x.mod}
}


func (
	x Modular,
) AddInv() (
	interface{},
) {
	x.value *= -1
	x.init()
	return x
}


func (
	x *Modular,
) init() {
	m := x.mod
	v := x.value % m
	x.value = (v + m) % m
}



func (
	x Modular,
) Mul(
	y interface{},
) (
	interface{},
) {
	x.value *= y.(Modular).value
	x.init()
	return x
}


func (
	x Modular,
) MulIdentity() (
	interface{},
) {
	return Modular{1, x.mod}
}


func (
	x Modular,
) MulInv() (
	interface{},
) {
	return x.Pow(x.mod - 2)
}




func (
	x Modular,
) Pow(n int) (
	interface{},
) {
	if n == 0 {
		return x.MulIdentity()
	}
	y := x.Pow(n >> 1)
	y = y.(Modular).Mul(y)
	if n & 1 == 0 { return y }
	return x.Mul(y)
}



func (
	x Modular,
) String() string {
	return fmt.Sprint(x.value)
} 




func (
	x Modular,
) Factorial() Mods {
	n, m := x.value, x.mod
	fact := make(Mods, n)
	for i := 0; i < n; i++ {
		fact[i] = Modular{i, m}
	}
	fact[0] = Modular{1, m}
	return CumProd(fact).(Mods)
}



// func (
// 	m Modular,
// ) InvFactorial() (
// 	iFact Mods,
// ) {
// 	n, mod := m.Value, m.Mod
// 	fact := m.Factorial()
// 	iFact = make(Mods, n)
// 	for i := 0; i < n; i++ {
// 		iFact[i] = Modular{
// 			n - i,
// 			mod,
// 		}
// 	}
// 	x := fact[n - 1].MulInv()
// 	iFact[0] = x.(Modular)
// 	iFact = CumProd(iFact).(Mods)
// 	Reverse(iFact)
// 	return
// }


type Mods []Modular


type AccumulateIF interface {
	Clone() interface{}
	Len() int 
	Get(i int) interface{}
	Set(i int, x interface{})
}






type Problem struct {
	io *IO
	mod int
	w, h int
}


func (
	p *Problem,
) Init() {
	p.io = new(IO)
	p.io.Init()
}


func (
	p *Problem,
) Input() {
	io := p.io
	p.w = io.ReadInt()
	p.h = io.ReadInt()
	p.mod = 1e9 + 7
}


func (
	p *Problem,
) Solve() {
	w, h := p.w, p.h	
	
}



func main() {
	p := new(Problem)
	p.Init()
	// t := p.io.ReadInt()
	t := 1
	for i := 0; i < t; i++ {
		Run(p)
	}
}



type IO struct {
	r *Read
	w *Write
}


func (
	io *IO,
) Init() {
	r, w := new(Read), new(Write)
	r.Init()
	w.Init()
	io.r, io.w = r, w
}


func (
	io *IO,
) Read() (
	string,
) {
	return io.r.Str()
}


func (
	io *IO,
) ReadInt() (
	int,
) {
	return io.r.Int()
}


func (
	io *IO,
) Write(
	a ...interface{},
) {
	io.w.All(a...)
}



type Read struct {
	sc *bufio.Scanner
}


func (
	r *Read,
) Init() {
	r.setScanner()
	const buf = 1 << 20
	r.setBuf(buf)
}


func (
	r *Read,
) Int() (
	int,
) {
	s := r.Str()
	i, _ := strconv.Atoi(s)
	return i
}


func (
	r *Read,
) setBuf(
	bufSize int,
) {
	r.sc.Buffer(
		[]byte{},
		bufSize,
	)
}


func (
	r *Read,
) setScanner() {
	sc := bufio.NewScanner(
		os.Stdin,
	)
	sc.Split(
		bufio.ScanWords,
	)
	r.sc = sc
}


func  (
	r *Read,
) Str() (
	string,
) {
	sc  := r.sc
	sc.Scan()
	return sc.Text()
}



type Solver interface {
	Init()
	Input()
	Solve()
}


func Run(
	s Solver,
) {
	s.Input()
	s.Solve()
}



type Write struct {
	writer *bufio.Writer
}


func (
	w *Write,
) All(
	a ...interface{},
) {
	writer := w.writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}


func (
	w *Write,
) Init() {
	w.setWriter()
}


func (
	w *Write,
) setWriter() {
	w.writer = bufio.NewWriter(
		os.Stdout,
	)
}