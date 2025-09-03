import pytest
import ipv4_subnet as ipn

# /24：起點、終點
def test_24_network_and_broadcast():
    s = "192.168.1.42/24"
    assert ipn.network_of(s) == "192.168.1.0"
    assert ipn.broadcast_of(s) == "192.168.1.255"

# /24：首尾可用與數量
def test_24_hosts_range_and_count():
    s = "192.168.1.42/24"
    assert ipn.first_host(s) == "192.168.1.1"
    assert ipn.last_host(s) == "192.168.1.254"
    assert ipn.hosts_count(s) == 254

# /26：起點、終點
def test_26_network_and_broadcast():
    s = "10.0.0.130/26"
    assert ipn.network_of(s) == "10.0.0.128"
    assert ipn.broadcast_of(s) == "10.0.0.191"

# /26：包含與不包含
def test_26_contains_in_and_out():
    s = "10.0.0.130/26"
    assert ipn.contains(s, "10.0.0.150") is True
    assert ipn.contains(s, "10.0.0.192") is False

# /26：可用數 62
def test_26_hosts_count_62():
    s = "10.10.10.64/26"
    assert ipn.hosts_count(s) == 62

# /31：特例（無可用），network/broadcast 仍定義
def test_31_special_case_no_usable():
    s = "172.16.5.10/31"
    assert ipn.hosts_count(s) == 0
    assert ipn.first_host(s) is None
    assert ipn.last_host(s) is None
    assert ipn.network_of(s) == "172.16.5.10"
    assert ipn.broadcast_of(s) == "172.16.5.11"

# /32：單位址，無可用
def test_32_special_case_single_ip():
    s = "203.0.113.99/32"
    assert ipn.hosts_count(s) == 0
    assert ipn.first_host(s) is None
    assert ipn.last_host(s) is None
    assert ipn.network_of(s) == "203.0.113.99"
    assert ipn.broadcast_of(s) == "203.0.113.99"

# 邊界點皆屬於集合（但一般不分配）
def test_boundary_contains_start_and_end_true():
    s = "192.0.2.64/26"
    assert ipn.contains(s, "192.0.2.64") is True   # 起點
    assert ipn.contains(s, "192.0.2.127") is True  # 終點

# 斜線數字回傳
def test_cidr_returns_prefixlen():
    assert ipn.cidr("192.168.1.42/24") == 24
    assert ipn.cidr("10.0.0.130/26") == 26

# 壞輸入與 IPv6 拒收
def test_invalid_inputs_raise():
    with pytest.raises(ValueError):
        ipn.network_of("300.1.1.1/24")
    with pytest.raises(ValueError):
        ipn.network_of("192.168.1.1/-1")
    with pytest.raises(ValueError):
        ipn.contains("192.168.1.0/24", "999.999.0.1")
    with pytest.raises(ValueError):
        ipn.contains("192.168.1.0/24", "::1")
