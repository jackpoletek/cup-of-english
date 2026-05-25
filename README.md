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
- [Acknowledgements](#acknowledgements)
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
--> B[Django Views] </br>

B --> C[Business Logic] </br>
B --> D[Authentication System] </br>
B --> E[Stripe Integration] </br>
B --> F[PostgreSQL Database] </br>

E --> G[Stripe Webhooks] </br>

G --> H[Enrollment Automation] </br>

F --> I[Course Access Control] </br>

B --> J[AWS S3 Media Storage]

---

# Payment & Enrollment Flow

The payment architecture follows a real-world production pattern where Stripe acts as the payment authority while the webhook acts as the enrollment trigger.

## Enrollment Flow

graph TD </br>

A[Learner Selects Course] </br>
--> B[Stripe Checkout Session] </br> 

B --> C[Payment Completed] </br>

C --> D[Stripe Sends Webhook] </br>

D --> E[Django Verifies Signature] </br>

E --> F[Enrollment Created] </br>

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
--> B[post_save Signal Triggered] </br>

B --> C[UserProfile Automatically Created] </br>

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
|-------|-------------|
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
&nbsp;&nbsp;&nbsp;&nbsp;├── bio <br>
&nbsp;&nbsp;&nbsp;&nbsp;└── image

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

### Enrollment

The Enrollment model acts as the business-critical bridge between learners and courses.

This architecture was intentionally separated instead of using a direct ManyToMany relationship because enrollments contain additional business logic:
- enrollment timestamps
- active/inactive state
- teacher assignment
- access validation
- payment-driven ownership

### Enrollment Constraints
- One learner can only enroll in a course once
- Duplicate purchases prevented
- Access controlled through enrollment checks
- Soft-deactivation supported via `is_active`

### Review Constraints
- One review per learner per course
- Reviews restricted to enrolled learners only
- Ownership validation for edit/delete actions

---

# Design

## Wireframes
Initial wireframes were created to plan:
- responsive layout structure
- conversion-focused navigation
- checkout flow clarity
- dashboard usability
- mobile responsiveness

The wireframes prioritised low cognitive load and simple user journeys following KISS design principles.

### Homepage Desktop Wireframe
<img src="https://github.com/jackpoletek/cup-of-english/blob/main/screenshots/wireframes/Cup%20of%20English%20-%20home_large_screen.png" alt="Homepage Desktop Wireframe" width=35% height=35%/>&nbsp;

### Homepage Tablet Wireframe
<img src="https://github.com/jackpoletek/cup-of-english/blob/main/screenshots/wireframes/Cup%20of%20English%20-%20home_tablet.png" alt="Homepage Tablet Wireframe" width=35% height=35%/>&nbsp;

### Homepage Mobile Wireframe
<img src="https://github.com/jackpoletek/cup-of-english/blob/main/screenshots/wireframes/Cup%20of%20English%20-%20home_mobile.png" alt="Homepage Mobile Wireframe" width=35% height=35%/>&nbsp;

## Colour Scheme

| Colour | Hex | Usage |
|--------|-----|-------|
| Orange | #FF6B35 | Call-to-action buttons, engagement |
| Dark Blue | #2D3142 | Navigation, structure, readability |
| Light Grey | #F5F5F5 | Background sections |
| Green | #06D6A0 | Success states and confirmations |

### Colour Strategy
The colour palette was chosen to balance educational professionalism with conversion-oriented UI design.
- Orange increases visibility of important actions such as registration and purchasing
- Dark blue improves contrast and platform readability
- Light grey reduces visual fatigue during long browsing sessions
- Green reinforces positive user feedback and successful actions

## Typography

### Primary Font
- Inter

### Typography Strategy
Inter was selected because it:
- improves readability across devices
- performs well in responsive layouts
- provides modern SaaS-style aesthetics
- maintains accessibility for long-form educational content

The typography system prioritises:
- readability
- low cognitive load
- visual clarity
- mobile accessibility

## Backend Design

### E-Commerce Design Decision (No Basket)

The platform intentionally does not include a shopping basket.

#### Why This Decision Was Made
- learners typically purchase one course at a time
- checkout friction is reduced
- backend architecture remains simpler
- conversion-focused UX is prioritised

This decision follows both:
- MVP product strategy
- KISS development principles

---

# Technologies Used

## Languages

### Python
Primary backend language used to build:
- business logic
- authentication system
- payment processing
- enrollment architecture
- role-based access control
- webhook automation

### JavaScript
Used for frontend interactivity and progressive enhancement:
- Bootstrap carousel controls
- autoplay and hover pause functionality
- animated UI behaviour
- back-to-top button
- responsive interaction improvements

Graceful degradation principles were applied so the platform remains fully usable even if JavaScript becomes unavailable.

### HTML 5
Used to structure:
- responsive page layouts
- semantic educational content
- forms
- navigation systems
- accessibility-focused components

### CSS3
Used for:
- responsive styling
- layout customisation
- visual hierarchy
- UX consistency
- mobile-first design improvements

Custom CSS variables were implemented for reusable platform-wide design consistency.

## Frameworks & Libraries

### Django
Primary backend framework responsible for:
- MVC architecture
- routing
- ORM/database management
- authentication
- template rendering
- form handling
- admin dashboard
- security protections
- session management

Django was selected because it provides rapid development speed while maintaining production-grade security and scalability.

### Bootstrap 5
Frontend framework used for:
- responsive grid system
- mobile-first layouts
- reusable UI components
- navigation structure
- form styling
- rapid MVP development

Bootstrap aligned with the project's KISS architecture approach by reducing unnecessary frontend complexity.

## Database

### PostgreSQL (Neon)
Production cloud database used for:
- relational data integrity
- enrollment relationships
- transactional consistency
- scalable production deployment

PostgreSQL was chosen because it provides:
- strong relational modeling
- production reliability
- ACID compliance
- scalable cloud deployment compatibility

Neon was used as the managed PostgreSQL provider.


## Third-Party Services

### Stripe
Used for:
- secure payment processing
- hosted checkout pages
- payment verification
- webhook event handling
- enrollment automation

Stripe webhooks act as the source of truth for successful purchases.

### AWS S3
Used for:
- teacher profile image uploads
- media storage
- static asset hosting
- scalable production file delivery

The project integrates:
- S3 bucket configuration
- IAM access policies
- Django storage backends
- cloud-based media persistence

### Gmail SMTP
Used for:
- account activation emails
- communication workflows
- production email delivery

Integrated with:
- Django email backend
- HTML email templates
- token-based account activation system

## Development & Deployment Tools

### Git
Version control system used for:
- feature branching
- commit history
- development workflow management

### GitHub
Used for:
- repository hosting
- portfolio presentation
- documentation management
- version control collaboration

### Heroku
Cloud deployment platform used for:
- production hosting
- environment variable management
- deployment pipeline
- application scaling

The deployed production stack combines:
- Django
- PostgreSQL
- AWS S3
- Stripe
- Heroku infrastructure

---

# Testing

## Manual Testing
The platform was manually tested across authentication, enrollment, payments, access control, and profile management flows.

### Manual Testing Results

| Feature | Action | Expected Result | Actual Result |
|---------|--------|-----------------|---------------|
| User Registration | Submit valid registration form | Account created inactive | Pass |
| Email Activation | Click activation link | Account activated | Pass |
| Resend Activation | Submit resend form | New activation email sent | Pass |
| Login | Submit valid credentials | User logged in | Pass |
| Invalid Login | Submit wrong password | Error message displayed | Pass |
| Logout | Click logout | Session terminated | Pass |
| Course Search | Search by title | Matching courses displayed | Pass |
| Course Filtering | Filter by level | Correct level courses displayed | Pass |
| Stripe Checkout | Complete payment | Redirect to success page | Pass |
| Stripe Webhook | Successful Stripe event | Enrollment created | Pass |
| Duplicate Enrollment | Purchase owned course | Enrollment blocked | Pass |
| Course Access Protection | Non-enrolled user accesses content | Redirected safely | Pass |
| Add Review | Enrolled learner submits review | Review created | Pass |
| Edit Review | Review owner edits review | Review updated | Pass |
| Delete Review | Review owner deletes review | Review removed | Pass |
| Teacher Bio Update | Submit teacher profile form | Bio updated | Pass |
| Teacher Image Upload | Upload valid image | Image saved to AWS S3 | Pass |
| Teacher Image Validation | Upload invalid file type | Validation error displayed | Pass |
| Teacher Image Deletion | Delete existing image | Image removed | Pass |
| Profile Update | Change email/username | Profile updated | Pass |
| Contact Form | Submit valid form | Message stored and email sent | Pass |
| CAPTCHA Validation | Submit invalid captcha | Form blocked | Pass |

## Automated Testing

The project includes automated Django TestCase coverage focused on critical business logic and security-sensitive flows.

### Automated Test Coverage

#### Accounts App
Tests include:
- registration flow
- login validation
- inactive user blocking
- activation token verification
- profile signal execution
- activation link generation

#### Courses App
Tests include:
- course listing
- course detail rendering
- review permissions
- enrolled/non-enrolled review restrictions

#### Enrollments App
Tests include:
- enrollment access protection
- login restrictions
- enrollment creation

#### Payments App
Tests include:
- Stripe webhook processing
- checkout restrictions
- Stripe session creation
- enrollment automation

#### Core App
Tests include:
contact form validation
CAPTCHA verification
homepage course rendering logic

### Why Automated Tests Matter
Automated testing helps ensure:
- payment flows remain secure
- access control cannot be bypassed
- role architecture remains stable
- enrollment logic stays consistent
- future refactoring does not break business-critical systems

#### Running Tests
`python manage.py test`

---

# AWS S3 Media Storage

The platform uses AWS S3 for production-ready media and static asset storage.

## AWS S3 Responsibilities
- teacher profile image storage
- static file hosting
- scalable media delivery
- production asset management

## Why AWS S3 Was Used

AWS S3 improves:
- scalability
- deployment reliability
- media persistence
- production performance

The implementation includes:
- bucket configuration
- IAM access management
- media upload integration
- Django storage configuration

---

# Future Improvements

Future roadmap section to be expanded and prioritised further.

## Planned Improvements

### High Priority
- Course lesson/module architecture
- Video-based learning system
- Teacher-managed course content
- Advanced admin dashboard

### Medium Priority
- Progress tracking
- Learning analytics
- Certificates
- Student learning history

### Long-Term Scaling
- Live lessons
- Subscription model
- Multi-language support
- AI-assisted learning recommendations

### Backend Architecture Refactor

The current architecture contains two teacher relationship sources:

- `Enrollment.teacher`
- `Course.teacher`

This introduces unnecessary data duplication and increases the risk of inconsistent application state.

Example of the issue:

```python
Enrollment.teacher = Teacher_Ula
Course.teacher = None
```

In this situation:
- frontend components may read one source
- admin tools may read another source
- enrollment and course ownership can become inconsistent

#### Recommended Future Structure

The long-term architecture plan is to simplify the `Enrollment` model and use `Course.teacher` as the single source of truth.

### Current Enrollment Model

```python
Enrollment
├── learner
├── course
├── teacher
├── is_active
└── created_at
```

### Planned Enrollment Model

```python
Enrollment
├── learner
├── course
├── is_active
└── created_at
```

### Planned Refactor

Remove:
- `Enrollment.teacher`

Keep:
- `learner`
- `course`
- `is_active`
- `created_at`

Teacher relationships would always be accessed through:

```python
enrollment.course.teacher
```

### Benefits of This Refactor

- simpler database architecture
- single source of truth
- cleaner admin logic
- easier maintenance
- fewer synchronization bugs
- safer long-term scalability
- simpler ORM queries

Example simplified query:

```python
Enrollment.objects.filter(course__teacher=user)
```

instead of:

```python
Enrollment.objects.filter(teacher=user)
```

### Minimal / Safe Migration Strategy

The preferred implementation approach is:

- remove only `Enrollment.teacher` usage
- keep all existing platform functionality intact
- migrate all teacher lookups to `course.teacher`
- avoid unrelated changes to profile or image systems

This approach follows the project's KISS architecture principles while improving long-term maintainability.

---

### React + Django REST Framework Migration

A planned long-term improvement is gradual migration toward a hybrid Django + React architecture.

The goal is to improve:
- frontend scalability
- user interactivity
- dashboard responsiveness
- reusable component architecture
- API-driven development experience

The recommended approach is **incremental migration**, not a full frontend rewrite.

## Recommended Stack

### Frontend
- React
- React Router
- Bootstrap

### Backend
- Django
- Django REST Framework (DRF)

### Optional Additions
- Axios

The project intentionally avoids introducing excessive frontend complexity too early.

Technologies intentionally postponed:
- Redux
- TypeScript
- Next.js
- Tailwind

This keeps the learning and development process aligned with KISS principles.

---

## Recommended Migration Strategy

### Phase 1 - React Fundamentals + DRF
Learn:
- JSX
- components
- props
- hooks
- forms
- API fetching

Introduce Django REST Framework APIs for:
- courses
- reviews
- enrollments

Templates remain unchanged initially.

---

### Phase 2 - React Reviews System

First React integration target:
- course reviews system

Reason:
- isolated feature
- already fully functional
- strong portfolio value
- ideal for API integration practice

Planned React functionality:
- fetch reviews
- add review
- edit/delete review
- live average rating updates

---

### Phase 3 - React Dashboards

Convert:
- learner dashboard
- teacher dashboard

This introduces:
- reusable UI components
- async API handling
- dynamic rendering
- loading states

---

### Phase 4 - Optional Full Frontend Migration

Potential future migration:
- course pages
- profile pages
- authentication pages
- payment flows

At this stage:
- Django becomes API backend
- React becomes frontend application

---

## Why This Architecture Matters

This roadmap would transform the project into a modern hybrid full-stack architecture demonstrating:

- Django backend development
- REST API architecture
- React frontend integration
- scalable SaaS structure
- production-ready frontend/backend separation

The migration strategy prioritises:
- low-risk refactoring
- stable backend preservation
- gradual frontend modernisation
- portfolio-focused scalability

---

# Deployment

## Local Setup

```bash
git clone https://github.com/jackpoletek/cup-of-english.git
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

---

- **Bug:** Django success messages persisted in session storage after logout and appeared repeatedly on the login page:
- **Error:** Messages such as _Teacher profile updated successfully_ continued appearing after logout.
- **Fix:**
- Messages were cleared before logout using Django message storage iteration.
The login template message block was removed.
Removed Code
{% if messages %}
{% for message in messages %}
<div class="alert alert-danger">{{ message }}</div>
{% endfor %}
{% endif %}

Message rendering was centralised inside `base.html`.

---

- **Bug:** Homepage "Popular Courses" displayed duplicated course categories because the queryset selected the first six database rows instead of one course per category.
Example incorrect output:
- Business English A2
- Business English B1
- Business English B2

instead of:
- General English
- Business English
- English for Specific Purposes

- **Error:** No Django or Python error occurred.
The issue caused:
- duplicated course categories
- repeated Business English cards
- incorrect homepage categorisation
- inconsistent UX between homepage and courses page
- **Fix:**
- Implemented one-course-per-category logic.

---

### Known Issues
- Stripe webhook processing may occasionally introduce slight enrollment delay
- Full course lesson architecture is not yet implemented
- Progress tracking system not yet available
- Teacher/course architecture still contains duplicated teacher references (`Enrollment.teacher` and `Course.teacher`)

---

# Credits

## Template & Design Adaptation

The frontend design was adapted and customised from the following educational template:
[Ecourses Template by Html Codex](https://htmlcodex.com/online-courses-html-template/) </br>

The original template structure was heavily modified and extended to support:
- Django template rendering
- Stripe payment integration
- responsive educational marketplace architecture
- authentication workflows
- dynamic course management
- role-based user functionality

The project followed KISS principles by reusing and adapting a clean educational UI foundation instead of overengineering the frontend architecture.

Technical Documentation:
- Django: https://docs.djangoproject.com/
- Stripe: https://stripe.com/docs
- Bootstrap: https://getbootstrap.com/

---

# Acknowledgements

Cup of English was developed as a portfolio-grade full-stack application focused on combining practical backend engineering with user-friendly educational experience design.

The project explores the balance between functionality and simplicity - a continuous process of negotiating form and content while avoiding unnecessary complexity. Throughout development, the focus remained on building a platform that feels intuitive for users while still implementing production-oriented architecture, secure payment handling, scalable database relationships, and maintainable backend logic.

The application was also an opportunity to apply KISS (Keep It Simple, Stupid) principles in a real-world context, where technical decisions were guided not only by implementation difficulty, but also by usability, clarity, maintainability, and long-term scalability.

Special thanks to:
- Brian Macharia for mentorship and guidance
- Manuel Perez for teaching and academic support
- Urszula for encouragement, support, and patience throughout the development process

Original design template courtesy of Html Codex:
https://htmlcodex.com/online-courses-html-template/

Adapted, expanded, and developed further by Jack Poletek.
