class Phone:
    number: str = None
    __call_count: int = 0

    def set_number(self, new_number: str) -> None:
        """
        Sets the phone number.

        :param new_number: New phone number.
        """
        self.number = new_number

    def get_call_count(self) -> int:
        """
        Returns the number of received calls.

        :return: Number of received calls.
        """
        return self.__call_count

    def take_call(self) -> None:
        """
        Increases the number of received calls by one.
        """
        self.__call_count += 1


phone1 = Phone()
phone2 = Phone()
phone3 = Phone()

phone1.set_number("+42077554433")
phone2.set_number("+42066234567")
phone3.set_number("+42077543210")

phone1.take_call()
phone1.take_call()
phone1.take_call()
phone2.take_call()
phone2.take_call()
phone3.take_call()
phone3.take_call()
phone3.take_call()
phone3.take_call()
phone3.take_call()


def get_total__call_count(phones: list) -> int:
    """
    Returns the total number of received calls for a list of phones.

    :param phones: List of Phone objects.
    :return: Total number of received calls.
    """
    total_count = 0
    for phone in phones:
        total_count += phone.get_call_count()
    return total_count


phones = [phone1, phone2, phone3]

total_count = get_total__call_count(phones)
print(f"Total number of received calls: {total_count}")
