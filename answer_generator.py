from api_config import client, MODEL_NAME
from langchain.prompts import PromptTemplate

answer_prompt = PromptTemplate(template="根据以下用户问题和数据库查询结果生成回答：问题：{user_question} 结果：{query_results}")

def generate_answer(user_question, query_results):
    prompt = answer_prompt.format(user_question=user_question, query_results=query_results)
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    answer = completion.choices[0].message.content
    print(f"[Answer Generator] 使用的输入: {user_question}, 查询结果: {query_results}")  # 增加日志记录
    print(f"[Answer Generator] 生成的回答: {answer}")  # 记录生成的回答
    return answer