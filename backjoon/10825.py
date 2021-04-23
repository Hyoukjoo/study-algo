import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    name, *scores = input().split()
    students.append([name, *list(map(int, scores))])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])