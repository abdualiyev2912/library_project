from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        isbn = data.get('isbn', None)
        # ---------------------------
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob sarlavhasi harflardan iborat bo\'lishi kerak!'
                }
            )
        # ---------------------------
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob allaqachon bazaga saqlangan!'
                }
            )

        return data

    def validate_price(self, price):
        if not 0 <= price <= 10000000:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob narxi 0 va 10000000 so\'m oralig\'ida bo\'lishi kerak!'
                }
            )

