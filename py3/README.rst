================================================================================================
bisos.sites: Manages the /bisos/var/sites symlink base, /bisos/site, and site registrar services
================================================================================================

.. contents::
   :depth: 3
..

Overview
========

bisos.sites is a python package for managing BISOS Sites – the
``/bisos/var/sites`` symlink base, the ``selected`` and per-site
symlinks under it, and the ``/bisos/site`` symlink that BISOS tooling
ultimately resolves through. It also umbrellas site registrar
(boxes/containers inventory and performer) services.

bisos.sites is the converted, PyCS-native replacement for the Bash-ICM
``/bisos/core/bsip/bin/site_lib.sh`` library (``vis_siteBisosBase``,
``vis_siteBisosAdd``, ``vis_siteBisosSelect``).

Package Documentation At Github
===============================

The information below is a subset of the full of documentation for this
bisos-pip package. More complete documentation is available at:
https://github.com/bisos-pip/sites-cs

Realted Resources
=================

+-------------------+-------------------------------------------------+
| bisos Sites Panel | file:/pane                                      |
|                   | ls/bisos.sites/_nodeBase_/fullUsagePanel-en.org |
+-------------------+-------------------------------------------------+
|                   |                                                 |
+-------------------+-------------------------------------------------+

.. _table-of-contents:

Table of Contents TOC
=====================

-  `Overview <#overview>`__
-  `Package Documentation At
   Github <#package-documentation-at-github>`__
-  `Realted Resources <#realted-resources>`__
-  `Installation <#installation>`__

   -  `Installation With pip <#installation-with-pip>`__
   -  `Installation With pipx <#installation-with-pipx>`__

-  `Part of BISOS and ByStar — ByStar Internet Services Operating
   System <#part-of-bisos-and-bystar-----bystar-internet-services-operating-system>`__
-  `bisos.sites is a Command-Only PyCS
   Facility <#bisossites-is-a-command-only-pycs-facility>`__
-  `bisos.sites as a Standalone Piece of
   BISOS <#bisossites-as-a-standalone-piece-of-bisos>`__
-  `Usage <#usage>`__

   -  `Sites Information <#sites-information>`__
   -  `Site Base – obtain/update the selected
      site <#site-base----obtainupdate-the-selected-site>`__
   -  `Add or Select a Site (converted from
      site\ lib.sh) <#add-or-select-a-site-converted-from-site_libsh>`__

-  `Key Files <#key-files>`__
-  `Documentation and Blee-Panels <#documentation-and-blee-panels>`__

   -  `bisos.sites Blee-Panels <#bisossites-blee-panels>`__

-  `Support <#support>`__
-  `Planned Improvements <#planned-improvements>`__

   -  `Add py3/tests/ live-execution coverage for
      siteBase/siteBisosAdd/siteBisosSelect (currently smoke-tested
      only, never
      executed) <#add-py3tests-live-execution-coverage-for-sitebasesitebisosaddsitebisosselect-currently-smoke-tested-only-never-executed>`__
   -  `Document the /bisos/var/sites/<siteBxoId> and selected symlink
      layout with a diagram in the
      Blee-Panel <#document-the-bisosvarsitessitebxoid-and-selected-symlink-layout-with-a-diagram-in-the-blee-panel>`__
   -  `Revisit whether platfSiteBootstrap.py should be merged into or
      deprecated in favor of
      sites\ csu.py <#revisit-whether-platfsitebootstrappy-should-be-merged-into-or-deprecated-in-favor-of-sites_csupy>`__

Installation
============

The sources for the bisos.sites pip package is maintained at:
https://github.com/bisos-pip/sites.

The bisos.sites pip package is available at PYPI as
https://pypi.org/project/bisos.sites

You can install bisos.sites with pip or pipx.

Installation With pip
---------------------

If you need access to bisos.sites as a python module, you can install it
with pip:

.. code:: bash

   pip install bisos.sites

Installation With pipx
----------------------

If you only need access to bisos.sites as a command on command-line, you
can install it with pipx:

.. code:: bash

   pipx install bisos.sites

The following commands are made available:

-  sitesManage.cs
-  site-fps.cs
-  platfSiteBootstrap-fps.cs
-  platfSitesActivate-fps.cs
-  site-registrarsBoxInv-fps.cs
-  site-registrarsBoxPerf-fps.cs
-  site-registrarsContainerInv-fps.cs
-  site-registrarsContainerPerf-fps.cs

Part of BISOS and ByStar — ByStar Internet Services Operating System
====================================================================

| Layered on top of Debian, **BISOS**: (By\* Internet Services Operating
  System) is a unified and universal framework for developing both
  internet services and software-service continuums that use internet
  services. See `Bootstrapping ByStar, BISOS and
  Blee <https://github.com/bxGenesis/start>`__ for information about
  getting started with BISOS.
| **BISOS** is a foundation for **The Libre-Halaal ByStar Digital
  Ecosystem** which is described as a cure for losses of autonomy and
  privacy in a book titled: `Nature of
  Polyexistentials <https://github.com/bxplpc/120033>`__

