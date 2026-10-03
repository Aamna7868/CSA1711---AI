from itertools import permutations

letters = "SENDMORY"

digits = range(10)

for p in permutations(digits, len(letters)):
    S, E, N, D, M, O, R, Y = p

    # S and M cannot be zero
    if S == 0 or M == 0:
        continue

    SEND = 1000*S + 100*E + 10*N + D
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    if SEND + MORE == MONEY:
        print("Solution found:")
        print("S =", S)
        print("E =", E)
        print("N =", N)
        print("D =", D)
        print("M =", M)
        print("O =", O)
        print("R =", R)
        print("Y =", Y)

        print("\n", SEND)
        print("+", MORE)
        print("------")
        print(MONEY)
        break