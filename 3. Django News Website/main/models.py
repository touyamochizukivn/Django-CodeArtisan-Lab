from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imgs/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
    