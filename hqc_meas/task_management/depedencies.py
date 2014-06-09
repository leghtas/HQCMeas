# -*- coding: utf-8 -*-
#==============================================================================
# module : dependencies.py
# author : Matthieu Dartiailh
# license : MIT license
#==============================================================================
"""
"""

from atom.api import (Callable, List, Dict, Str, Unicode)
from enaml.core.declarative import Declarative, d_


class BuildDependencies(Declarative):
    """Extension to the 'build-dependencies' extensions point of the
    TaskManagerPlugin.

    Attributes
    ----------
    id : unicode
        Unique Id.

    walk_members : list(str)
        List of members for the walk method of the ComplexTask.

    collect : callable(workbench, flat_walk)
        Callable in charge of collecting the identified build dependencies.
        It should take as arguments the workbench of the application and a dict
        in the format {name: set()}. It should return a dict holding the
        dependencies (as dictionaries) in categories.

    """
    id = d_(Unicode())

    walk_members = d_(List(Str()))

    collect = d_(Callable())


class RuntimeDependencies(Declarative):
    """Extension to the 'runtime-dependencies' extensions point of the
    TaskManagerPlugin.

    Attributes
    ----------
    id : unicode
        Unique Id.

    walk_members : list(str)
        List of members for the walk method of the ComplexTask.

    walk_kwargs : dict(str: callable)
        Dict of name: callables for the walk method of the ComplexTask.

    collect : callable(workbench, flatten_walk)
        Callable in charge of collecting the identified build dependencies.
        It should take as arguments the workbench of the application and a dict
        in the format {name: set()}. It should return a dict holding the
        dependencies (as dictionaries) in categories.


    """
    id = d_(Unicode())

    walk_members = d_(List(Str()))

    walk_callables = d_(Dict(Str(), Callable()))

    collect = d_(Callable())
