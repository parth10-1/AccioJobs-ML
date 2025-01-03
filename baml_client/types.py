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
from typing import Dict, Generic, List, Literal, Optional, TypeVar, Union


T = TypeVar('T')
CheckName = TypeVar('CheckName', bound=str)

class Check(BaseModel):
    name: str
    expression: str
    status: str

class Checked(BaseModel, Generic[T,CheckName]):
    value: T
    checks: Dict[CheckName, Check]

def get_checks(checks: Dict[CheckName, Check]) -> List[Check]:
    return list(checks.values())

def all_succeeded(checks: Dict[CheckName, Check]) -> bool:
    return all(check.status == "succeeded" for check in get_checks(checks))



class Activites(BaseModel):
    involvements: Optional[str] = None
    achievements: Optional[str] = None
    volunteer: Union[List["Volunteer"], Optional[None]]
    awards: Union[List["Award"], Optional[None]]

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
    location: "Location"
    relExp: Optional[str] = None
    totalExp: Optional[str] = None
    objective: Optional[str] = None
    profiles: Union[List["Profile"], Optional[None]]

class Company(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    position: Optional[str] = None
    url: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    highlights: Union[List[str], Optional[None]]
    summary: Optional[str] = None

class Education(BaseModel):
    universities: Union[List["University"], Optional[None]]

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
    languages: Union[List["SkillDetails"], Optional[None]]
    frameworks: Union[List["SkillDetails"], Optional[None]]
    technologies: Union[List["SkillDetails"], Optional[None]]
    libraries: Union[List["SkillDetails"], Optional[None]]

class University(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None
    studyType: Optional[str] = None
    area: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    score: Optional[str] = None
    courses: Union[List[str], Optional[None]]

class Volunteer(BaseModel):
    id: Optional[str] = None
    organization: Optional[str] = None
    position: Optional[str] = None
    url: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    summary: Optional[str] = None
    highlights: Union[List[str], Optional[None]]
    isVolunteeringNow: Optional[bool] = None

class Work(BaseModel):
    companies: Union[List["Company"], Optional[None]]
