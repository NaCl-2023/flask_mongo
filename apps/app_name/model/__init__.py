# File       : __init__.py.py
# Time       ：2024/9/8 下午12:39
# Author     ：nacl
# version    ：python 3.10
# Description：数据模型
import copy
from dataclasses import dataclass


@dataclass
class BaseModel:
    _id: str = None

    def get_data(self):
        """
        主动将数据类转成常规dict（需要可进行json话）
        """
        keys = dir(self)
        for index, key in enumerate(copy.deepcopy(keys)):
            if key.startswith('_'):
                keys.pop(index)

        keys_data = {}
        if not keys:
            return {}
        for key in keys:
            keys_data[key] = getattr(self, key)
        return keys_data

    def get_id(self):
        return self._id

class BaseModels:
    """
    数据集
    """
    
    def __init__(self, original_data, model_type=BaseModel):
        self._original_data = original_data
        self.model_class: type(BaseModel) = model_type
        self.data = self.analysis_data()

        self.__next_count = 0  # 迭代用
    
    def analysis_data(self) -> list[BaseModel]:
        """
        解析db来的数据
        :return: list(Account)
        """
        if not self._original_data:
            return []
        models = []
        for _data in self._original_data:
            model = self.model_class(**_data)
            models.append(model)
        return models

    def get_datas(self):
        """
        获取全部数据的dict集合
        """
        if not self.data:
            return []
        datas = [model.get_data() for model in self.data if model.get_data()]
        return datas

    def __iter__(self):
        """
        让for识别能迭代
        :return:
        """
        return self

    def __next__(self):
        """
        具体迭代的索引和值传输
        :return:
        """
        if self.__next_count < len(self.data):
            result = self.data[self.__next_count]
            self.__next_count += 1
            return result
        else:
            # 遍历结束后，抛出异常，终止遍历
            self.__next_count = 0  # 使得能重复遍历
            raise StopIteration