*bisos.sites* is part of BISOS.

bisos.sites is a Command-Only PyCS Facility
===========================================

bisos.sites is a command-line tool. It is a PyCS single-unit command
service. PyCS is a framework that converges development of CLI tools and
services. PyCS is an alternative to FastAPI, Typer and Click.

bisos.sites uses the PyCS-Framework to:

#. Manage the ``/bisos/var/sites`` symlink base – per-site symlinks and
   the ``selected`` symlink that ``/bisos/site`` resolves through
#. Bootstrap and activate BISOS platform sites
   (``platfSiteBootstrap-fps.cs``, ``platfSitesActivate-fps.cs``)
#. Serve as a registrar for site boxes and containers inventory
   (``site-registrarsBoxInv-fps.cs``,
   ``site-registrarsContainerInv-fps.cs``) and their performer-side
   counterparts

The core of PyCS-Framework is the *bisos.b* package (the
PyCS-Foundation). See `bisos.b <https://github.com/bisos-pip/b>`__ for
an overview.

bisos.sites as a Standalone Piece of BISOS
==========================================

bisos.sites is a standalone piece of BISOS. It can be used as a
self-contained Python package separate from BISOS. Follow the
installation and usage instructions below for your own use.

Usage
=====

Sites Information
-----------------

.. code:: bash

   sitesManage.cs -i sitesInfo

Lists the current ``/bisos/site``, ``/bisos/var/sites/*``, and
``selected`` symlinks (read-only).

Site Base – obtain/update the selected site
-------------------------------------------

.. code:: bash

   sitesManage.cs -i siteBase -- obtain
   sitesManage.cs -p bpoId=<siteBxoId> -i siteBase -- update

``obtain`` returns ``/bisos/site``; ``update`` re-points
``/bisos/var/sites/selected`` (and hence ``/bisos/site``) at the given
``siteBxoId``.

Add or Select a Site (converted from site\ :sub:`lib`.sh)
---------------------------------------------------------

.. code:: bash

   sitesManage.cs -i siteBisosAdd <siteBxoId>       # create /bisos/var/sites/<siteBxoId>
   sitesManage.cs -i siteBisosSelect <siteBxoId>    # update /bisos/var/sites/selected

These are the direct PyCS conversions of
``/bisos/core/bsip/bin/site_lib.sh``'s ``vis_siteBisosAdd`` and
``vis_siteBisosSelect``.

For the full, current set of examples (including the registrar and
platform-bootstrap commands), run any binary with ``-i examples``, e.g.
``sitesManage.cs -i examples``.

Key Files
=========

-  ``py3/bin/sitesManage.cs`` – the primary CS binary; csuList includes
   ``bisos.sites.sites_csu``.
-  ``py3/bisos/sites/sites_csu.py`` – ``sitesInfo``, ``siteBase``,
   ``siteBisosAdd``, ``siteBisosSelect``, ``siteBisosBase()`` – site
   symlink-base management.
-  ``py3/bisos/sites/platfSiteBootstrap.py`` /
   ``py3/bisos/sites/platfSiteBootstrap_fps.py`` – platform site
   bootstrap (primary site BPO-ID lookup, etc.); kept separate from
   ``sites_csu.py``.
-  ``py3/bisos/sites/site_registrarsBox{Inv,Perf}_fps.py`` /
   ``site_registrarsContainer{Inv,Perf}_fps.py`` – registrar inventory
   and performer Cmnds for boxes and containers.

Documentation and Blee-Panels
=============================

bisos.sites is part of ByStar Digital Ecosystem http://www.by-star.net.

This module's primary documentation is in the form of Blee-Panels.
Additional information is also available in:
http://www.by-star.net/PLPC/180047

bisos.sites Blee-Panels
-----------------------

bisos.sites Blee-Panels are in ./panels directory. From within Blee and
BISOS these panels are accessible under the Blee "Panels" menu.

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Planned Improvements
====================

.. _add-py3tests-live-execution-coverage-for-sitebasesitebisosaddsitebisosselect-currently-smoke-tested-only-never-executed:

TODO Add py3/tests/ live-execution coverage for siteBase/siteBisosAdd/siteBisosSelect (currently smoke-tested only, never executed)
-----------------------------------------------------------------------------------------------------------------------------------

.. _document-the-bisosvarsitessitebxoid-and-selected-symlink-layout-with-a-diagram-in-the-blee-panel:

TODO Document the /bisos/var/sites/<siteBxoId> and selected symlink layout with a diagram in the Blee-Panel
-----------------------------------------------------------------------------------------------------------

.. _revisit-whether-platfsitebootstrap.py-should-be-merged-into-or-deprecated-in-favor-of-sitescsu.py:

TODO Revisit whether platfSiteBootstrap.py should be merged into or deprecated in favor of sites\ :sub:`csu`.py
---------------------------------------------------------------------------------------------------------------
