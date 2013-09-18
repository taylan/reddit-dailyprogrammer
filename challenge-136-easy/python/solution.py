
def main():
    inp = open("input.txt").read().splitlines()
    student_count = int(inp[0].split(' ')[0])
    assgn_count = int(inp[0].split(' ')[1])

    students = []
    for line in inp[1:]:
        params = line.split(' ')
        grades = [int(g) for g in params[1:]]
        students.append((params[0], sum(grades) / assgn_count))

    avg_grades = [grd for name, grd in students]
    print("{0:.2f}".format(sum(avg_grades) / student_count))
    [print(name, grd) for name, grd in students]

if __name__ == "__main__":
    main()