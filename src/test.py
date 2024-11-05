import json
import re 

res = '```json\n{\n  "model_name": "书生浦语InternLM2.5",\n  "developer": "上海人工智能实验室",\n  "parameter_versions": [1.8B, 7B, 20B],\n  "context_length": 1M\n}\n```'
aa = res.strip("```json\n").strip("```")
res_aa = json.dumps(aa)
res_aa_json = json.loads(res_aa)
print(res_aa_json)

start_index = res.find('{') 
end_index = res.find('}')+1

result = res[start_index:end_index]

res_relt = json.dumps(result)
res_relt_json = json.loads(res_relt)
print(res_relt_json)



res = res[res.find('{') : res.find('}')+1]

res_dps = json.dumps(res)
res_json = json.loads(res_dps)

print(res_json)