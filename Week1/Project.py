import requests
import pandas as pd
class PostCommentProcessor:
    def __init__(self):
        self.posts_url = "https://dummyjson.com/posts"
        self.comments_url = "https://dummyjson.com/comments"
        self.output_file = "posts_with_comment_counts.csv"

    def fetch_posts(self):
        return pd.DataFrame(
            requests.get(self.posts_url).json()["posts"]
        )

    def fetch_comments(self):
        return pd.DataFrame(
            requests.get(self.comments_url).json()["comments"]
        )

    def process(self):
        posts = self.fetch_posts()
        comments = self.fetch_comments()

        posts["id"] = posts["id"].astype(int)
        comments["postId"] = comments["postId"].astype(int)

        #Merge posts with comment counts
        comment_counts = (comments.groupby("postId").size().reset_index(name="comment_count"))
        result = ( pd.merge(posts,comment_counts,left_on="id",right_on="postId",how="left").fillna(0)
            [["id", "title", "comment_count"]].rename(columns={"id": "post_id"})
        )

        result.to_csv(self.output_file, index=False)            #remove row number
        print("Processing completed successfully")
        print("Output file:", self.output_file)
        print("Total records:", len(result))
        print(result)

processor = PostCommentProcessor()
processor.process()
