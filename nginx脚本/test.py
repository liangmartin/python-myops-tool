import json

with open('nginx.log', 'r', encoding='utf-8') as f:
    # 逐行读取文件
    for line in f:
        try:
            # 解析每行中包含的 JSON 对象
            log_json = json.loads(line)
            pretty_log = json.dumps(log_json, indent=4, ensure_ascii=False)
            print(pretty_log)
        except json.decoder.JSONDecodeError as e:
            # 处理当前行无法解析为JSON对象的问题
            print(f'{e}: {line}')
