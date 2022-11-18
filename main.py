def bin_to_dec(i:int) -> int:
    x = [int(o) for o in str(i)];
    for y in range(0, len(x)):
        x[y] = x[y]*(2**y);
    return sum(x);

print(str(int(input("Binario > "), 2))+ "," + str(bin_to_dec(int(input("Virgola > ")))));
