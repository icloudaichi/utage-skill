# UTAGE AI Skill - accounts

配信アカウントの作成・一覧取得を行います。
ラベル管理も含みます。

---

## 配信アカウント

### 一覧取得

```bash
curl -s "https://api.utage-system.com/v1/accounts" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# typeで絞り込み
curl -s "https://api.utage-system.com/v1/accounts?type=mail" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

| typeの値 | 用途 |
|:---|:---|
| `mail` | メールのみ |
| `line` | LINEのみ |
| `mail_line` | メール + LINE 統合 |

### 作成

```bash
curl -s -X POST "https://api.utage-system.com/v1/accounts" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "メインリスト", "type": "mail"}'
```

### 削除

```bash
curl -s -X DELETE "https://api.utage-system.com/v1/accounts/ACCOUNT_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## ラベル管理

ラベルは読者をセグメント分けするための機能。配信条件（conditions）で使用。

### ラベル一覧取得

```bash
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/labels" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

### ラベル作成

```bash
curl -s -X POST "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/labels" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "購入者", "color": "#e74c3c"}'
```

### ラベル更新・削除

```bash
# 更新
curl -s -X PUT "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/labels/LABEL_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "新しい名前", "color": "#3498db"}'

# 削除
curl -s -X DELETE "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/labels/LABEL_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

### 読者へのラベル付与・削除

```bash
# ラベル付与
curl -s -X POST "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/readers/READER_ID/labels" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"label_id": "LABEL_ID"}'

# ラベル削除
curl -s -X DELETE "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/readers/READER_ID/labels/LABEL_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## 読者一覧取得（参照のみ）

```bash
# 全読者
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/readers" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# シナリオ別読者
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios/SCENARIO_ID/readers" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# 読者詳細（カスタムフィールド含む）
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/readers/READER_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

> 読者データの更新（メール変更等）は API 非対応。管理画面のみ。

---

## MCPツール（同等操作）

```
message_account_list / message_account_create
message_label_list / message_label_create / message_label_get / message_label_update / message_label_delete
message_common_reader_label_list / message_common_reader_label_create / message_common_reader_label_delete
message_reader_list_all / message_reader_list / message_reader_get
```
