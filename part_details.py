import os
import pandas as pd
import requests
from runtime_keys import api_url, bearer

INPUT_FILE = "input.xlsx"
OUTPUT_FILE = "output.csv"

def headers():
    return {
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {bearer()}",
        "user-agent": "Mozilla/5.0"
    }

def run():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    df = pd.read_excel(INPUT_FILE)
    searches = df["part"].dropna().astype(str).tolist()

    for s in searches:
        try:
            r = requests.get(
                api_url(),
                headers=headers(),
                params={
                    "categoryId": 3,
                    "ipAddress": "",
                    "fromSearchButton": "true",
                    "search": s
                },
                timeout=30
            )

            if r.status_code != 200:
                continue

            rows = []
            for item in r.json():
                qty = part = None
                for sp in item.get("specs", []):
                    if sp.get("key") == "qty":
                        qty = sp.get("value")
                    elif sp.get("key") == "partNumber":
                        part = sp.get("value")

                rows.append({
                    "input_search": s,
                    "vendor": item.get("companyName"),
                    "phone": item.get("contactPhoneNumber") or item.get("branchNumber"),
                    "brand": item.get("brandName"),
                    "part": part,
                    "desc": item.get("description"),
                    "qty": qty,
                    "price": item.get("price") or "Call"
                })

            if rows:
                pd.DataFrame(rows).to_csv(
                    OUTPUT_FILE,
                    mode="a",
                    header=not os.path.exists(OUTPUT_FILE),
                    index=False
                )

        except Exception:
            continue

if __name__ == "__main__":
    run()
