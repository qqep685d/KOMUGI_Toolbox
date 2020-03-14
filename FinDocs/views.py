from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django_pandas.io import read_frame
from django.views.decorators.http import require_POST

import os, io, csv, urllib
from functools import reduce
from operator import and_

from .models import *
from .forms import *

class DocListView(ListView):
    """検索＆一覧"""
    model = Doc
    template_name = 'FinDocs/index.html'
    context_object_name = 'recs'
    strict = False
    paginate_by = 10

    # クエリセット
    def get_queryset(self):
        if self.request.GET:
            cond_k = Q()
            cond_c = Q()
            cond_y = Q()
            if self.request.GET.get('k'):
                words = self.request.GET.get('k').split()
                cond_k = reduce(and_, [Q(title__icontains=w) | Q(content__icontains=w) | Q(barcode__icontains=w) | Q(keywords__icontains=w) for w in words])
            if self.request.GET.get('c'):
                cond_c = Q(type__id=self.request.GET.get('c'))
            if self.request.GET.get('y'):
                cond_y = Q(date__year=self.request.GET.get('y'))
            context = Doc.objects.filter(cond_k & cond_c & cond_y).order_by('-date', 'title', 'id') # 一覧（検索結果）
        else:
            context = Doc.objects.all().order_by('-date', 'title', 'id') # 一覧（全件）
        return context

    # その他のクエリセットなど
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # セレクトボックス「カテゴリ」
        context["cats"] = DocType.objects.all().order_by('priority', '-name',)
        # セレクトボックス「作成年」
        y_list = Doc.objects.all().dates('date', 'year', order='DESC')
        context["years"] = y_list.values_list('date__year', flat=True).distinct()

        if self.request.GET:
            if self.request.GET.get('k'):
                context["k"] = self.request.GET.get('k')
            if self.request.GET.get('c'):
                context["c"] = int(self.request.GET.get('c'))
            if self.request.GET.get('y'):
                context["y"] = int(self.request.GET.get('y'))

        return context

class DocDetailView(DetailView):
    """詳細"""
    model = Doc
    template_name = 'FinDocs/detail.html'
    context_object_name = 'rec'


class DocEditView(UpdateView):
    """編集"""
    model = Doc
    form_class = DocForm
    template_name = 'FinDocs/edit.html'
    context_object_name = 'rec'
    success_url = reverse_lazy('FinDocs:index')

    def form_valid(self, form):
        saved_rec = form.save()

        # バーコード付与
        if not saved_rec.barcode:
            saved_rec.barcode = "%03d%05d" %  (saved_rec.contact_to.pk, saved_rec.pk)
            saved_rec = form.save()

        # 「保存して詳細ページへ」
        if 'save_and_detail' in self.request.POST:
            return redirect('FinDocs:detail', pk=saved_rec.pk)
        # 「保存して編集を続ける」
        elif 'save_and_edit' in self.request.POST:
            return redirect('FinDocs:edit', pk=saved_rec.pk)
        # 「保存」
        return redirect('FinDocs:index')

    def form_isvalid(self, form):
        messages.error(self.request, '入力内容をご確認ください。')
        return super().form_invalid(form)


class DocCreateView(CreateView):
    """追加"""
    model = Doc
    form_class = DocForm
    template_name = 'FinDocs/add.html'
    context_object_name = 'rec'
    success_url = reverse_lazy('FinDocs:index')

    def form_valid(self, form):
        saved_rec = form.save()

        # バーコード付与
        if not saved_rec.barcode:
            saved_rec.barcode = "%03d%05d" %  (saved_rec.contact_to.pk, saved_rec.pk)
            saved_rec = form.save()

        # 「保存してもう一つ追加」
        if 'save_and_add' in self.request.POST:
            return redirect('FinDocs:add')
        # 「保存して編集を続ける」
        elif 'save_and_edit' in self.request.POST:
            return redirect('FinDocs:edit', pk=saved_rec.pk)
        # 「保存」
        return redirect('FinDocs:index')


class DocDeleteView(DeleteView):
    """削除"""
    model = Doc
    template_name = 'FinDocs/edit.html'
    context_object_name = 'rec'
    success_url = reverse_lazy('FinDocs:index')

#==============================

