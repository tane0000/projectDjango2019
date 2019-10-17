from django.db import models

# Create your models here.

from django.utils import timezone
from django.core import validators

# 製品名
class Product(models.Model):
    name = models.CharField(verbose_name='製品名',max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '製品名'
        verbose_name_plural = '01製品名'

# 物件名
class Bruser(models.Model):
    product_name = models.ForeignKey(Product,verbose_name='製品名',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='物件名',max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '物件名'
        verbose_name_plural = '02物件名'

# 機器名
class Brmachine(models.Model):
#    user_name = models.ManyToManyField(Bruser,verbose_name='物件名',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='機器名',max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '機器名'
        verbose_name_plural = '03機器名'

# 受付方法
class Acceptedmethod(models.Model):
    method = models.CharField(verbose_name='受付方法',max_length=10)
    def __str__(self):
        return self.method
    class Meta:
        verbose_name = '受付方法'
        verbose_name_plural = '10受付方法'

# 対応区分
class Actioncategory(models.Model):
    category = models.CharField(verbose_name='対応区分',max_length=10)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name = '対応区分'
        verbose_name_plural = '11対応区分'

# 停止区分
class Suspendcategory(models.Model):
    category = models.CharField(verbose_name='停止区分',max_length=10)
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = '停止区分'
        verbose_name_plural = '12停止区分'

# 処置区分
class Disposalcategory(models.Model):
    category = models.CharField(verbose_name='処置区分',max_length=10)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name = '処置区分'
        verbose_name_plural = '13処置区分'

# 不具合情報
class TroubleStatus(models.Model):
    status = models.CharField(verbose_name='不具合情報',max_length=10)
    def __str__(self):
        return self.status
    class Meta:
        verbose_name = '不具合情報'
        verbose_name_plural = '14不具合情報'

# 管理情報
class ControlStatus(models.Model):
    status = models.CharField(verbose_name='管理情報',max_length=10)
    def __str__(self):
        return self.status
    class Meta:
        verbose_name = '管理情報'
        verbose_name_plural = '15管理情報'

# 不具合ＤＢ
class Trouble(models.Model):
#    product_name = models.ForeignKey(Product,verbose_name='製品名',on_delete=models.CASCADE)
    user_name = models.ForeignKey(Bruser,verbose_name='物件名',on_delete=models.CASCADE,null=True)
    staff_name = models.CharField(verbose_name='担当者名',max_length=15,blank=True,null=True)
    accepted_method = models.ForeignKey(Acceptedmethod,verbose_name='受付方法',on_delete=models.CASCADE,null=True)
    occurrence_datetime = models.DateTimeField(verbose_name='発生日時',default=timezone.now)
#    occurrence_date = models.DateField(verbose_name='発生日',default=timezone.now)
#    occurrence_time = models.TimeField(verbose_name='発生時',default=timezone.now)
    restoration_datetime = models.DateTimeField(verbose_name='復旧日時',blank=True,null=True)
#    restoration_date = models.DateField(verbose_name='復旧日',blank=True,null=True)
#    restoration_time = models.TimeField(verbose_name='復旧時',blank=True,null=True)

    action_category = models.ForeignKey(Actioncategory,verbose_name='対応区分',on_delete=models.CASCADE,null=True)

    trouble_machine = models.ForeignKey(Brmachine,verbose_name='不具合機器',on_delete=models.CASCADE,null=True)
    trouble_location = models.CharField(verbose_name='発生部位',max_length=50,blank=True,null=True)
    error_code = models.CharField(verbose_name='エラーコード',max_length=20,blank=True,null=True)
    error_name = models.CharField(verbose_name='エラー名',max_length=50,blank=True,null=True)

    trouble_name = models.CharField(verbose_name='不具合件名',max_length=50)
    situation = models.TextField(verbose_name='不具合状況',max_length=1000,blank=True,null=True)
    cause = models.TextField(verbose_name='不具合原因',max_length=1000,blank=True,null=True)
    measure = models.TextField(verbose_name='不具合対策',max_length=1000,blank=True,null=True)
    restoration_procedure = models.TextField(verbose_name='復旧手順',max_length=1000,blank=True,null=True)
    special_note = models.TextField(verbose_name='特記事項',max_length=1000,blank=True,null=True)

    complete_date = models.DateField(verbose_name='処置完了日',blank=True,null=True)
    disposal_category = models.ForeignKey(Disposalcategory,verbose_name='処置区分',on_delete=models.CASCADE,null=True)
    field_worker = models.CharField(verbose_name='現地対応者',max_length=30,blank=True,null=True)
    office_worker = models.CharField(verbose_name='社内対応者',max_length=20,blank=True,null=True)
    first_contact = models.CharField(verbose_name='１次受付者',max_length=20,blank=True,null=True)
    first_contact_datetime = models.DateTimeField(verbose_name='１次受付日時',blank=True,null=True)
 #   first_contact_date = models.DateField(verbose_name='１次受付日',blank=True,null=True)
 #   first_contact_time = models.TimeField(verbose_name='１次受付時',blank=True,null=True)

    report_history = models.CharField(verbose_name='客先報告履歴',max_length=10,blank=True,null=True)
    input_date = models.DateField(verbose_name='入力日',default=timezone.now)
    inputter = models.CharField(verbose_name='入力者',max_length=10,blank=True,null=True)
    suspend_category = models.ForeignKey(Suspendcategory,verbose_name='停止カテゴリ',on_delete=models.CASCADE,null=True)
    prompt_report = models.BooleanField(verbose_name='不具合速報F',default=False)
    personal_report = models.BooleanField(verbose_name='個別報告書F',default=False)
    supplier_report = models.BooleanField(verbose_name='不具合連絡票F',default=False)
    d32 = models.BooleanField(verbose_name='実施票F',default=False)
    related_report = models.BooleanField(verbose_name='関連報告F',default=False)

    trouble_status = models.ForeignKey(TroubleStatus,verbose_name='不具合情報',on_delete=models.CASCADE,null=True)
    control_status = models.ForeignKey(ControlStatus,verbose_name='管理情報',on_delete=models.CASCADE,null=True)
    trouble_memo = models.TextField(verbose_name='メモ',max_length=500,blank=True,null=True)

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.trouble_name
    class Meta:
        verbose_name = '不具合ＤＢ'
        verbose_name_plural = '99不具合ＤＢ詳細'
