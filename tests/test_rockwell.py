import httpretty
from freezegun import freeze_time
from rockwell import watch, judge


@httpretty.activate
def test_watch_site_ok():
    url = "http://example-ok.com"
    httpretty.register_uri(httpretty.GET, url, status=200)

    assert watch(url) == 200


@httpretty.activate
def test_watch_site_acceptable_redirect():
    url = "http://example-acceptable-redirect.com"
    httpretty.register_uri(httpretty.GET, url, status=302)

    assert watch(url) == 302


@freeze_time("2015-10-31 13:00:00", tz_offset=4)
def test_judge_site_ok():
    status_code = 200

    assert judge(status_code) == {"status": "up",
                                  "timestamp": "2015-10-31 13:00"}


@freeze_time("2015-10-31 13:00:00", tz_offset=4)
def test_judge_site_acceptable_redirect():
    status_code = 302

    assert judge(status_code) == {"status": "up",
                                  "timestamp": "2015-10-31 13:00"}


@freeze_time("2015-10-31 13:00:00", tz_offset=4)
def test_judge_site_down():
    status_codes = (i for i in range(400, 600))
    for status_code in status_codes:
        assert judge(status_code) == {"status": "down",
                                      "timestamp": "2015-10-31 13:00"}

