'''
subarrays with product less than a target
'''
class solutions:
    def find_subarrays(self, arr, target):
        if arr is None:
            return None
        
        l = 0
        r = 0
        product = 1
        ans = []
        while l<= len(arr)-1 and r<=len(arr)-1:
            if l == r:
                product = arr[l]
                if product < target:
                    ans.append(arr[l:l+1])
                    if r < len(arr) - 1:
                        r += 1
                    else:
                        l += 1
                        r = l
                else:
                    l+=1
                    r+=1
            else:
                product *= arr[r]
                if product < target:
                    ans.append(arr[l:r+1])
                    if r < len(arr) - 1:
                        r += 1
                    else:
                        l += 1
                        r = l
                else:
                    l +=1
                    r = l
        return ans
            
arr = [8,2,6,5]
target = 50
solution = solutions()
solution.find_subarrays(arr, target)