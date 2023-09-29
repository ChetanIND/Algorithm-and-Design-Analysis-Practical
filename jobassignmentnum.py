# Write a program to implement job assignment problem using branch and bound
import sys
import heapq


class JobAssignmentProblem:
    def __init__(self, cost_matrix):
        # Initialize the problem with the given cost matrix
        self.cost_matrix = cost_matrix
        self.num_rows = len(cost_matrix)  # Number of workers (rows)
        self.num_cols = len(cost_matrix[0])  # Number of jobs (columns)
        self.best_solution = None  # Best assignment found so far
        self.best_cost = sys.maxsize  # Cost of the best assignment

    def calculate_lower_bound(self, start_row):
        # Calculate a lower bound for the remaining unassigned rows
        lower_bound = 0
        for i in range(start_row, self.num_rows):
            # Find the minimum cost in each row and add it to the lower bound
            min_cost = min(self.cost_matrix[i])
            lower_bound += min_cost
        return lower_bound

    def branch_and_bound(self):
        priority_queue = [
            (0, [], 0)
        ]  # Priority queue to store nodes (cost, assignment, row_index)

        while priority_queue:
            current_cost, current_assignment, row_index = heapq.heappop(priority_queue)

            # If the assignment is complete for all rows, check if it's better than the best solution
            if row_index == self.num_rows:
                if current_cost < self.best_cost:
                    self.best_solution = current_assignment
                    self.best_cost = current_cost
                continue

            # Calculate a lower bound for the current node
            lower_bound = current_cost + self.calculate_lower_bound(row_index)

            # If the lower bound is greater than or equal to the best cost, prune this node
            if lower_bound >= self.best_cost:
                continue

            # Branch into each column for the current row
            for col_index in range(self.num_cols):
                if col_index not in current_assignment:
                    new_cost = current_cost + self.cost_matrix[row_index][col_index]
                    new_assignment = current_assignment + [col_index]
                    heapq.heappush(
                        priority_queue, (new_cost, new_assignment, row_index + 1)
                    )

    def find_optimal_assignment(self):
        # Start the branch and bound process
        self.branch_and_bound()
        return self.best_solution, self.best_cost


if __name__ == "__main__":
    # Example cost matrix representing the cost of assigning each worker to each job
    cost_matrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]

    # Create an instance of the JobAssignmentProblem class
    job_assignment_problem = JobAssignmentProblem(cost_matrix)

    # Find the optimal assignment and its cost
    solution, cost = job_assignment_problem.find_optimal_assignment()

    # Print the results
    print("Optimal Assignment:", solution)
    print("Total Cost:", cost)
