import tweepy

# 取得した各種キーを代入
CK="<Consumer Key>"
CS="<Consumer Secret>"
AT="<Access Token>"
AS="<Access Token Secret>"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# 好きな言葉をツイート
#api.update_status("Pythonから投稿!")
