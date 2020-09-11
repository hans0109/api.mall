from django.contrib import admin
from .models import SwiperImages, HomeSort, HomeRecommend, CategoryData, GoodsListData, GoodsDetail
# Register your models here.


@admin.register(SwiperImages)
class SwiperImagesAdmin(admin.ModelAdmin):
    list_display = ['images', 'link']


@admin.register(HomeSort)
class HomeSortAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'link']


@admin.register(HomeRecommend)
class HomeRecommendAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'price', 'link']


@admin.register(CategoryData)
class CategoryDataAdmin(admin.ModelAdmin):
    list_display = ['cat_id', 'title', 'icon', 'pid', 'link']


@admin.register(GoodsListData)
class GoodsListDataAdmin(admin.ModelAdmin):
    list_display = ['img', 'title', 'old_price', 'new_price', 'recommend', 'link', 'classify', 'page']


@admin.register(GoodsDetail)
class GoodsDetailAdmin(admin.ModelAdmin):
    list_display = ['cat_id', 'pid', 'belong', 'img', 'title', 'old_price', 'new_price', 'recommend', 'discuss',
                    'classify']
