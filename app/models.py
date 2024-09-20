from django.db import models
from django.contrib.auth.models import User

#Supplier
class Category(models.Model):
    categoryname = models.CharField(max_length=50, default = "link")
    
    def __str__(self):
        return f"{self.categoryname}"


#Product
class Link(models.Model):
    linkname = models.CharField(max_length=50, default = "link")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link_link = models.URLField(max_length=200, blank=True, null=True)  # Uusi kenttä hyperlinkille

    def __str__(self):
        return f"{self.linkname}"
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
