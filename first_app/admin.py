from django.contrib import admin
from first_app.models import Topic,webpage,AccessRecord,UserProfileInfo
# Register your models here.
admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(AccessRecord)
admin.site.register(UserProfileInfo)
