n = int(input("Enter Score: "))
arr = list(map(int, input().split()))

max_score = max(arr)
while max_score in arr:
    arr.remove(max_score)

runner_up = max(arr)
print(runner_up)