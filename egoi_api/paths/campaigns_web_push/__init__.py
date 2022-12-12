# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from egoi_api.paths.campaigns_web_push import Api

from egoi_api.paths import PathValues

path = PathValues.CAMPAIGNS_WEBPUSH