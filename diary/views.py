#####              #####
    #8つの追加or変更#
#####              #####
from django.shortcuts import render, redirect ###11追加###
from django.views import generic ###1 追加###
import logging ###8 追加###
from django.urls import reverse_lazy ###9 追加###
logger = logging.getLogger(__name__) ###10 追加###
from django.contrib import messages  ###12 追加###
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm, DiaryCreateForm   ###2 追加###
from .models import Diary

class IndexView(generic.TemplateView):  ###3 追加###
    template_name = "index.html"

class InquiryView(generic.FormView):   ###4 追加###
    template_name = "inquiry.html"
    form_class = InquiryForm
# ↑と↓は同じ意味らしい。注意:互換性はあるが、urls.pyも変えないといけないからね。
# def inquiryview(request): 
#     """forms.Formを用いたお問い合わせ"""
#     if request.method == "POST":
#         form = InquiryForm() # request.POST, request.FILES
#     elif request.method == "GET":
#         form = InquiryForm()
#     return render(request, 'inquiry.html', {'form': form})
    success_url = reverse_lazy('inquiry') #reverse_lazy('diary:inquiry')ほんとはね。urlsのとこ消したから、inquiryだけでいい
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "メッセージを送信しました。")
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name'])) 
        #form.cleaned_data['']で、バリデーションを通ったユーザー入力値を取り出せる
        #logger.<ログレベル>(<内容>)で、ログを出力している。
        return super().form_valid(form)
    
class LoginView(generic.TemplateView):    ###5 追加###
    template_name = "login.html"

class SignupView(generic.TemplateView):     ###6 追加###
    template_name = "signup.html"

class Member_ShipView(generic.TemplateView):      ###7 追加###
    template_name = "member_ship.html"

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
    
class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form) ###この行で、成功したら、successurlに飛べって言ってるらしい
    
    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)
    
class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm
    
    def get_success_url(self):
        return reverse_lazy('diary_detail', kwargs={'pk': self.kwags['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form) ###この行で、成功したら、successurlに飛べって言ってるらしい
    
    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)
    
class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary_list')

    def delete(self, request, *arg, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *arg, **kwargs)