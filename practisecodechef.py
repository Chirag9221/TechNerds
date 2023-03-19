# def fre(A):
#     count = A.

# T = int(input())
# for i in range(0,T):
#     N = int(input())
#     A = [int(i) for i in input().split(" ",N-1)]
#     print(fre(A))



# # Program to find most frequent
# # element in a list
 
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
 
    return counter
 
List = [2, 1, 1,2]
print(most_frequent(List))