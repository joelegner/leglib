.. _numpy:

Numpy
=====

.. todo:: Consider using Numpy for adding up load combinations.

.. code-block:: python

   """Numpy proof of concept for leglib"""
   import numpy

   ITERATIONS = 100

   # Create two arrays: first is D and 2nd is L
   a = numpy.array([3.0, 1.0, 4.0, 1.0, 5.0])
   b = numpy.array([2.0, 7.0, 1.0, 8.0, 2.0])
   print "Array"
   # Print 1.4D + 1.6L
   print 1.4*a + 1.6*b

   # Create a matrix where the first row is D and 2nd is L
   m = numpy.matrix([[3.0, 1.0, 4.0, 1.0, 5.0],[2.0, 7.0, 1.0, 8.0, 2.0]])

   print "Matrix"
   print m
   # Print 1.4D + 1.6L
   print [1.4, 1.6]*m

   m = numpy.matrix([a, b])

   print "Matrix"
   print m
   # Print 1.4D + 1.6L
   print [1.4, 1.6]*m

