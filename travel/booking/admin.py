from django.contrib import admin

from booking.models import Profile, Hotel, Flight


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('address', 'name')
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': [ 'name', 'address']}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()

        return 'hotel',


admin.site.register(Profile)
admin.site.register(Hotel, BookingAdmin)
admin.site.register(Flight)
