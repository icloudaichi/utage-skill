# UTAGE AI Skill - セットアップ

初回利用時に実行してください。

---

## Step 1: .env を作成

```bash
cp .env.example .env
```

`.env` を開いて以下を設定:

- `UTAGE_API_KEY`: UTAGE管理画面 > API設定 から取得
- `GITHUB_TOKEN`: https://github.com/settings/tokens から取得（任意）
  - 必要スコープ: `repo`

---

## Step 2: UTAGE API疎通確認

```bash
source .env
curl -s "https://api.utage-system.com/v1/funnels" \
  -H "Authorization: Bearer $UTAGE_API_KEY" | head -c 200
```

レスポンスが返ればOKです。

---

## Step 3: MCPサーバー設定 または REST API直接利用

このスキルは **2つの動作モード** があります。

| モード | 対応ツール | 認証方法 |
|:---|:---|:---|
| **MCP接続** | Claude Code / claude.ai | OAuth（ブラウザ認証） |
| **REST API直接** | Cursor / Antigravity / その他 | UTAGE_API_KEY（.env） |

---

### モードA: MCP接続（Claude Code / claude.ai）

UTAGEのMCPサーバーURL:
```
https://api.utage-system.com/mcp
```

**Claude Code（`.mcp.json`）**:
```json
{
  "mcpServers": {
    "utage-api": {
      "url": "https://api.utage-system.com/mcp"
    }
  }
}
```

**claude.ai（ブラウザ版）**:
1. 画面左下 **カスタマイズ** → **コネクター** → **+** → **カスタムコネクターを追加**
2. URL に `https://api.utage-system.com/mcp` を入力
3. UTAGEのログイン/認可画面で認証

---

### モードB: REST API直接利用（Cursor / Antigravity 推奨）

> ⚠️ **Cursorでは現時点（2026-04）でUTAGE MCPのOAuth認証が動作しません。**  
> Streamable HTTP MCP + OAuth のフローがCursorの実装と噛み合わない既知の問題です。  
> **REST API方式（UTAGE_API_KEY）を使ってください。**

`.env` に `UTAGE_API_KEY` を設定済みであれば、追加設定は不要です。  
AIが各 `SKILL.md` のcurlサンプルを参照して直接REST APIを呼び出します。

```bash
# 動作確認
source .env
curl -s "https://api.utage-system.com/v1/funnels" \
  -H "Authorization: Bearer $UTAGE_API_KEY" | python3 -m json.tool | head -20
```

レスポンスが返ればセットアップ完了です。


---

## Step 4: 動作確認

ルートの SKILL.md を読み込んで「UTAGEのファネル一覧を取得して」と指示してみてください。
