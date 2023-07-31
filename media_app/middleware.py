from datetime import datetime


def requests_per_session(get_response):
    def middleware(request):
        print("requests_per_session is called during the request")
        if 'request_count' not in request.session:
            request.session['request_count'] = 1
        else:
            request.session['request_count'] += 1
        print(f"Request count is {request.session.get('request_count',0)}")

        print(f"HTTP X {request.META.get('HTTP_X_FORWARDED_FOR')}")
        start = datetime.now()
        response = get_response(request)
        print(f"Response - {dir(response)}")
        end = datetime.now()

        print(f"The request took {end - start}")
        print("requests_per_session is called during the response")
        return response
    return middleware
