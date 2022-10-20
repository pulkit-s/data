"""This script has the tests for wfigs_data.py.
It imports two test datasets and checks if the processed output matches the
expected output.
"""
import unittest
import os
import pandas as pd
import sys
from datetime import datetime

module_dir_ = os.path.dirname(__file__)
sys.path.insert(0, module_dir_)
import wfigs_data

pd.set_option("display.max_rows", None)


def _GetTestPath(relative_path):
    return os.path.join(module_dir_, relative_path)


class PreprocessDataTest(unittest.TestCase):
    """This class has the method required to test preprocess_data script."""

    def test_ProcessDF(self):
        typeDict = {
            "FireCause": str,
            "FireCauseGeneral": str,
            "FireCauseSpecific": str,
            "POOFips": str
        }
        df = pd.read_csv(_GetTestPath("test_data/historical.csv"),
                         converters=typeDict)
        expected_df = pd.read_csv(_GetTestPath("test_data/expected.csv"))
        processed = wfigs_data.process_df(df)
        sort_column_list = [
            "dcid", "name", "typeOf", "Location", "FireCause",
            "FireCauseGeneral", "FireCauseSpecific", "FireDiscoveryDateTime",
            "ControlDateTime", "ContainmentDateTime", "BurnedArea", "Costs",
            "TotalIncidentPersonnel", "IrwinID", "wfigsFireID", "ParentFire",
            "InitialResponseDateTime", "InitialResponseAcres"
        ]
        self.assertIsNone(
            pd.testing.assert_frame_equal(
                processed.sort_values(by=sort_column_list, ignore_index=True),
                expected_df.sort_values(by=sort_column_list, ignore_index=True),
                check_dtype=False))


if __name__ == "__main__":
    unittest.main()
