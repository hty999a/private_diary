from django import forms
from django.core.mail import EmailMessage
from .models import Diary

class InquiryForm(forms.Form):
    # fieldがメイン
    # CharFieldはフォームのテキスト型に対応
    name = forms.CharField(
        label='お名前',
        max_length=40, # max_lengthで長さを指定できる
        required=True  # このフォームが入力必須かどうか
    )

    # EmailFieldはフォームのemail型に対応
    email = forms.EmailField(
        label='メールアドレス',
        required=True
    )

    # IntegerFieldは整数を入力するフィールド
    age = forms.IntegerField(
        label='年齢',
        # required=True
    )

    title = forms.CharField(
        label='タイトル',
        required=True
    )

    contents = forms.CharField(
        label='内容',
        required=True
        # widget=forms.Textarea # フォームをtextarea要素に変更できる
    )

    # DateTimeFieldは日付を入力するフィールド
    # occurrence_time = forms.DateTimeField(
    #     label='問題発生時刻',
    # )

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        age = self.cleaned_data['age']
        title = self.cleaned_data['title']
        contents = self.cleaned_data['contents']
        # occurrence_time = self.cleaned_data['occurrence_time']

        subject = 'お問い合わせ.{}'.format(title)
        message = '送信者名：{0}/nメールアドレス：{1}/n年齢：{2}/n内容：{3}/n'.format(name, email, age, contents) #問題発生時刻：{4}, , occurrence_time
        from_email = 'admin@example.com'
        to_list = ['test@example.com']
        cc_list = [email]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)