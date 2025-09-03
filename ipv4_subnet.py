"""
ipv4_subnet.py — Minimal IPv4 subnet utilities (standard library only).

提供七個函式，針對「位址/斜線」描述的一塊 IPv4 子網，回答：
- 起點 (network_of)
- 終點 (broadcast_of)
- 第一可用位址 (first_host)
- 最後可用位址 (last_host)
- 可用位址數 (hosts_count)
- 是否包含某位址 (contains)
- 斜線表示法 (cidr)

壞格式會拋 ValueError。/31 與 /32 視為無可用位址。
"""

from ipaddress import ip_network, ip_address, IPv4Address

def _net(subnet: str):
    # strict=False 允許輸入為「主機位址/斜線」，自動對齊到該子網
    try:
        return ip_network(subnet, strict=False)
    except Exception as e:
        raise ValueError(f"invalid subnet: {subnet}") from e

def network_of(subnet: str) -> str:
    """回傳子網的起點位址字串，例如 '192.168.1.128'。"""
    n = _net(subnet)
    return str(n.network_address)

def broadcast_of(subnet: str) -> str:
    """回傳子網的終點位址字串，例如 '192.168.1.191'。"""
    n = _net(subnet)
    return str(n.broadcast_address)

def first_host(subnet: str) -> str | None:
    """
    回傳子網的第一個可用位址。
    /31 或 /32 特例：回傳 None。
    """
    n = _net(subnet)
    if n.prefixlen >= 31:
        return None
    first = IPv4Address(int(n.network_address) + 1)
    return str(first)

def last_host(subnet: str) -> str | None:
    """
    回傳子網的最後一個可用位址。
    /31 或 /32 特例：回傳 None。
    """
    n = _net(subnet)
    if n.prefixlen >= 31:
        return None
    last = IPv4Address(int(n.broadcast_address) - 1)
    return str(last)

def hosts_count(subnet: str) -> int:
    """
    回傳可用主機數。
    一般情況 = 總數 - 2；/31 與 /32 回 0。
    """
    n = _net(subnet)
    if n.prefixlen >= 31:
        return 0
    return n.num_addresses - 2

def contains(subnet: str, ip: str) -> bool:
    """判斷位址 ip 是否落在 subnet 裡（含端點）。壞格式丟 ValueError。"""
    n = _net(subnet)
    try:
        a = ip_address(ip)
    except Exception as e:
        raise ValueError(f"invalid ip: {ip}") from e
    return a in n

def cidr(subnet: str) -> int:
    """回傳斜線數字（CIDR prefix length），例如 24。壞格式丟 ValueError。"""
    n = _net(subnet)
    return n.prefixlen
