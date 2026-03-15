import pytest
import sys

# Path to HTML report
report_file = "Pytest-Report-Print-Testing-Automation.html"

# Pytest arguments
pytest_args = [
    "test_print.py",  # test file
    "-v",             # verbose
    "--html=" + report_file,
    "--self-contained-html",  # include styles in HTML
]

# Run pytest
exit_code = pytest.main(pytest_args)

if exit_code == 0:
    print("\n✅ All tests passed successfully!")
else:
    print("\n❌ Some tests failed. Check the HTML report:", report_file)

# Exit with pytest code (important for CI)
sys.exit(exit_code)