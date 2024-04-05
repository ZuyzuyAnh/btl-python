from django.shortcuts import render, get_object_or_404
from .models import Page
from manga.models import Chapter
from django.contrib.auth.models import AnonymousUser
# Create your views here.
def readingPage(request, pk):
    chapter = get_object_or_404(Chapter, pk = pk)
    if(request.user.is_anonymous == False and request.user not in chapter.user_visited.all()):
        chapter.user_visited.add(request.user)
    pages = Page.objects.filter(chapter = chapter)
    chapters_in_manga = Chapter.objects.filter(manga = chapter.manga)
    chaplist = list(chapters_in_manga.all().values_list("name", flat = True))
    currentIndex = chaplist.index(chapter.name)
    numberOfChapter = len(chaplist)
    manga = chapter.manga
    if(currentIndex == 0 and numberOfChapter > 1):
        nextChap = chapters_in_manga.all()[currentIndex+1]
        return render(request, 'readingPage/readingPage.html',{
        'pages': pages,
        'chapter': chapter,
        'nextChap': nextChap,
        'numberOfChapter': chapters_in_manga.all().__len__,
        'chapters_in_manga': chapters_in_manga,
        'manga': manga
    })
    elif currentIndex == numberOfChapter-1 and numberOfChapter > 1:
        prevChap = chapters_in_manga.all()[currentIndex-1]
        return render(request, 'readingPage/readingPage.html',{
            'pages': pages,
            'chapter': chapter,
            'prevChap': prevChap,
            'numberOfChapter': chapters_in_manga.all().__len__,
            'chapters_in_manga': chapters_in_manga,
            'manga': manga
    })
    elif currentIndex == 0 and numberOfChapter ==1:
        return render(request, 'readingPage/readingPage.html',{
            'pages': pages,
            'chapter': chapter,
            'numberOfChapter': chapters_in_manga.all().__len__,
            'chapters_in_manga': chapters_in_manga,
            'manga': manga
        })
    else:
        nextChap = chapters_in_manga.all()[currentIndex+1]
        prevChap = chapters_in_manga.all()[currentIndex-1]
        return render(request, 'readingPage/readingPage.html',{
            'pages': pages,
            'chapter': chapter,
            'nextChap': nextChap,
            'prevChap': prevChap,
            'numberOfChapter': chapters_in_manga.all().__len__,
            'chapters_in_manga': chapters_in_manga,
            'manga': manga
        })
