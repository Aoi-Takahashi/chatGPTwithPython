# chatGPTのPython Scriptコード
import time
import openai
import sys


# APIキーを設定
openai.api_key = "YOUR_API_KEY"

# GPTのIDを設定
model_engine = "davinci"  # GPT-3を使う場合は"davinci"を指定


def accept_question():
    question = input('Enter your question: ')
    return question


def send_question(question):
    # GPTにプロンプトを送信して回答を取得する
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=1024,  # You can change here to 2048.
        n=1,
        stop=None,
        temperature=0.5
    )
    # APIのレートリミットに達した場合に備えて、適切な時間を待つ
    if "seconds" in response.get("choices")[0]["finish_reason"]:
        time.sleep(response.choices[0].get("estimated_completion_seconds"))
    return response


def show_answer(response):
    print(response.choices[0].text)


def main():

    try:
        question = accept_question()
        answer = send_question(question)
        show_answer(answer)
    except openai.error.AuthenticationError:
        print("chatGPTのAPIキーがありません\nAPIキーを取得してください\nシステムを終了します")
        sys.exit()


if __name__ == "__main__":
    main()
