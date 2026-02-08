import json
import random
import time
import pandas as pd
from datetime import datetime, timedelta

# --- SETTINGS ---
PROJECT_ID = "your-gcp-project-id" # Change this to your project ID
TOPIC_ID = "order-stream-raw"

# 1. GENERATE BATCH DATA (Users for SCD Type 2)
def generate_batch_users(n=50):
    users = []
    for i in range(n):
        users.append({
            "user_id": f"USER_{100 + i}",
            "name": f"Customer_{i}",
            "email": f"user_{i}@example.com",
            "address": random.choice(["New York", "London", "Tokyo", "Berlin"]),
            "updated_at": (datetime.now() - timedelta(days=1)).isoformat()
        })
    df = pd.DataFrame(users)
    df.to_csv("users_batch.csv", index=False)
    print("✅ Created users_batch.csv for the Batch/SCD layer.")

# 2. GENERATE STREAMING DATA (Live Orders)
def stream_orders():
    # Use dummy client if not connected to GCP yet for testing
    print("🚀 Starting Stream... (Press Stop to end)")
    try:
        while True:
            order = {
                "order_id": f"ORD_{random.randint(1000, 9999)}",
                "user_id": f"USER_{random.randint(100, 149)}",
                "product_id": random.choice(["PROD_A", "PROD_B", "PROD_C"]),
                "amount": round(random.uniform(10.5, 500.0), 2),
                "timestamp": datetime.utcnow().isoformat()
            }
            print(f"📡 Sending: {order}")
            # After you setup GCP, uncomment the lines below to send to Pub/Sub
            # publisher.publish(topic_path, json.dumps(order).encode("utf-8"))
            time.sleep(2) 
    except KeyboardInterrupt:
        print("🛑 Stream stopped.")

generate_batch_users()
stream_orders()