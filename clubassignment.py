import sys
import heapq


class ClubAssignmentProblem:
    def __init__(self, cost_matrix):
        # Initialize the problem with the given cost matrix
        self.cost_matrix = cost_matrix
        self.num_agents = len(cost_matrix)  # Number of students/clubs
        self.best_solution = None  # Best assignment found so far
        self.best_cost = sys.maxsize  # Cost of the best assignment

    def calculate_lower_bound(self, start_agent):
        # Calculate a lower bound for the remaining unassigned agents
        lower_bound = 0
        for i in range(start_agent, self.num_agents):
            # Find the minimum cost in each row (agent) and add it to the lower bound
            min_cost = min(self.cost_matrix[i])
            lower_bound += min_cost
        return lower_bound

    def branch_and_bound(self):
        priority_queue = [
            (0, [], 0)
        ]  # Priority queue to store nodes (cost, assignment, agent_index)

        while priority_queue:
            current_cost, current_assignment, agent_index = heapq.heappop(
                priority_queue
            )

            # If the assignment is complete for all agents, check if it's better than the best solution
            if agent_index == self.num_agents:
                if current_cost < self.best_cost:
                    self.best_solution = current_assignment
                    self.best_cost = current_cost
                continue

            # Calculate a lower bound for the current node
            lower_bound = current_cost + self.calculate_lower_bound(agent_index)

            # If the lower bound is greater than or equal to the best cost, prune this node
            if lower_bound >= self.best_cost:
                continue

            # Branch into each club for the current student
            for club_index in range(self.num_agents):
                if club_index not in current_assignment:
                    new_cost = current_cost + self.cost_matrix[agent_index][club_index]
                    new_assignment = current_assignment + [club_index]
                    heapq.heappush(
                        priority_queue, (new_cost, new_assignment, agent_index + 1)
                    )

    def find_optimal_assignment(self):
        # Start the branch and bound process
        self.branch_and_bound()
        return self.best_solution, self.best_cost


if __name__ == "__main__":
    # Example cost matrix representing the cost of assigning each student to each club
    cost_matrix = [[9, 2, 7], [6, 4, 3], [5, 8, 1]]

    # Create an instance of the ClubAssignmentProblem class
    club_assignment_problem = ClubAssignmentProblem(cost_matrix)

    # Find the optimal assignment and its cost
    solution, cost = club_assignment_problem.find_optimal_assignment()

    # Print the results
    print("Optimal Assignment:", solution)
    print("Total Cost:", cost)
