#

## Example

Points|RGB
-|-
(2,0)|(1.0.1,0.2)
(1,1)|(0,1,1)
(3,2)|(0.2,0.3,0.4)

If we want the RGB at point (1.5, 0.8), the contribution is determined by the coefficients of the affine combination of (1.5, 0.8) in terms of the 3 points $\vec{y}-\vec{v}_1, \vec{v_2}-\vec{v_1}, \vec{v_3}-\vec{v_1}$ 

$\begin{bmatrix} 2 & 1 & 3 & 1.5 // 0 & 1 & 2 & 0.8 // 1 & 1 & 1 & 1 \end{bmatrix}$
$\begin{bmatrix} 1 & 0 & 0 & 0.3 // 0 & 1 & 0 & 0.6 // 0 & 0 & 1 & 0.1 \end{bmatrix}$

RGB values are $0.3(1,0.1,0.2)+0.6(0,1,1)+0.1(0.2,0.3,0.4) = (0.32,0.66,0.7)$

We know the affine coordinates sum to one by definition -- but how do we know they're all positive? It's inuitive geometrically that any point we sample inside of a triangle which is bounded by all-positive-coordinate vertices will have all positive coordinates. This isn't generally true for *any* shape we construct out of these points.

**Def**: a **convex combination** of $\vec{v}_1, ..., \vec{v}_m$ is a linear combination $\sum c_i \vec{v_i}$ such that $\sum c_i = 1$ *and* $c_1, ..., c_m \geq 0$.

**Ex**: that is the set of convex combinations for 2 points $\vec{v}_1, \vec{v}_2$?

$$\vec{y} = c_1\vec{v}_1+c_2\vec{v}_2, c_1+c_2=0, c_1, c_2 \geq 0 \\
- c_1\vec{v}_1+(1-c_1)\vec{v}_2 \text{ since } c_2 = 1-c_1\\
= \vec{v_2}+c_1(\vec{v}_1+\vec{v}_2) \\
0 \leq c_1 \leq 1 \text{ because } c_2=1-c_1 \geq 0 \text{ and } c_1 \geq 0$$

Therefore, it is a line segment (part of a line where line parameter is bounded between 0 and 1)

**Def**: The **convext hull** $\text{conv}(S)$ is the set of all convex combinations of a set of points S.

**Def**: A set is **convex** if for every pair of points in $S$, the line segment between them is also in $S$. 

If we wanted to take a triangle with vertices $v_1, v_2, v_3$, we can divide $\mathbb{R}^2$ into seven convex regions:

![](02-07-Fig2.png)

What are the signs of the coefficients in each of these regions? (e.g. signs of $c_1, c_2, c_3$ for point $\vec{y} = c_1\vec{v}_1+c_2\vec{v}_2+c_3\vec{v}_3$)

For example, take the cyan region above. We can determine the sign of the value for coefficient. e.g., $c_1$ by looking at the line formed by the points besides $\vec{v}_1$ (i.e. line containing $\vec{v}_2$ and $\vec{v}_3$). If the point is on the *same* side of that line as $\vec{v}_1$, then $c_1>0$; if it's on the opposite side, then $c_1 < 0$.

![](02-07-Fig3.png)

Using this, we can determine the signs of all the regions:

[TODO]

### Section 2.4: Singular Value Decomposition (SVD)

**Thm**: Let $A$ be an $m$ by $n$ matrix. Then we can write $A = U\Sigma V^T$, where:
- $U$ is an *orthogonal* $m$ by $m$ matrix (i.e. rows and columns are orthogonal unit vectors -- their magnitudes are 1, and the dot product of each pair is 0)
- $\Sigma$ is an $m$ by $n$ matrix where all values are entries are $0$ except for $\sigma_{ii}$ where $i$ is between 0 and some value $k \leq \min(m,n)$ (i.e. the diagonal for some $k$ by $k$ upper left submatrix):

![](02-07-Fig5.png)

These **singular values** $s_1, ..., s_n$ are all positive and non-increasing -- $s_1 \leq s_2 \leq ... > 0$

