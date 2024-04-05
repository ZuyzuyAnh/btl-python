from django.shortcuts import render, get_object_or_404, redirect
from manga.models import Tag, Manga, Chapter, Author
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
#Trang chủ
def frontpage(request):
    manga = Manga.objects.all()
    item_per_page = 10
    paginator = Paginator(manga, item_per_page)
    page = request.GET.get('page')
    try:
        manga = paginator.page(page)
    except PageNotAnInteger:
        manga = paginator.page(1)
    except EmptyPage:
        manga = paginator.page(paginator.num_pages)
    sorted_mangas = sorted(manga, key = lambda x: x.like_count(), reverse=True)
    most_viewed_manga = sorted_mangas.pop(0)
    return render(request, 'core/frontpage.html', {
        'mangas' : manga,
        'sorted_mangas': sorted_mangas,
        'most_viewed_manga' : most_viewed_manga,
    })
#tìm kiếm theo tên
def searchpage(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        mangas = Manga.objects.filter(name__contains = searched)
        item_per_page = 10
        paginator = Paginator(mangas, item_per_page)
        page = request.GET.get('page')
        try:
            mangas = paginator.page(page)
        except PageNotAnInteger:
            mangas = paginator.page(1)
        except EmptyPage:
            mangas = paginator.page(paginator.num_pages)
        return render(request, "core/searchpage.html", {
            'searched': searched,
            'mangas': mangas
        })
    

#đăng kí 
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
#Tab Truyện hot
def mangaByLikes(request):
    mangas = Manga.objects.all() 
    mangas = sorted(mangas, key=lambda x: x.like_count(), reverse=True)
    items_per_page = 4
    paginator = Paginator(mangas, items_per_page)
    page = request.GET.get('page')
    try:
        mangas = paginator.page(page)
    except PageNotAnInteger:
        mangas = paginator.page(1)
    except EmptyPage:
        mangas = paginator.page(paginator.num_pages)
    return render(request, 'core/mangaByLikes.html', {
        'mangas': mangas
    })

#Danh sách truyện đã thích của user
@login_required
def likedManga(request):
    mangas = Manga.objects.filter(like=request.user)

    items_per_page = 10  # Đặt số item muốn hiển thị trên mỗi trang
    paginator = Paginator(mangas, items_per_page)
    page = request.GET.get('page')

    try:
        mangas = paginator.page(page)
    except PageNotAnInteger:
        mangas = paginator.page(1)
    except EmptyPage:
        mangas = paginator.page(paginator.num_pages)

    return render(request, 'core/likedManga.html', {
        'mangas': mangas
    })
#Tìm kiếm nâng cao

def filterView(request):
    tags = Tag.objects.all()
    mangas = Manga.objects.all()
    name_contains_query = request.GET.get('name_contains')
    author_query = request.GET.get('author')
    tag_list = request.GET.getlist('tags')
    sort = request.GET.get('sort')

    if name_contains_query != '' and name_contains_query is not None:
        mangas = mangas.filter(name__icontains=name_contains_query)
    if author_query != '' and author_query is not None:
        mangas = mangas.filter(author__name__icontains=author_query)
    if len(tag_list) > 0:
        for tag in tag_list:
            mangas = mangas.filter(tag__name__icontains=tag)
    if sort == 'A-Z':
        mangas = mangas.order_by('name')
    elif sort == 'Z-A':
        mangas = mangas.order_by('-name')
    elif sort == 'Ngày Cập Nhật Giảm Dần':
        mangas = mangas.order_by('-updated')
    elif sort == 'Ngày Cập Nhật Tăng Dần':
        mangas = mangas.order_by('updated')
    elif sort == 'Lượt Thích Giảm Dần':
        mangas = sorted(mangas, key=lambda x: x.like_count(), reverse=True)
    elif sort == 'Lượt Thích Tăng Dần':
        mangas = sorted(mangas, key=lambda x: x.like_count())
    elif sort == 'Lượt Xem Giảm Dần':
        mangas = sorted(mangas, key=lambda x: x.views, reverse=True)
    elif sort == 'Lượt Xem Tăng Dần':
        mangas = sorted(mangas, key=lambda x: x.views)
    items_per_page = 10  # Đặt số item muốn hiển thị trên mỗi trang
    paginator = Paginator(mangas, items_per_page)
    page = request.GET.get('page')

    try:
        mangas = paginator.page(page)
    except PageNotAnInteger:
        mangas = paginator.page(1)
    except EmptyPage:
        mangas = paginator.page(paginator.num_pages)

    return render(request, 'core/filterView.html', {
        'tags': tags,
        'mangas': mangas,
    })
def mangaByTag(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    mangas = Manga.objects.filter(tag=tag)
    items_per_page = 10  # Đặt số item muốn hiển thị trên mỗi trang
    paginator = Paginator(mangas, items_per_page)
    page = request.GET.get('page')

    try:
        mangas = paginator.page(page)
    except PageNotAnInteger:
        mangas = paginator.page(1)
    except EmptyPage:
        mangas = paginator.page(paginator.num_pages)

    return render(request, 'core/mangaByTag.html', {
        'tag': tag,
        'mangas': mangas
    })
def mangaByUpdate(request):
    mangas = Manga.objects.all().order_by('-updated')

    items_per_page = 10  # Đặt số item muốn hiển thị trên mỗi trang
    paginator = Paginator(mangas, items_per_page)
    page = request.GET.get('page')

    try:
        mangas = paginator.page(page)
    except PageNotAnInteger:
        mangas = paginator.page(1)
    except EmptyPage:
        mangas = paginator.page(paginator.num_pages)

    return render(request, 'core/mangaByUpdate.html', {
        'mangas': mangas
    })
def author(request, pk):
    author = get_object_or_404(Author, pk = pk)
    mangas = Manga.objects.all().filter(author = author)
    item_per_page = 10
    paginator = Paginator(mangas, item_per_page)
    page = request.GET.get('page')
    try:
        mangas = paginator.page(page)
    except PageNotAnInteger:
        mangas = paginator.page(1)
    except EmptyPage:
        mangas = paginator.page(paginator.num_pages)
    mangas = Manga.objects.filter(author = author)
    return render(request, 'core/author.html',{
        'author': author,
        'mangas': mangas
    })
