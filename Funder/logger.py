import logging

class Logger:
    _log = None  # 私有类变量，存储单例 Logger 对象

    @classmethod
    def init_logger(cls, level=logging.DEBUG, log_format=None, handler=None):
        """
        初始化日志记录器。
        :param level: 日志级别（默认 DEBUG）
        :param log_format: 日志格式（可选）
        :param handler: 自定义日志处理器（可选）
        """
        if cls._log is not None:
            return  # 如果已经初始化过，直接返回

        # 创建日志记录器
        cls._log = logging.getLogger("ApplicationLogger")
        cls._log.setLevel(level)

        # 如果未指定日志格式，则使用默认格式
        if log_format is None:
            log_format = '%(levelname)s %(asctime)s - %(name)s - %(message)s'

        # 如果未指定处理器，则默认使用 StreamHandler 输出到控制台
        if handler is None:
            handler = logging.StreamHandler()
            handler.setLevel(level)

        # 设置格式化器
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)

        # 添加处理器到日志记录器
        cls._log.addHandler(handler)

        # 防止重复添加处理器
        cls._log.propagate = False

        # 初始化日志成功
        cls._log.info("Logger 初始化成功")

    @classmethod
    def get_logger(cls):
        """
        获取日志记录器实例。
        :return: 日志记录器实例
        """
        if cls._log is None:
            raise RuntimeError("Logger 未初始化。请先调用 init_logger() 方法。")
        return cls._log

