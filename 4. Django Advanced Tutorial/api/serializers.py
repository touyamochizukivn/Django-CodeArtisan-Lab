from rest_framework import serializers

from post import models as post_models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = post_models.Post
        fields = ('id', 'title', 'detail')