from django.utils.text import slugify
from rest_framework import serializers
from blog.models import Post, Tag
from blango_auth.models import User

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="value", many=True, queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="api_user_detail",
        # lookup_field="email"
    )

    # slug = serializers.SlugField(required=False)
    # autogenerate_slug = serializers.BooleanField(required=False, write_only=True, default=False)

    class Meta:
        model = Post
        readonly = ["modified_at", "created_at"]
        fields = '__all__'

    # def validate(self, data):
    #     if not data.get("slug"):
    #         if data["autogenerate_slug"]:
    #             data["slug"] = slugify(data["title"])
    #         else:
    #             raise serializers.ValidationError("slug is required if autogenerate_slug is not set")
    #     del data["autogenerate_slug"]
    #     return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]