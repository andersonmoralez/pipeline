from .http_requester import HttpResquester

def test_request_from_page():
    http_requester = HttpResquester()
    req_res = http_requester.request_from_page()
    print()
    print(req_res)
