from django.conf import settings
from django.db import models
from django.utils import timezone
#from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#class Food(models.Model): #à modifier
#    # ... fields here

#    tags = TaggableManager()


###### tag ######
#if request.method == "POST":
#    form = MyFormClass(request.POST)
#    if form.is_valid():
#        obj = form.save(commit=False)
#        obj.user = request.user
#        obj.save()
#        # Without this next line the tags won't be saved.
#        form.save_m2m()