from django.db import models

class Cash(models.Model):

    CASH_TYPE_CHOICES = {
        ("deposit", "Deposit"),
        ("withdraw","Withdraw")
    }

    date = models.DateField()
    cash_type = models.CharField(choices=CASH_TYPE_CHOICES, max_length=20)
    item = models.CharField(max_length=100, help_text="업체명")
    classfication = models.CharField(max_length=30, help_text="입출금 항목", blank=True)
    op_month = models.DateField(verbose_name="AR/AP Operating Month", blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=0)
    memo = models.TextField(help_text="비고", blank=True)
    #username = models.CharField(max_length=30) 로그인 계정이 자동으로 들어갈 수 있도록. 입력 담당자 확인용
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cash_type + ":" + self.item
 
    
