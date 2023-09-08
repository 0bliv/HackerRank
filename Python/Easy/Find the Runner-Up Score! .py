if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = list(set(arr))
    
    if len(score) < 2:
        print("ERROR")
    else:
        score.sort(reverse=True)
        print(score[1])