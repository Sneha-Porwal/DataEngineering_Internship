import requests
import pandas as pd


class PostCommentProcessor:
    def run(self):
        posts = pd.DataFrame(requests.get("https://dummyjson.com/posts").json()["posts"])
        comments = pd.DataFrame(requests.get("https://dummyjson.com/comments").json()["comments"])

        posts["id"] = posts["id"].astype(int)
        comments["postId"] = comments["postId"].astype(int)

        comment_counts = comments.groupby("postId").size().reset_index(name="comment_count")

        result = pd.merge(
            posts,
            comment_counts,
            left_on="id",
            right_on="postId",
            how="left"
        ).fillna(0)

        result = result[["id", "title", "comment_count"]].rename(columns={"id": "post_id"})

        result.to_csv("posts_with_comment_counts.csv")

        print("posts_with_comment_counts.csv created")
        print(result)

processor = PostCommentProcessor()

# Call method using the object
processor.run()
