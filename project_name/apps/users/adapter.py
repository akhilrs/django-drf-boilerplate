# -*- coding: utf-8 -*-
from allauth.account.adapter import DefaultAccountAdapter


class UserAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super(UserAccountAdapter, self).save_user(
            request, user, form, commit
        )
        data = form.cleaned_data
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.save()
        return user
