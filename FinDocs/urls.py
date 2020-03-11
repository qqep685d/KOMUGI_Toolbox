from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'findocs' # namespace

urlpatterns = [
    # Doc
    path('', views.DocListView.as_view(), name='index'), # 検索
    path('add/', login_required(views.DocCreateView.as_view()), name='add'), # 追加
    path('<int:pk>/detail/', views.DocDetailView.as_view(), name='detail'), # 詳細
    path('<int:pk>/edit/', login_required(views.DocEditView.as_view()), name='edit'), # 編集
    path('<int:pk>/del/', login_required(views.DocDeleteView.as_view()), name='del'), # 削除
    # DocType
    path('category/', login_required(views.DocTypeListView.as_view()), name='category_index'), # 検索
    path('category/add/', login_required(views.DocTypeCreateView.as_view()), name='category_add'), # 検索
    path('category/<int:pk>/edit/', login_required(views.DocTypeEditView.as_view()), name='category_edit'), # 編集
    path('category/<int:pk>/del/', login_required(views.DocTypeDeleteView.as_view()), name='category_del'), # 削除
    # Contact
    path('contact/', login_required(views.ContactListView.as_view()), name='contact_index'), # 検索
    path('contact/add/', login_required(views.ContactCreateView.as_view()), name='contact_add'), # 検索
    path('contact/<int:pk>/edit/', login_required(views.ContactEditView.as_view()), name='contact_edit'), # 編集
    path('contact/<int:pk>/del/', login_required(views.ContactDeleteView.as_view()), name='contact_del'), # 削除
    # DocType
    path('docplace/', login_required(views.OriginalDocPlaceListView.as_view()), name='docplace_index'), # 検索
    path('docplace/add', login_required(views.OriginalDocPlaceCreateView.as_view()), name='docplace_add'), # 検索
    path('docplace/<int:pk>/edit/', login_required(views.OriginalDocPlaceEditView.as_view()), name='docplace_edit'), # 編集
    path('docplace/<int:pk>/del/', login_required(views.OriginalDocPlaceDeleteView.as_view()), name='docplace_del'), # 削除
    # Import/Export
    path('import/', login_required(views.DataImport.as_view()), name='import'), # インポート
    path('export/', login_required(views.DataExport), name='export'), # エクスポート
]
