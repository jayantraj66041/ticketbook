from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Theater, Movie, Booking, TimeSlot
from api.serializers import MovieSerializer, MovieTheaterSerializer


# Views for showing all/particular movies
class MoviesView(APIView):
    
    def get(self, request, id=None, *args, **kwargs):

        if id:
            movie = Movie.objects.get(id=id)        # get only that movie whose id = url id
            serializer = MovieSerializer(movie)
        
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
        
        return Response(serializer.data, status=200)    
    
    def post(self, request, *args, **kwargs):
        pass


# views for showing any movies theater and timeslot list
class MovieTheaterView(APIView):

    def get(self, request, *args, **kwargs):

        m_id = kwargs.get("id")

        timeslot = TimeSlot.objects.filter(movie__id=m_id)      # filtering all timeslots whose movie id = url id
        serializer = MovieTheaterSerializer(timeslot, many=True)

        return Response(serializer.data, status=200)