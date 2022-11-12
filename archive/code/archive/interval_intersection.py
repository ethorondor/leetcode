'''
interval intersaction
find overlaping interval of two lists of intervals
'''
class solutions:
    def interval_intersaction(self, l1, l2):
        res = []
        for j in range(len(l2)):
            for i in range(len(l1)):
                if max(l2[j][0],l1[i][0]) <= min(l2[j][1],l1[i][1]):
                    overlap_start = max(l2[j][0],l1[i][0])
                    overlap_end = min(l2[j][1],l1[i][1])
                    res.append([overlap_start, overlap_end])
                else:
                    pass
        return res
    
l1 = [[1,3],[5,6],[7,9]]
l2 = [[2,3],[5,7]]
solution = solutions()
solution.interval_intersaction(l1,l2)