import logging
from pylogrus import PyLogrus, TextFormatter, CL_BLDYLW, CL_BLDWHT, CL_BAKRED, CL_BAKBLU, CL_BAKGRN, CL_BAKPUR, CL_TXTWHT, CL_BAKYLW, CL_BLDBLK

def get_logger():
    logging.setLoggerClass(PyLogrus)

    logger = logging.getLogger(__name__)  # type: PyLogrus
    logger.setLevel(logging.DEBUG)

    formatter = TextFormatter(datefmt='Z', colorize=True)
    formatter.override_level_names({'CRITICAL': 'CRIT', 'ERROR': 'ERRO', 'WARNING': 'WARN', 'DEBUG': 'DEBU'})
    formatter.override_colors({
        'prefix': CL_BLDYLW + CL_BAKPUR,
        'debug': CL_BLDWHT + CL_BAKBLU,
        'info':  CL_TXTWHT + CL_BAKGRN,
        'warning': CL_BLDBLK + CL_BAKYLW,
        'error': CL_BLDYLW + CL_BAKRED,
        'critical': CL_BLDYLW + CL_BAKRED
        })
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger