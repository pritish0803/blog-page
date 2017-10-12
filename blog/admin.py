

from django.contrib import admin

# Register your models here.
from blog.models import Post
class profileadmin(admin.ModelAdmin):
	class Meta:
		model=Post
admin.site.register(Post,profileadmin)
