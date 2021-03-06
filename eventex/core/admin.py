from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk
from django.utils.html import format_html

class ContactInLine(admin.TabularInline):
    model = Contact
    extra=1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'photo_img', 'website_link', 'email', 'phone')

    @classmethod
    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    @classmethod
    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.short_description = 'foto'

    @classmethod
    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'e-mail'

    @classmethod
    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'telefone'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)