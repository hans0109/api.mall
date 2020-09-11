from django.db import models

# Create your models here.


class SwiperImages(models.Model):
    images = models.CharField(max_length=255, verbose_name="轮播图图片", null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name="链接网址", null=True, blank=True)

    def __str__(self):
        return self.images

    class Meta:
        db_table = 'data_home_swiper'
        verbose_name = '轮播图管理'
        verbose_name_plural = verbose_name


class HomeSort(models.Model):
    icon = models.CharField(max_length=255, verbose_name="分类图标", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="分类标题", null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name="链接", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'data_home_sort'
        verbose_name = '首页分类管理'
        verbose_name_plural = verbose_name


class HomeRecommend(models.Model):
    title = models.CharField(max_length=255, verbose_name="推荐标题", null=True, blank=True)
    image = models.CharField(max_length=255, verbose_name="推荐图片", null=True, blank=True)
    price = models.CharField(max_length=255, verbose_name="推荐价格", null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name="推荐链接", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'data_home_recommend'
        verbose_name = '首页推荐管理'
        verbose_name_plural = verbose_name


class CategoryData(models.Model):
    cat_id = models.CharField(max_length=255, verbose_name="关联ID", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="标题", null=True, blank=True)
    icon = models.CharField(max_length=255, verbose_name="图标", null=True, blank=True)
    pid = models.CharField(max_length=255, verbose_name="关联上级ID", null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name="链接", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'data_category'
        ordering = ['cat_id']
        verbose_name = '分类数据'
        verbose_name_plural = verbose_name


class GoodsListData(models.Model):
    img = models.CharField(max_length=255, verbose_name="图片", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="标题", null=True, blank=True)
    old_price = models.CharField(max_length=255, verbose_name="原价", null=True, blank=True)
    new_price = models.CharField(max_length=255, verbose_name="现价", null=True, blank=True)
    recommend = models.CharField(max_length=255, verbose_name="推荐理由", null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name="链接", null=True, blank=True)
    classify = models.CharField(max_length=255, verbose_name="分类", null=True, blank=True)
    page = models.CharField(max_length=255, verbose_name="页码", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'data_goods_list'
        ordering = ['classify']
        verbose_name = '物品列表数据'
        verbose_name_plural = verbose_name


class GoodsDetail(models.Model):
    cat_id = models.CharField(max_length=255, verbose_name="关联ID", null=True, blank=True)
    pid = models.CharField(max_length=255, verbose_name="关联上级ID", null=True, blank=True)
    belong = models.CharField(max_length=255, verbose_name="类型", null=True, blank=True)
    img = models.CharField(max_length=255, verbose_name="图片", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="标题", null=True, blank=True)
    old_price = models.CharField(max_length=255, verbose_name="原价", null=True, blank=True)
    new_price = models.CharField(max_length=255, verbose_name="现价", null=True, blank=True)
    recommend = models.CharField(max_length=255, verbose_name="优惠活动", null=True, blank=True)
    discuss = models.CharField(max_length=255, verbose_name="评论", null=True, blank=True)
    classify = models.CharField(max_length=255, verbose_name="归属", null=True, blank=True)

    def __str__(self):
        return self.classify

    class Meta:
        db_table = 'data_goods_detail_data'
        ordering = ['classify', 'cat_id']
        verbose_name = '物品详情图片及介绍'
        verbose_name_plural = verbose_name
