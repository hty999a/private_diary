from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary

class LoggedInTestCase(TestCase):
    def setUp(self):
        self.password = '<ログインパスワード>'
        self.test_user = get_user_model().objects.create_user(
            username='<ログインユーザー名>',
            email='<ログインユーザーのメールアドレス>',
            password=self.password
        )
        self.client.login(email=self.test_user.email, password=self.password)

class TestDiaryCreateView(LoggedInTestCase):
    def test_create_diary_success(self):
        params = {'title':'テストタイトル',
                  'content':'本文',
                  'photo1':"",
                  'photo2':"",
                  'photo3':"",
                  }
        response = self.client.post(reverse_lazy('diary_create'), params)

        self.assertRedirects(response, reverse_lazy('diary_list'))  ###実行

        self.assertEqual(Diary.objects.filter(title='テストタイトル').count(),1)  ###比較

    def test_create_diary_failure(self):
        response = self.client.post(reverse_lazy('diary_create'))

        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。') ###比較

class TestDiaryUpdateView(LoggedInTestCase):
    def test_update_diary_success(self):
        diary = Diary.objects.create(user=self.test_user, title='タイトル編集前')

        params={'title':'タイトル編集後'}

        response = self.client.post(reverse_lazy('diary_update', kwargs={'pk': diary.pk}), params) ###編集処理実行

        self.assertRedirects(response, reverse_lazy('diary_detail', kwargs={'pk':diary.pk})) ###詳細ページへ飛んでみる

        self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'タイトル編集後') ###編集されたか確認

    def test_update_diary_failure(self):
        response = self.client.post(reverse_lazy('diary_update', kwargs={'pk':999})) ###日記編集処理実行

        self.assertEqual(response.status_code, 404) ###存在しない日記データの編集して失敗

class TestDiaryDeleteView(LoggedInTestCase):
    def test_delete_diary_succcess(self):
        diary = Diary.objects.create(user=self.test_user, title='タイトル')

        response = self.client.post(reverse_lazy('diary_list', kwargs={'pk':diary.pk}))

        self.assertRedirects(response, reverse_lazy('diary_list'))

        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

    def test_delete_diary_failure(self):
        response = self.client.post(reverse_lazy('diary_delete', kwargs={'pk':999}))

        self.assertEqual(response.status_code, 404)