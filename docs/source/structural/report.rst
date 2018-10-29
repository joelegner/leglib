.. _report:

:mod:`report` -- Structural report generation
=============================================

.. class:: report

   The Report class allows you to generate reports of any format if a template
   file has been written. For example:

   .. code-block:: python

      >>> from structural.report import Report
      >>> from structural.footing import FootingPierAssembly
      >>> m = FootingPierAssembly(B=5.0, L=5.0, T=1.5, Lp=2.0, Bp=2.0, Hp=3.0, \
      >>>       gamma_c=0.145, gamma_s=0.090)
      >>> r = Report(m)
      >>> print r.render("txt")
      Legner Structural Engineering Library

      Footing/Pier Assembly
      =====================
      Footing
          Length,    L = 5.00 ft = 5'-0"
      ...
      
