def most_frequent(List):
    set(List)
    return max( key = List.count)
 
T = int(input())
for i in range(0,T):
    N = int(input())
    A = [int(i) for i in input().split(" ",N-1)]
    value = most_frequent(A)
    rep=A.count(value)
    # print(rep)
    print(N-rep)