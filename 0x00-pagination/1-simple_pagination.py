#!/usr/bin/env python3
"""
Simple helper function for pagination
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The appropriate page of the dataset.
        """
        assert isinstance(page_size, int) and page_size > 0,\
            "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()

        return dataset[start_index:end_index]
