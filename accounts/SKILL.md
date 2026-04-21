# UTAGE AI Skill - accounts

配信アカウント・ラベル・読者データを管理します。

## MCPツール

| ツール名 | 操作 |
|:---|:---|
| `message_account_list` / `message_account_create` | アカウントCRUD |
| `message_label_list` / `message_label_create` / `message_label_get` | ラベル取得・作成 |
| `message_label_update` / `message_label_delete` | ラベル更新・削除 |
| `message_common_reader_label_list` / `_create` / `_delete` | 読者へのラベル付与・削除 |
| `message_reader_list_all` / `message_reader_list` / `message_reader_get` | 読者データ参照 |

---

## アカウントタイプ

| type | 用途 |
|:---|:---|
| `mail` | メールのみ |
| `line` | LINEのみ |
| `mail_line` | メール + LINE 統合 |

---

## ⚠️ 注意点

> → 全カテゴリ共通トラップはルートの SKILL.md を参照

- 読者データの更新（メール変更等）は API 非対応。管理画面のみ

---

## 補足: REST API（curl）

```bash
# アカウント一覧
curl -s "https://api.utage-system.com/v1/accounts" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# ラベル一覧
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/labels" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# 読者一覧
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/readers" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```
