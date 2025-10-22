
from typing import Any
from types import TracebackType
import logging
from pymongo import ReplaceOne
from pymongo.collection import Collection

class Writer:
    def __enter__(self):
        return self
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_traceback: TracebackType | None,
    ) -> bool | None:
        self._write()
    def __init__(
        self,
        collection: Collection,
        batch_size: int = 1000,
        verbose: int | None = None
    ) -> None:
        self._verbose = verbose
        self._collection = collection
        self._batch_size = batch_size
        self._batch = []
        self._i = 0
    def __call__(self, rec: dict[str, Any]) -> None:
        if len(self._batch) == self._batch_size:
            self._write()
        if self._verbose and self._i % self._verbose == 0:
            logging.info(f'Processed {self._i} records')
        self._i += 1
        stmt = ReplaceOne({'_id': rec['_id']}, rec, upsert=True)
        self._batch.append(stmt)
    def _write(self) -> None:
        if len(self._batch) == 0:
            return
        self._collection.bulk_write(self._batch)
        self._batch = []
