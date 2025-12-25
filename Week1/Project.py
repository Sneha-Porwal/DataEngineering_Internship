import requests
import pandas as pd

# Fetch data
posts = pd.DataFrame(requests.get("https://dummyjson.com/posts").json()["posts"])
comments = pd.DataFrame(requests.get("https://dummyjson.com/comments").json()["comments"])

# Count comments per post
comment_counts = comments.groupby("postId").size().reset_index(name="comment_count")

# Merge posts with comment counts
result = posts.merge(comment_counts, left_on="id", right_on="postId", how="left").fillna(0)

# Keep only required columns
result = result[["id", "title", "comment_count"]]
result.rename(columns={"id": "post_id"}, inplace=True)

# Save to CSV
result.to_csv("posts_with_comment_counts.csv", index=False)

print("posts_with_comment_counts.csv created")
print(result)
