import openai
import os
import json
import pandas as pd
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
What are the best Nike running shoe models for beginners? 
Respond **only** in JSON using the exact schema below. Include **all sources** where each shoe is available (official Nike site, marketplaces, online retailers, etc.). Use short URLs (domain + main slug — no query parameters) and **verify** each link returns HTTP status 200.

[
  {
    "model": "<model name>",
    "brand": "Nike",
    "link": "<short URL>",
    "source": "<site or marketplace>",
    "valid": true
  },
  …
]
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=400,
    temperature=0.1,
)

raw = response.choices[0].message["content"].strip()
start, end = raw.find("["), raw.rfind("]") + 1
json_str = raw[start:end]

try:
    data = json.loads(json_str)
except json.JSONDecodeError:
    print("❌ Failed to parse JSON from the LLM response:")
    print(raw)
    exit(1)

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

domains = [urlparse(item.get("link", "")).netloc for item in data if item.get("link")]
total = len(domains)

if total == 0:
    print("⚠️ No valid links found in JSON.")
    df = pd.DataFrame(columns=["domain", "percentage"])
else:
    counts = {d: domains.count(d) for d in set(domains)}
    df = pd.DataFrame({
        "domain": list(counts.keys()),
        "percentage": [counts[d] / total * 100 for d in counts]
    })

df.to_csv("domain_percentages.csv", index=False)

print("✅ output.json saved (all items)")
print("✅ domain_percentages.csv saved (percentage by domain)")
print(df.to_string(index=False))
