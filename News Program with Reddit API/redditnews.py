import praw

agent = praw.Reddit(user_agent = 'Reddit_News_Application')
articleLimit = int(input("Limit of articles (More articles = More time): "))
printToFile = input("Print output to file? ").lower()
articles = agent.get_subreddit('news').get_hot(limit = articleLimit)
f = open('news.txt', 'w')

print("\n" + "Articles:" + "\n")

for x in articles:
    print(str(x) + "\n")
    f.write(str(x) + "\n")

f.close()
