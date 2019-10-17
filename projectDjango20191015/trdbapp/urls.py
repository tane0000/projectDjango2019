from django.urls import path
from . import views

from .views import TroubleFilterView, TroubleDetailView, TroubleCreateView, TroubleUpdateView, TroubleDeleteView
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views import BruserListView, BruserCreateView, BruserUpdateView, BruserDeleteView
from .views import BrmachineListView, BrmachineCreateView, BrmachineUpdateView, BrmachineDeleteView

from .views import AcceptedmethodListView, AcceptedmethodCreateView, AcceptedmethodUpdateView, AcceptedmethodDeleteView
from .views import ActioncategoryListView, ActioncategoryCreateView, ActioncategoryUpdateView, ActioncategoryDeleteView
from .views import SuspendcategoryListView, SuspendcategoryCreateView, SuspendcategoryUpdateView, SuspendcategoryDeleteView
from .views import DisposalcategoryListView, DisposalcategoryCreateView, DisposalcategoryUpdateView, DisposalcategoryDeleteView

from .views import PostImport, post_export

#app_name = 'trdbapp'
urlpatterns = [
    #テスト用
#    path('', views.index, name='index'),

    # 画面（メイン、詳細、登録、更新、削除）
    path('', views.TroubleFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', views.TroubleDetailView.as_view(), name='detail'),
    path('create/', views.TroubleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TroubleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TroubleDeleteView.as_view(), name='delete'),

    # CSVファイル操作
    path('import/', views.PostImport.as_view(), name='import'),
    path('export/', views.post_export, name='export'),

    # 製品名編集画面
    path('product/', views.ProductListView.as_view(), name='product'),
    path('productcreate/', views.ProductCreateView.as_view(), name='productcreate'),
    path('productupdate/<int:pk>/', views.ProductUpdateView.as_view(), name='productupdate'),
    path('productdelete/<int:pk>/', views.ProductDeleteView.as_view(), name='productdelete'),

    # 物件名編集画面
    path('bruser/', views.BruserListView.as_view(), name='bruser'),
    path('brusercreate/', views.BruserCreateView.as_view(), name='brusercreate'),
    path('bruserupdate/<int:pk>/', views.BruserUpdateView.as_view(), name='bruserupdate'),
    path('bruserdelete/<int:pk>/', views.BruserDeleteView.as_view(), name='bruserdelete'),

    # 機器名編集画面
    path('brmachine/', views.BrmachineListView.as_view(), name='brmachine'),
    path('brmachinecreate/', views.BrmachineCreateView.as_view(), name='brmachinecreate'),
    path('brmachineupdate/<int:pk>/', views.BrmachineUpdateView.as_view(), name='brmachineupdate'),
    path('brmachinedelete/<int:pk>/', views.BrmachineDeleteView.as_view(), name='brmachinedelete'),

    # 受付方法編集画面
    path('acceptedmethod/', views.AcceptedmethodListView.as_view(), name='acceptedmethod'),
    path('acceptedmethodcreate/', views.AcceptedmethodCreateView.as_view(), name='acceptedmethodcreate'),
    path('acceptedmethodupdate/<int:pk>/', views.AcceptedmethodUpdateView.as_view(), name='acceptedmethodupdate'),
    path('acceptedmethoddelete/<int:pk>/', views.AcceptedmethodDeleteView.as_view(), name='acceptedmethoddelete'),

    # 対応区分編集画面
    path('actioncategory/', views.ActioncategoryListView.as_view(), name='actioncategory'),
    path('actioncategorycreate/', views.ActioncategoryCreateView.as_view(), name='actioncategorycreate'),
    path('actioncategoryupdate/<int:pk>/', views.ActioncategoryUpdateView.as_view(), name='actioncategoryupdate'),
    path('actioncategorydelete/<int:pk>/', views.ActioncategoryDeleteView.as_view(), name='actioncategorydelete'),

    # 停止区分編集画面
    path('suspendcategory/', views.SuspendcategoryListView.as_view(), name='suspendcategory'),
    path('suspendcategorycreate/', views.SuspendcategoryCreateView.as_view(), name='suspendcategorycreate'),
    path('suspendcategoryupdate/<int:pk>/', views.SuspendcategoryUpdateView.as_view(), name='suspendcategoryupdate'),
    path('suspendcategorydelete/<int:pk>/', views.SuspendcategoryDeleteView.as_view(), name='suspendcategorydelete'),

    # 処置区分編集画面
    path('disposalcategory/', views.DisposalcategoryListView.as_view(), name='disposalcategory'),
    path('disposalcategorycreate/', views.DisposalcategoryCreateView.as_view(), name='disposalcategorycreate'),
    path('disposalcategoryupdate/<int:pk>/', views.DisposalcategoryUpdateView.as_view(), name='disposalcategoryupdate'),
    path('disposalcategorydelete/<int:pk>/', views.DisposalcategoryDeleteView.as_view(), name='disposalcategorydelete'), ]

