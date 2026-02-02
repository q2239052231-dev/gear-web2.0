from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='称呼')
    phone = models.CharField(max_length=20, verbose_name='手机号')
    product_type = models.CharField(max_length=100, verbose_name='产品类型', blank=True, null=True)
    demand = models.TextField(verbose_name='需求描述', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='提交时间')
    is_handled = models.BooleanField(default=False, verbose_name='是否已处理')
    
    class Meta:
        verbose_name = '联系表单'
        verbose_name_plural = '联系表单'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.phone}'
