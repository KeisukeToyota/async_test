import responder
import random

api = responder.API(
    cors=True,
    allowed_hosts=["*"]
)


@api.route('/')
async def hello(req, resp):
    resp.media = {
        'text': random.random()
    }


if __name__ == '__main__':
    api.run()
