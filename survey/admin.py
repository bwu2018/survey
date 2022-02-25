from django.contrib import admin
from .models import Answer

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('code', 'num_players', 'text',)



# admin.site.register(Room, RoomAdmin)
admin.site.register(Answer, AnswerAdmin)