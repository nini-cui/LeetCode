#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#
from collections import deque

# @lc code=start
class deckRevealIncreasing:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        q = deque(range(len(deck)))

        for n in deck:
            i = q.popleft()
            res[i] = n

            if q:
                q.append(q.popleft())

        return res

        
# @lc code=end
if __name__ == "__main__":
    deckRevealIncreasing = deckRevealIncreasing()
    deckRevealIncreasing.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])

