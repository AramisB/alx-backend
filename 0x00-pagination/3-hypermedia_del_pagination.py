#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10):
        """
        Return a dictionary containing the pagination
        information that is resilient to deletions.
        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page.
        Returns:
            Dict[str, Any]: A dictionary containing the index,
            next_index, page_size, and data.
        """
        # Validate that the index is within a valid range
        assert isinstance(index, int)\
            and 0 <= index < len(self.indexed_dataset()), "Index out of range"

        # Fetch the indexed dataset
        indexed_data = self.indexed_dataset()

        # Prepare the data slice and calculate the next index
        data = []
        current_index = index
        for _ in range(page_size):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index\
            if current_index < len(indexed_data) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
