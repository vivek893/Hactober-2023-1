# we added a HackerRank problem. Find the  runner-up score . i write  a code in python for finding runner-up score.
def runner_score(l):
    l1=sorted(l)
    for i in range(len(l1)-1,0,-1):
        if l1[i]!=l1[i-1]:
            return l1[i-1]
   
# make a list:
l=[int(s) for s in input().split()]

print("runner_score",runner_score(l))
