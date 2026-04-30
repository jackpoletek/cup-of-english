# Cup of English

![Responsive Mockup](docs/readme-images/responsive-placeholder.png)

Cup of English is a fullstack web application designed to provide structured English language courses for learners at different proficiency levels. Users can browse courses, securely purchase access via Stripe, and access course content after enrollment.

The platform is built using Django, PostgreSQL, and vanilla JavaScript, focusing on simplicity, performance, and a clean user experience.

---

# Table of Contents

- [User Experience (UX)](#user-experience-ux)
- [Strategy](#strategy)
- [User Stories](#user-stories)
- [Features](#features)
- [Existing Features](#existing-features)
- [Future Features](#future-features)
- [Design](#design)
- [Database Structure](#database-structure)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs and Fixes](#bugs-and-fixes)
- [Deployment](#deployment)
- [Credits](#credits)

---

# User Experience (UX)

## Strategy

The goal of Cup of English is to provide a simple and focused platform for learners to:

- Improve their English skills through structured courses
- Access content after secure payment
- Navigate content easily without unnecessary complexity

The platform prioritizes:

- clarity over complexity
- fast load times
- minimal friction in purchasing and accessing courses

---

## Target Users

- Learners improving general English (A2-C2)
- Professionals learning Business English
- Students preparing for:
- IGCSE English
- IB English
- Academic English (EAP)

---

## User Stories

### First-time Visitor

- As a visitor, I want to understand what the platform offers so that I can decide whether it suits my needs
- As a visitor, I want to browse available courses so that I can explore options

### Registered User

- As a user, I want to register and verify my email so that I can access the platform securely
- As a user, I want to log in and view my profile so that I can manage my account

### Learner

- As a learner, I want to purchase a course so that I can access its content
- As a learner, I want to see my enrolled courses so that I can continue learning
- As a learner, I want restricted access to content unless enrolled

### Admin

- As an admin, I want to manage courses so that I can control available content
- As an admin, I want to manage users and enrollments

---

# Features

## Existing Features

### Authentication System

- User registration with email verification
- Login/logout functionality
- Role-based system (admin, teacher, learner)

![Auth Screenshot](docs/readme-images/auth-placeholder.png)

---

### Course Browsing

- Courses grouped by type:
- General English
- Business English
- EAP / ESP
- Exam preparation

- Courses filtered by level (A2-C2)

![Courses Screenshot](docs/readme-images/courses-placeholder.png)

---

### Course Details

- Detailed course view
- Enrollment status displayed
- Clear call-to-action for purchase

---

### Stripe Payments

- Secure checkout using Stripe
- Metadata used to link user and course
- Webhook-based enrollment activation (source of truth)

![Stripe Screenshot](docs/readme-images/stripe-placeholder.png)

---

### Enrollment System

- One enrollment per user per course (DB constraint)
- Access control for course content
- Enrollment activated after successful payment

---

### Course Access Control

- Only enrolled users can access course content
- Unauthorized users redirected safely

---

### Profile Page

- Displays user enrollments
- Allows profile updates

---

### Contact Form

- Users can send messages
- Email notification sent to admin

---

## Future Features

- Course content structure (Modules & Lessons)
- Video-based lessons
- Progress tracking system
- Quizzes and assessments
- Teacher dashboard (if expanded later)
- Improved payment confirmation UX
- Course reviews and ratings

---

# Design

## Layout

- Clean, minimal layout using Bootstrap
- Mobile-first responsive design

## Typography

- Simple and readable fonts
- Focus on clarity and accessibility

## Color Scheme

*(To be added with final design)*

---

# Database Structure

### Core Models

- User (Django default)
- UserProfile (role management)
- Course
- Enrollment

### Relationships

- One user → one profile
- One course → many enrollments
- One user → many enrollments

![ERD](docs/readme-images/erd-placeholder.png)

---

# Technologies Used

## Languages

- Python
- JavaScript
- HTML5
- CSS3

## Frameworks & Libraries

- Django
- Bootstrap

## Database

- PostgreSQL

## Third-Party Services

- Stripe (payments)
- AWS S3 (media storage)

## Tools

- Git
- GitHub
- Heroku (deployment)

---

# Testing

## Manual Testing

- User registration and login flow tested
- Email verification tested
- Stripe payments tested in test and live mode
- Enrollment creation verified via webhook
- Access restrictions tested across views

## Automated Testing

- Django tests implemented across apps
- All tests passing

---

# Bugs and Fixes

### Fixed Issues

- Duplicate enrollment checks across views → refactored into helper (`is_enrolled`)
- Webhook race condition → fixed with `transaction.atomic()` + `get_or_create`
- Exception handling order issue → corrected to ensure specific exceptions are caught

### Known Issues

- Payment success page does not confirm enrollment instantly (webhook delay possible)
- No progress tracking yet

---

# Deployment

## Local Setup

```bash
git clone https://github.com/your-username/cup-of-english.git
cd cup-of-english
pip install -r requirements.txt
