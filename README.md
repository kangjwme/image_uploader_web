
# 圖片上傳平台

這是一個簡單的圖片上傳平台，用於上傳和儲存 GIF、JPG、PNG、HEIF 格式的圖片。上傳成功後，使用者將獲得圖片的直接連結。

## 功能特點

- **支援的圖片格式**：GIF, JPG, JPEG, PNG, HEIF
- **大小限制**：圖片大小不得超過 10MB
- **即時連結生成**：上傳後會顯示圖片的直接連結
- **錯誤提示**：如果上傳的檔案格式不符或大小超過限制，會顯示錯誤訊息

## 技術棧

- **前端**：HTML, CSS, JavaScript
- **後端**：Flask (Python)

## 本地部署

### 步驟 1: 安裝依賴套件

首先，確保您已安裝 Python 3。接著，使用以下指令安裝 Flask 及其他必要的套件：

```bash
pip install Flask
```

### 步驟 2: 將專案克隆或下載到本地

下載專案程式碼，並進入專案目錄。

### 步驟 3: 檔案結構

確保專案結構如下：

```
project_folder/
│
├── app.py               # 主程式碼文件
├── templates/
│   └── upload.html      # 上傳頁面的 HTML 檔案
└── uploads/             # 圖片儲存目錄 (自動創建)
```

### 步驟 4: 啟動本地伺服器

在專案目錄下，執行以下指令來啟動 Flask 應用：

```bash
python app.py
```

如果一切正常，伺服器將會在 `http://127.0.0.1:5000` 啟動。您可以在瀏覽器中訪問此網址來查看上傳頁面。

### 步驟 5: 使用說明

1. 使用者可以將圖片檔案拖曳到上傳區域，或點擊上傳區域以選擇檔案。
2. 上傳圖片後，頁面會顯示圖片的連結。點擊連結即可在新頁籤中查看圖片。
3. 若上傳的檔案格式不符或超過大小限制，系統會在上傳區域下方顯示紅色的錯誤訊息。

## 錯誤處理

- **格式不符或大小超限**：上傳的檔案格式不符合或超過 10MB 時，會在上傳區域下方顯示紅色錯誤訊息。
- **上傳失敗**：若伺服器端出現錯誤，頁面會顯示「上傳失敗」訊息。

## 開發

若您想修改並重新啟動伺服器，可以手動執行 `python app.py` 或使用工具（如 Flask 的 `flask run` 或 `nodemon`）進行自動重新加載。

## 版權宣告

此專案為學習用途，可自由使用和修改。若需進行商業用途，請考慮相關的儲存空間與網路配置。