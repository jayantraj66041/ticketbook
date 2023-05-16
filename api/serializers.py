from rest_framework import serializers
from api.models import Theater, Movie, Booking, Category, TimeSlot, Seats
from django.contrib.auth.models import User


# movie cateogry serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category    # database model(table) name
        fields = ['name']   # only name of the category has to be shown


# theater details serializer
class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ['id', 'name', 'no_of_seats', 'location']


# movie model data serializer
class MovieSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True)        # one movie has multiple category like anction, romantic etc.
    class Meta:
        model = Movie
        fields = ['id', 'name', 'category', 'release_date']     # list of column which has to be shown


# timeslot of movie as per theater serializer
class MovieTheaterSerializer(serializers.ModelSerializer):

    theater = TheaterSerializer()       # theater of the movie
    # theater = serializers.StringRelatedField()
    class Meta:
        model = TimeSlot
        fields = ['id', 'theater', 'start_time', 'end_time', 'date']    # data info of timeslot



class MemberSerializer(serializers.ModelSerializer):
    # booking = serializers.IntegerField()
    class Meta:
        model = Seats
        fields = ['name', 'seat_no']

class BookingSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    # time_slot = serializers.IntegerField()

    def create(self, attr):
        # print("pass5")
        members = attr.get("members")
        booking = Booking.objects.create(time_slot=attr.get("time_slot"))

        # print(members[0]["seat_no"], "@@$$$$@@@$$")
        # print(booking)
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        for member in members:
            Seats.objects.create(booking=booking, seat_no=member["seat_no"], name=member['name'])

        return booking

    class Meta:
        model = Booking
        fields = ['time_slot', 'members']

