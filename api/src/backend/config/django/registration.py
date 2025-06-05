from config.env import env

# User registration settings
DISABLE_SIGNUP = env.bool("DISABLE_SIGNUP", default=False)
