import pytest

from blackfennec.util.meta_info import BlackFennecMetaInfo

def test_get_app_id():
    meta_info = BlackFennecMetaInfo()
    assert meta_info.get_app_id() == 'org.blackfennec.app'

def test_get_name():
    meta_info = BlackFennecMetaInfo()
    assert meta_info.get_name() == 'BlackFennec'

def test_get_summary():
    meta_info = BlackFennecMetaInfo()
    assert len(meta_info.get_summary()) > 10

def test_get_version():
    meta_info = BlackFennecMetaInfo()
    assert '.' in meta_info.get_version()

def test_get_release_notes():
    meta_info = BlackFennecMetaInfo()
    assert len(meta_info.get_release_notes()) > 7

def test_get_description():
    meta_info = BlackFennecMetaInfo()
    assert len(meta_info.get_description()) > 15

def test_get_authors():
    meta_info = BlackFennecMetaInfo()
    assert len(meta_info.get_authors()) > 0

def test_get_license():
    meta_info = BlackFennecMetaInfo()
    assert 'GPL-3' in meta_info.get_license()

def test_get_home_page():
    meta_info = BlackFennecMetaInfo()
    assert 'blackfennec.org' in meta_info.get_home_page()

def test_get_issue_page():
    meta_info = BlackFennecMetaInfo()
    assert 'issues' in meta_info.get_issue_page()

def test_get_icon_path():
    meta_info = BlackFennecMetaInfo()
    assert meta_info.get_icon_path().endswith('icon.png')

def test_get_copy_right():
    meta_info = BlackFennecMetaInfo()
    assert meta_info.get_copy_right().startswith('©')

