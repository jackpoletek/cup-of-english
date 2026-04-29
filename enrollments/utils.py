from .models import Enrollment

def is_enrolled(user, course):
    # Safe check for user authentication
    if not user or not user.is_authenticated:
        return False

    return Enrollment.objects.filter(
        learner=user,
        course=course,
        is_active=True
    ).exists()
