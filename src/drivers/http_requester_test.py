from .http_requester import HttpResquester

def test_request_from_page(requests_mock):
    url = 'http://web.archive.org/web/20200329014303/https://www.nga.gov/collection/artists.html'

    res_con = '<h1>Hello World!</h1>'

    requests_mock.get(url, status_code=200, text=res_con)
    http_requester = HttpResquester()
    req_res = http_requester.request_from_page()

    assert 'status_code' in req_res
    assert 'html' in req_res
    assert req_res['status_code'] == 200
    assert req_res['html'] == res_con