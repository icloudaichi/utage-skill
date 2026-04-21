# UTAGE AI Skill - media

UTAGE内にアップロードされた動画・音声のURLを取得します。
※ メディアのアップロードはAPIに非対応（管理画面のみ）

---

## 動画一覧取得

```bash
curl -s "https://api.utage-system.com/v1/media/videos" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# キーワード検索
curl -s "https://api.utage-system.com/v1/media/videos?keyword=セミナー" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# フォルダ指定
curl -s "https://api.utage-system.com/v1/media/videos?folder_id=FOLDER_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

## 動画フォルダ一覧

```bash
curl -s "https://api.utage-system.com/v1/media/videos/folders" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

## 音声一覧取得

```bash
curl -s "https://api.utage-system.com/v1/media/audios" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

## 音声フォルダ一覧

```bash
curl -s "https://api.utage-system.com/v1/media/audios/folders" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## 取得したURLの使い方

動画URLはページ要素の `video` タイプで使用:

```json
{
  "type": "video",
  "video_url": "https://取得したURL"
}
```

> ⚠️ `video_id` は NG。必ず `video_url`（絶対パスURL）を使うこと。

---

## MCPツール（同等操作）

```
media_video_list / media_video_folder_list
media_audio_list / media_audio_folder_list
```
