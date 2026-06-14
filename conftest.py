# Takes a picture when test fails
import os
import pytest

@pytest.hookimpl(tryfirst = True, hookwrapper = True)
def pytest_runtest_makereport(item, call):

    # Grabs result
    outcome = yield
    report = outcome.get_result()

    # Checks if test failed during its execution
    if report.when == "call" and report.failed:

        # Checks if test was using the browser
        if "page" in item.fixturenames:
            page = item.funcargs["page"]

            # Creates a folder named 'screenshots' if it doesnt exist yet
            os.makedirs("screenshots", exist_ok  = True)

            # Creates a filename using the test's name
            filename = f"screenshots/{item.name}.png"

            # Takes the screenshot
            page.screenshot(path = filename)