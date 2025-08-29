import requests
import pytest

BASE_URL = "https://www.httpbin.org"

def test_get_ip():
    """1. 查询 IP"""
    r = requests.get(f"{BASE_URL}/ip")
    assert r.status_code == 200
    assert "origin" in r.json()

def test_get_headers():
    """2. 获取请求头"""
    r = requests.get(f"{BASE_URL}/headers")
    assert r.json()["headers"]["Host"] == "www.httpbin.org"

def test_post_json():
    """3. POST JSON"""
    payload = {"name": "西安"}
    r = requests.post(f"{BASE_URL}/post", json=payload)
    assert r.json()["json"]["name"] == "西安"

def test_put_data():
    """4. PUT 数据"""
    data = {"age": 18}
    r = requests.put(f"{BASE_URL}/put", data=data)
    assert r.json()["form"]["age"] == "18"

def test_delete():
    """5. DELETE 请求"""
    r = requests.delete(f"{BASE_URL}/delete")
    assert r.status_code == 200