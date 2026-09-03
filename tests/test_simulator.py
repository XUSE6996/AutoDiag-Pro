from autodiag.adapters.simulator import SimulatorAdapter


def test_simulator():

    adapter = SimulatorAdapter()


    assert adapter.connect()

    assert len(
        adapter.read_errors()
    ) > 0
