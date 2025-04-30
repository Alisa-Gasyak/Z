from abc import abstractmethod, ABC


class Vacancy(ABC):
    @abstractmethod
    def get_vacancy_count(self):
        """ Получить кол-во вакансий. """
        pass

    @abstractmethod
    def set_vacancy_count(self):
        """ Установить новое кол-во вакансий. """
        pass

    @abstractmethod
    def save(self):
        """ Сохранить состояние. """
        pass

    @abstractmethod
    def restore(self, memento):
        """ Восстановить состояние. """
        pass


class MementoVacancy(ABC):
    """ Класс, где мы можем получить состояние для текущей итерации объекта. """

    @abstractmethod
    def get_state(self):
        """ Получить состояние. """
        pass


class VaultJobs(ABC):
    """
    Класс, который будет содержать список
    сохранённых состояний (Что-то типо стека).
    """

    @abstractmethod
    def save_state(self):
        """ Сохранить состояние. """
        pass

    @abstractmethod
    def get_previous_state(self):
        """ Получить предыдущее состояние. """
        pass


class PythonVaultJobs(VaultJobs):
    """ Сохроняем список состояний для Python вакансий. """

    def __init__(self, _jobs: Vacancy):
        # Список, где будут находится наши состояния
        self.__vault_jobs = []
        self._jobs = _jobs

    def save_state(self, __state: MementoVacancy):
        """ Сохранить состояние. """
        self.__vault_jobs.append(__state)

    def get_previous_state(self):
        """ Получить предыдущее состояние. """
        memento = self.__vault_jobs.pop()
        self._jobs.restore(memento)

    def show_history(self) -> list:
        """ Получить список всех состояний. """
        return self.__vault_jobs


class MementoPythonVacancy(MementoVacancy):
    def __init__(self, _state):
        self.__state = _state

    def get_state(self):
        return self.__state

    def __repr__(self):
        return f'<Кол-во вакансий: {self.__state} >'


class PythonVacancy(Vacancy):
    def __init__(self):
        self._vacancy_count = 17000

    def get_vacancy_count(self) -> int:
        return self._vacancy_count

    def set_vacancy_count(self, count: int):
        """
        Установить новое кол-во вакансии. Если кол-во < 0,
        то новое значение установленно не будет.
        """
        if abs(count) == count:
            self._vacancy_count = count

    def save(self) -> MementoVacancy:
        return MementoPythonVacancy(self._vacancy_count)

    def restore(self, memento: MementoVacancy):
        """ Восстановить предыдущее состояние. """
        self._vacancy_count = memento.get_state()
        print(f'Новое кол-во вакансий: {self._vacancy_count}')


feb = PythonVacancy()

feb.set_vacancy_count(15000)

feb.set_vacancy_count(16000)

python_saver = PythonVaultJobs(feb)
python_saver.save_state(feb.save())

feb.set_vacancy_count(13000)
python_saver.save_state(feb.save())

feb.set_vacancy_count(12000)
python_saver.save_state(feb.save())

print(python_saver.show_history())

python_saver.get_previous_state()
python_saver.get_previous_state()

print(feb.get_vacancy_count())


