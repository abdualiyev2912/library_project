from django.urls import path
from rest_framework.routers import SimpleRouter


from books.views import BookListApiView, BookListCreateApiView, \
    BookDetailApiView, BookUpdateApiView, BookDeleteApiView, \
    BookCreateApiView, BookDetailDeleteApiView, BookDetailUpdateApiView, \
    BookDetailUpdateDeleteApiView, BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view(),),
    # path('booklistcreate/', BookListCreateApiView.as_view(),),
    # path('bookupdate/<int:pk>/', BookDetailUpdateApiView.as_view(),),
    # path('bookdelete/<int:pk>/', BookDetailDeleteApiView.as_view(),),
    # path('bookupdatedelete/<int:pk>/', BookDetailUpdateDeleteApiView.as_view(),),
    # path('books/create/', BookCreateApiView.as_view(),),
    # path('books/<int:pk>', BookDetailApiView.as_view(),),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view(),),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view(),),
]

urlpatterns += router.urls
