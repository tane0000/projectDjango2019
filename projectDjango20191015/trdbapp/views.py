from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

import csv, io

from django.views.generic import FormView
from django.http import HttpResponse
from django.db import IntegrityError, transaction
from pure_pagination.mixins import PaginationMixin

from .models import Trouble
from .models import Product, Bruser, Brmachine
from .models import Acceptedmethod, Actioncategory, Suspendcategory, Disposalcategory

from .models import TroubleStatus, ControlStatus

from .forms import TroubleForm
from .forms import ProductForm, BruserForm, BrmachineForm
from .forms import AcceptedmethodForm, ActioncategoryForm, SuspendcategoryForm, DisposalcategoryForm
from .forms import CSVUploadForm

from .filters import TroubleFilter

# 製品名編集画面
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
#    paginate_by = 5

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('index')

# 物件名編集画面
class BruserListView(LoginRequiredMixin, ListView):
    model = Bruser
#    paginate_by = 5

class BruserCreateView(LoginRequiredMixin, CreateView):
    model = Bruser
    form_class = BruserForm
    success_url = reverse_lazy('index')

class BruserUpdateView(LoginRequiredMixin, UpdateView):
    model = Bruser
    form_class = BruserForm
    success_url = reverse_lazy('index')

class BruserDeleteView(LoginRequiredMixin, DeleteView):
    model = Bruser
    success_url = reverse_lazy('index')

# 機器名編集画面
class BrmachineListView(LoginRequiredMixin, ListView):
    model = Brmachine
#    paginate_by = 5

class BrmachineCreateView(LoginRequiredMixin, CreateView):
    model = Brmachine
    form_class = BrmachineForm
    success_url = reverse_lazy('index')

class BrmachineUpdateView(LoginRequiredMixin, UpdateView):
    model = Brmachine
    form_class = BrmachineForm
    success_url = reverse_lazy('index')

class BrmachineDeleteView(LoginRequiredMixin, DeleteView):
    model = Brmachine
    success_url = reverse_lazy('index')

# 受付方法編集画面
class AcceptedmethodListView(LoginRequiredMixin, ListView):
    model = Acceptedmethod
#    paginate_by = 5

class AcceptedmethodCreateView(LoginRequiredMixin, CreateView):
    model = Acceptedmethod
    form_class = AcceptedmethodForm
    success_url = reverse_lazy('index')

class AcceptedmethodUpdateView(LoginRequiredMixin, UpdateView):
    model = Acceptedmethod
    form_class = AcceptedmethodForm
    success_url = reverse_lazy('index')

class AcceptedmethodDeleteView(LoginRequiredMixin, DeleteView):
    model = Acceptedmethod
    success_url = reverse_lazy('index')

# 対応区分編集画面
class ActioncategoryListView(LoginRequiredMixin, ListView):
    model = Actioncategory
#    paginate_by = 5

class ActioncategoryCreateView(LoginRequiredMixin, CreateView):
    model = Actioncategory
    form_class = ActioncategoryForm
    success_url = reverse_lazy('index')

class ActioncategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Actioncategory
    form_class = ActioncategoryForm
    success_url = reverse_lazy('index')

class ActioncategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Actioncategory
    success_url = reverse_lazy('index')

# 停止区分編集画面
class SuspendcategoryListView(LoginRequiredMixin, ListView):
    model = Suspendcategory
#    paginate_by = 5

class SuspendcategoryCreateView(LoginRequiredMixin, CreateView):
    model = Suspendcategory
    form_class = SuspendcategoryForm
    success_url = reverse_lazy('index')

class SuspendcategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Suspendcategory
    form_class = SuspendcategoryForm
    success_url = reverse_lazy('index')

class SuspendcategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Suspendcategory
    success_url = reverse_lazy('index')

# 処置区分編集画面
class DisposalcategoryListView(LoginRequiredMixin, ListView):
    model = Disposalcategory
#    paginate_by = 5

class DisposalcategoryCreateView(LoginRequiredMixin, CreateView):
    model = Disposalcategory
    form_class = DisposalcategoryForm
    success_url = reverse_lazy('index')

class DisposalcategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Disposalcategory
    form_class = DisposalcategoryForm
    success_url = reverse_lazy('index')

class DisposalcategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Disposalcategory
    success_url = reverse_lazy('index')

# 検索一覧画面
class TroubleFilterView(LoginRequiredMixin, PaginationMixin, FilterView):
    model = Trouble
    filterset_class = TroubleFilter
    # デフォルトの並び順を新しい順とする
    queryset = Trouble.objects.all().order_by('-id')
#    queryset = Trouble.objects.all()

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
    strict = False
    # pure_pagination用設定
    paginate_by = 10
    object = Trouble

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]
        return super().get(request, **kwargs)

# 不具合詳細画面
class TroubleDetailView(LoginRequiredMixin, DetailView):
    model = Trouble

# 不具合登録画面
class TroubleCreateView(LoginRequiredMixin, CreateView):
    model = Trouble
    form_class = TroubleForm
    success_url = reverse_lazy('index')

# 不具合更新画面
class TroubleUpdateView(LoginRequiredMixin, UpdateView):
    model = Trouble
    form_class = TroubleForm
    success_url = reverse_lazy('index')

# 不具合削除画面
class TroubleDeleteView(LoginRequiredMixin, DeleteView):
    model = Trouble
    success_url = reverse_lazy('index')

# CSVインポート
class InvalidColumnsExcepion(Exception):
    """CSVの列が足りなかったり多かったりしたらこのエラー"""
    pass

class InvalidSourceExcepion(Exception):
    """CSVの読みとり中にUnicodeDecordErrorが出たらこのエラー"""
    pass

