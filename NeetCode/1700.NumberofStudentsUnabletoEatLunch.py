from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students who prefer each type of sandwich
        count = [students.count(0), students.count(1)]
        
        for sandwich in sandwiches:
            # If no student prefers the current sandwich, break
            if count[sandwich] == 0:
                break
            # Decrease the count of students who prefer the current sandwich
            count[sandwich] -= 1

        # Return the sum of the students left without their preferred sandwich
        return count[0] + count[1]
    # TC: O(n) where n is the length of students
    # Space complexity: O(1) since we use a constant space count

# Test processing function
def testCountStudents():
    testCases = [
        {
            "description": "Example 1",
            "students": [1,1,0,0],
            "sandwiches": [0,1,0,1],
            "expectedOutput": 0
        },
        {
            "description": "Example 2",
            "students": [1,1,1,0,0,1],
            "sandwiches": [1,0,0,0,1,1],
            "expectedOutput": 3
        }
    ]

    solution = Solution()
    for test in testCases:
        print("----------")
        print(test["description"])
        print("Expected output: {}".format(test["expectedOutput"]))
        print("Actual output: {}".format(solution.countStudents(test["students"], test["sandwiches"])))

if __name__ == "__main__":
    testCountStudents()