# 🤖 AI専門家相談アプリ

LangChainとOpenAI GPTを活用した専門家相談システムです。4つの異なる専門分野から選択して、AIによる専門的なアドバイスを受けることができます。

## ✨ 機能

- **4つの専門分野**: 健康・医療、プログラミング・技術、キャリア・人生相談、財務・投資
- **インタラクティブUI**: Streamlitによる使いやすいWebインターフェース
- **LangChain統合**: Lesson8で学習したLangChainのパターンを活用
- **レスポンシブデザイン**: デスクトップとモバイルに対応

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-username/streamlit-llm-app.git
cd streamlit-llm-app
```

### 2. 仮想環境の作成と有効化

```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

`.env.example` をコピーして `.env` ファイルを作成し、OpenAI APIキーを設定してください。

```bash
cp .env.example .env
```

`.env` ファイルを編集:
```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 5. アプリケーションの起動

```bash
streamlit run app.py
```

## 🌐 Streamlit Community Cloudでのデプロイ

1. このリポジトリをGitHubにプッシュ
2. [Streamlit Community Cloud](https://share.streamlit.io/) にアクセス
3. 「New app」をクリックしてリポジトリを選択
4. Secretsに `OPENAI_API_KEY` を設定
5. デプロイを実行

## 📋 使い方

1. **専門家を選択**: サイドバーから相談したい分野の専門家を選択
2. **質問を入力**: メインエリアのテキストボックスに相談内容を入力
3. **回答を取得**: 「相談する」ボタンをクリックして回答を受け取る

## 🎯 専門家の種類

- **健康・医療アドバイザー**: 健康管理、症状の理解、予防法
- **プログラミング・技術顧問**: プログラミング、技術的問題解決
- **キャリア・人生相談顧問**: キャリア設計、人生の悩み相談
- **財務・投資アドバイザー**: 資産管理、投資戦略、財務計画

## 🔧 技術スタック

- **Python 3.11**
- **Streamlit 1.41.1**
- **LangChain 1.0.0**
- **OpenAI API 2.5.0**
- **python-dotenv 1.1.1**

## ⚠️ 注意事項

- このアプリの回答は参考情報として提供されます
- 医療に関する質問の場合、必要に応じて医療機関にご相談ください
- 投資に関するアドバイスにはリスクが伴いますので、十分にご検討ください
- OpenAI APIの使用には料金が発生する場合があります

## 📝 ライセンス

MIT License