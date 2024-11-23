from abc import ABC, abstractmethod
import datetime
from django.utils import timezone


class TimeService(ABC):
    @abstractmethod
    def getCurrentTime(self) -> datetime.datetime:
        raise NotImplementedError()


class SystemTimeService(TimeService):
    def getCurrentTime(self) -> datetime.datetime:
        return timezone.now()
