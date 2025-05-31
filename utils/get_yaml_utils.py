import os
import yaml

class GetElements:

    """
    初始化：生成 YAML 文件路径，如果 elements 目录不存在则创建
    :param page_name: 页面配置文件名，如 'baidu.yaml'
    """
    def __init__ (self, page_name):

        self.page_name = page_name

        # 获取当前文件（get_yaml_utils.py）所在的目录的上上级目录，即项目根目录
        base_dir = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))
        # 拼接 elements 文件夹路径
        elements_dir = os.path.join(base_dir,'elements')
        # 如果 elements 文件夹不存在，就创建它
        if not os.path.exists(elements_dir):
            os.mkdir(elements_dir)
        # 最终的 yaml 文件完整路径
        self.page_path = os.path.join(elements_dir,page_name)


    """
    读取 YAML 文件中的页面元素配置
    :return: 一个字典，表示元素信息
    """
    def get_elements (self):

        if not os.path.exists(self.page_path):
            raise FileNotFoundError (f"文件不存在: {self.page_path}")

        with open(self.page_path,'r',encoding='UTF-8') as f:
            elements = yaml.load(f,Loader=yaml.FullLoader)

        return  elements






