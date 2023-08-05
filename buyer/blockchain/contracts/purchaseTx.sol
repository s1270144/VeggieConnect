// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract PurchaseTx {
	// ①コントラクトオーナーのアドレス
    address private owner;
    uint private numTransaction;  // 購入取引数

    // ②登録情報を保存するデータ構造体
    struct transactionInfo {
        string purchase_id;         // 購入取引ID
        string user_id;             // 購入ユーザID
        string item_id;             // 購入商品ID
        uint256 purchase_date;      // 購入日時(タイムスタンプ)
        string purchase_price;      // 購入価格
        string quantity;            // 購入数量
    }
    mapping(uint => transactionInfo) private transaction;

    // ③コンストラクタ
    // コントラクトを公開した際に実行されます
    constructor() {
        owner = msg.sender;     // コントラクトを公開したアドレスをオーナーに指定する
        numTransaction = 0;     // 登録数の初期化
    }

    // ④アクセス制限の実装
    modifier onlyOwner {
	    // コントラクトを呼び出したアドレスがオーナーと一致するか確認する
	    // 一致しない場合は処理を止める
        require(msg.sender == owner);
        _; // modifierの末尾に必要
    }

    // ⑤modifierを関数に付与する
    // 取引情報を登録する関数
    function setInfo(string memory _purchase_id, string memory _user_id, string memory _item_id, string memory _purchase_price, string memory _quantity) public onlyOwner{
        transaction[numTransaction].purchase_id = _purchase_id;
        transaction[numTransaction].user_id = _user_id;
        transaction[numTransaction].item_id = _item_id;
        transaction[numTransaction].purchase_date = block.timestamp;
        transaction[numTransaction].purchase_price = _purchase_price;
        transaction[numTransaction].quantity = _quantity;
        numTransaction++;
    }

    // // 取引情報を取得する関数[配列ユーザ番号](購入取引ID, 購入ユーザID, 購入商品ID, 購入日時, 購入価格, 購入数量)
    // function getInfo(uint _numTransaction) view public onlyOwner returns(string memory, string memory, string memory, uint256, string memory, string memory) {
    //     return (transaction[_numTransaction].purchase_id, transaction[_numTransaction].user_id, transaction[_numTransaction].item_id, transaction[_numTransaction].purchase_date, transaction[_numTransaction].purchase_price, transaction[_numTransaction].quantity);
    // }

    // 引数のpurchase_idにマッチするtransactionInfo構造体を取得する関数
    function get_detail(string memory purchase_id) public view returns (transactionInfo memory) {
        for (uint i = 0; i < numTransaction; i++) {
            transactionInfo memory info = transaction[i];
            if (compareStrings(info.purchase_id, purchase_id)) {
                return info;
            }
        }
        revert("Transaction not found");
    }

    // 引数のuser_idにマッチするtransactionInfo構造体を取得する関数
    function getTransactionInfo(string memory user_id) public view returns (transactionInfo[] memory) {
        uint count = 0;
        for (uint i = 0; i < numTransaction; i++) {
            if (compareStrings(transaction[i].user_id, user_id)) {
                count++;
            }
        }

        // マッチするtransactionInfoを保存する配列を初期化
        transactionInfo[] memory matches = new transactionInfo[](count);
        uint index = 0;

        // マッチするtransactionInfoを配列に追加
        for (uint i = 0; i < numTransaction; i++) {
            if (compareStrings(transaction[i].user_id, user_id)) {
                matches[index] = transaction[i];
                index++;
            }
        }

        // 一致するtransactionInfoが存在しない場合はエラーを発生させる
        if (count == 0) {
            revert("Transaction not found");
        }

        return matches;
    }


    // 文字列を比較するためのヘルパー関数（Solidityのバージョンによって異なる）
    function compareStrings(string memory a, string memory b) private pure returns (bool) {
        return keccak256(abi.encodePacked(a)) == keccak256(abi.encodePacked(b));
    }

    // 取引数
    function getNumTransaction() external view returns (uint) {
        return numTransaction;
    }

}
