#Time complexity : O(n)
#Space complexity: O(1)
#Works on leetcode : yes
#Approach : For an efficient approach, we just need to calculate the product in format (a+1)*(b+1)*(c+1)....-1 for 
#input [a,b,c....]

def productOfSubsetSums(arr): 
    ans = 1
    for i in range(len(arr)): 
        ans = ans * (arr[i] + 1) 
    return ans-1