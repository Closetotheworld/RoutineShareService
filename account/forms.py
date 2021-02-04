from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 수정 시 아이디 불가하게 하기 위함.
        self.fields['username'].disabled = True