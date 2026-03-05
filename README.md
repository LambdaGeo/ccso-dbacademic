 
# CCSO-DBAcademic Ontology Extension

[![Ontology](https://img.shields.io/badge/vocabulary-CCSO--DBAcademic-blue.svg)](https://purl.org/linked-data/ccso-dbacademic#)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview
**CCSO-DBAcademic** is an extension of the [Curriculum Course Syllabus Ontology (CCSO)](https://w3id.org/ccso/ccso) specifically designed to support the **DBAcademic** project. This ontology bridges the gap between academic curricula, educational organizations, and research activities (groups and projects).

It provides a semantic layer to describe how professors, coordinators, and research leaders are connected to educational institutions and research organizations.

## Metadata
* **IRI:** `https://purl.org/linked-data/ccso-dbacademic#`
* **Prefix:** `ccsoacad`
* **Creator:** [Sérgio Souza Costa](mailto:sergio.costa@ufma.br) (LambdaGeo - UFMA)
* **Contributor:** André Moura Lima
* **Version:** 0.1
* **Date:** 2023-08-15

## Key Features & Classes
This extension imports CCSO and integrates with well-known vocabularies like **FOAF**, **Schema.org**, and **Dublin Core**.

### Core Classes
- `ccsoacad:ResearchOrganization`: A specialized organization focused on research (Subclass of `schema:Organization`).
- `ccsoacad:ResearchGroup`: A group of researchers working on common topics.
- `ccso:ResearchProject`: Specific research studies or projects (integrated with CCSO namespace).

### Key Properties
- `ccsoacad:hasLeader`: Connects a Research Organization to its `foaf:Person` leader.
- `ccsoacad:hasCoordinator`: Links a `ccso:ProgramofStudy` to its `ccso:AcademicStaff`.
- `ccsoacad:providedBy`: Maps study programs to their parent `schema:EducationalOrganization`.
- `ccsoacad:startDate` / `endDate`: Datatype properties to define the temporal scope of research projects.
- `ccsoacad:aboutMe`: A literal property for biographical information about a `foaf:Person`.

## Namespaces Used
| Prefix | Namespace |
|        |           |
| **ccsoacad** | `https://purl.org/linked-data/ccso-dbacademic#` |
| **ccso** | `https://w3id.org/ccso/ccso#` |
| **foaf** | `http://xmlns.com/foaf/0.1/` |
| **schema** | `http://schema.org/` |
| **owl** | `http://www.w3.org/2002/07/owl#` |

## Usage
This ontology is intended for use in academic data integration, Lattes-like platforms, and institutional repositories that require a formal description of the relationship between teaching programs and research groups.

## About LambdaGeo
This project is part of the research conducted by **LambdaGeo** (Universidade Federal do Maranhão - UFMA), focusing on Geocomputation, Functional Programming, and Semantic Web technologies.

