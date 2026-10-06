class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        n = len(cardScore)

        # Initially take k cards from the left
        curr = sum(cardScore[:k])
        res = curr

        # Gradually replace left cards with right cards
        for i in range(1, k + 1):
            curr -= cardScore[k - i]
            curr += cardScore[n - i]
            res = max(res, curr)

        return res
