from django.contrib import admin

from lestvica.models import Municipality, Bucket, GroupBucket, Group, Question, Answer, Recommendation

# Register your models here.
admin.site.register(Municipality)
admin.site.register(Bucket)
admin.site.register(GroupBucket)
admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Recommendation)
