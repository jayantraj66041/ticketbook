from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Theater, Movie, Booking, TimeSlot
from api.serializers import MovieSerializer, MovieTheaterSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Views for showing all/particular movies
class MoviesView(APIView):
    
    def get(self, request, id=None, *args, **kwargs):

        if id:
            movie = Movie.objects.get(id=id)        # get only that movie whose id = url id
            serializer = MovieSerializer(movie)
        
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    def post(self, request, *args, **kwargs):
        pass


# views for showing any movies theater and timeslot list
class MovieTheaterView(APIView):

    def get(self, request, *args, **kwargs):

        m_id = kwargs.get("id")

        timeslot = TimeSlot.objects.filter(movie__id=m_id)      # filtering all timeslots whose movie id = url id
        serializer = MovieTheaterSerializer(timeslot, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BookingView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # print("pass1", request.user)
        serializer = BookingSerializer(data=request.data)
        print("pass2")
        if serializer.is_valid():
            # print("pass3")
            serializer.save()

            # get last booking for updating the user who booked seat.
            booking = Booking.objects.last()
            booking.user = request.user
            booking.save()
            return Response({"status": "successfully booked"},status=status.HTTP_200_OK)

        # print('pass4')
        return Response({"status": "Booking Failed!!"},status=status.HTTP_400_BAD_REQUEST)