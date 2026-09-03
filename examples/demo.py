from autodiag.adapters.simulator import SimulatorAdapter
from autodiag.services.diagnostic_service import DiagnosticService


adapter = SimulatorAdapter()

adapter.connect()


service = DiagnosticService(adapter)


errors = service.scan_vehicle()


print(errors)
