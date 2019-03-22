import responder
import random
import time

api = responder.API(
    cors=True,
    allowed_hosts=["*"]
)


@api.route('/')
async def index(req, resp):
    resp.media = {
        'text': random.random()
    }


@api.route('/hello')
async def hello(req, resp):

    @api.background.task
    def sleep_func(data):
        time.sleep(int(data['n']))
        print(data['n'])

    data = await req.media()

    sleep_func(data)

    resp.media = {
        'n': int(data['n']) + 1
    }


if __name__ == '__main__':
    api.run()
