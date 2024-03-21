from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Books_Book
from .serializers import BooksBookSerializer

class BookListView(generics.ListAPIView):
    queryset = Books_Book.objects.all().order_by('-download_count')
    serializer_class = BooksBookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'gutenberg_id': ['exact'],
        'authors__name': ['icontains'],
        'bookshelves__name': ['icontains'],
        'languages__code': ['exact'],
        'subjects__name': ['icontains'],
        'title': ['icontains'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        topic_filter = self.request.query_params.get('topic', None)
        if topic_filter:
            topic_parts = [topic_part.lower() for topic_part in topic_filter.split(',')]
            for topic_part in topic_parts:
                queryset = queryset.filter(subjects__name__icontains=topic_part)
            queryset = queryset.distinct()
        return queryset
