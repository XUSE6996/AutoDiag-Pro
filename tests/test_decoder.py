from autodiag.core.dtc_decoder import DTCDecoder


def test_unknown_code():

    decoder = DTCDecoder()

    result = decoder.decode(
        "XXXXX"
    )


    assert result["code"] == "XXXXX"
