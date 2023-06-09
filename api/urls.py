from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import MoviesView, MovieTheaterView, BookingView, MyBookingView

urlpatterns = [

    # Public url path
    path('movies/', MoviesView.as_view()),
    path('movie/<int:id>/', MoviesView.as_view()),
    path('movie-theater/<int:id>/', MovieTheaterView.as_view()),

    # for authentication from JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Booking urls
    path("booking/", BookingView.as_view()),
    path("my-bookings/", MyBookingView.as_view()),
    
]
