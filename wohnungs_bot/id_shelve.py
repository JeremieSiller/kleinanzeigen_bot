import shelve


class IdShelve:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def store_used_ids(self, ids: list[str]) -> None:
        with shelve.open(self._file_name) as sh:
            sh["ids"] = ids

    def read_used_ids(self) -> list[str]:
        with shelve.open(self._file_name) as sh:
            return sh.get("ids", [])
