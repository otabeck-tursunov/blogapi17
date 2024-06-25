from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class MaqolalarAPIView(APIView):
    def get(self, request):
        maqolalar = Maqola.objects.all()
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)


class MaqolalarimAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            maqolalar = Maqola.objects.filter(user=request.user)
            serializer = MaqolaSerializer(maqolalar, many=True)
            return Response(serializer.data)
        return Response(status=401)
