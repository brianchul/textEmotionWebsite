class Config(object):
    db_host = "HOST"
    db_port = "3306"
    db_account = "USERNAME"
    db_passwd = "PASSWD"
    db_database = "DATABASE"
    db = "mysql+pymysql://" + db_account + ":" + db_passwd + "@" + db_host+":"+db_port+ "/" + db_database
    
    #for docker use
    # db = "mysql+pymysql://Username:password@host.docker.internal:3306/DATABASE"

    jwt_secret = "ITS_A_SECRET"
    jwt_expire_time = 30*60 # 5 minute

    sentiment_key = "KEY"
    sentiment_url = 'https://japaneast.api.cognitive.microsoft.com'
    sentiment_path = '/text/analytics/v2.0/Sentiment'

    translate_key = "KEY"
    translate_base_url = 'https://api.cognitive.microsofttranslator.com'
    translate_path = '/translate?api-version=3.0'
    translate_params = '&to=en'