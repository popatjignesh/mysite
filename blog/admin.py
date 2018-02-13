from django.contrib import admin
from blog.models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('Post data', {'fields': ('title', 'text', 'post_type')}),
	    ('Date', {'fields': ('created_date',)}),
	    ('Permission', {'fields': ('is_active', )}),
	)

	exclude = ('published_date',)

	search_fields = ('title',)
	ordering = ('-created_date',)
	list_display = ('title', 'post_type')
	list_display_links = ('title', 'post_type')
	list_filter = ('post_type', )

	def enable(self, request, queryset):
		queryset.update(is_active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

