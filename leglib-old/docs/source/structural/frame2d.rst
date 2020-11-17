.. _frame2d:

:mod:`frame2d` -- Simple 2D Frame Analysis
==========================================

.. class:: Frame2D

   This class allows the direct stiffness method analysis of a 2D frame.  It is
   a combination of nodes, members and nodal forces.

   .. function:: support_nodes()
     
      Returns list of nodes which have a boundary condition

   .. function:: renumber_nodes()
     
      Renumbers nodes left to right, bottom to top

   .. function:: node_ids()

      Returns sorted node id's

   .. function:: add_node(x, y)

      Creates a new *Node* object at coordinates *(x, y)*.

   .. function:: add_member(i, j, A=1.0, E=1.0, I=1.0)

      Creates a new *FrameMember* object from node *i* to node *j*.

   .. function:: add_pin(i)

      Changes node *i* to a pinned support.

   .. function:: add_roller_x(i)

      Changes node *i* to a roller support (free in *x* direction).

   .. function:: add_roller_y(i)

      Changes node *i* to a roller support (free in *y* direction).

   .. function:: fixed(i)

      Changes node *i* to a fixed support.

   .. function:: build_K()

      Create an empty global stiffness matrix.

   .. function:: validate()

      Check frame for various problems.

   .. function:: analyze()

      Solves the analysis problem using numpy matrix methods.

      Returns a dictionary ``{ "reactions" : R, "deflections" : U }`` where
      ``R`` is a list of 3-tuples ``(P, V, M)`` of axial (``P``), shear
      (``V``) and moment (``M``) reactions.

      ``U`` is a list of deflections at each node in 3 degrees of freedom.


.. class:: Node(frame, id, x, y)

   A node is a joint within the structure.  The *frame* is the main ``Frame2D``
   instance for the structure.  *id* is a node number and *x* and *y* are
   2D coordinates locating the node.

   A node is typically not directly instanced but is created by the Frame3D
   function ``add_node()``.

.. class:: FrameMember(frame, id, i_node, j_node, A=1.0, E=1.0, I=1.0)

   This is a member which extends between two Nodes: the starting node is the
   ``i_node`` and the ending node is the ``j_node`` which are instances of
   ``Node``.  The *frame* is the structure's ``Frame2D`` instance. *A* is the
   member's cross-sectional area, *E* is its modulus of elasticity and *I* is
   its moment of inertia.


   A frame member is typically not directly instanced but is created by the
   Frame3D function ``add_member()``.


   .. function:: add_uniform(kips_per_inch)
      
      Append a uniform load to the list of uniform loads.

   .. function:: add_point(kips, x)

      Append a point load with *kips* kips at location *x* from the *i_node*.

   .. function:: t()
      
      Returns transformation matrix for member.

   .. function k()

      Returns element stiffness matrix in global coordinates.

   .. function:: ue(u)
        
      Recover member displacements given global displacements.

   .. function:: Fe(u)

      Recover member forces, Fe, given global displacements, *u*

   .. function:: fef()

      Returns fixed-end forces in local coordinates. 
      (Pi, Vi, Mi, Pj, Vi, Mj)

   .. function:: dofs():
      
      Returns degrees of freedom for the member.

   .. function:: DoFs()

      Returns global degrees of freedom for the member.


.. todo:: Outline the procedure for analysis including load cases.  Use BEARS BeamColumn class as the basis.

.. todo:: Document how Frame2D works.

.. todo:: Create new BeamColumn class.

.. todo::

   Add some tests for BeamColumn class with uniform and point loads, checking for
   shear, moment, deflection.


.. literalinclude:: ../../../structural/frame2d.py
   :language: python

