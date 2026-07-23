from stroop.keyboard import Response


def test_response_structure():

    response = Response(
        key="1",
        rt_ms=500,
        timeout=False
    )

    assert response.key == "1"
    assert response.rt_ms == 500
    assert response.timeout is False