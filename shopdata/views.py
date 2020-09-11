from django.shortcuts import render
from .models import SwiperImages, HomeSort, HomeRecommend, CategoryData, GoodsListData, GoodsDetail
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
# Create your views here.


def home_data(request):
    swiper_data = SwiperImages.objects.all()
    swiper_image = serializers.serialize('json', swiper_data)
    swiper_image = json.loads(swiper_image)
    swiper_image_info = []
    for i in range(len(swiper_image)):
        swiper_image_info.append(swiper_image[i]['fields'])

    sort_data = HomeSort.objects.all()
    home_sort = serializers.serialize('json', sort_data)
    home_sort = json.loads(home_sort)
    home_sort_info = []
    for i in range(len(home_sort)):
        home_sort_info.append(home_sort[i]['fields'])

    recommend_data = HomeRecommend.objects.all()
    home_recommend = serializers.serialize('json', recommend_data)
    home_recommend = json.loads(home_recommend)
    home_recommend_info = []
    for i in range(len(home_recommend)):
        home_recommend_info.append(home_recommend[i]['fields'])

    data = {
        'data': {
            'swiper_image_info': swiper_image_info,
            'home_sort_info': home_sort_info,
            'home_recommend_info': home_recommend_info
        },
        'code': 200,
        'msg': 'true'
    }
    return JsonResponse(data, safe=False)


def category_data(request):
    category = CategoryData.objects.all()
    category_info = serializers.serialize('json', category)
    category_info = json.loads(category_info)
    category_info_data = []

    for i in range(len(category_info)):
        category_info_data.append(category_info[i]['fields'])

    lists = []
    tree = {}
    pid = ''
    for i in category_info_data:
        item = i
        tree[item['cat_id']] = item
    root = None
    for i in category_info_data:
        obj = i
        if not obj['pid']:
            root = tree[obj['cat_id']]
            lists.append(root)
        else:
            pid = obj['pid']
            if 'childList' not in tree[pid]:
                tree[pid]['childList'] = []
            tree[pid]['childList'].append(tree[obj['cat_id']])

    data = {
        'data': {
            'category_data': lists
        },
        'code': 200,
        'msg': 'true'
    }
    return JsonResponse(data, safe=False)


def goods_list_data(request):
    if request.method == "POST":
        param = request.POST.get('param')
        goods_list = GoodsListData.objects.filter(classify=param)
        goods_list_info = serializers.serialize('json', goods_list)
        goods_list_info = json.loads(goods_list_info)
        goods_list_info_data = []

        for i in range(len(goods_list_info)):
            goods_list_info_data.append(goods_list_info[i]['fields'])

        data = {
            'data': {
                'goods_list_info_data': goods_list_info_data,
            },
            'code': 200,
            'msg': 'true'
        }
        return JsonResponse(data, safe=False)


def goods_detail(request):
    if request.method == "POST":
        param = request.POST.get('param')
        detail_data = GoodsDetail.objects.filter(classify=param)
        detail_data_info = serializers.serialize('json', detail_data)
        detail_data_info = json.loads(detail_data_info)
        detail_data_info_data = []

        for i in range(len(detail_data_info)):
            detail_data_info_data.append(detail_data_info[i]['fields'])

        lists = []
        tree = {}
        pid = ''
        for i in detail_data_info_data:
            item = i
            tree[item['cat_id']] = item
        root = None
        for i in detail_data_info_data:
            obj = i
            if not obj['pid']:
                root = tree[obj['cat_id']]
                lists.append(root)
            else:
                pid = obj['pid']
                if 'childList' not in tree[pid]:
                    tree[pid]['childList'] = []
                tree[pid]['childList'].append(tree[obj['cat_id']])

        data = {
            'data': {
                'goods_detail': lists
            },
            'code': 200,
            'msg': 'true'
        }
        return JsonResponse(data, safe=False)
