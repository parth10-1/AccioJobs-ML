###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import Dict, List, Optional, Union, Literal

from . import types
from .types import Checked, Check

###############################################################################
#
#  These types are used for streaming, for when an instance of a type
#  is still being built up and any of its fields is not yet fully available.
#
###############################################################################


class Activites(BaseModel):
    involvements: Optional[str] = None
    achievements: Optional[str] = None
    volunteer: Optional[Union[List["Volunteer"], Optional[None]]] = None
    awards: Optional[Union[List["Award"], Optional[None]]] = None

class Award(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    date: Optional[str] = None
    awarder: Optional[str] = None
    summary: Optional[str] = None

class Basics(BaseModel):
    name: Optional[str] = None
    label: Optional[str] = None
    email: Optional[str] = None
    image: Optional[str] = None
    phone: Optional[str] = None
    url: Optional[str] = None
    summary: Optional[str] = None
    location: Optional["Location"] = None
    relExp: Optional[str] = None
    totalExp: Optional[str] = None
    objective: Optional[str] = None
    profiles: Optional[Union[List["Profile"], Optional[None]]] = None

class Company(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    position: Optional[str] = None
    url: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    highlights: Optional[Union[List[Optional[str]], Optional[None]]] = None
    summary: Optional[str] = None

class Education(BaseModel):
    universities: Optional[Union[List["University"], Optional[None]]] = None

class Location(BaseModel):
    address: Optional[str] = None
    postalCode: Optional[str] = None
    city: Optional[str] = None
    countryCode: Optional[str] = None
    region: Optional[str] = None

class Profile(BaseModel):
    network: Optional[str] = None
    username: Optional[str] = None
    url: Optional[str] = None

class Resume(BaseModel):
    basics: Optional["Basics"] = None
    skills: Optional["Skills"] = None
    work: Optional["Work"] = None
    education: Optional["Education"] = None
    activities: Optional["Activites"] = None

class SkillDetails(BaseModel):
    name: Optional[str] = None
    level: Optional[int] = None

class Skills(BaseModel):
    languages: Optional[Union[List["SkillDetails"], Optional[None]]] = None
    frameworks: Optional[Union[List["SkillDetails"], Optional[None]]] = None
    technologies: Optional[Union[List["SkillDetails"], Optional[None]]] = None
    libraries: Optional[Union[List["SkillDetails"], Optional[None]]] = None

class University(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None
    studyType: Optional[str] = None
    area: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    score: Optional[str] = None
    courses: Optional[Union[List[Optional[str]], Optional[None]]] = None

class Volunteer(BaseModel):
    id: Optional[str] = None
    organization: Optional[str] = None
    position: Optional[str] = None
    url: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    summary: Optional[str] = None
    highlights: Optional[Union[List[Optional[str]], Optional[None]]] = None
    isVolunteeringNow: Optional[bool] = None

class Work(BaseModel):
    companies: Optional[Union[List["Company"], Optional[None]]] = None
