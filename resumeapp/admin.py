from django.contrib import admin
from .models import ContactInformation, PreviousEmployment, Education, ProfessionalSkills, SoftwareData, LanguagesData

# Register your models here.
admin.site.register(ContactInformation)
admin.site.register(PreviousEmployment)
admin.site.register(Education)


class SoftwareDataTabularInline(admin.TabularInline):
    model = SoftwareData


class LanguagesDataTabularInline(admin.TabularInline):
    model = LanguagesData


class ProfessionalSkillsModelAdmin(admin.ModelAdmin):
    inlines = [SoftwareDataTabularInline, LanguagesDataTabularInline]

    class Meta:
        model = ProfessionalSkills


admin.site.register(ProfessionalSkills, ProfessionalSkillsModelAdmin)

# class SkillDataTabularInline(admin.TabularInline):
#     model = SoftwareData
#
#
# class SkillModelAdmin(admin.ModelAdmin):
#     inlines = [SkillDataTabularInline]
#
#     class Meta:
#         model = ProfessionalSkills
#
#
# admin.site.register(ProfessionalSkills, SkillModelAdmin)
