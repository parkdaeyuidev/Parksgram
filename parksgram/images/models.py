from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager
from parksgram.users import models as user_models


@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):

    """ Images Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT, null=True, related_name='images')
    tags = TaggableManager()

    @property
    def like_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()

    def __str__(self) :
        return '{} - {}'.format(self.location, self.caption)

    class Meta: # 메타클래스를 모델의 설정을 위해 사용한다.
        ordering = ['-created_at'] #created_at으로 정렬

@python_2_unicode_compatible
class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete = models.PROTECT, null=True)
    image = models.ForeignKey(Image,on_delete=models.PROTECT, null=True, related_name='comments')

    def __str__(self) :
        return '{}'.format(self.message)

@python_2_unicode_compatible
class Like(TimeStampedModel):

    """Like Model"""

    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image,on_delete=models.PROTECT, null=True, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)