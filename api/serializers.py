from rest_framework import serializers
from .models import Country, Author, Book

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'country']

class BookSerializer(serializers.ModelSerializer):
    title_upper = serializers.SerializerMethodField()

    def get_title_upper(self, obj):
        return obj.title.upper()

    def validate_title(self, value):
        if not value or not value[0].isupper():
            raise serializers.ValidationError("Title must start with a capital letter.")
        return value

    def validate(self, data):
        # During partial updates, use existing values for fields omitted from the request.
        pages = data.get('pages', getattr(self.instance, 'pages', None))
        price = data.get('price', getattr(self.instance, 'price', None))
        if pages is not None and pages <= 0:
            raise serializers.ValidationError({'pages': 'Pages must be greater than 0.'})
        if pages is not None and price is not None and pages > 1000 and price <= 200:
            raise serializers.ValidationError({'price': 'Books over 1000 pages must cost more than 200.'})
        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['is_big_book'] = instance.pages > 1000
        return rep

    class Meta:
        model = Book
        fields = '__all__'
