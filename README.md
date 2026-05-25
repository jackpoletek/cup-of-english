# Cup of English

![Cup of English](https://github.com/jackpoletek/cup-of-english/blob/main/screenshots/home/Cup%20of%20English%20-%20home.png) </br>

[Live Project](https://cup-of-english-ddc7ce9e283b.herokuapp.com/) </br>
[Repository](https://github.com/jackpoletek/cup-of-english) </br>

Cup of English is a full-stack Django educational e-commerce platform designed as a real-world MVP online English school for teenagers and adults.

The platform solves a practical business problem:

Many online learning platforms are overloaded with unnecessary complexity, fragmented payment systems, and unclear course access flows. Cup of English focuses on a streamlined learning and purchasing experience where learners can quickly discover a course, purchase access securely, and immediately unlock protected educational content.

The application combines:

- Secure role-based authentication
- Email account activation
- Structured English course catalogue
- Stripe-powered checkout system
- Automated enrollment handling via Stripe webhooks
- Protected premium course access
- Teacher profile management
- AWS S3 media storage
- PostgreSQL cloud database architecture
- Production-ready deployment pipeline
- Heroku cloud deployment
- Gmail SMTP communication system

The project was intentionally designed using KISS (Keep It Simple, Stupid) principles while still demonstrating production-level backend architecture, payment processing, security, and scalable application structure.

---

# Table of Contents

- [Business Problem](#business-problem)
- [Project Highlights](#project-highlights)
- [User Experience (UX)](#user-experience-ux)
- [User Types](#user-types)
- [User Journeys](#user-journeys)
- [User Stories](#user-stories)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Payment & Enrollment Flow](#payment--enrollment-flow)
- [Signals & Automation](#signals--automation)
- [Database Design](#database-design)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Bugs and Fixes](#bugs-and-fixes)
- [Credits](#credits)

---

# Business Problem

Traditional language school platforms often suffer from:
- complicated onboarding
- slow payment flows
- unclear access permissions
- disconnected learning systems
- poor mobile usability

Cup of English was designed to solve these issues through a focused MVP architecture that prioritises:
- simple course discovery
- secure enrollment
- fast payment flow
- immediate course access
- role-based content protection
- scalable backend architecture

The platform demonstrates how a modern educational business can automate enrollment, payments, and access control while maintaining a clean and user-friendly experience.

---

# Project Highlights

## Key Technical Highlights
- Full-stack Django application deployed to production
- Stripe Checkout integration with webhook automation
- Role-based authentication system (Admin / Teacher / Learner)
- Automated email activation workflow
- Protected premium content architecture
- PostgreSQL cloud database integration
- AWS S3 media and static asset storage
- Responsive Bootstrap frontend
- Production-safe transaction handling
- Secure webhook verification
- Automated test suite for critical flows

## Business-Oriented Highlights
- Conversion-focused checkout flow
- Simplified "single-course purchase" UX strategy (no basket)
- Real-world educational marketplace architecture
- Automated learner enrollment after payment
- Secure premium-content delivery system
- Scalable role-based platform foundation

---

# User Experience (UX)

## UX Strategy

Cup of English was designed around simplicity, clarity, and conversion-focused user experience.

Instead of overwhelming users with unnecessary dashboard complexity, the platform focuses on helping learners complete three core actions efficiently:

1. Discover a relevant course
2. Purchase access securely
3. Start learning immediately

The interface prioritises:
- low cognitive load
- mobile responsiveness
- fast navigation
- secure purchasing
- seamless onboarding

The overall UX direction follows modern SaaS and educational marketplace patterns while maintaining accessibility and readability.

---

# User Types

## Learner

Learners are users who browse, purchase, and access premium English courses.

Key learner capabilities:
- register and activate account
- browse courses by category and level
- purchase courses securely
- access enrolled course content
- leave course reviews
- manage account profile

## Teacher

Teachers manage educational visibility within the platform.

Key teacher capabilities:
- manage teacher profile
- upload profile image
- add professional biography
- view learners enrolled in assigned courses
- access grouped enrollment dashboard

## Admin

Administrators manage the entire platform ecosystem.

Key admin capabilities:
- manage users
- manage courses
- manage enrollments
- oversee platform operations
- control educational content structure
- manage platform administration through Django admin tools

---

# User Journeys

## Learner Journey

graph TD </br>
A[Visitor Browses Courses] --> B[Registers Account] </br>
B --> C[Receives Activation Email] </br>
C --> D[Activates Account] </br>
D --> E[Logs In] </br>
E --> F[Selects Course] </br>
F --> G[Stripe Checkout] </br>
G --> H[Stripe Webhook] </br>
H --> I[Enrollment Created] </br>
I --> J[Premium Content Unlocked]

## Teacher Journey

graph TD </br>
A[Teacher Registers] --> B[Activates Account] </br>
B --> C[Logs In] </br>
C --> D[Creates Teacher Profile] </br>
D --> E[Uploads Bio & Image] </br>
E --> F[Views Assigned Courses] </br>
F --> G[Views Enrolled Learners] </br>

## Admin Journey

graph TD </br>
A[Admin Accesses Dashboard] --> B[Manages Users] </br>
B --> C[Manages Courses] </br>
C --> D[Manages Enrollments] </br>
D --> E[Oversees Platform Operations]

---

# User Stories

## Course Discovery

### User Story

As a learner, I want to browse courses by category and level so that I can quickly find a course suitable for my learning goals.

### How This Is Achieved
- Courses grouped by educational purpose
- Level filtering (A2-C2)
- Responsive course catalogue layout
- Search functionality by course title
- Category-based navigation structure

**Browse Courses By Category** </br>
![Browse Courses By Category](docs/readme-images/auth-placeholder.png) </br>

**Browse Courses By Level** </br>
![Browse Courses By Level](docs/readme-images/auth-placeholder.png) </br>

## Secure Enrollment

### User Story

As a learner, I want to securely purchase a course and immediately gain access after payment.

### How This Is Achieved
- Stripe Checkout integration
- Secure payment verification
- Webhook-driven enrollment automation
- Access validation using shared enrollment helper
- Protected course content routes

## Teacher Visibility

### User Story
As a teacher, I want to manage my profile and view enrolled learners so that I can monitor my assigned courses.

### How This Is Achieved
- Dedicated TeacherProfile model
- Image upload validation
- Grouped enrollment dashboard
- Teacher-course relationship architecture

**Upload Picture & Bio** </br>
![Upload Picture & Bio](docs/readme-images/auth-placeholder.png)

---

# Features

## Authentication

### Feature Highlights
- Secure registration system
- Email account activation
- Role-based authentication
- Protected login flow
- Resend activation system
- Session-safe authentication handling

**Email Account Activation** </br>
![Email Account Activation](docs/readme-images/auth-placeholder.png)

## Course Discovery

### Feature Highlights
- Course segmentation by learning purpose
- English level filtering
- Search functionality
- Dynamic course pages
- Structured catalogue navigation

### Course Categories
- General English
- Business English
- English for Academic Purposes (EAP)
- English for Specific Purposes (ESP)
- IB English
- IGCSE English

## Stripe Payment

### Feature Highlights

- Secure Stripe Checkout integration
- Payment verification via webhooks
- Metadata-based enrollment linking
- Duplicate enrollment prevention
- Transaction-safe enrollment creation

**Stripe Payment Completed** </br>
![Stripe Payment Completed](docs/readme-images/stripe-placeholder.png) </br>

**Stripe Successful Payment** </br>
![Stripe Successful Payment](docs/readme-images/stripe-placeholder.png)

## Review System

### Feature Highlights
- Course review submission
- One review per learner
- Edit/delete review ownership protection
- Average course rating calculation
- Enrollment-based review permissions

## Teacher Profile

### Feature Highlights
- Teacher biography management
- Image upload validation
- AWS S3 media storage
- Secure file validation
- Teacher dashboard integration

---

# System Architecture

## High-Level Architecture

graph TD </br>

A[Frontend - Bootstrap UI] </br>
--> B[Django Views] </br> </br>

B --> C[Business Logic] </br>
B --> D[Authentication System] </br>
B --> E[Stripe Integration] </br>
B --> F[PostgreSQL Database] </br> </br>

E --> G[Stripe Webhooks] </br> </br>

G --> H[Enrollment Automation] </br> </br>

F --> I[Course Access Control] </br> </br>

B --> J[AWS S3 Media Storage]

---

# Payment & Enrollment Flow

The payment architecture follows a real-world production pattern where Stripe acts as the payment authority while the webhook acts as the enrollment trigger.

## Enrollment Flow

graph TD </br>

A[Learner Selects Course] </br>
--> B[Stripe Checkout Session] </br> </br>

B --> C[Payment Completed] </br> </br>

C --> D[Stripe Sends Webhook] </br> </br>

D --> E[Django Verifies Signature] </br> </br>

E --> F[Enrollment Created] </br> </br>

F --> G[Course Access Granted]

## Why Webhooks Are Important

Stripe webhooks ensure that enrollments are only created after Stripe confirms successful payment.

This prevents:
- fake enrollments
- client-side payment bypassing
- duplicate purchases
- inconsistent payment states

The webhook implementation includes:
- Stripe signature verification
- transaction safety using transaction.atomic()
- duplicate enrollment prevention
- logging and exception handling

---

# Signals & Automation

The project uses Django signals to automate profile creation and maintain consistent user architecture.

## Signal Flow

graph TD </br>

A[New User Created] </br>
--> B[post_save Signal Triggered] </br> </br>

B --> C[UserProfile Automatically Created] </br> </br>

C --> D[Role System Ready]

## Why Signals Are Used

Signals eliminate the need to manually create user profiles during registration.

This ensures:
- every user always has a profile
- role-based permissions remain consistent
- profile creation logic stays centralised
- cleaner registration workflow

The project uses:
- post_save signals
- automatic profile creation
- automatic profile saving

---

# Database Design

## Database Models

| Model | Description |
|------|-------------|
| User | Django authentication model |
| UserProfile | Extends User with role-based permissions |
| TeacherProfile | Stores teacher biography and image |
| Course | Stores course information and pricing |
| Enrollment | Links learners to purchased courses |
| Review | Stores learner reviews and ratings |

## Database Schema

User <br>
└── UserProfile (role)

User <br>
└── TeacherProfile </br>
    ├── bio <br>
    └── image

Course <br>
├── teacher -> User <br>
├── level <br>
├── course_type <br>
└── price

Enrollment <br>
├── learner -> User <br>
├── course -> Course <br>
├── teacher -> User <br>
└── is_active

Review <br>
├── learner -> User <br>
├── course -> Course <br>
├── rating <br>
└── comment

## Relationship Rules & Constraints

### UserProfile
- Each user has exactly one profile
- Profile stores role permissions
- Roles:
- - Admin
- - Teacher
- - Learner



---

### JavaScript Enhancements & Graceful Degradation

- Carousel with autoplay, hover pause, and caption animation
- Back-to-top button for UX improvement

Graceful degradation applied:

- If JavaScript fails, core navigation and content remain fully accessible
- Carousel falls back to static content

---

## Future Features

- Course modules and lessons
- Video-based content
- Progress tracking
- Quizzes and assessments
- Teacher dashboards
- Reviews and ratings
- Certificates

---

# Design

## Layout

- Clean, minimal layout using Bootstrap
- Mobile-first responsive design
- Clear content hierarchy

**Rationale:**
Educational platforms require clarity and low cognitive load to support learning focus.

---

## Typography

- Inter font
- High readability
- Modern SaaS-like appearance

**Rationale:**
Improves readability for long-form educational content.

---

## Colour Scheme

Defined using CSS variables:

- Primary: `#FF6B35` (call-to-action, engagement)
- Dark accent: `#2D3142` (structure, readability)
- Secondary/light: `#F5F5F5` (clean background)
- Success: `#06D6A0` (positive feedback)

**Rationale:**

- Orange encourages action (buy, register)
- Dark tones provide contrast and professionalism
- Light background reduces visual fatigue

---

# Database Structure

### Core Models

- User
- UserProfile (roles)
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
- Bootstrap 5

## Database

- PostgreSQL (Neon)

## Third-Party Services

- Stripe
- AWS S3
- Gmail SMTP

## Tools

- Git
- GitHub
- Heroku

---

# Testing

## Manual Testing

- Authentication flow verified
- Email activation working
- Stripe checkout tested
- Webhook enrollment confirmed
- Access control enforced

## Automated Testing

- Model tests
- View tests
- Access control tests
- Payment webhook tests

All tests passing.

---

# Bugs and Fixes

### Fixed Issues

---

- **Bug:** The registration page crashed because the `RegisterForm` was defined as a `ModelForm` without specifying a model in its `Meta` class.
- **Error:** Registration page crash due to missing model configuration in `ModelForm`.
- **Fix:**
- Imported Django `User` model
- Added proper `Meta` class inside `RegisterForm`
- Set:
- `model = User`
- defined required fields

---

- **Bug:** Inconsistent URL naming across the project caused routing failures.
- **Error:** `NoReverseMatch` for `"home"` and `"index"` due to mismatches between:
- `core/urls.py`
- `accounts/views.py` redirects
- Template `{% url %}` usage
- **Fix:**
- Standardised URL naming across the project
- Updated redirects in views
- Final implementation:
```python
redirect("core:index")
```
---

- **Bug:** User was created even when registration process failed, causing inconsistent database state.
- **Error:** `IntegrityError`: duplicate key value violates unique constraint, accounts_userprofile_user_id_key
- **Fix:**
- Wrapped user and profile creation in `transaction.atomic()`
- Replaced `.create()` with `.get_or_create()`
- Added global exception handling to prevent Django crash pages

---

- **Bug:** Stripe webhook events were not reaching the Django application.
- **Error:** No visible Django error; only symptom was missing enrollment creation after payment.
- **Fix:**
- Used Stripe CLI to forward webhook events to the local development server

---

- **Bug:** Multiple issues in account activation and email flow:
- Activation URL mismatch (`uid64` vs `uidb64`)
- Email sending not protected
- User created even if email sending failed
- **Error:**
- `NoReverseMatch`
- Partial user creation without activation
- **Fix:**
- Unified URL parameter to `uidb64`
- Wrapped email sending in `try/except`
- Moved email logic inside `transaction.atomic()`
- Fixed session key naming
- Added safe fallback messages to prevent 500 errors

---

- **Bug:** Contact form resubmitted on page refresh due to direct render response:
```python
return render(request, "core/contact.html", {...})
```
- **Error:** Duplicate emails sent when user refreshed the page.
- **Fix:**
- Implemented Post/Redirect/Get (PRG) pattern:
```python
return redirect("core:contact")
```

### Known Issues

- Webhook delay may cause slight delay in enrollment visibility
- No progress tracking yet

---

# Deployment

## Local Setup

```bash
git clone https://github.com/your-username/cup-of-english.git
cd cup-of-english
pip install -r requirements.txt
```

Create .env:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
STRIPE_PUBLIC_KEY=your_key
STRIPE_SECRET_KEY=your_key
STRIPE_WEBHOOK_SECRET=your_secret
```

Run:

```bash
python manage.py migrate
python manage.py runserver
```

## Gmail SMTP Setup
- Enable 2FA
- Generate App Password
- Use in Django email settings

## AWS S3 Setup
- Create bucket
- Enable static hosting
- Configure CORS
- Add bucket policy
- Create IAM user and access keys

## Stripe Webhooks
- Create endpoint /checkout/wh/
- Add signing secret to environment variables
- Test using Stripe test cards

## Production
- Hosted on Heroku
- PostgreSQL (Neon)
- AWS S3 for static/media
- Stripe live payments enabled

# Credits
- Django: https://docs.djangoproject.com/
- Stripe: https://stripe.com/docs
- Bootstrap: https://getbootstrap.com/

# Acknowledgements

This project was developed as a portfolio-grade full-stack application demonstrating:

- Backend architecture
- Secure payment systems
- Real-world deployment
- Access control and business logic

Designed and developed by Jack Poletek.
