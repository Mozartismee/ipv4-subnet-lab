import pytest
import ipv4_subnet.ipv4_subnet as ipn

def test_24_network_and_broadcast():
    s = "192.168.1.42/24"
    assert ipn.network_of(s) == "192.168.1.0"
    assert ipn.broadcast_of(s) == "192.168.1.255"

def test_24_hosts_range_and_count():
    s = "192.168.1.42/24"
    assert ipn.first_host(s) == "192.168.1.1"
    assert ipn.last_host(s) == "192.168.1.254"
    assert ipn.hosts_count(s) == 254

def test_26_network_and_broadcast():
    s = "10.0.0.130/26"
    assert ipn.network_of(s) == "10.0.0.128"
    assert ipn.broadcast_of(s) == "10.0.0.191"

def test_26_contains_in_and_out():
    s = "10.0.0.130/26"
    assert ipn.contains(s, "10.0.0.150") is True
    assert ipn.contains(s, "10.0.0.192") is False

def test_26_hosts_count_62():
    s = "10.10.10.64/26"
    assert ipn.hosts_count(s) == 62

def test_31_special_case_no_usable():
    s = "172.16.5.10/31"
    assert ipn.hosts_count(s) == 0
    assert ipn.first_host(s) is None
    assert ipn.last_host(s) is None
    assert ipn.network_of(s) in {"172.16.5.10", "172.16.5.10"}  # network_of still defined
    assert ipn.broadcast_of(s) in {"172.16.5.11", "172.16.5.11"}

def test_32_special_case_single_ip():
    s = "203.0.113.99/32"
    assert ipn.hosts_count(s) == 0
    assert ipn.first_host(s) is None
    assert ipn.last_host(s) is None
    assert ipn.network_of(s) == "203.0.113.99"
    assert ipn.broadcast_of(s) == "203.0.113.99"

def test_boundary_contains_start_and_end_true():
    s = "192.0.2.64/26"
    assert ipn.contains(s, "192.0.2.64") is True  # 起點
    assert ipn.contains(s, "192.0.2.127") is True  # 終點

def test_cidr_returns_prefixlen():
    assert ipn.cidr("192.168.1.42/24") == 24
    assert ipn.cidr("10.0.0.130/26") == 26

def test_invalid_inputs_raise():
    with pytest.raises(ValueError):
        ipn.network_of("300.1.1.1/24")
    with pytest.raises(ValueError):
        ipn.network_of("192.168.1.1/-1")
    with pytest.raises(ValueError):
        ipn.contains("192.168.1.0/24", "999.999.0.1")
