from package_cursach3.viewer import *


def test_load_data():
    assert load_data("[]") == []


def test_mask_kard():
    assert mask_kard("Счет 75106830613657916952") == "Счет **6952"
    assert mask_kard("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658 "


def test_operation_sting():
    test_1 = {"from": "Visa Classic 6831982476737658", "to": "Visa Platinum 8990922113665229"}
    assert operation_sting(test_1) == "Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229 "