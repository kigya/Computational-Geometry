# Computational Geometry and Computer Graphics

## Lab1

> **Task 1.**
Given: Points p1(x1, y1), p2(x2, y2), p0(x0, y0)
It is necessary: To determine the position of point p0 relative to a straight line passing
through points p1 and p2 (“on the straight line“ or ”to the left", “to the right” of the straight line). The direction
on the straight line from p1 to p2.
Notes: as a result, a message about the position of the point
and a picture with the image of three signed points and a straight line are displayed.
**Task 2.**
Given: Points
p1(x1, y1), p2(x2, y2),
p3(x3, y3), p4(x4, y4)
Need to: Determine whether the segments p1p2 and p3p4 intersect?
Notes: as a result, a position message is issued
segments and a picture with the image of segments.
**Task 3.**
Given: P = {p1(x1, y1), p2(x2, y2), ...,pn(xn, yn)}
It is necessary: To determine whether the polygon P is a simple polygon?
Notes: as a result, a message and a picture with
the image of a polygon with signed vertices are output.
> 

## Lab2

> 
> 
> 
> Given: P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} is a simple polygon;
> p0(x0, y0) is a point.
> It is necessary: Using the “ray test" to determine the position of the point p0
> relative to the polygon P.
> Notes: as a result, a message and a picture with
> the image of a point and a polygon with signed vertices are displayed.
> The first stage is to implement the “dimensional test".
> If the ray hits the vertex of the polygon, handle this
> situation (do not generate a new ray).
> 

## Lab3

> 
> 
> 
> Given:
> P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} is a simple polygon;
> Q = {q1(x1, y1), q2(x2, y2), … ,qm(xm, ym)} – convex polygon;
> The polygon P is inside the polygon Q. Between these
> polygons (inside Q and outside P), k points of the set S
> are given (for example, see the figure). Create an animation of the movement of points S inside
> the polygon Q with reflection from its walls. When a point gets inside
> the polygon P, its velocity is reset to zero.
> When performing the task, the following algorithms must be implemented:
> 
> - “angle test” through octanes to determine the position of a point
> relatively simple polygon;
> - “binary test” to determine the position of a point relative
> to a convex polygon.

## Lab4

> 
> 
> 
> Given:
> P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} is an arbitrary set of points on
> the plane.
> It is necessary: Using the “Graham algorithm” to build a convex hull
> sets of P.
> Notes: as a result, an animation is created in which
> a polyline is displayed, built on the elements of the stack accumulating
> the vertices of the convex hull (any change in the stack is a new
> animation frame).
> 

## Lab5

> 
> 
> 
> Given:
> Let D be some given constant and P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} be
> an arbitrary set of points on the plane.
> It is necessary to implement an animation in which the points move with
> constant speeds and directions. As soon as the distance between
> two points becomes greater than In, these two points change their
> speeds to opposite ones.
> Notes: At each step of the animation, it is necessary to find the two most
> distant points using the algorithm for finding the “diameter of the set”.
> The first step of this algorithm is to construct a convex hull,
> which must be implemented by the “Jarvis algorithm".
> 

## Lab6

> 
> 
> 
> Given:
> Let S be some given constant and P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} be
> an arbitrary set of points on the plane.
> It is necessary to implement an animation in which the points move with
> constant speeds and directions. As soon as the perimeter of the convex
> hull becomes larger than S, all the vertices of the shell change their
> velocities to the opposite.
> Notes: At each step of the animation, a convex hull is constructed
> using the “Quick Hull” algorithm.
> 

## Lab7

> 
> 
> 
> Given:
> P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} is an arbitrary set of points on
> the plane, and the points in the set are not generated immediately, but
> sequentially one after the other.
> It is necessary to implement the construction of a convex hull for each of
> the states of the set P and create the appropriate animation.
> Notes: The problem is solved by the "Dynamic Convex
> Hull" algorithm (see lectures).
> 

## Lab8

> 
> 
> 
> Given:
> P = {p1(x1, y1), p2(x2, y2), … ,pn(xn, yn)} – convex polygon (the inner
> area is filled with color 1);
> Q = {q1(x1, y1), q2(x2, y2), … ,qm(xm, ym)} – convex polygon (the inner
> area is filled with color 2);
> Polygons P and Q move towards each other, starting from some
> the steps intersect and pass through.
> It is necessary to create the appropriate animation. At each step
> of the animation, fill the intersection area with color 3. In addition, in
> the polygon P, draw a segment connecting the vertices with the indices
> 1 and 3. At each step of the animation, build a clipping of this segment
> polygon Q and highlight with color.
> When performing the task, the following algorithms must be implemented:
> 
> - algorithm of intersection of two convex polygons;
> - the Cyrus-Beck algorithm for finding the clipping of a segment by a convex
> polygon.

## Lab9

> 
> 
> 
> Given:
> P = {p1(x1, y1), p2(x2, y2), ...,pn(xn, yn)} is an arbitrary set of points on
> the plane, inside the rectangle A(xA, yA), B(xA, yB), C(xc, yB), D(xC, yA). R is
> some fixed number.
> It is necessary: to create an animation of the movement of balls (circles of radius R) with centers at
> points from P. When colliding with the side from ABCD, the balls are reflected. When
> two balls collide with each other, their speeds change to the
> opposite.
> Notes: on each frame of the animation, an algorithm is implemented to find the two
> closest elements in the set P (see lectures). If the distance between
> if the nearest elements found are less than 2* R, then we assume that
> the balls collided.
> If desired, you can slightly modify the algorithm and find not only
> the nearest, but all the "colliding" balls.
> 

## Lab10

> 
> 
> 
> Given:
> P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} is an arbitrary set of points on
> the plane.
> It is necessary: to implement the construction of the Delaunay triangulation (by any algorithm).
>
