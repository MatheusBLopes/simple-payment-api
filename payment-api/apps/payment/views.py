import requests
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaymentSerializer, ErrorSerializer

class PaymentView(APIView):

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.data["value"]
            serializer.data["webhook_url"]
            payment_code = uuid.uuid4()
            try:
                response = requests.post(url=serializer.data["webhook_url"], data={"payment_status": "success", "payment_code": payment_code})
                response.raise_for_status()
            except Exception as e:
                error_serializer = ErrorSerializer({"message": "failed", "error": str(e)})
                return Response(error_serializer.data, status=status.HTTP_400_BAD_REQUEST)

        
        return Response({"message": "success", "payment_code": payment_code})