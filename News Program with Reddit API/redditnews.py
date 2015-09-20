import praw

agent = praw.Reddit(user_agent = 'Reddit_News_Application')
articleLimit = int(input("Limit of articles (More articles = More time): "))
articles = agent.get_subreddit('news').get_hot(limit = articleLimit)
f = open('news.txt', 'w')

print("\n" + "Articles:" + "\n")

for x in articles:
    print(str(x) + "\n" + x.url + "\n")
    f.write(str(x) + "\n")

f.close()