class DocTypeListView(ListView):
    """一覧"""
    model = DocType
    template_name = 'FinDocs/category_index.html'
    context_object_name = 'cats'
    strict = False

    # クエリセット
    def get_queryset(self):
        context = DocType.objects.all().order_by('priority') # 一覧（全件）
        return context


class DocTypeCreateView(CreateView):
    """追加"""
    model = DocType
    form_class = DocTypeForm
    template_name = 'FinDocs/category_add.html'
    context_object_name = 'cat'
    success_url = reverse_lazy('FinDocs:category_index')

    def form_valid(self, form):
        saved_cat = form.save()
        # 「保存」
        return redirect('FinDocs:category_index')


class DocTypeEditView(UpdateView):
    """編集"""
    model = DocType
    form_class = DocTypeForm
    template_name = 'FinDocs/category_edit.html'
    context_object_name = 'cat'
    success_url = reverse_lazy('FinDocs:category_index')

    def form_valid(self, form):
        saved_cat = form.save()
        # 「保存」
        return redirect('FinDocs:category_index')


class DocTypeDeleteView(DeleteView):
    """削除"""
    model = DocType
    template_name = 'FinDocs/category_del.html'
    context_object_name = 'cat'
    success_url = reverse_lazy('FinDocs:category_index')


#==============================

class ContactListView(ListView):
    """一覧"""
    model = Contact
    template_name = 'FinDocs/contact_index.html'
    context_object_name = 'cons'
    strict = False

    # クエリセット
    def get_queryset(self):
        context = Contact.objects.all().order_by('priority') # 一覧（全件）
        return context


class ContactCreateView(CreateView):
    """追加"""
    model = Contact
    form_class = ContactForm
    template_name = 'FinDocs/contact_add.html'
    context_object_name = 'con'
    success_url = reverse_lazy('FinDocs:contact_index')

    def form_valid(self, form):
        saved_cat = form.save()
        # 「保存」
        return redirect('FinDocs:contact_index')


class ContactEditView(UpdateView):
    """編集"""
    model = Contact
    form_class = ContactForm
    template_name = 'FinDocs/contact_edit.html'
    context_object_name = 'con'
    success_url = reverse_lazy('FinDocs:contact_index')

    def form_valid(self, form):
        saved_cat = form.save()
        # 「保存」
        return redirect('FinDocs:contact_index')


class ContactDeleteView(DeleteView):
    """削除"""
    model = Contact
    template_name = 'FinDocs/contact_del.html'
    context_object_name = 'con'
    success_url = reverse_lazy('FinDocs:contact_index')


#==============================

class OriginalDocPlaceListView(ListView):
    """一覧"""
    model = OriginalDocPlace
    template_name = 'FinDocs/docplace_index.html'
    context_object_name = 'plcs'
    strict = False

    # クエリセット
    def get_queryset(self):
        context = OriginalDocPlace.objects.all().order_by('priority') # 一覧（全件）
        return context


class OriginalDocPlaceCreateView(CreateView):
    """追加"""
    model = OriginalDocPlace
    form_class = OriginalDocPlaceForm
    template_name = 'FinDocs/docplace_add.html'
    context_object_name = 'plc'
    success_url = reverse_lazy('FinDocs:docplace_index')

    def form_valid(self, form):
        saved_cat = form.save()
        # 「保存」
        return redirect('FinDocs:docplace_index')


class OriginalDocPlaceEditView(UpdateView):
    """編集"""
    model = OriginalDocPlace
    form_class = OriginalDocPlaceForm
    template_name = 'FinDocs/docplace_edit.html'
    context_object_name = 'plc'
    success_url = reverse_lazy('FinDocs:docplace_index')

    def form_valid(self, form):
        saved_cat = form.save()
        # 「保存」
        return redirect('FinDocs:docplace_index')


class OriginalDocPlaceDeleteView(DeleteView):
    """削除"""
    model = OriginalDocPlace
    template_name = 'FinDocs/docplace_del.html'
    context_object_name = 'plc'
    success_url = reverse_lazy('FinDocs:docplace_index')

#==============================

