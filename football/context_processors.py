from .models import Countries, News


def all_info_processors(request):
    return {
        'all_countries': Countries.objects.all().order_by('rating_uefa'),
        'all_news': News.objects.all()[:3]
    }