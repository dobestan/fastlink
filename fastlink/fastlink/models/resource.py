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

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
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
        return self.get_shorten_url()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse(
            'resource-redirect',
            kwargs={'hash_id': self.hash_id, },
        )

    def _create_hash_id(self):
        from fastlink.utils.hashids import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()

    def get_shorten_url(self):
        return "https://r.fastcamp.us/{hash_id}".format(
            hash_id=self.hash_id,
        )
