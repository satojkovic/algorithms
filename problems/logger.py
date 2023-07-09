class Logger:
    def __init__(self) -> None:
        self.msg_stream = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.msg_stream or self.msg_stream[message] + 10 <= timestamp:
            self.msg_stream[message] = timestamp
            return True
        return False


def test_logger():
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(2, "bar") is True
    assert logger.shouldPrintMessage(3, "foo") is False
    assert logger.shouldPrintMessage(10, "foo") is False
    assert logger.shouldPrintMessage(11, "foo") is True
