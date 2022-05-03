private func readStrings() -> [String] {
    return readLine()!.split(separator: " ").map { String($0) }
}

private func readInts() -> [Int] {
    return readLine()!.split(separator: " ").map { Int($0)! }
}

func main() {
    let label = 50

    print(label)

    let a = Int(readLine()!)!
    print(a)

    let b = readLine()!.split(separator: " ").map { Int($0)! }
    print(b)

}

main()
