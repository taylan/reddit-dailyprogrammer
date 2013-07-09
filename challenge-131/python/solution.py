

tokens = [tok for tok in [line.split(" ") for line in open("input.txt").read().splitlines()] if len(tok) == 3 or tok[0] in ["0", "1"]]

for t in tokens:
    print("Good test data" if (t[1][::-1] if t[0] == "0" else t[1].upper()) == t[2] else "Mismatch! Bad test data")
