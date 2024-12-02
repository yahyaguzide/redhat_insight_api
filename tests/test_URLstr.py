import pytest

from redhat_insight_api.utils.helper_types import URLstr


def test_slashes():
    correct_url = "https://hello/world"
    tmp_url_1 = "//https://hello/world//"
    tmp_url_2 = "https://hello/world//"
    tmp_url_3 = "https://hello/world"

    tmp_urlstr_1 = URLstr(tmp_url_1)
    tmp_urlstr_2 = URLstr(tmp_url_2)
    tmp_urlstr_3 = URLstr(tmp_url_3)

    assert tmp_urlstr_1.url == correct_url
    assert tmp_urlstr_2.url == correct_url
    assert tmp_urlstr_3.url == correct_url


def test_join():
    correct_url = "https://hello/world"
    tmp_urlstr = URLstr("https://hello")
    url_path = "world"
    url_str = URLstr("world")

    assert tmp_urlstr.join(url_path).url == correct_url
    assert tmp_urlstr.join(url_str).url == correct_url


def test_add():
    correct_url = "https://hello/world"
    tmp_urlstr = URLstr("https://hello")
    url_path = "world"
    url_str = URLstr("world")

    assert (tmp_urlstr + url_path).url == correct_url
    assert (tmp_urlstr + url_str).url == correct_url


def test_to_str():
    tmp_urlstr = URLstr("https://hello/world")

    assert isinstance(str(tmp_urlstr), str)


def test_repr():
    pass


def test_eq():
    tmp_urlstr = URLstr("https://hello/world")
    tmp_urlstr_same = URLstr("https://hello/world")
    tmp_urlstr_diffrent = URLstr("https://not/so/hello/world")

    assert tmp_urlstr_same == tmp_urlstr
    assert not (tmp_urlstr_diffrent == tmp_urlstr)
