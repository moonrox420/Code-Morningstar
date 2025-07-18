class DatabaseRouter:
    """
    Production-grade, pluggable DB router for multi-DB/multi-tenant patterns.
    """
    def __init__(self, db_services: dict):
        self._db_services = db_services

    def get_service(self, db_type: str):
        service = self._db_services.get(db_type)
        if not service:
            raise ValueError(f"Unsupported database type: {db_type}")
        return service
