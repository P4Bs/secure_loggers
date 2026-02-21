# Definir logger para una tarea especifica
# Registrar un evento de forma estructurada
# Registrar eventos de forma segura

# Definir el logger con decoradores
# trazar llamadas entre funciones

from Constants.constants import INFO
from Loggers.TypeLoggers.log_application_event import log_application_event


# def setup_logger(logger_name, log_file, level=logging.INFO):
#     l = logging.getLogger(logger_name)
#     formatter = logging.Formatter(
#         fmt = "%(asctime)s: %(levelname)-8s | %(message)s |",
#         datefmt = "%Y-%m-%d %H:%M:%S"
#     )
#
#     file_handler = logging.FileHandler(log_file, mode = 'a')
#     file_handler.setFormatter(formatter)
#     stream_handler = logging.StreamHandler()
#     stream_handler.setFormatter(formatter)
#
#     l.setLevel(level)
#     l.addHandler(file_handler)
#     l.addHandler(stream_handler)
#
#
# setup_logger('log1', "log_file_1.txt")
# logger_1 = logging.getLogger('log1')
# logger_1.info('111 - message 1')

def log_call(logger):
    def log_function_call(func):
        def func_wrapper(*args, **kwargs):
            logger.log_info(f'Function {func.__name__} called with args: {args}, kwargs: {kwargs}')
            return func(*args, **kwargs)

        return func_wrapper

    return log_function_call
