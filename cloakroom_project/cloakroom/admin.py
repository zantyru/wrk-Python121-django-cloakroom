from django.contrib import admin

from .models import (
    Label,
    LabelState
)


class LabelAdmin(admin.ModelAdmin):
    fields = ('number', 'state')
    list_filter = ('state', )


admin.site.register(Label, LabelAdmin)
admin.site.register(LabelState)