def repair_date_format(text):
    reg = re.compile('^([0-9]{4})/([0-9]{1,2})/([0-9]{1,2})')
    m = reg.search(text)
    if m:
        text = "%04d-%02d-%02d" % (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return text


def check_created_at(now, query):
    T = now.strftime("%Y-%m-%d")
    q = repair_date_format(query)
    t = timezone.datetime.strptime(q, "%Y-%m-%d")
    if t < now:
        T = q
    return T


class DataImport(FormView):
    """インポート"""
    template_name = 'FinDocs/import.html'
    success_url = reverse_lazy('FinDocs:index')
    form_class = DocUploadForm

    def form_valid(self, form):
        if self.request.POST and self.request.FILES:
            if self.request.POST["selectedTable"] == "doc":
                try:
                    # フォームからの受け取り
                    import_file = self.request.FILES["importFile"]
                    csvfile = io.TextIOWrapper(import_file, encoding='utf-8')
                    reader = csv.reader(csvfile, delimiter="\t")
                    # 現在の時刻
                    now   = timezone.datetime.now()
                    now_HR= now.strftime("%Y-%m-%d") # フォーマット変換
                    # 1行ずつ取り出し、更新or作成していく
                    for row in reader:
                        if type(row[0])!='int':
                            continue
                        if row[0]:
                            # インデックス（pk）がある場合
                            if Doc.objects.filter(pk=row[0]).exists():
                                # 一致するデータがある => 更新
                                doc = Doc.objects.get(pk=row[0])
                                doc.title      = row[1]
                                doc.type       = DocType.objects.get(name=row[2])
                                doc.content    = row[3]
                                doc.date       = repair_date_format(row[4])
                                doc.contact_to = Contact.objects.get(contact_to=row[5])
                                doc.is_public  = 1 if row[6]=="公開" or row[6]=="1" else 0
                                doc.url        = row[7]
                                doc.image      = row[8]
                                doc.original   = OriginalDocPlace.objects.get(place=row[10])
                                doc.backup     = row[11]
                                doc.keywords   = row[12]
                                doc.save()

                            else:
                                # 一致するデータがない => 新規作成
                                doc = Doc(
                                    title      = row[1],
                                    type       = DocType.objects.get(name=row[2]),
                                    content    = row[3],
                                    date       = repair_date_format(row[4]),
                                    contact_to = Contact.objects.get(contact_to=row[5]),
                                    is_public  = 1 if row[6]=="公開" or row[6]=="1" else 0,
                                    url        = row[7],
                                    image      = row[8],
                                    original   = OriginalDocPlace.objects.get(place=row[10]),
                                    backup     = row[11],
                                    keywords   = row[12],
                                )
                                doc.save()
                                if not doc.barcode:
                                    doc.barcode = "%03d%05d" %  (doc.contact_to.pk, doc.pk)
                                    doc.save()
                        else:
                            # pkがない => 新規作成
                            doc = Doc(
                                title      = row[1],
                                type       = DocType.objects.get(name=row[2]),
                                content    = row[3],
                                date       = repair_date_format(row[4]),
                                contact_to = Contact.objects.get(contact_to=row[5]),
                                is_public  = 1 if row[6]=="公開" or row[6]=="1" else 0,
                                url        = row[7],
                                image      = row[8],
                                original   = OriginalDocPlace.objects.get(place=row[10]),
                                backup     = row[11],
                                keywords   = row[12],
                            )
                            doc.save()
                            if not doc.barcode:
                                doc.barcode = "%03d%05d" %  (doc.contact_to.pk, doc.pk)
                                doc.save()
                    return super().form_valid(form)
                except:
                    redirect('FinDocs:import')
            else:
                redirect('FinDocs:import')
        return redirect('FinDocs:import')


def DataExport(request):
    """エクスポート"""
    # 出力データ
    if 'category' in request.GET:
        recs = DocType.objects.all()
        tablename = 'Category'
    elif 'contact' in request.GET:
        recs = Contact.objects.all()
        tablename = 'Contact'
    elif 'docplace' in request.GET:
        recs = OriginalDocPlace.objects.all()
        tablename = 'Docplace'
    else:
        recs = Doc.objects.all()
        tablename = 'Document'

    # ファイル名
    now = timezone.datetime.now().strftime("%Y%m%d%H%M%S")
    name = u'FinDocs_%s_%s.txt' % (tablename, now)
    filename = urllib.parse.quote((name).encode("utf8"))

    # テキストファイル出力
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    df = read_frame(recs)
    df.to_csv(path_or_buf=response, sep='\t', index=False)
    return response

#==============================
