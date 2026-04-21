# UTAGE MCP Guide - セットアップ

VS Codeフォーク系IDE（Cursor・Antigravity・Windsurf等）でUTAGE MCPサーバーに接続するためのガイドです。

> **Claude（Claude Code / claude.ai）をお使いの方へ**  
> Claudeは公式でUTAGE MCPに対応しています。  
> → 公式ドキュメント: [docs.utage-system.com](https://docs.utage-system.com)  
> このガイドの落とし穴集（ルートの SKILL.md）は Claude でもそのまま活用できます。

---

## Step 1: MCPサーバーを設定する

VS Codeフォーク系IDEはOAuthブラウザフローを直接サポートしないため、`mcp-remote` をプロキシとして使用します。  
**前提**: Node.js v18以上（npx）がインストール済みであること

使用するIDEに合わせて、以下の設定ファイルに追記してください。

| IDE | 設定ファイル |
|:---|:---|
| Cursor | `~/.cursor/mcp.json` |
| Antigravity | `~/.gemini/antigravity/mcp_config.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |

```json
{
  "mcpServers": {
    "utage-api": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.utage-system.com/mcp"
      ]
    }
  }
}
```

設定後にIDEを再起動すると、**初回のみブラウザでUTAGEのOAuth認証画面が開きます**。  
認証完了後はトークンが自動キャッシュされ、次回以降は再認証不要です。

---

## Step 2: 動作確認

IDEを再起動後、AIに以下のように指示してみてください：

> 「UTAGEのファネル一覧を取得して」

ファネル一覧が返ればセットアップ完了です。

---

## トークン失効時の再認証

認証エラーが発生した場合は以下を実行してからIDEを再起動してください：

```bash
rm -rf ~/.mcp-auth/
```

---

## 補足: REST API直接利用（任意）

MCPを使わずREST APIで直接操作したい場合は、`.env` に `UTAGE_API_KEY` を設定します。

```bash
cp .env.example .env
# .env を開いて UTAGE_API_KEY を設定
```

```bash
# 疎通確認
source .env
curl -s "https://api.utage-system.com/v1/funnels" \
  -H "Authorization: Bearer $UTAGE_API_KEY" | python3 -m json.tool | head -20
```
