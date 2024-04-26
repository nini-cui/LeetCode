#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#
from typing import List
from collections import Counter

# @lc code=start
class eatSandwiches:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if not students or not sandwiches:
            return 0
        
        while True:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                student_first_elem = students[0]
                students.pop(0)
                students.append(student_first_elem)

            if len(set(students)) == 1 and students[0] != sandwiches[0]:
                return len(students)
            
            if len(students) == 0:
                return 0
# @lc code=end

if __name__ == "__main__":
    eatSandwiches = eatSandwiches()
    # eatSandwiches.countStudents([1,1,0,0], [0,1,0,1])
    eatSandwiches.countStudentsLen([0,1,1,0,1,1], [0,0,0,1,1,0])