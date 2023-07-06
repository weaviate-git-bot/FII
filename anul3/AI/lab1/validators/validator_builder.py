from lib.logging import LoggerBuilder
from lib.models import Validator

class ValidatorBuilder:

    def __init__(self) -> None:
        self.__validators = list()
        self.logger = LoggerBuilder.get_instance().get_logger()

    def add_validator(self, validator: Validator) -> None:
        self.__validators.append(validator)

    def validate(self) -> bool:
        for validator in self.__validators:
            if not validator.validate():
                self.logger.error('[x][%s] Validation failed', str(validator))
                return False

            self.logger.info('[+][%s] Validation successful', str(validator))
        return True