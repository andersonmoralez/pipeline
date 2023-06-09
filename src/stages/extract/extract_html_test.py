from src.drivers.http_requester import HttpResquester
from src.drivers.html_collector import HtmlCollector
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError
from .extract_html import ExtractHtml

def test_extract():
    http_requester = HttpResquester()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)

    res = extract_html.extract()
    print()
    print(res)

    assert isinstance(res, ExtractContract)

def test_extract_error():
    http_requester = 'GerarErro'
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        extract_html.extract()
    except Exception as exception: # pylint: disable=broad-except
        assert isinstance(exception, ExtractError)
