## Problem
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

## Approach
The problem can be solved with DP. The hint suggests that:

> *Without loss of generality, there is a triangle that uses adjacent vertices A[0] and A[N-1] (where N = A.length). Depending on your choice K of it, this breaks down the triangulation into two subproblems A[1:K] and A[K+1:N-1].*

Thus we can say that the formula that describes the problem is:

$$f(i,j) = \begin{cases}0 & \text{when } i > j-2\\\displaystyle \min_{i<k<j}\{f(i,k)+f(k,j)+v[i]\cdot v[k]\cdot v[j]\}& \text{if } i \le j-2\end{cases} $$

The idea is always to consider the values $i,j$ as vertices of the triangle. Then the problem is very similar to the matrix chain multiply problem, except that we have $i \le j-2$. To solve the problem means to compute $f(1,n)$, and the solution is found in $M_{1n}$, where $M$ is the matrix in which we save the values of $f$.

