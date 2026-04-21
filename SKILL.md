---
name: utage-skill
description: >
  UTAGEをAI（MCP + REST API）で操作するための実機検証済みスキル。
  公開情報をもとに検証した知見をOSSとして共有します。
  エラー・発見はGitHub Discussionsで報告してください。
requires:
  - .env（UTAGE_API_KEY設定済み）
  - UTAGEのMCPサーバー接続
---

# UTAGE AI Skill

> 公開情報をもとに実機検証した知見のオープンスキルです。  
> 「UTAGEの操作ナレッジは、みんなで育てた方が速い」という思想で公開しています。  
> エラー・新発見はぜひ [GitHub Discussions](https://github.com/icloudaichi/utage-skill/discussions) へ。

---

## 初回セットアップ

`.env` が未設定の場合は先にセットアップを完了してください:

```
setup/ フォルダの SKILL.md を参照してください
```

---

## 操作カテゴリ

目的に応じて対応するサブスキルを読み込んでください:

| カテゴリ | 参照先 | 内容 |
|:---|:---|:---|
| ステップメール・LINE配信 | `messages/SKILL.md` | 作成・編集・削除・一括投入 |
| ファネル・LP・ページ要素 | `funnels/SKILL.md` | ファネルCRUD・要素タイプ一覧 |
| シナリオ管理 | `scenarios/SKILL.md` | シナリオCRUD |
| 配信アカウント | `accounts/SKILL.md` | アカウントCRUD |
| メディア参照 | `media/SKILL.md` | 画像・動画URLの確認 |
| エラー報告・フィードバック | `report/SKILL.md` | GitHub Discussionsへ投稿 |

---

## 共通設定の読み方

`.env` から以下を読み込んでください:

```bash
source .env
# UTAGE_API_KEY が設定されていることを確認
echo $UTAGE_API_KEY
```

API呼び出し共通ヘッダー:
```bash
-H "Authorization: Bearer $UTAGE_API_KEY" \
-H "Content-Type: application/json"
```

ベースURL: `https://api.utage-system.com/v1`

---

## ⚠️ 全カテゴリ共通の既知トラップ

> 実機検証で発見したエラー一覧です。AIはこれを参照してから操作してください。

### メッセージAPI

| # | 症状 | 原因 | 正解 |
|:---|:---|:---|:---|
| 1 | `validation_error: 送信タイプは必ず指定してください` | `send_type` を省略 | `send_type: "scheduled"` or `"immediately"` を必ず付ける |
| 2 | 即時配信のステップが公開できない | `send_type: "immediately"` はAPI経由で公開不可 | 管理画面から手動公開 or `send_date: 0` で代替 |

### ファネル要素 — プロパティ名の誤記

| # | 要素 | ❌ 使えない | ✅ 正しい | 症状 |
|:---|:---|:---|:---|:---|
| 3 | `image` | `image_src` | **`image_url`** | エラーなし・サイレント失敗 |
| 4 | `video` | `video_id` | **`video_url`（絶対パスURL）** | 保存されない |
| 5 | `table` | `content` | **`body_rows` + `body_cols` + `table_data`** | キーが存在しない |
| 6 | `deadline` | `target_datetime` | **`target_type`（必須）+ `target_date`** | 受け付けられない |
| 7 | `accordion` | `title` | **`content`（ヘッダー）+ `sub_content`** | サイレント失敗 |
| 8 | `form-button` | `button_text` / `button_text_color` | **`content` / `color`** | サイレント失敗 |

### ページAPI

| # | 症状 | 原因 | 対策 |
|:---|:---|:---|:---|
| 9 | PUT後に他の要素がnullリセット | 変更箇所だけ送った | PUT前に必ずGETして全フィールド含めて送信 |
| 10 | `padding_top/bottom` が効かない | `section` に設定した | **`col`** に設定する |
| 11 | 日本語JSONでエンコードエラー | パイプで渡した | `--data-binary @file` でファイル経由 |

### API制限

| # | 操作 | 結果 |
|:---|:---|:---|
| 12 | `POST /actions` アクション作成 | **405 Method Not Allowed**（管理画面のみ） |
| 13 | シナリオ作成で `name` フィールド | **フィールド名は `title`** が正しい |

---

## このスキルについて

- **ライセンス**: MIT（スクリプト）/ CC BY 4.0（ドキュメント）
- **対象API**: UTAGE 公式 MCP + REST API v1 のみ
- **メンテナー**: [@icloudaichi](https://github.com/icloudaichi)
- **バージョン**: 0.1.0（2026-04-21）
- **フィードバック**: [GitHub Discussions](https://github.com/icloudaichi/utage-skill/discussions)
