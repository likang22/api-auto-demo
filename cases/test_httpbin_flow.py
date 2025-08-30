# cases/test_httpbin_flow.py
import pytest, requests, random
from urllib.parse import urlencode

BASE_URL = "https://httpbin.org"

def test_full_flow(session):
    """下单-支付-查询-删除（httpbin 模拟）"""
    pet_id = random.randint(10_000_000, 99_999_999)
    order_id = random.randint(1_000_000, 9_999_999)

    # 1. 创建宠物（POST）
    create_pet = {"id": pet_id, "name": "doggie", "status": "available"}
    r = session.post(f"{BASE_URL}/post", json=create_pet)
    assert r.status_code == 200
    assert r.json()["json"]["id"] == pet_id

    # 2. 查询宠物（GET）
    r = session.get(f"{BASE_URL}/get", params={"id": pet_id})
    assert r.status_code == 200
    assert str(pet_id) in r.json()["args"]["id"]

    # 3. 下单（POST）
    order = {"id": order_id, "petId": pet_id, "quantity": 1, "status": "placed"}
    r = session.post(f"{BASE_URL}/post", json=order)
    assert r.status_code == 200
    assert r.json()["json"]["id"] == order_id

    # 4. 查询订单（GET）
    r = session.get(f"{BASE_URL}/get", params={"id": order_id})
    assert r.status_code == 200
    assert str(order_id) in r.json()["args"]["id"]

    # 5. 删除订单（POST 模拟 DELETE）
    r = session.post(f"{BASE_URL}/post", json={"action": "delete", "id": order_id})
    assert r.status_code == 200
    assert r.json()["json"]["action"] == "delete"