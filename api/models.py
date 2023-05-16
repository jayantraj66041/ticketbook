from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# category table in database
class Category(models.Model):

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=(("Active", "Active"), ("Inactive", "Inactive")), default="Active")

    # showing default name
    def __str__(self) -> str:
        return self.name


# movie table in database
class Movie(models.Model):

    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    release_date = models.DateField(auto_now_add=True)

    # showing default name
    def __str__(self) -> str:
        return self.name


# theater table in databse
class Theater(models.Model):

    name = models.CharField(max_length=100)
    no_of_seats = models.IntegerField()
    location = models.CharField(max_length=100)

    # showing default name
    def __str__(self) -> str:
        return self.name


# timeslot table in database
class TimeSlot(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    # showing default name
    def __str__(self) -> str:
        return self.theater.name + " - " + self.movie.name


# booking table in database
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    total_amount = models.IntegerField(default=0)

    # showing default name
    def __str__(self) -> str:
        return self.user + " - " + self.time_slot


# seats table in database
class Seats(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    name = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)

    # showing default name
    def __str__(self) -> str:
        return self.seat_no + " - " + self.name