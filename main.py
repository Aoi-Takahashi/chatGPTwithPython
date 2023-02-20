# chatGPTのPython Scriptコード
import time
import openai


# APIキーを設定
openai.api_key = "YOUR_API_KEY"

# GPTのIDを設定
model_engine = "davinci"  # GPT-3を使う場合は"davinci"を指定

# プロンプトを設定
prompt = "Hello, how are you?"

# GPTにプロンプトを送信して回答を取得する
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

# 回答を表示する
print(response.choices[0].text)

# APIのレートリミットに達した場合に備えて、適切な時間を待つ
if "seconds" in response.get("choices")[0]["finish_reason"]:
    time.sleep(response.choices[0].get("estimated_completion_seconds"))
