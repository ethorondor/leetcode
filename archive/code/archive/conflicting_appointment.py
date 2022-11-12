'''
conflicting appointment
given an array of intervals representing N appointment, find out if a person can attend all the appointments
'''
class solutions:
    def conflicting_appointment(self, l):
        l.sort(key=lambda x:x[0])
        start = l[0][0]
        end = l[0][1]
        for i in range(1,len(l)):
            if l[i][0] < end:
                return False
            else:
                end = l[i][1]
        return True
    
l = [[1,4],[2,5],[7,9]]
solution = solutions()
solution.conflicting_appointment(l)