#!/usr/bin/env python3
"""
implement a get_hyper method that takes the
same arguments (and defaults) as get_page and
returns a dictionary containing the following
key-value pairs
"""
import csv
import math
from typing import List, Dict, Any


def index_range(page, page_size):
    """index_range documentation"""
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index


class Server:
    """server documentation"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset documentation"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page documentation"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """get_hyper documentation"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
