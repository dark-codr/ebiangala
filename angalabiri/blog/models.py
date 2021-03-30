import os
import random
import readtime

from category.models import Category, Tag
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    TextField,
    ForeignKey,
    GenericIPAddressField,
    PositiveIntegerField,
    ImageField,
    IntegerField,
    IPAddressField,
    ManyToManyField,
    OneToOneField,
    Q,
    SlugField,
    URLField,
)
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel

from comment.models import Comment
from .managers import PostManager
from .validators import file_validator
from django_resized import ResizedImageField

# Create your models here.


User = settings.AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def blog_file_path(filename, instance):
    return "blog/videos/{filename}".format(filename=filename)


def blog_image_path(instance, filename):
    return "blog/images/{filename}".format(filename=filename)


class Post(TimeStampedModel):
    author = ForeignKey(User, on_delete=SET_NULL, null=True)
    title = CharField(_("Post Title"), blank=False, null=True, max_length=255)
    slug = SlugField(unique=True, null=True, blank=True, max_length=500)
    videos = FileField(
        _("Upload Video"),
        upload_to=blog_file_path,
        null=True,
        blank=True,
        validators=[file_validator],
    )
    url = URLField(blank=True, max_length=500, null=True, unique=True)
    pub_date = DateField(
        _("Post Published Date"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=False,
    )
    draft = BooleanField(default=False)
    featured = BooleanField(default=False)
    content = RichTextUploadingField()
    comments = GenericRelation(Comment)
    added_by = CharField(_("added_by"), max_length=555, null=True, blank=True)
    categories = ManyToManyField("category.Category", help_text="Categorize this item.")
    tags = ManyToManyField("category.Tag", help_text="Tag this item.")
    objects = PostManager()

    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return "title", "author"

    @property
    def readtime(self):
        return str(readtime.of_test(self.content))


    @property
    def get_image_url(self):
        img = self.image_set.first()
        if img:
            return img.image.url
        return img #None



    class Meta:
        managed = True
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title", "-pub_date"]

    @property
    def get_related_posts_by_tags(self):
        return Post.objects.filter(tags__in=self.tags.all())[:4]

    # @property
    # def comments(self):
    #     instance = self
    #     return Comment.objects.filter_by_instance(instance)

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type




    def get_absolute_url(self):
        return f"/blogs/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"


class Image(TimeStampedModel):
    post = ForeignKey(Post, on_delete=CASCADE)
    image = ResizedImageField(
        _("Upload Post Image"), quality=75, force_format='JPEG', size=[1920, 1148], crop=['middle', 'center'], upload_to=blog_image_path, null=True, blank=True
    )

    def __str__(self):
        return self.post.title

    class Meta:
        managed = True
        verbose_name = "Post Files"
        verbose_name_plural = "Post Files"
        ordering = ["-created"]


# class Comment(TimeStampedModel):
#     post = ForeignKey(Post, related_name="comments", on_delete=CASCADE)
#     author = CharField(_("FullName"), max_length=500, null=True, blank=True)
#     email = EmailField(_("Add your email"), null=True, blank=True)
#     text = TextField()
#     active = BooleanField(default=True)

#     class Meta:
#         ordering = ["-created"]

#     def _str_(self):
#         return f"Comment {self.text} by {self.author}"
