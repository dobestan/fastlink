from django.db import models


class CourseManager(models.Manager):
    pass


class Course(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='이름',
    )
    slug = models.SlugField(
    )

    objects = CourseManager()

    class Meta:
        verbose_name = '코스'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
