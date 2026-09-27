class Solution:
    def minimumMultiplications(self, arr, start, end):
        q = deque() #current_value , steps_takes 
        q.append((start , 0))
        visited = [False] * (100000)
        visited[start] = True
        while q:
            current_value , steps_taken = q.popleft()
            if current_value == end:
                return steps_taken
            for number in arr:
                new_val = (current_value * number ) % 100000 
                if visited[new_val] == False:
                    visited[new_val] = True
                    q.append((new_val, steps_taken + 1))

        return -1
                    




     