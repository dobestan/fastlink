from django.db import models


class ResourceManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'course',
        )


class Resource(models.Model):

    course = models.ForeignKey(
        'Course',
    )

    url = models.URLField(
        verbose_name='URL',
    )
    description = models.CharField(
        max_length=255,
        verbose_name='설명',
    )

    class Meta:
        verbose_name = '리소스'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url
