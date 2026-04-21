# UTAGE AI Skill - media

UTAGE内にアップロードされた動画・音声のURLを取得します。  
※ メディアのアップロードはAPIに非対応（管理画面のみ）

## MCPツール

| ツール名 | 操作 |
|:---|:---|
| `media_video_list` | 動画一覧取得（keyword / folder_id で絞り込み可） |
| `media_video_folder_list` | 動画フォルダ一覧 |
| `media_audio_list` | 音声一覧取得 |
| `media_audio_folder_list` | 音声フォルダ一覧 |

---

## ⚠️ 注意点

> → 全カテゴリ共通トラップはルートの SKILL.md を参照

- 取得したURLをページ要素で使う場合: `video_id` は NG。必ず **`video_url`（絶対パスURL）** を使うこと

---

## 補足: REST API（curl）

```bash
# 動画一覧
curl -s "https://api.utage-system.com/v1/media/videos" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# 音声一覧
curl -s "https://api.utage-system.com/v1/media/audios" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```
