from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from apps.utils import APIResponse

from .models import *
from .serializers import *


class DouyinAPIView(APIView):
    def get(self, request):
        data = Douyin.objects.all()
        serializer = RanksModelSerializer(data, many=True)
        # 使用分页器


        # pagination_class = PageNumberPagination(page_size=20)

        return APIResponse(result=serializer.data)
