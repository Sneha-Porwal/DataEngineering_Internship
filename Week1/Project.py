import requests
import pandas as pd

# Fetch posts and comments
posts = pd.DataFrame(requests.get("https://dummyjson.com/posts").json()["posts"])
comments = pd.DataFrame(requests.get("https://dummyjson.com/comments").json()["comments"])

# Ensure IDs are integers for safe merging
posts["id"] = posts["id"].astype(int)
comments["postId"] = comments["postId"].astype(int)

# Count comments per post
comment_counts = comments.groupby("postId").size().reset_index(name="comment_count")

# Merge posts with comment counts
result = pd.merge(
    posts,
    comment_counts,
    left_on="id",
    right_on="postId",
    how="left"
).fillna(0)

# Keep required columns and rename
result = result[["id", "title", "comment_count"]].rename(columns={"id": "post_id"})

# Save to CSV
result.to_csv("posts_with_comment_counts.csv")

print("posts_with_comment_counts.csv created")
print(result)
