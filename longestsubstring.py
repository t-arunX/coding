def maxelement():
    cnt=0
    for k in range(len(count)):
        if(count[k]>cnt):
            cnt=count[k]
    return cnt

def check(val):
    if val in arr:
        count.append(len(arr))
        temp = arr[-1]
        arr.clear()
        arr.append(temp)
    else:
        arr.append(val)

def lls(s):
    if s == " " or s == "":
        return 0
    else:
        for j in range(len(s)):
            check(s[j])
    return max(count)

val =0
arr = list()
count = list()

print(lls("abcabcbb"))
