# ipv4-subnet-lab


最小可執行的 IPv4 子網小工具：給一段「位址/斜線」的描述，回答七種問題（起點、終點、第一可用、最後可用、可用數量、包含關係、斜線數字）。附單元測試與一頁法典。

## SLO（5 行）
目的：把「位址/斜線」這一塊子網說清楚，並可重現驗收。  
輸入輸出：輸入一段像 `"192.168.1.130/26"` 與可選的單一位址；輸出為字串、整數或布林。  
驗收方式：`pytest -q` 全綠（覆蓋 /26、/24、/31、/32、首尾邊界、包含與不包含）。  
邊界語句：壞格式丟錯；/31、/32 視為無可用主機；包含關係包含端點。  
版本/日期：v0.1（2025-09-03）

## 目錄
- `ipv4_subnet/ipv4_subnet.py`：核心 API（7 個函式）
- `tests/test_ipv4_subnet.py`：10–12 條測試
- `lawpage_ipv4_subnet.md`：Definitions、核心三律、When/When-not
- `requirements.txt`：僅 `pytest`
- `.gitignore`、`LICENSE`

## 安裝與重現
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
