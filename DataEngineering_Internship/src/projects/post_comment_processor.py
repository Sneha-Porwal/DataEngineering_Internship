import pandas as pd
from src.common.api_client import get_json


class PostCommentProcessor:
    POSTS_URL = "https://dummyjson.com/posts"
    COMMENTS_URL = "https://dummyjson.com/comments"

    def __init__(self, output_path):
        self.output_path = output_path

    def fetch_posts(self):
        return pd.DataFrame(get_json(self.POSTS_URL)["posts"])

    def fetch_comments(self):
        return pd.DataFrame(get_json(self.COMMENTS_URL)["comments"])

    def process(self):
        posts = self.fetch_posts()
        comments = self.fetch_comments()

        comment_counts = (
            comments.groupby("postId")
            .size()
            .reset_index(name="comment_count")
        )

        result = (
            posts.merge(comment_counts, left_on="id", right_on="postId", how="left")
            .fillna(0)[["id", "title", "comment_count"]]
            .rename(columns={"id": "post_id"})
        )

        result.to_csv(self.output_path, index=False)
        return result


if __name__ == "__main__":
    processor = PostCommentProcessor(
        "data/processed/posts_with_comment_counts.csv"
    )
    df = processor.process()
    print(df.head())
