with open("in.txt", mode="w") as f:
    f.writelines(["aaaaaaaaasadfasdf\n" for _ in range(1 << 20)])
