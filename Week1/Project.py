import requests
import pandas as pd

# Fetch posts
posts = requests.get("https://dummyjson.com/posts").json()["posts"]

# Fetch comments
comments = requests.get("https://dummyjson.com/comments").json()["comments"]

# Count comments per post
count = {}
for c in comments:
    pid = c["postId"]
    count[pid] = count.get(pid, 0) + 1

# Prepare final data
data = []
for p in posts:
    data.append([p["id"], p["title"], count.get(p["id"], 0)])

# Save to CSV
df = pd.DataFrame(data, columns=["post_id", "title", "comment_count"])
df.to_csv("posts_with_comment_counts.csv", index=False)

print("posts_with_comment_counts.csv created")
print(df)
