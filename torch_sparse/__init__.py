import torch

torch.ops.load_library('torch_sparse/convert_cpu.so')
torch.ops.load_library('torch_sparse/diag_cpu.so')
torch.ops.load_library('torch_sparse/spmm_cpu.so')

try:
    torch.ops.load_library('torch_sparse/convert_cuda.so')
    torch.ops.load_library('torch_sparse/diag_cuda.so')
    torch.ops.load_library('torch_sparse/spmm_cuda.so')
    torch.ops.load_library('torch_sparse/spspmm_cuda.so')
except OSError as e:
    if torch.cuda.is_available():
        raise e

from .convert import to_torch_sparse, from_torch_sparse, to_scipy, from_scipy
from .coalesce import coalesce
from .transpose import transpose
from .eye import eye
from .spmm import spmm
from .spspmm import spspmm

__version__ = '0.4.3'

__all__ = [
    '__version__',
    'to_torch_sparse',
    'from_torch_sparse',
    'to_scipy',
    'from_scipy',
    'coalesce',
    'transpose',
    'eye',
    'spmm',
    'spspmm',
]

from .storage import SparseStorage
from .tensor import SparseTensor
from .transpose import t
from .narrow import narrow
from .select import select
from .index_select import index_select, index_select_nnz
from .masked_select import masked_select, masked_select_nnz
from .diag import set_diag, remove_diag
from .add import add, add_, add_nnz, add_nnz_
from .mul import mul, mul_, mul_nnz, mul_nnz_
from .reduce import sum, mean, min, max
from .matmul import (spmm_sum, spmm_add, spmm_mean, spmm_min, spmm_max, spmm,
                     spspmm_sum, spspmm_add, spspmm, matmul)
