
class POst:
    post_id = str
    title = str
    content = str
    author = "user"
    created_at = str 
    updated_at = str
    tags = str
    
    class Comment:
        comment_id = str
        post = str
        author = "user"
        created_at = str
        updated_at = str