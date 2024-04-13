#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#
from typing import List

# @lc code=start
class Tickets:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # the number of tickets to buy: tickets[k]
        # the number of people in front of him: k
        ticket_num = tickets[k]
        
        if ticket_num == 0:
            return 0

        if ticket_num == 1:
            return (k + 1)
        
        if ticket_num >= 2:
            total_time = 0
            total_time += len(tickets)

            for iter_num in range((ticket_num - 2)):
                tickets = [(ticket - 1) if ticket != 0 else ticket for ticket in tickets]
                not_null_count = sum(x != 0 for x in tickets)
                total_time += not_null_count

            tickets = [(ticket - 1) if ticket != 0 else ticket for ticket in tickets]
            tickets = tickets[0:k+1]
            not_null_count = sum(x != 0 for x in tickets)

            total_time += not_null_count

            return total_time
        
# @lc code=end

if __name__ == "__main__":
    tickets = Tickets()
    # tickets.timeRequiredToBuy([2, 3, 2], k=2)
    tickets.timeRequiredToBuy([5, 1, 1, 1], k=0)
    # tickets.timeRequiredToBuy([88,76,77,82,62,20,26,72,45,54], k=2)

