if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    resp = student_marks[query_name] 
    final = sum(resp)/3
    formated_final = f"{final:.2f}"
    print(formated_final)
