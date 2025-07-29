from abc import ABCMeta
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta): 
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        raise NotImplementedError