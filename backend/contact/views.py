from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from django.utils.html import escape
from .models import Contact
from .serializers import ContactSerializer

class ContactView(APIView):
    def get_permissions(self):
        # 为不同HTTP方法设置不同权限
        if self.request.method == 'POST':
            # POST方法允许匿名访问（提交表单）
            return [AllowAny()]
        elif self.request.method == 'GET':
            # GET方法只允许管理员访问（查看所有表单数据）
            return [IsAdminUser()]
        return super().get_permissions()
    def post(self, request):
        # 对输入数据进行XSS过滤
        safe_data = {
            'name': escape(request.data.get('name', '')),
            'phone': escape(request.data.get('phone', '')),
            'product_type': escape(request.data.get('product_type', '')),
            'demand': escape(request.data.get('demand', ''))
        }
        serializer = ContactSerializer(data=safe_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': '提交成功！我们的工程师将尽快联系您。',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': '提交失败，请检查输入信息。',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
