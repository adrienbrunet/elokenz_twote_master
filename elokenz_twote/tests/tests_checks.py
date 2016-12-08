# -*- coding: utf-8 -*-

import pytest

import django

from distutils.version import LooseVersion

from django.test import SimpleTestCase

from ..checks import check_mandatory_apps_are_in_installed_apps


def dummy_decorator(func, *args, **kwargs):
    return func


if LooseVersion(django.get_version()) < LooseVersion('1.10'):
    isolate_apps = dummy_decorator
else:
    from django.test.utils import isolate_apps


@pytest.mark.skipif(LooseVersion(django.get_version()) < LooseVersion('1.10'),
                    reason="requires django 1.10")
@isolate_apps('contact_form', attr_name="apps")
class TestCheck(SimpleTestCase):
    def test_check_installed_app(self):
        with self.settings(INSTALLED_APPS=('django.contrib.admin',)):
            assert len(
                check_mandatory_apps_are_in_installed_apps(
                    app_configs=self.apps.get_app_configs())
            ) == 3

        assert len(
            check_mandatory_apps_are_in_installed_apps(
                app_configs=self.apps.get_app_configs())
        ) == 0
