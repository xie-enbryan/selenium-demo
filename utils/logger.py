import os
import sys
import time
import logging


def get_logger():
    # 设置日志存储路径/日志名称
    root_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    current_time = time.strftime('%Y-%m-%d-%H%M%S')
    log_dir = os.path.join(root_path, 'res', 'logs')

    # 确保日志目录存在
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_name = os.path.join(log_dir, f'{current_time}-webui.log')

    # 创建一个 logger 实例
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 创建一个 handler，用于写入日志文件
    file_handler = logging.FileHandler(log_name, 'a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # 创建一个 handler，用于输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 定义 handler 的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 给 logger 添加 handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 返回配置好的 logger 实例
    return logger


if __name__ == '__main__':
    log = get_logger()
    log.info("这是一条 info 日志")
    log.debug("这是一条 debug 日志")
    log.warning("这是一条 warning 日志")
    log.error("这是一条 error 日志")
