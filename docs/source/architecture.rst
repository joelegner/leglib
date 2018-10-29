.. _architecture:

leglib Architecture
===================

This section documents the overall design concept of leglib and :mod:`leglib.structural` in particular.

::

   leglib
   |
   +--- Core
   |
   +--- Structural
           |
           +--- Components
           |
           +--- Compositions


Decoupling
----------

The basic means of de-coupling in leglib involves the use of *Compositions* and *Components*.

Composition
   A class which constructs instances of component classes to perform a task.  For example, the :class:`DriftCalc` class creates component instances for :class:`Roof`, :class:`Building`, and :class:`Site` in its ``_init_components()`` method.

Component
   An independent class that abstracts one real world thing.  For example, a :class:`Building`.

The basic sequence is:

1. Create a composition instance:

   .. code-block:: python
   
      calc = DriftCalc(pg=30, ... )

#. Call a method which needs the components:

   .. code-block:: python
   
      calc.report()

#. The method creates components as needed:

   .. code-block:: python

      def report(self):
         self._init_components()
         ...
   
      def _init_components(self):
         self._site = Site(self.pg)
         ...

