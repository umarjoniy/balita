from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import FormComment


def header_maker(ctx: dict):
    regions = Regions.objects.all()
    ctx['regions'] = regions

    cats = Categories.objects.all()
    ctx['cats'] = cats

    return ctx


def footer_maker(ctx: dict, article):
    articles = article.order_by('-created_at')
    ctx['latest_post'] = articles[:3]
    return ctx


def give_articles(articles, num, name, ctx):
    if len(articles) > num:
        ctx[name] = articles[:num]
        articles = articles[num:]
    else:
        ctx[name] = articles[:num]
    return ctx


def get_cat_num(ctx: dict):
    cats = Categories.objects.all()
    for i in cats:
        num = len(Articles.objects.filter(category=i))
        i.num = num
    ctx['cats'] = cats
    return ctx


def home(request):
    ctx = {}

    ctx = header_maker(ctx)
    articles = Articles.objects.filter(is_published=True)
    ctx = footer_maker(ctx, articles)

    for i in articles:
        com_num = len(Comments.objects.filter(article=i))
        i.com_num = com_num

    ctx = give_articles(articles, 5, 'car_arts', ctx)

    ctx = give_articles(articles, 3, 'row_0_articles', ctx)

    ctx = give_articles(articles, 8, 'row_1_articles', ctx)

    ctx = give_articles(articles, 3, 'hor_articles', ctx)

    tags = Tags.objects.all()
    ctx['tags'] = tags

    ctx = get_cat_num(ctx)

    t = Articles.objects.filter(is_published=True).order_by('-views')

    ctx = give_articles(t, 4, 'popular_posts', ctx)

    p = Paginator(Articles.objects.filter(is_published=True), 8)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    ctx['p'] = p
    ctx['posts'] = posts_

    return render(request, 'index.html', ctx)


def regions(request):
    ctx = {}
    ctx = header_maker(ctx)
    reg = request.GET.get('region')
    ctx = give_articles(Articles.objects.filter(is_published=True).order_by('-views'), 15, 'popular_posts',ctx)
    if reg:
        reg_obj = Regions.objects.get(name=reg)
        articles = Articles.objects.filter(region=reg_obj)
        ctx = footer_maker(ctx, articles)
        ctx['cat_name'] = 'Region: ' + reg
        ctx = give_articles(articles, 8, 'row_1_articles', ctx)
    else:
        articles = Articles.objects.filter(is_published=True)
        ctx = give_articles(articles, 15, 'row_1_articles', ctx)
        ctx['cat_name'] = 'All'
    for i in articles:
        com_num = len(Comments.objects.filter(article=i))
        i.com_num = com_num

    ctx = give_articles(articles, 3, 'hor_articles', ctx)
    ctx = get_cat_num(ctx)
    tags = Tags.objects.all()
    ctx['tags'] = tags
    
    p = Paginator(articles, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    ctx['p'] = p
    ctx['posts'] = posts_

    return render(request, 'regions.html', ctx)


def blog_single(request, slug):
    ctx = {}
    post = Articles.objects.get(slug=slug)

    form = FormComment(request.POST or None)
    if form.is_valid():
        form.article = post
        print(1)
        a = form.save(commit=False)
        a.article = post
        a.save()

    if request.method == 'POST':
        return redirect(f'/blog-single/{post.slug}')

    post.views += 1
    post.save()
    ctx['article'] = post
    ctx['form'] = form
    ctx['tags'] = post.tags.all()
    comments = Comments.objects.filter(article=post)
    ctx['comments'] = comments

    return render(request, 'blog-single.html', ctx)


def category(request):
    ctx = {}
    ctx = header_maker(ctx)
    cat = request.GET.get('name')
    ctx = give_articles(Articles.objects.filter(is_published=True).order_by('-views'), 4, 'popular_posts',
                                  ctx)
    if cat:
        cat_obj = Categories.objects.get(name=cat)
        articles = Articles.objects.filter(category=cat_obj)
        ctx = footer_maker(ctx, articles)
        ctx['cat_name'] = 'Category: ' + cat
        ctx = give_articles(articles, 8, 'row_1_articles', ctx)
    else:
        articles = Articles.objects.filter(is_published=True)
        ctx = give_articles(articles, 8, 'row_1_articles', ctx)
        ctx['cat_name'] = 'All'
    for i in articles:
        com_num = len(Comments.objects.filter(article=i))
        i.com_num = com_num

    ctx = give_articles(articles, 3, 'hor_articles', ctx)
    ctx = get_cat_num(ctx)
    tags = Tags.objects.all()articles
    ctx['tags'] = tags

    p = Paginator(articles, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    ctx['p'] = p
    ctx['posts'] = posts_

    return render(request, 'category.html', ctx)


def search(request):
    ctx = {}
    ctx = header_maker(ctx)
    cat = request.POST.get('q')
    ctx = give_articles(Articles.objects.filter(is_published=True).order_by('-views'), 4, 'popular_posts',
                                  ctx)
    if cat:
        articles = Articles.objects.filter(is_published=True).filter(title__contains=cat)
        ctx = footer_maker(ctx, articles)
        ctx['cat_name'] = 'Results: ' + cat
        ctx = give_articles(articles, 8, 'row_1_articles', ctx)
    else:
        return HttpResponse('Not Found')
    for i in articles:
        com_num = len(Comments.objects.filter(article=i))
        i.com_num = com_num

    ctx = give_articles(articles, 3, 'hor_articles', ctx)
    ctx = get_cat_num(ctx)
    tags = Tags.objects.all()
    ctx['tags'] = tags

    p = Paginator(articles, 8)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    ctx['p'] = p
    ctx['posts'] = posts_

    return render(request, 'search.html', ctx)
