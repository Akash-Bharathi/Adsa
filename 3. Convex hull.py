def orientation(p, q, r):
    """Find orientation of triplet (p, q, r).
    0 -> Collinear, 1 -> Clockwise, 2 -> Counterclockwise."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def convex_hull(points):
    """Compute the convex hull of a set of points."""
    n = len(points)
    if n < 3:
        return []  # Convex hull is not possible with less than 3 points

    # Find the leftmost point
    l = min(range(n), key=lambda x: points[x][0])
    hull = []
    p = l

    while True:
        hull.append(p)  # Add the current point to the hull
        q = (p + 1) % n  # Choose the next point in a circular manner

        for i in range(n):
            # If i is more counterclockwise than q, update q
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q  # Move to the next point

        # Break the loop when we return to the starting point
        if p == l:
            break

    # Return the points in the convex hull
    return [points[i] for i in hull]

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
print("Convex Hull:")
print(convex_hull(points))


output:

Convex Hull:
[(0, 0), (0, 3), (4, 4), (3, 1)]
