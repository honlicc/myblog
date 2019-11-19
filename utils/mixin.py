#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#date:  2019/11/19 0019
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
