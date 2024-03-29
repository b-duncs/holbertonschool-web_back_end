#!/usr/bin/env python3
"""
implement a get_hyper_index method with
two integer arguments: index with a None
default value and page_size with default
value of 10
"""

import csv
import math
from typing import List, Dict


class Server:
    """server documentation"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """dataset documentation"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """indexed_dataset documentation"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index documentation"""
        assert type(index) == int and type(page_size) == int
        assert 0 <= index < len(self.indexed_dataset())
        pages = []
        next_index = index + page_size
        for i in range(index, index + page_size):
            if not self.indexed_dataset().get(i):
                i += 1
                next_index += 1
            pages.append(self.indexed_dataset()[i])
        return {'index': index,
                'next_index': next_index,
                'page_size': page_size,
                'data': pages
                }
