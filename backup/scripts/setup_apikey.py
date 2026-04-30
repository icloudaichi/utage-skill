#!/usr/bin/env python3
"""
UTAGE API キーのセットアップスクリプト

APIキーを ~/.utage-mcp-guide/.env に安全に保存します。
プロジェクトフォルダ内には保存しません（Git誤アップロード防止）。

使い方:
  python3 backup/scripts/setup_apikey.py
"""

import os
import sys
from pathlib import Path

CONFIG_DIR = Path.home() / ".utage-mcp-guide"
ENV_FILE = CONFIG_DIR / ".env"


def main():
    print("=" * 50)
    print("  UTAGE API キー セットアップ")
    print("=" * 50)
    print()
    print("APIキーは以下の場所に保存されます:")
    print(f"  📁 {ENV_FILE}")
    print()
    print("⚠️  プロジェクトフォルダ内には保存しません。")
    print("    Git等で誤ってアップロードされるリスクを防ぎます。")
    print()

    # 既存の設定を確認
    existing_key = ""
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("UTAGE_API_KEY=") and not line.startswith("#"):
                existing_key = line.split("=", 1)[1].strip()
                break

    if existing_key:
        masked = existing_key[:4] + "*" * (len(existing_key) - 8) + existing_key[-4:]
        print(f"✅ 既存のAPIキーが見つかりました: {masked}")
        print()
        choice = input("上書きしますか？ (y/N): ").strip().lower()
        if choice != "y":
            print("キャンセルしました。")
            return

    print()
    print("─" * 50)
    print("APIキーの取得方法:")
    print("  1. UTAGEの管理画面にログイン")
    print("  2. 左メニュー → [API設定]")
    print("  3. APIキーをコピー")
    print("─" * 50)
    print()

    api_key = input("APIキーを入力してください: ").strip()

    if not api_key:
        print("❌ APIキーが入力されませんでした。")
        sys.exit(1)

    # ディレクトリ作成
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    # .env ファイルを書き込み（既存の他の設定は保持）
    env_lines = []
    key_written = False

    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("UTAGE_API_KEY="):
                env_lines.append(f"UTAGE_API_KEY={api_key}")
                key_written = True
            else:
                env_lines.append(line)

    if not key_written:
        env_lines.append(f"# UTAGE REST API キー")
        env_lines.append(f"# 取得方法: UTAGE管理画面 > API設定")
        env_lines.append(f"UTAGE_API_KEY={api_key}")

    ENV_FILE.write_text("\n".join(env_lines) + "\n")

    # パーミッション設定（owner のみ読み書き可能）
    ENV_FILE.chmod(0o600)

    print()
    print(f"✅ APIキーを保存しました: {ENV_FILE}")
    print(f"   パーミッション: 600 (owner のみ読み書き可)")
    print()
    print("次のステップ:")
    print("  python3 backup/scripts/backup_funnels.py")
    print()


if __name__ == "__main__":
    main()
