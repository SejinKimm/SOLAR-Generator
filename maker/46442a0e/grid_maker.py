from typing import Dict, List, Tuple
from numpy.typing import NDArray
import numpy as np
import random
from maker.base_grid_maker import BaseGridMaker


class GridMaker(BaseGridMaker):

    def parse(self, **kwargs) -> List[Tuple[List[NDArray], List[NDArray], List[NDArray], List[NDArray], Dict]]:
        dat = []
        num = 0

        num_samples = kwargs['num_samples']
        max_h, max_w = kwargs['max_grid_dim']
        num_examples = kwargs['num_examples']

        # randomly generate inputs
        while num < num_samples:
            num += 1
            pr_in: List[NDArray] = []
            pr_out: List[NDArray] = []
            ex_in: List[NDArray] = []
            ex_out: List[NDArray] = []
            selection: List[NDArray] = []
            operation: List[NDArray] = []

            for _ in range(num_examples):
                # set grid size randomly and randomly generate grid.
                h = np.random.randint(1, max_h//2+1)
                w = h  # w=np.random.randint(1,max_w//2+1) for rectangular grid
                rand_grid = np.random.randint(0, 10, size=[h, w], dtype=np.uint8)
                ex_in.append(rand_grid)
                ex_out.append(self.make_answer(rand_grid))

            # set grid size randomly and randomly generate grid.
            h = np.random.randint(1, max_h//2+1)
            w = h  # w=np.random.randint(1,max_w//2+1) for rectangular grid
            rand_grid = np.random.randint(0, 10, size=[h, w], dtype=np.uint8)
            pr_in.append(rand_grid)
            pr_out.append(self.make_answer(rand_grid))
            method = self.get_random_method()
            operation, selection = method(h, w)
            desc = {'id': '46442a0e',
                    'selections': selection,
                    'operations': operation}
            dat.append((ex_in, ex_out, pr_in, pr_out, desc))
        return dat

    def make_answer(self, grid):
        # task == '46442a0e'
        h, w = grid.shape
        ans = np.zeros([2*h, 2*w], dtype=np.int8)
        ans[:h, :w] = grid.copy()
        ans[h:2*h, :w] = np.rot90(grid).copy()
        ans[h:2*h, w:2*w] = np.rot90(grid, 2).copy()
        ans[:h, w:2*w] = np.rot90(grid, 3).copy()
        return ans

    def get_random_method(self):
        methods = [method for method in dir(
            self) if method.startswith("method")]
        random_method = random.choice(methods)
        return getattr(self, random_method)

    def method1(self, h, w):
        operations = [33, 29, 30, 24, 29, 30, 26, 27, 34]
        selections = [[0, 0, 2*h-1, 2*w-1],  # 33
                      [0, 0, h-1, w-1],  # 29
                      [h, 0, h-1, w-1],  # 30
                      [h, 0, h-1, w-1],  # 24
                      [0, 0, 2*h-1, w-1],  # 29
                      [0, w, 2*h-1, w-1],  # 30
                      [0, w, 2*h-1, w-1],  # 26
                      [0, w, 2*h-1, w-1],  # 27
                      [0, 0, 2*h-1, 2*w-1]  # 34
                      ]
        return operations, selections

    def method2(self, h, w):
        operations = [33, 29, 30, 25, 29, 30, 26, 27, 34]
        selections = [[0, 0, 2*h-1, 2*w-1],  # 33
                      [0, 0, h-1, w-1],  # 29
                      [0, w, h-1, w-1],  # 30
                      [0, w, h-1, w-1],  # 25
                      [0, 0, h-1, 2*w-1],  # 29
                      [h, 0, h-1, 2*w-1],  # 30
                      [h, 0, h-1, 2*w-1],  # 26
                      [h, 0, h-1, 2*w-1],  # 27
                      [0, 0, 2*h-1, 2*w-1]  # 34
                      ]
        return operations, selections

    def method3(self, h, w):
        operations = [33, 29, 30, 24, 29, 30, 24, 29, 30, 24, 34]
        selections = [[0, 0, 2*h-1, 2*w-1],  # 33
                      [0, 0, h-1, w-1],  # 29
                      [h, 0, h-1, w-1],  # 30
                      [h, 0, h-1, w-1],  # 24
                      [h, 0, h-1, w-1],  # 29
                      [h, w, h-1, w-1],  # 30
                      [h, w, h-1, w-1],  # 24
                      [h, w, h-1, w-1],  # 29
                      [0, w, h-1, w-1],  # 30
                      [0, w, h-1, w-1],  # 24
                      [0, 0, 2*h-1, 2*w-1]  # 34
                      ]
        return operations, selections

    def method4(self, h, w):
        operations = [33, 29, 30, 25, 29, 30, 25, 29, 30, 25, 34]
        selections = [[0, 0, 2*h-1, 2*w-1],  # 33
                      [0, 0, h-1, w-1],  # 29
                      [0, w, h-1, w-1],  # 30
                      [0, w, h-1, w-1],  # 25
                      [0, w, h-1, w-1],  # 29
                      [h, w, h-1, w-1],  # 30
                      [h, w, h-1, w-1],  # 25
                      [h, w, h-1, w-1],  # 29
                      [h, 0, h-1, w-1],  # 30
                      [h, 0, h-1, w-1],  # 25
                      [0, 0, 2*h-1, 2*w-1]  # 34
                      ]
        return operations, selections
