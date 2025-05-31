import unittest
import os
from datetime import datetime
from BeautifulReport import BeautifulReport as bf

@staticmethod
def all_cases():
    current_time = datetime.now().strftime("%Y-%m-%d-%H%M-S")
    file_name = f"{current_time}-TestReport.html"

    case_path = os.path.join(os.getcwd(),"tests")
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    bf(discover).report(filename=file_name, description='testReport', report_dir='res/report')


if __name__ == "__main__":
    all_cases()