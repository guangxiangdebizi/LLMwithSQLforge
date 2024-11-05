from api_config import client, MODEL_NAME
from langchain.prompts import PromptTemplate

sql_prompt = PromptTemplate(template="为以下问题生成一个SQL查询：{user_question}。请注意，你只能生成SQL语句，其余的内容一律不要给我返回！且确保你生成的SQL语句和用户输入的请求相匹配。确保输出给我的东西里面只有sql命令的纯文本，别的都不要。不要给我这种 ```sql xxxx ```格式的东西，我只要里面的命令行")
extract_sql_prompt = PromptTemplate(template="请从以下内容中提取有效的SQL查询语句：{llm_output}。请注意，你只能生成SQL语句，其余的内容一律不要给我返回！且确保你生成的SQL语句和用户输入的请求相匹配。确保输出给我的东西里面只有sql命令的纯文本，别的都不要。不要给我这种 ```sql xxxx ```格式的东西，我只要里面的命令行")

def generate_sql(user_question):
    # 第一次调用 LLM 生成可能包含描述的 SQL 查询
    prompt = sql_prompt.format(user_question=user_question)
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    llm_output = completion.choices[0].message.content
    print(f"[SQL Generator] 第一次 LLM 生成的输出: {llm_output}")  # 增加日志记录

    # 第二次调用 LLM 提取有效的 SQL 查询
    extract_prompt = extract_sql_prompt.format(llm_output=llm_output)
    extraction_completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": extract_prompt}],
        temperature=0.3
    )
    sql_query = extraction_completion.choices[0].message.content
    print(f"[SQL Generator] 提取后的 SQL 查询: {sql_query}")  # 增加日志记录
    return sql_query
