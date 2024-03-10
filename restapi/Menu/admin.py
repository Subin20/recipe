from django.contrib import admin

# Register your models here.
from Menu.models import Menu
from Menu.models import RatingAndReview


admin.site.register(Menu)

admin.site.register(RatingAndReview)