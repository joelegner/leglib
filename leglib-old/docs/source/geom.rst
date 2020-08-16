:mod:`geom` -- 2D geometry classes and functions
================================================

.. todo:: Add tests for ``geom`` module.


.. todo:: Consider replacing this whole mess with sympy.geometry: http://docs.sympy.org/dev/modules/geometry.html


.. function:: dist(pt1, pt2)

   Returns distance between two points

.. class:: Point(x, y)

   Represents a 2D point in space with at (*x*, *y*)

   .. function:: move(dx, dy)

      Translate *x = x + dx* and *y = y + dy*.

   .. function:: rotate(angle, base_pt=None)

      Rotate the point *angle* radians about *base_pt* or about the origin if
      *base_pt* is not passed to the function.

   .. function:: get_tuple()

      Returns coordinates as a tuple (*x*, *y*).

   .. function:: dist(other)

      Returns distance from the point to an *other* point or line.

   .. function:: copy(dir_vec)

      Returns a new point translated by *dir_vec* vector.

.. class:: Line(pt1, pt2)

   Infinite 2D line passing through two specified points: *pt1* and *pt2* which
   are instances of ``Point``.

   .. data:: x1

      Start point *x* coordinate.

   .. data:: y1

      Start point *y* coordinate.

   .. data:: x2

      End point *x* coordinate.

   .. data:: y2

      End point *y* coordinate.

   .. function:: midpoint()

      Returns mid ``Point``.

   .. function:: length()

      Returns length scalar.

   .. function:: vertical()

      Returns true if the line is vertical.

   .. function:: slope()

      Returns the slope (rise/run) or ``None`` if the line is vertical.

   .. function:: yintercept()

      Returns the y-intercept value of the line.

   .. function:: intersection(other)

      Returns ``Point`` of intersection with *other* ``Line``.

   .. function:: in_bbox(point)

      Returns ``True`` if *point* is between end points in both directions.

   .. function:: rotate(angle, base_pt)

      Rotates the end points *angle* radians about *base_pt* or origin if
      *base_pt* is omitted.

   .. function:: bearing()
      
      Returns the bearing angle of the line in radians.

   .. function:: angle_of_int(line):

      Returns the angle of intersection with another *line*.

   .. function:: offset(dist, to_left=True)

      Offsets the line *dist* to left if *to_left* is true or to right otherwise.

   .. function:: offset_left(dist)

      Offsets the line *dist* to left.

   .. function:: offset_right(dist)

      Offsets the line *dist* to right.

   .. function:: dir_vector()

      Returns unity direction vector (x, y) as tuple.

   .. function:: copy(d)

      Returns a new line where *d* is a translation tuple (*dx*, *dy*).

   .. function:: dist_to_pt(point)

      Returns distance to a point.

.. class:: Ray(pt1, pt2)
    
   A 2D ray projecting from pt1 through pt2.  Extends ``Line``.

   .. function:: intersection(other)

      Returns point of intersection with another line.

.. class:: Segment(point1, point2)

   Simple 2D line segment.

   .. function:: midpoint()

      Returns mid ``Point``.

   .. function:: frac_loc(fraction)

      Returns a ``Point`` which is *fraction* from ``point1`` to ``point2``.

   .. function:: fraction(pt_along)

      Returns ratio of distance from ``point1`` to length of segment.

   .. function:: length()

      Returns length of segment.

   .. function:: lengthen1(dist)

      Moves ``point1`` so that length increases by *dist*.

   .. function:: lengthen2(dist)

      Moves ``point2`` so that length increases by *dist*.

   .. function:: lengthen(dist)

      Lengthen about midpoint by *dist*, moving both endpoints.

   .. function:: shorten(dist)

      Shorten about midpoint by *dist*, moving both endpoints.

   .. function:: intersection(other)

      Returns ``Point`` of intersection with *other* ``Line``, extending
      as necessary.

   .. function:: clip(rect)

      Returns new segment object which is clipped by specified rectangle.

   .. function:: in_bbox(point)

      Returns ``True`` if *point* is within bounding box formed by end points.

   .. function:: dist_to_pt(point)

      Returns distance between a point and the line.

.. class:: Level(z)

    Notional member which defines horizontal (x, y) plane with *z* coordinate.

.. class:: Polygon(points)

   A polygon of *point*.  Must have at least 3 points.

   ``len()`` returns number of points.

   .. function:: area()

      Returns area of polygon.


   .. function:: rotate(angle, base_pt=None)

      Rotate the polygon *angle* radians about *base_pt* or about the origin if
      *base_pt* is not passed to the function.

   .. function:: point_within(point)

      Returns ``True`` if point falls inside polygon.

   .. function:: offset(dist=1.0, outward=True)

      Offsets the polygon inward or outward by *dist*.

   .. function:: get_segments()

      Returns a list of all line segments.

.. class:: Rectangle(pt1, pt2)

   .. function:: intersection(other)

      Returns a list of intersection points where *other* is a line or a
      segment.

   .. function:: inside(other)

      Returns ``True`` if *other* is a ``Point`` or ``Segment`` falling inside
      the rectangle.


.. class:: Vector(x=1, y=0)

    General 2-dimensional vector.

   .. function:: norm()

      Returns length of vector.

   .. function:: unit_vector()

      Returns a unit vector in the same direction.

   .. function dot(other)

      Returns vector dot product with *other* vector.

   .. function cross(other)

      Returns vector cross product with *other* vector.

   .. function perp()

      Returns a perpendicular vector.

