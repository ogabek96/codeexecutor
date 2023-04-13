import time


def stats_middleware(get_response):

    def middleware(request):
        start_time = time.time()

        response = get_response(request)

        duration = time.time() - start_time

        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)
        print("response time: ", int(duration * 1000))
        return response

    return middleware