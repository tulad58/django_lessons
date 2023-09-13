from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return f"name: {self.name}, " \
               f"price:{self.price}," \
               f"image: {self.image}," \
               f"release_date: {self.release_date}," \
               f"lte_exists: {self.lte_exists}," \
               f"slug: {self.slug}"
