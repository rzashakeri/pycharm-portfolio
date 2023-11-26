from django.contrib import admin

from pages.models import Page, About, SkillCategory, Skill, ContactUs, Project, SiteSettings, SocialMedia, Education

admin.site.register(SiteSettings)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "parent", "is_parent"]
    list_filter = ["is_parent"]
    ordering = ["is_parent"]
    search_fields = ["title"]



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["page", "heading"]
    search_fields = ["title"]



@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["category", "name"]
    ordering = ["name"]
    search_fields = ["name"]



@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project)
admin.site.register(SocialMedia)
admin.site.register(Education)
