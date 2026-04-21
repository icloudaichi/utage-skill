# UTAGE AI Skill - messages

ステップメール・LINE配信の作成・編集・削除を行います。

---

## メッセージ作成（ステップメール）

### 必須パラメータ（省略するとvalidation_error）

```json
{
  "account_id": "...",
  "scenario_id": "...",
  "channel": "mail",
  "type": "step",
  "send_type": "scheduled",
  "send_date": 2,
  "send_hour": 18,
  "send_min": 0,
  "title": "件名",
  "mail": {
    "type": "plain_text",
    "from_mail": "info@example.com",
    "from_name": "送信者名",
    "subject": "件名",
    "text": "本文"
  }
}
```

### send_type の値

| 値 | 意味 | 追加パラメータ |
|:---|:---|:---|
| `"immediately"` | 登録直後に送信 | 不要（send_date等は無視） |
| `"scheduled"` | 指定日時に送信 | `send_date`（日数）+ `send_hour` + `send_min` |

> ⚠️ `send_type: "immediately"` のステップはAPI経由での公開（reserved化）が不可。管理画面から手動公開すること。

### curl サンプル

```bash
# ステップメール作成
curl -s -X POST "https://api.utage-system.com/v1/messages" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  --data-binary @- << 'EOF'
{
  "account_id": "YOUR_ACCOUNT_ID",
  "scenario_id": "YOUR_SCENARIO_ID",
  "channel": "mail",
  "type": "step",
  "send_type": "scheduled",
  "send_date": 1,
  "send_hour": 18,
  "send_min": 0,
  "title": "2通目：翌日18時",
  "mail": {
    "type": "plain_text",
    "from_mail": "info@example.com",
    "from_name": "送信者名",
    "subject": "件名",
    "text": "本文テキスト"
  }
}
EOF
```

---

## メッセージ一覧取得

```bash
curl -s "https://api.utage-system.com/v1/messages?account_id=ACCOUNT_ID&scenario_id=SCENARIO_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## メッセージ更新（PUT）

> ⚠️ PUT は全フィールド必須。未指定フィールドは null にリセットされる。  
> 必ず GET で現在値を取得してから、変更箇所だけ書き換えて送信すること。

```bash
curl -s -X PUT "https://api.utage-system.com/v1/messages/MESSAGE_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  --data-binary @payload.json
```

---

## メッセージ削除

```bash
curl -s -X DELETE "https://api.utage-system.com/v1/messages/MESSAGE_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## LINE配信（channel: line）

```json
{
  "account_id": "...",
  "scenario_id": "...",
  "channel": "line",
  "type": "step",
  "send_type": "scheduled",
  "send_date": 1,
  "send_hour": 18,
  "send_min": 0,
  "title": "LINE 2通目",
  "line": {
    "messages": [
      {
        "type": "text",
        "text": "メッセージ本文"
      }
    ]
  }
}
```

---

## MDファイルからの一括投入パターン

フロントマターで設定を書き、本文をテキストにする形式:

```markdown
---
account_id: ACCOUNT_ID
scenario_id: SCENARIO_ID
channel: mail
type: step
send_type: scheduled
send_date: 2
send_hour: 18
send_min: 0
title: 3通目：2日後18時
from_mail: info@example.com
from_name: 送信者名
subject: 【Day2】件名
---
本文テキストをここに書く
```

AIはこのMDを読み取り、フロントマターをAPIパラメータに変換して送信する。
