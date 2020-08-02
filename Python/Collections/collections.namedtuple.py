import collections

N = int(input())
columns = ','.join(input().split())
Student = collections.namedtuple('Student', columns)

sum = 0
for i in range(N):
    line = input().split()
    student = Student(*line)
    sum += int(student.MARKS)

print(sum/N)
