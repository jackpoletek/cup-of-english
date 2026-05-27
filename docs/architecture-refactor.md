# Architecture Refactor

## Overview

The current application stores teacher relationships in two places:

- `Enrollment.teacher`
- `Course.teacher`

This creates duplicated sources of truth and increases the risk
of inconsistent application state.

Example inconsistency:

```python
Enrollment.teacher = Teacher_Ula
Course.teacher = None
```

As the application grows, maintaining synchronization between
these relationships becomes increasingly difficult and error-prone.

---

## Refactor Goal

The long-term goal is to simplify the architecture by making:

```python
Course.teacher
```

the single source of truth for teacher assignments.

Enrollment objects should derive teacher data through:

```python
enrollment.course.teacher
```

instead of storing duplicated teacher references.

---

## Why This Architecture Is Better

The `Enrollment` model represents:

```text
Learner enrolled in Course
```

NOT:

```text
Learner enrolled with Teacher
```

Teacher ownership belongs to the `Course` domain.

This simplifies:

- business logic
- database integrity
- queries
- templates
- admin configuration
- API serialization
- future React integration

---

## Benefits

- Eliminates duplicated data
- Prevents synchronization issues
- Reduces database complexity
- Simplifies maintenance
- Cleaner ORM relationships
- Easier REST API development
- Better scalability
- Cleaner React integration later

---

## Target Architecture

```text
Learner
|
Enrollment
|
Course
|
Teacher
```

---

## Planned Future Improvements

- Introduce Django REST Framework
- Gradually integrate React
- Convert interactive UI sections into API-driven components
- Preserve Django server-rendered architecture where appropriate

---

## Non-Goals

The project does NOT currently require:

- teacher history tracking
- many-to-many teacher assignments
- historical enrollment snapshots
- full SPA frontend architecture

The focus is maintaining a clean, practical, scalable architecture
using KISS principles.
