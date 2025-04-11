from django.db import models

# Product Category model
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_id = models.PositiveIntegerField()


class polls(models.Model):
    category_name = models.ForeignKey('ProductCategory', related_name='productCategory', on_delete=models.CASCADE,null=True)
    pr_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateTimeField()
    desc = models.TextField()

    def __str__(self):
        return self.name
