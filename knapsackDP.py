# Write a program to implement 1/0 knapsack problem using dynamic programming
def knapsack(values, weights, capacity):
    # Get the number of items (n)
    n = len(values)

    # Create a 2D array (dp) to store the maximum values for different capacities and items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Building the dynamic programming table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # If the current item can be included in the knapsack, we have two choices:
                # 1. Include the item and add its value to the maximum value obtained without it.
                # 2. Exclude the item and keep the maximum value obtained without it.
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                # If the current item's weight exceeds the current capacity, we can't include it,
                # so just copy the maximum value obtained without it.
                dp[i][w] = dp[i - 1][w]

    # Find the items included in the knapsack
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            # If the value in the table changed, it means the item was included in the knapsack.
            # So, add its index (i-1) to the selected_items list.
            selected_items.append(i - 1)
            j -= weights[
                i - 1
            ]  # Reduce the remaining capacity by the weight of the included item.
        i -= 1  # Move to the previous item

    # Return the maximum value and the list of selected items
    return dp[n][capacity], selected_items[::-1]


if __name__ == "__main__":
    # Input values, weights, and capacity from the user
    n = int(input("Enter the number of items: "))
    values = []
    weights = []
    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))

        values.append(value)
        weights.append(weight)

    capacity = int(input("Enter the capacity of the knapsack: "))

    # Calculate the maximum value and selected items
    max_value, selected_items = knapsack(values, weights, capacity)

    # Display the results
    print("Maximum Value:", max_value)
    print("Selected Items:", selected_items)
