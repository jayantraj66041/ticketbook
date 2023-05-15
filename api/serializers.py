from rest_framework import serializers
from api.models import Theater, Movie, Booking, Category, TimeSlot


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


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
