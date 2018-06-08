from datetime import datetime
from dateutil.tz.tz import (
    tzfile,
    tzoffset,
)
from decimal import Decimal
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)


def _parsetz(tzstr: str) -> Optional[_tzparser._result]: ...


def parse(
    timestr: Any,
    parserinfo: None = None,
    **kwargs
) -> Union[Tuple[datetime, Tuple[str, str, str, str, str]], datetime, Tuple[datetime, Tuple[str, str]], Tuple[datetime, Tuple[str, str, str]]]: ...


class _resultbase:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def _repr(self, classname: str) -> str: ...


class _timelex:
    def __init__(self, instream: Any) -> None: ...
    def __iter__(self) -> _timelex: ...
    def __next__(self) -> str: ...
    def get_token(self) -> Optional[str]: ...
    @classmethod
    def isnum(cls, nextchar: str) -> bool: ...
    @classmethod
    def isspace(cls, nextchar: str) -> bool: ...
    @classmethod
    def isword(cls, nextchar: str) -> bool: ...
    @classmethod
    def split(cls, s: Any) -> List[str]: ...


class _tzparser:
    class _result(_resultbase):
        class _attr(_resultbase):
            def __init__(self) -> None: ...
        def __init__(self) -> None: ...
    def parse(self, tzstr: str) -> Optional[_tzparser._result]: ...


class _ymd:
    def __init__(self, *args, **kwargs) -> None: ...
    def _resolve_from_stridxs(
        self,
        strids: Dict[str, int]
    ) -> Union[Tuple[int, None, None], Tuple[int, int, int], Tuple[None, int, None], Tuple[int, int, None]]: ...
    def append(self, val: Union[int, str, Decimal], label: Optional[str] = None) -> None: ...
    def could_be_day(self, value: Union[int, Decimal]) -> bool: ...
    @property
    def has_day(self) -> bool: ...
    @property
    def has_month(self) -> bool: ...
    @property
    def has_year(self) -> bool: ...
    def resolve_ymd(self, yearfirst: bool, dayfirst: bool) -> Any: ...


class parser:
    class _result(_resultbase):
        def __init__(self) -> None: ...
    def __init__(self, info: None = None) -> None: ...
    def _adjust_ampm(self, hour: int, ampm: int) -> int: ...
    def _ampm_valid(self, hour: Optional[int], ampm: Optional[int], fuzzy: bool) -> bool: ...
    def _assign_hms(self, res: parser._result, value_repr: str, hms: int) -> None: ...
    def _assign_tzname(self, dt: datetime, tzname: str) -> datetime: ...
    def _build_naive(self, res: parser._result, default: datetime) -> datetime: ...
    def _build_tzaware(
        self,
        naive: datetime,
        res: parser._result,
        tzinfos: Optional[Union[Dict[str, tzfile], Callable, Dict[str, None], Dict[str, int]]]
    ) -> datetime: ...
    def _build_tzinfo(
        self,
        tzinfos: Union[Dict[str, None], Dict[str, int], Dict[str, tzfile], Callable],
        tzname: str,
        tzoffset: None
    ) -> Optional[Union[tzoffset, tzfile]]: ...
    def _could_be_tzname(self, hour: Optional[int], tzname: Optional[str], tzoffset: Optional[int], token: str) -> bool: ...
    def _find_hms_idx(
        self,
        idx: int,
        tokens: List[str],
        info: parserinfo,
        allow_jump: bool
    ) -> Optional[int]: ...
    def _parse(
        self,
        timestr: Any,
        dayfirst: Optional[bool] = None,
        yearfirst: Optional[bool] = None,
        fuzzy: bool = False,
        fuzzy_with_tokens: bool = False
    ) -> Any: ...
    def _parse_hms(
        self,
        idx: int,
        tokens: List[str],
        info: parserinfo,
        hms_idx: int
    ) -> Tuple[int, int]: ...
    def _parse_min_sec(self, value: Decimal) -> Union[Tuple[int, int], Tuple[int, None]]: ...
    def _parse_numeric_token(
        self,
        tokens: List[str],
        idx: int,
        info: parserinfo,
        ymd: _ymd,
        res: parser._result,
        fuzzy: bool
    ) -> int: ...
    def _parsems(self, value: str) -> Tuple[int, int]: ...
    def _recombine_skipped(self, tokens: List[str], skipped_idxs: List[int]) -> List[str]: ...
    def _to_decimal(self, val: str) -> Decimal: ...
    def parse(
        self,
        timestr: Any,
        default: Optional[datetime] = None,
        ignoretz: bool = False,
        tzinfos: Optional[Union[Dict[str, tzfile], Callable, Dict[str, None], Dict[str, int]]] = None,
        **kwargs
    ) -> Union[Tuple[datetime, Tuple[str, str, str, str, str]], datetime, Tuple[datetime, Tuple[str, str]], Tuple[datetime, Tuple[str, str, str]]]: ...


class parserinfo:
    def __init__(self, dayfirst: bool = False, yearfirst: bool = False) -> None: ...
    def _convert(
        self,
        lst: Union[List[str], List[Tuple[str, str]], List[Union[Tuple[str, str], Tuple[str, str, str]]], List[Tuple[str, str, str]]]
    ) -> Dict[str, int]: ...
    def ampm(self, name: str) -> Optional[int]: ...
    def convertyear(self, year: int, century_specified: bool = False) -> int: ...
    def hms(self, name: str) -> Optional[int]: ...
    def jump(self, name: str) -> bool: ...
    def month(self, name: str) -> Optional[int]: ...
    def pertain(self, name: str) -> bool: ...
    def tzoffset(self, name: str) -> None: ...
    def utczone(self, name: str) -> bool: ...
    def validate(self, res: parser._result) -> bool: ...
    def weekday(self, name: str) -> Optional[int]: ...
