from django.contrib import admin
from api.models import Movie, Category, Theater, TimeSlot, Booking, Seats
# Register your models here.


# showing data in django admin dashboard of movies
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'release_date']


# showing data in django admin dashboard of movies category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


# showing data in django admin dashboard of theaters
@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['name', 'no_of_seats', 'location']


# showing data in django admin dashboard of timeslots of movie in theaters
@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['theater', 'movie', 'start_time', 'end_time', 'date']


# showing data in dajngo admin dashboard of booking details
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'time_slot', 'total_amount']


# showing data in django adminn dashboard of members of booking details
@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ['name', 'seat_no', 'booking', 'cost']