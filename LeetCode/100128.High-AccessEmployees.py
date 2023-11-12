class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # Helper function to convert time string to minutes
        def time_to_minutes(t):
            return int(t[:2]) * 60 + int(t[2:])

        # Create a dictionary to hold the access times for each employee
        employees = defaultdict(list)
        for name, time in access_times:
            employees[name].append(time_to_minutes(time))

        # Sort the times for each employee and find high-access employees
        high_access_employees = []
        for name, times in employees.items():
            times.sort()
            # Check for each time if there are at least two other access times within the same hour
            for i in range(len(times)):
                count = 1  # Start count as 1 for the current access time
                # Check the subsequent times to see if they are within the same hour
                for j in range(i + 1, len(times)):
                    if times[j] - times[i] < 60:
                        count += 1
                    else:
                        break  # No need to check further if the time difference is more than an hour
                if count >= 3:
                    high_access_employees.append(name)
                    break  # No need to check further if the employee is already identified as high-access

        return high_access_employees