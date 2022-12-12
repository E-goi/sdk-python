# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from egoi_api.paths.webhooks_webhook_id import Api

from egoi_api.paths import PathValues

path = PathValues.WEBHOOKS_WEBHOOK_ID