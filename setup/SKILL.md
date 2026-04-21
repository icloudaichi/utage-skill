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

## Step 3: MCPサーバー設定（AI CLIツール用）

UTAGEのMCPサーバーは **URLベースの接続**（Streamable HTTP）です。
`npx` コマンドは不要です。

### 接続URL

```
https://api.utage-system.com/mcp
```

認証は OAuth（UTAGEログイン + 認可画面）が自動で行われます。

---

### Claude Code（`.mcp.json`）

```json
{
  "mcpServers": {
    "utage-api": {
      "url": "https://api.utage-system.com/mcp"
    }
  }
}
```

ファイルの場所: プロジェクトルートの `.mcp.json`、またはグローバル設定

---

### claude.ai（ブラウザ版）

1. 画面左下 **カスタマイズ** → **コネクター** → **+** → **カスタムコネクターを追加**
2. URL に `https://api.utage-system.com/mcp` を入力
3. UTAGEのログイン画面が表示されるので認証・認可

---

### Cursor / Windsurf / その他（URLベース対応ツール）

各ツールのMCP設定でURLを指定:

```json
{
  "mcpServers": {
    "utage-api": {
      "url": "https://api.utage-system.com/mcp"
    }
  }
}
```

設定ファイルの場所:
- Cursor: `~/.cursor/mcp.json`
- Windsurf: `~/.codeium/windsurf/mcp_config.json`

---

### Antigravity（本スキルの想定環境）

MCPサーバーへの接続はAntigravityのMCP設定で行います。  
URLを `https://api.utage-system.com/mcp` に設定してください。  
→ 設定後、AIがMCPツール（`funnel_list` 等）を自動で呼び出せるようになります。


---

## Step 4: 動作確認

ルートの SKILL.md を読み込んで「UTAGEのファネル一覧を取得して」と指示してみてください。
