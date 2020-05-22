from djongo import models
from django.utils.safestring import mark_safe

class Library(models.Model):
    library_name = models.CharField(max_length=200)
    saved_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.library_name


class LibraryComponent(models.Model):
    name = models.CharField(max_length=200)
    svg_path = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    data_link = models.URLField(max_length=200)
    full_name = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    symbol_prefix = models.CharField(max_length=10)
    part = models.CharField(max_length=10)
    dmg = models.PositiveSmallIntegerField()
    component_library = models.ForeignKey(
        Library, on_delete=models.CASCADE, null=False, related_name='library')

    def image_tag(self):
        if self.svg_path:
            return mark_safe('<img src="/%s" style="width: 45px; height:45px;" />' % self.svg_path)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name
