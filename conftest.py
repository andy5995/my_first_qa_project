import pytest
import os

os.makedirs("screenshots", exist_ok=True)


# capture test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# screenshot on failure
@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield

    failed = getattr(request.node, "rep_call", None)
    failed = failed and failed.failed

    if failed:
        page.screenshot(
            path=f"screenshots/{request.node.name}.png",
            full_page=True
        )