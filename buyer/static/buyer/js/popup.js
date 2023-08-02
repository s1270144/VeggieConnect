// ポップアップを表示する関数
function openPopup() {
    var popupContent = document.getElementById('popup-content');
    popupContent.style.display = 'block';
}

// ポップアップを閉じる関数
function closePopup() {
    var popupContent = document.getElementById('popup-content');
    popupContent.style.display = 'none';
}

function goBack() {
    window.history.back(); // ブラウザの履歴を操作して前のページに戻る
}
