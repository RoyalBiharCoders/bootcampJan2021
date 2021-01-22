#Designing a simple social network where user posted two posts i.e. post1 and post2 having likes and comments as 12, 2 and 32, 3 respectively. Finally, we will print all details for post2 and 2nd comment of post2

post1Comment = ["wow", "nice"]
post2Comment = ["super", "you are amazing", "kab gaye waha?"]

myPosts = {"post1": {"likes": 12, "comment":2, "comment_list": post1Comment}, "post2": {"likes": 32, "comment":3, "comment_list": post2Comment}}

all_details_post_2 = myPosts["post2"]
print(all_details_post_2)

second_Comment_from_post2 = myPosts["post2"]["comment_list"][1]
print(second_Comment_from_post2)