class PostImport(FormView):
    model = Trouble
#    template_name = 'app/import.html'
    template_name = 'trdbapp/csv_import.html'
    success_url = reverse_lazy('import')
    form_class = CSVUploadForm
    number_of_columns = 36 # 列の数を定義しておく。各行の列がこれかどうかを判断する

    def save_csv(self, form):
        # csv.readerに渡すため、TextIOWrapperでテキストモードなファイルに変換
        csvfile = io.TextIOWrapper(form.cleaned_data['file'])
        reader = csv.reader(csvfile)
        i = 1 # 1行目でのUnicodeDecodeError対策。for文の初回のnextでエラーになるとiの値がない為
        try:
            # iは、現在の行番号。エラーの際に補足情報として使う
            for i, row in enumerate(reader, 1):
                # 列数が違う場合
                if len(row) != self.number_of_columns:
                    raise InvalidColumnsExcepion('{0}行目が変です。本来の列数: {1}, {0}行目の列数: {2}'.format(i, self.number_of_columns, len(row)))

                # 問題なければ、この行は保存する。(実際には、form_validのwithブロック終了後に正式に保存される)
                trouble, created = Trouble.objects.get_or_create(pk=row[0])

#                product.name = row[1]
                trouble.user_name = Bruser.objects.get(name=row[2])
                trouble.staff_name = row[3]
                trouble.accepted_method = Acceptedmethod.objects.get(method=row[4])
                trouble.occurrence_datetime = row[5]
                trouble.restoration_datetime = row[6]

                if row[7] != "":
                    trouble.action_category = Actioncategory.objects.get(category=row[7])

                trouble.trouble_machine = Brmachine.objects.get(name=row[8])
                trouble.trouble_location = row[9]
                trouble.error_code = row[10]
                trouble.error_name = row[11]

                trouble.trouble_name = row[12]
                trouble.situation = row[13]
                trouble.cause = row[14]
                trouble.measure = row[15]
                trouble.restoration_procedure = row[16]
                trouble.special_note = row[17]

                if row[18] != "":
                    trouble.complete_date = row[18]

                if row[19] != "":
                    trouble.disposal_category = Disposalcategory.objects.get(category=row[19])

                trouble.field_worker = row[20]
                trouble.office_worker = row[21]
                trouble.first_contact = row[22]
                trouble.first_contact_datetime = row[23]
                trouble.report_history = row[24]
                trouble.input_date = row[25]
                trouble.inputter = row[26]

                if row[27] != "":
                    trouble.suspend_category = Suspendcategory.objects.get(category=row[27])

                trouble.prompt_report = row[28]
                trouble.personal_report = row[29]
                trouble.supplier_report = row[30]
                trouble.d32 = row[31]
                trouble.related_report = row[32]

                trouble.trouble_status = TroubleStatus.objects.get(status=row[33])
                trouble.control_status = ControlStatus.objects.get(status=row[34])
                trouble.trouble_memo = row[35]
                trouble.save()

        except UnicodeDecodeError:
            raise InvalidSourceExcepion('{}行目でデコードに失敗しました。ファイルのエンコーディングや、正しいCSVファイルか確認ください。'.format(i))

    def form_valid(self, form):
            try:
                # CSVの100行目でエラーがおきたら、前の99行分は保存されないようにする
                with transaction.atomic():
                    self.save_csv(form)

            # 今のところは、この2つのエラーは同様に対処します。
            except InvalidSourceExcepion as e:
                form.add_error('file', e)
                return super().form_invalid(form)

            except InvalidColumnsExcepion as e:
                form.add_error('file', e)
                return super().form_invalid(form)

            else:
                return super().form_valid(form) # うまくいったので、リダイレクトさせる

def post_export(request):
    response = HttpResponse(content_type='text/csv; charset=Shift_JIS')
    response['Content-Disposition'] = 'attachment; filename="posts.csv"'
    # HttpResponseオブジェクトはファイルっぽいオブジェクトなので、csv.writerにそのまま渡せます。
    writer = csv.writer(response)
    writer.writerow(
        [
            "No",
            "製品名",
            "物件名",
            "担当者名",
            "受付方法",
            "発生日時",
            "復旧日時",
            "対応区分",

            "不具合機器",
            "発生部位",
            "Ｅコード",
            "エラー名",

            "不具合名",
            "不具合状況",
            "不具合原因",
            "不具合対策",
            "復旧手順",
            "特記事項",

            "処置完了日",
            "処置区分",
            "現地対応者",
            "社内対応者",
            "１次受付者",
            "１次受付日時",
            "客先報告履歴",

            "入力日",
            "入力者",
            "停止区分",

            "不具合速報F",
            "個別報告書F",
            "不具合連絡票F",
            "実施票F",
            "関連報告F",

            '不具合情報',
            '管理情報',
            'メモ',

        ]
    )
    for post in Trouble.objects.all():
        writer.writerow(
            [
            post.pk,
            post.product_name,
            post.user_name,
            post.staff_name,
            post.accepted_method,
            post.occurrence_datetime,
            post.restoration_datetime,
            post.action_category,

            post.trouble_machine,
            post.trouble_location,
            post.error_code,
            post.error_name,

            post.trouble_name,
            post.situation,
            post.cause,
            post.measure,
            post.restoration_procedure,
            post.special_note,

            post.complete_date,
            post.disposal_category,
            post.field_worker,
            post.office_worker,
            post.first_contact,
            post.first_contact_datetime,
            post.report_history,

            post.input_date,
            post.inputter,
            post.suspend_category,

            post.prompt_report,
            post.personal_report,
            post.supplier_report,
            post.d32,
            post.related_report,

            post.trouble_status,
            post.control_status,
            post.toruble_memo,

            ]
        )
    return response
