import datetime
from infrastructure.service_locator.time_service import TimeService


class MockTimeService(TimeService):
    current_time: datetime.datetime = datetime.datetime(
        2021, 7, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
    )

    def getCurrentTime(self) -> datetime.datetime:
        return self.current_time

    def set_current_time(self, current_time: datetime.datetime) -> None:
        self.current_time = current_time

    def advance_time(self, seconds: int) -> datetime.datetime:
        self.current_time += datetime.timedelta(seconds=seconds)
        return self.current_time
