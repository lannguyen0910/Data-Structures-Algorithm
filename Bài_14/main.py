# Number of vertices in the graph
V = 4

# A naive recursive function to count
# walks from u to v with k edges

"""
Simple Approach: Create a recursive function that takes the current vertex, destination vertex, 
and the count of the vertex. Call the recursive function with all adjacent vertices of a current vertex 
with the value of k as k-1. When the value of k is 0, then check whether the current vertex is the destination 
or not. If destination, then the output answer is 1."""


def countwalks(graph, u, v, k):

    # Base cases
    if (k == 0 and u == v):
        return 1
    if (k == 1 and graph[u][v]):
        return 1
    if (k <= 0):
        return 0

    # Initialize result
    count = 0

    # Go to all adjacents of u and recur
    for i in range(0, V):

        # Check if is adjacent of u
        if (graph[u][i] == 1):
            count += countwalks(graph, i, v, k-1)

    return count


"""
Time Complexity: O(V^k). 
The worst-case time complexity of the above function is O(V^k) where V is the number of vertices in the given graph.
We can simply analyze the time complexity by drawing a recursion tree. The worst occurs for a complete graph.
In the worst case, every internal node of the recursion tree would have exactly n children.

Auxiliary Space: O(V). 
To store the stack space and the visited array O(V) space is needed.
"""


# A Dynamic programming based function
# to count walks from u to v with k edges

"""The solution can be optimized using Dynamic Programming. 
The idea is to build a 3D table where the first dimension is the source, the second dimension is the destination, 
the third dimension is the number of edges from source to destination, and the value is the count of walks.
Like others, Dynamic Programming problems, fill the 3D table in a bottom-up manner."""


def countwalks2(graph, u, v, k):

    # Table to be filled up using DP.
    # The value count[i][j][e] will/
    # store count of possible walks
    # from i to j with exactly k edges
    count = [[[0 for k in range(k + 1)]
              for i in range(V)]
             for j in range(V)]

    # Loop for number of edges from 0 to k
    for e in range(0, k + 1):
        for i in range(V):
            # For source
            for j in range(V):

                # For destination

                # Initialize value
                count[i][j][e] = 0

            # From base cases
            if (e == 0 and i == j):
                count[i][j][e] = 1
            if (e == 1 and graph[i][j] != 0):
                count[i][j][e] = 1

            # Go to adjacent only when number
            # of edges is more than 1
            if (e > 1):

                for a in range(V):

                    # Adjacent of i
                    if (graph[i][a] != 0):
                        count[i][j][e] += count[a][j][e - 1]

    return count[u][v][k]


graph = [[0, 1, 1, 1, ],
         [0, 0, 0, 1, ],
         [0, 0, 0, 1, ],
         [0, 0, 0, 0]]

u = 0
v = 3
k = 2
print(countwalks2(graph, u, v, k))

# Time Complexity: O(V^3*k).
# Three nested loops are needed to fill the DP table, and loop k edges, so the time complexity is O(V^3*k).
# Auxiliary Space: O(V^3).
# To store the DP table O(V^3) space is needed.
