# modelの構成

## User

- id
- password
- last_login
- account_id
- email
- last_name
- birth_date
- is_superuer
- staff status
- is_seller
- active
- created_at
- updateded_at
- address
- profile_picture

## Buyer

- id
- address
- favorite
- user_id

## Transaction

- purchase_id：購入情報を一意に識別するためのID。
- user_id：購入を行ったユーザのID。
- item_id：購入された商品のID。
- purchase_date：購入が行われた日時。
- purchase_price：商品の購入価格。
- quantity：購入した商品の数量。
- purchase_status：購入の進行状況を示すステータス（例：未処理、発送済み、配達済みなど）。
- payment_method：支払いに使用された方法（クレジットカード、銀行振込など）。
- shipping_info：商品の配送先情報（住所、氏名など）。
- billing_info：商品の請求情報（請求先住所、請求先氏名など）。
- additional_info：必要に応じて、特定のプロジェクトに固有の情報を含めることができます。

## Seller

- id
- address
- user_id

## Vegetable

- id
- item_name
- item_type
- price
- content_quantity
- content_price
- total_quantity
- seller_id -> (Seller.id)
