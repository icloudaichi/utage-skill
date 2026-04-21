# UTAGE AI Skill - funnels

ファネル・ステップ・ページの作成・編集・削除を行います。

---

## データ構造

```
ファネル
 └── ステップ（公開URLを持つ）
      └── ページ（A/Bテスト時に複数可）
           └── 要素（section > row > col > コンテンツ要素）
```

---

## ファネル操作

### 一覧取得
```bash
curl -s "https://api.utage-system.com/v1/funnels" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

### 作成
```bash
curl -s -X POST "https://api.utage-system.com/v1/funnels" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "ファネル名"}'
```

### 更新（JS/CSS埋め込みも可）
```bash
curl -s -X PUT "https://api.utage-system.com/v1/funnels/FUNNEL_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "新しい名前", "js_head": "<!-- GTMコード等 -->"}'
```

### 削除
```bash
curl -s -X DELETE "https://api.utage-system.com/v1/funnels/FUNNEL_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## ステップ操作

### 一覧取得（step_url を含む）
```bash
curl -s "https://api.utage-system.com/v1/funnels/FUNNEL_ID/steps" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

### 作成
```bash
curl -s -X POST "https://api.utage-system.com/v1/funnels/FUNNEL_ID/steps" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "LP"}'
```

### 並び替え
```bash
# ⚠️ 全ステップIDを含める必要あり（漏れると削除扱いになる可能性）
curl -s -X PUT "https://api.utage-system.com/v1/funnels/FUNNEL_ID/steps/reorder" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"step_ids": ["STEP_ID_1", "STEP_ID_2", "STEP_ID_3"]}'
```

---

## ページ操作

### ⚠️ 要素の階層ルール（必須）

```
section（最上位コンテナ）
 └── row（行）
      └── col（列、col_widthで幅指定、合計12）
           └── コンテンツ要素（text, image, button 等）
```

> ⚠️ section の直下に text 等を置くのは NG。必ず row > col を経由すること。

> ⚠️ `padding_top` / `padding_bottom` は **col** に設定する（section に設定しても効かない）

### ページ作成（LP例）

```bash
cat > /tmp/page.json << 'EOF'
{
  "title": "管理用タイトル",
  "page_title": "ページタイトル（ブラウザタブ）",
  "pc_width": 800,
  "elements": [
    {
      "type": "section",
      "children": [{
        "type": "row",
        "children": [{
          "type": "col",
          "padding_top": 60,
          "padding_bottom": 60,
          "children": [
            {"type": "text", "content": "<h1>見出しテキスト</h1>"},
            {
              "type": "image",
              "image_url": "https://example.com/image.jpg"
            },
            {
              "type": "button",
              "content": "申し込む",
              "color": "#ffffff",
              "background_color": "#e74c3c",
              "href": "https://example.com/apply"
            }
          ]
        }]
      }]
    }
  ]
}
EOF

curl -s -X POST \
  "https://api.utage-system.com/v1/funnels/FUNNEL_ID/steps/STEP_ID/pages" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/page.json
```

### ページ更新（⚠️ 必ずGETして全フィールドを含めること）

```bash
# Step 1: 現在のページデータを取得
curl -s "https://api.utage-system.com/v1/funnels/FUNNEL_ID/steps/STEP_ID/pages/PAGE_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY" > /tmp/current_page.json

# Step 2: 変更箇所のみ修正して /tmp/updated_page.json を作る

# Step 3: PUT送信（id, step_url, page_url, created_at, updated_at は除外）
curl -s -X PUT \
  "https://api.utage-system.com/v1/funnels/FUNNEL_ID/steps/STEP_ID/pages/PAGE_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/updated_page.json
```

> ⚠️ PUT は破壊的上書き。未指定フィールドは null にリセットされる。

> ⚠️ 日本語を含む JSON は `--data-binary @file` で送信（パイプ経由はエンコードエラーの可能性）

---

## 要素タイプ一覧の確認

```bash
# 基本要素
curl -s "https://api.utage-system.com/v1/element-types/funnel" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# フォーム・決済・イベント要素も含める
curl -s "https://api.utage-system.com/v1/element-types/funnel?include=form,payment,event" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## ⚠️ 既知のプロパティ名トラップ

| 要素 | ❌ 使えない | ✅ 正しい | 症状 |
|:---|:---|:---|:---|
| `image` | `image_src` | **`image_url`** | エラーなし・サイレント失敗 |
| `video` | `video_id` | **`video_url`（絶対パスURL）** | 保存されない |
| `button` | `button_text` | **`content`** | サイレント失敗 |
| `button` | `button_text_color` | **`color`** | サイレント失敗 |
| `table` | `content` | **`body_rows` + `body_cols` + `table_data`** | キーが存在しない |
| `deadline` | `target_datetime` | **`target_type`（必須）+ `target_date`** | 受け付けられない |
| `accordion` | `title` | **`content` + `sub_content`** | サイレント失敗 |
| `form-input` | `form-name`, `form-email` | **`form-input` + `item`プロパティ** | 存在しない要素タイプ |

---

## MCPツール（同等操作）

```
funnel_list / funnel_create / funnel_update
funnel_step_list / funnel_step_create / funnel_step_update / funnel_step_reorder
funnel_page_list / funnel_page_get / funnel_page_create / funnel_page_update / funnel_page_delete
element_types_funnel / element_types_funnel_properties
```
