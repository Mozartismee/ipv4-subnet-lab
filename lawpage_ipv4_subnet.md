# Lawpage — IPv4 Subnet（CIDR 一頁法典）

## 正規術語
**CIDR（Classless Inter-Domain Routing）** 以 **前綴** 表示位址集合：`a.b.c.d/p`。  
遮罩（mask）為前 `p` 位為 1、其餘為 0 的 32 位元向量。  
**網路位址（network）**為集合最小位址；**廣播位址（broadcast）**為集合最大位址。  
元素判定規則等價於：`ip AND mask = network`。

> 速記：`p` = 網路位數、`h = 32 − p` = 主機位數、集合大小 `2^h`。  
> `network = ip & mask`；`broadcast = network | ~mask`。

---

## 定義（Definitions）
- 子網（prefix）：所有前 `p` 位相同之位址的集合。  
- network：該集合最小位址。  
- broadcast：該集合最大位址。  
- 可用位址（一般）：除 network 與 broadcast 外的位址；`/31` 與 `/32` 為特例視為無可用。

---

## 核心三律（考點直擊）
1) **界線（AND 規則）**：`network ≤ ip ≤ broadcast`  
   等價於 `ip AND mask = network`（端點屬於集合，但一般不分配）。  
2) **數量**：一般可用主機數 `= 2^(32−p) − 2`。  
3) **例外**：`/31` 與 `/32` 無可用；若題目明示 RFC 3021（點對點），`/31` 可兩端皆用（本法典預設一般規則）。

---

## 使用窗口（When / When-not）
- **When**：需要界線（network/broadcast

