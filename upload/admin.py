from django.contrib import admin

from .models import FaceImage


class FaceImageAdmin(admin.ModelAdmin):
    list_display = ("name", "image")


admin.site.register(FaceImage, FaceImageAdmin)
