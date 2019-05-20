class Config(object):
    db = "mysql+pymysql://USERNAME:PASSWD@HOST:3306/DATABASE"
    #for docker use
    # db = "mysql+pymysql://Username:password@host.docker.internal:3306/DATABASE"

    jwt_secret = "ITS_A_SECRET"
    jwt_expire_time = 30*60 # 5 minute