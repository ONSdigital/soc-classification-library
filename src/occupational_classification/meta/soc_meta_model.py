"""Module for the `ClassificationMeta` class.

This module defines the `ClassificationMeta` class, which represents metadata
for occupational classification codes. It includes attributes for code, group
title, group description and qualifications and tasks lists, as well as methods
for code matching and formatted output.

Classes:
    ClassificationMeta: A Pydantic model for occupational classification metadata.
"""

from typing import Optional  # list for list for tasks

from pydantic import BaseModel, Field


class ClassificationMeta(BaseModel):
    """Represents a classification meta model.

    Attributes:
        code (str): Category code. A code of length between 1 and 4 digits long.
        soc2020_group_title (str): A short, general title of the group.
        group_description (str): Provides description of the group with more
            details than group_title.
        qualifications (str): Applies only for Unit Group. Provides string that
            represents typical entry routes and qualifications required.
        tasks (str): Applies only for Unit Group. Provides a string that
            represents a list of typical tasks for given unit group.
    """

    code: str = Field(
        description="""Group code; the level of the group is determined based on
        the length of  code. Each code contains between 1 and 4 digits."""
    )
    soc2020_group_title: str = Field(
        default="",
        description="""A short group title for the group code in SOC 2020.""",
    )
    group_description: str = Field(
        default="", description="""More in-depth description of the group."""
    )
    qualifications: Optional[str] = Field(
        default="",
        description="""Typical
        Entry Routes And Associated Qualifications for the unit group.""",
    )
    tasks: Optional[str] = Field(
        default="",
        description="""An optional string with a list of tasks for the group.
        Applies only for Unit Group (4 digit code)""",
    )
