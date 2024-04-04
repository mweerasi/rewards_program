from django.contrib import admin

from .models.history import History
from .models.member import Member
from .models.program import Program
from .models.reward import Reward


# Register your models here.
admin.site.register(History)
admin.site.register(Member)
admin.site.register(Program)
admin.site.register(Reward)
