from django.contrib import admin
from .models import attendance
from .models import attendee
from .models import meal
from .models import enableSignUp
from .models import announcement


# Show models in admin area
admin.site.register(meal)
admin.site.register(attendee)
admin.site.register(announcement)
admin.site.register(enableSignUp)
admin.site.register(attendance)