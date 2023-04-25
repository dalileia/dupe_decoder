# import os

# class PyHelperConfig(object):
    
#     if os.environ.get('ENV_PRODUCTION', '') == 'yes':
#         DEBUG = False
#         DEBUG_TB_ENABLED = False
#         DEBUG_TB_INTERCEPT_REDIRECTS = False
#     else:
#         DEBUG = True
#         DEBUG_TB_ENABLED = True
#         DEBUG_TB_INTERCEPT_REDIRECTS = False
    
#     ENV_MYSQL_HOST = os.environ.get('ENV_MYSQL_HOST', '')
#     ENV_MYSQL_USER = os.environ.get('ENV_MYSQL_USER', '')
#     ENV_MYSQL_PASSWORD = os.environ.get('ENV_MYSQL_PASSWORD', '')
#     ENV_MYSQL_PORT = os.environ.get('ENV_MYSQL_PORT', '')
    