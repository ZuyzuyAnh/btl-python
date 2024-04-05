from django.contrib import admin
from .models import Manga,Chapter,Tag,Author
from readingPage.models import Page
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
# Register your models here.    
class PageInline(NestedStackedInline):
    model = Page
    extra = 1
    fk_name = 'chapter'
class ChapterInLine(NestedStackedInline):
    model = Chapter
    extra = 1
    fk_name = 'manga'
    inlines = [PageInline]

class MangaAdmin(NestedModelAdmin):
    model = Manga
    inlines = [ChapterInLine]
admin.site.register(Manga, MangaAdmin)
admin.site.register(Tag)
admin.site.register(Author)
