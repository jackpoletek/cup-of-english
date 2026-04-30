# Cup of English

![Responsive Mockup](docs/readme-images/responsive-placeholder.png)

Cup of English is a full-stack Django e-commerce educational platform designed as a professional MVP online English school for teenagers and adults.

The platform enables users to browse structured English courses, securely purchase access via Stripe, and unlock premium content after successful enrollment.

The project combines:

- Secure user registration with email activation
- Role-based user architecture (Learner / Teacher / Admin)
- Course catalog segmentation by learning purpose
- Stripe-powered course purchasing
- Enrollment automation via Stripe webhooks
- Protected premium content access
- AWS S3 production asset storage
- Neon PostgreSQL production database
- Heroku cloud deployment
- Gmail SMTP communication system

The application follows **KISS (Keep It Simple, Stupid)** principles while demonstrating real-world full-stack development practices.

![Live Project](https://cup-of-english.herokuapp.com/)
![Repository](https://github.com/jackpoletek/cup-of-english)

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

The goal of Cup of English is to provide a simple, focused, and conversion-oriented platform for learners to:

- Improve English skills through structured courses
- Purchase access quickly and securely
- Access premium content without friction

The platform prioritizes:

- clarity over complexity
- fast load times
- direct monetization flow
- minimal user friction

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

### Project Planning - User Stories

---

### User Story 1: Responsive and intuitive navigation (must-have)

**User Story:**
As a First-Time Visitor, I want a responsive and intuitive interface so that I can easily explore the platform on any device.

**Acceptance Criteria**

- Fully responsive design across devices
- Clear navigation menu
- Accessible key pages

**Tasks**

- Implement Bootstrap responsive grid
- Design clear navigation structure

---

### User Story 2: Course discovery (must-have)

**User Story:**
As a Visitor, I want to browse courses by category so that I can find relevant learning content.

**Acceptance Criteria**

- Courses grouped by type
- Courses displayed clearly
- Easy navigation between categories

**Tasks**

- Create course category pages
- Display courses dynamically

---

### User Story 3: Secure registration and login (must-have)

**User Story:**
As a User, I want to register and activate my account so that I can securely access the platform.

**Acceptance Criteria**

- Email activation required
- Inactive users cannot log in
- Secure authentication flow

**Tasks**

- Implement activation tokens
- Configure email system

---

### User Story 4: Course purchase (must-have)

**User Story:**
As a Learner, I want to purchase a course easily so that I can access its content.

**Acceptance Criteria**

- Stripe checkout works
- Payment success triggers enrollment
- Cancel flow handled correctly

**Tasks**

- Integrate Stripe checkout
- Store metadata for user/course

---

### User Story 5: Protected content access (must-have)

**User Story:**
As a Learner, I want access only to purchased content so that the platform maintains content security.

**Acceptance Criteria**

- Non-enrolled users blocked
- Enrolled users granted access

**Tasks**

- Implement access checks
- Use shared enrollment helper

---

### User Story 6: Contact communication (should-have)

**User Story:**
As a Visitor, I want to contact the platform so that I can ask questions.

**Acceptance Criteria**

- Contact form available
- Email sent successfully

**Tasks**

- Implement form
- Configure SMTP

---

# Features

## Existing Features

### Authentication System

- User registration with email activation
- Secure login/logout
- Role-based architecture

![Auth Screenshot](docs/readme-images/auth-placeholder.png)

---

### Course Browsing

- Course categories:
- General English
- Business English
- EAP / ESP
- Exam preparation

- Courses filtered by level (A2-C2)

![Courses Screenshot](docs/readme-images/courses-placeholder.png)

---

### Course Details

- Detailed course information
- Enrollment status visibility
- Clear purchase CTA

---

### Stripe Payments

- Secure Stripe checkout
- Metadata linking user and course
- Webhook-driven enrollment (source of truth)

![Stripe Screenshot](docs/readme-images/stripe-placeholder.png)

---

### Enrollment System

- One enrollment per user per course
- Automatic creation via webhook
- Shared `is_enrolled` helper ensures consistency across app

---

### Course Access Control

- Content restricted to enrolled users
- Safe redirects for unauthorized access

---

### Profile Page

- Displays enrolled courses
- Supports user account management

---

### Contact Form

- Sends real emails via Gmail SMTP
- Fully functional in production

---

### E-commerce Design Decision (No Basket)

The platform intentionally does **not include a shopping basket**.

**Reasoning:**

- Users typically purchase one course at a time
- Reduces friction in checkout flow
- Simplifies backend logic
- Improves conversion rate

This aligns with MVP product strategy and KISS principles.

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

## Color Scheme

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
