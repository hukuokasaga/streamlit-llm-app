import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# 環境変数の読み込み
load_dotenv()

def get_llm_response(user_input: str, expert_type: str) -> str:
    """
    ユーザーの入力と専門家タイプを受け取り、LLMからの回答を返す関数
    
    Args:
        user_input (str): ユーザーからの入力テキスト
        expert_type (str): 専門家の種類
    
    Returns:
        str: LLMからの回答
    """
    try:
        # 専門家タイプに応じたシステムメッセージの設定
        system_messages = {
            "健康・医療アドバイザー": "あなたは健康・医療に関する専門家です。安全で科学的根拠のあるアドバイスを提供してください。ただし、具体的な診断や治療法の指示は避け、必要に応じて医療機関の受診を勧めてください。",
            "プログラミング・技術顧問": "あなたはプログラミングと技術に関する専門家です。初心者にも分かりやすく、実践的なアドバイスやコード例を提供してください。ベストプラクティスも含めて回答してください。",
            "キャリア・人生相談顧問": "あなたはキャリアと人生設計に関する専門家です。相談者の状況を理解し、建設的で実現可能なアドバイスを提供してください。多様な価値観を尊重した回答を心がけてください。",
            "財務・投資アドバイザー": "あなたは財務と投資に関する専門家です。リスクを適切に説明し、個人の状況に応じた堅実なアドバイスを提供してください。投資はリスクを伴うことを必ず伝えてください。"
        }
        
        # ChatOpenAIインスタンスの作成（Lesson8を参考）
        llm = ChatOpenAI(
            model_name="gpt-4o-mini",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # メッセージの作成（Lesson8のパターンを使用）
        messages = [
            SystemMessage(content=system_messages[expert_type]),
            HumanMessage(content=user_input)
        ]
        
        # LLMからの回答取得
        result = llm.invoke(messages)
        return result.content
    
    except Exception as e:
        error_msg = str(e)
        if "api_key" in error_msg.lower():
            return "❌ APIキーに関するエラーが発生しました。APIキーが正しく設定されているか確認してください。"
        elif "rate limit" in error_msg.lower():
            return "⏰ API使用制限に達しました。しばらく待ってから再試行してください。"
        elif "authentication" in error_msg.lower():
            return "🔐 認証エラーが発生しました。APIキーが有効か確認してください。"
        else:
            return f"❌ エラーが発生しました: {error_msg}"

def main():
    # ページ設定
    st.set_page_config(
        page_title="AI専門家相談アプリ",
        page_icon="🤖",
        layout="wide"
    )
    
    # タイトル
    st.title("🤖 AI専門家相談アプリ")
    
    # アプリの概要説明
    st.markdown("""
    ## 📋 アプリの概要
    このアプリは、LangChainとOpenAI GPTを活用した専門家相談システムです。
    4つの異なる専門分野から選択して、AIによる専門的なアドバイスを受けることができます。
    
    ## 🚀 使い方
    1. **専門家を選択**: 下のラジオボタンから相談したい分野の専門家を選んでください
    2. **質問を入力**: テキストエリアに相談内容や質問を入力してください
    3. **回答を取得**: 「相談する」ボタンをクリックして、AI専門家からの回答を受け取ってください
    
    ## ⚠️ 注意事項
    - このアプリの回答は参考情報として提供されます
    - 医療に関する質問の場合、必要に応じて医療機関にご相談ください
    - 投資に関するアドバイスにはリスクが伴いますので、十分にご検討ください
    """)
    
    st.divider()
    
    # サイドバーで専門家選択
    with st.sidebar:
        st.header("🎯 専門家の選択")
        expert_type = st.radio(
            "相談したい専門家を選んでください:",
            [
                "健康・医療アドバイザー",
                "プログラミング・技術顧問", 
                "キャリア・人生相談顧問",
                "財務・投資アドバイザー"
            ]
        )
        
        # 選択した専門家の説明
        expert_descriptions = {
            "健康・医療アドバイザー": "💊 健康管理、症状の理解、予防法などについてアドバイスします",
            "プログラミング・技術顧問": "💻 プログラミング、技術的な問題解決、ベストプラクティスについて支援します",
            "キャリア・人生相談顧問": "🎯 キャリア設計、人生の悩み、目標達成について相談に乗ります",
            "財務・投資アドバイザー": "💰 資産管理、投資戦略、財務計画についてアドバイスします"
        }
        
        st.info(expert_descriptions[expert_type])
    
    # メインコンテンツ
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(f"📝 {expert_type}への相談")
        
        # 入力フォーム
        user_input = st.text_area(
            "相談内容を入力してください:",
            height=200,
            placeholder="ここに質問や相談内容を入力してください..."
        )
        
        # 送信ボタン
        if st.button("🚀 相談する", type="primary", use_container_width=True):
            if user_input.strip():
                with st.spinner("AI専門家が回答を準備中..."):
                    response = get_llm_response(user_input, expert_type)
                    st.session_state.response = response
                    st.session_state.user_question = user_input
                    st.session_state.selected_expert = expert_type
            else:
                st.warning("相談内容を入力してください。")
    
    with col2:
        st.subheader("💬 AI専門家からの回答")
        
        # 回答の表示
        if hasattr(st.session_state, 'response'):
            st.markdown("### 📋 あなたの質問:")
            st.info(st.session_state.user_question)
            
            st.markdown(f"### 🎯 {st.session_state.selected_expert}からの回答:")
            st.success(st.session_state.response)
        else:
            st.info("左側のフォームから質問を送信すると、ここに回答が表示されます。")
    
    # フッター
    st.divider()
    st.markdown("""
    ---
    **🔧 技術仕様:**
    - **フレームワーク**: Streamlit
    - **AI モデル**: OpenAI GPT-4o-mini
    - **ライブラリ**: LangChain, python-dotenv
    
    **⚙️ 開発者向け情報:**
    - OpenAI APIキーが必要です（環境変数 `OPENAI_API_KEY` で設定）
    - `.env` ファイルまたは Streamlit Secrets で API キーを設定してください
    """)

if __name__ == "__main__":
    # APIキーの確認
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ OpenAI APIキーが設定されていません。環境変数 `OPENAI_API_KEY` を設定してください。")
        st.stop()
    elif api_key == "your_openai_api_key_here":
        st.error("⚠️ OpenAI APIキーがデフォルト値のままです。実際のAPIキーに変更してください。")
        st.stop()
    else:
        # APIキーが設定されていることを確認（最初の10文字のみ表示）
        st.sidebar.success(f"✅ APIキー設定済み: {api_key[:10]}...")
    
    main()