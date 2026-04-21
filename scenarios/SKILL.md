# UTAGE AI Skill - scenarios

配信アカウント配下のシナリオを管理します。

---

## ⚠️ 重要: フィールド名のトラップ

シナリオ作成のフィールド名は `name` ではなく **`title`**。
`name` を使うとエラーなく成功するが、タイトルが空になる（サイレント失敗）。

---

## シナリオ一覧取得

```bash
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios" \
  -H "Authorization: Bearer $UTAGE_API_KEY"

# タイトルで検索
curl -s "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios?title=テスト" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## シナリオ作成

```bash
curl -s -X POST "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "プロモーションシナリオ",
    "open_title": "公開タイトル（省略時はtitleを使用）"
  }'
```

| パラメータ | 必須 | 説明 |
|:---|:---|:---|
| `title` | ✅ | シナリオタイトル（`name` は NG） |
| `open_title` | - | 公開タイトル（読者に見える名前） |

---

## シナリオ更新

```bash
curl -s -X PUT "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios/SCENARIO_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "新しいタイトル"}'
```

---

## シナリオ削除

```bash
curl -s -X DELETE "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios/SCENARIO_ID" \
  -H "Authorization: Bearer $UTAGE_API_KEY"
```

---

## 実践フロー（プロモーション一括構築）

```bash
# 1. シナリオ作成
SCENARIO=$(curl -s -X POST "https://api.utage-system.com/v1/accounts/ACCOUNT_ID/scenarios" \
  -H "Authorization: Bearer $UTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "春のプロモーション2026"}')
SCENARIO_ID=$(echo $SCENARIO | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['id'])")

# 2. シナリオIDを使ってメッセージを一括投入
# → messages/SKILL.md を参照
```

---

## MCPツール（同等操作）

```
message_scenario_list / message_scenario_create
```
