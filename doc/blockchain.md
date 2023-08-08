# Blockchainの使用

## Blockchainの特徴、強み

1. トレーサビリティに優れている。
2. 信頼性に優れている

ブロックチェーンの不変性とセキュリティを利用して重要な情報を保護し、DBを軽量化して高速なデータアクセスを実現することが可能

## 環境

- Platform: Kaleido
  - Provider: Quorum: プライベートなブロックチェーン
  - Consensus Algorithm: Raft = ブロックの生成タイミングがトランザクション毎
- Language: Solidity

## 記録項目

- 購入ID (purchase_id)：購入情報を一意に識別するためのID。
- ユーザID (user_id)：購入を行ったユーザのID。
- 出品物ID (item_id)：購入された商品のID。
- 購入日時 (purchase_date)：購入が行われた日時。
- 購入価格 (purchase_price)：商品の購入価格。
- 購入数量 (quantity)：購入した商品の数量。
