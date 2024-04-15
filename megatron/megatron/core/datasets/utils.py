# Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.

import os
import logging
from enum import Enum
from typing import Any, List

import numpy
import torch

logger = logging.getLogger(__name__)


class Split(Enum):
    train = 0
    valid = 1
    test = 2


def compile_helpers():
    """Compile C++ helper functions at runtime. Make sure this is invoked on a single process.
    """
    import os
    import subprocess

    command = ["make", "-C", os.path.abspath(os.path.dirname(__file__))]
    if subprocess.run(command).returncode != 0:
        import sys

        log_single_rank(logger, logging.ERROR, "Failed to compile the C++ dataset helper functions")
        sys.exit(1)


def log_single_rank(logger: logging.Logger, *args: Any, rank: int = 0, **kwargs: Any):
    """If torch distributed is initialized, log only on rank

    Args:
        logger (logging.Logger): The logger to write the logs

        args (Tuple[Any]): All logging.Logger.log positional arguments

        rank (int, optional): The rank to write on. Defaults to 0.

        kwargs (Dict[str, Any]): All logging.Logger.log keyword arguments
    """
    if torch.distributed.is_initialized():
        if torch.distributed.get_rank() == rank:
            logger.log(*args, **kwargs)
    else:
        logger.log(*args, **kwargs)


def normalize(weights: List[float]) -> List[float]:
    """Do non-exponentiated normalization

    Args:
        weights (List[float]): The weights

    Returns:
        List[float]: The normalized weights
    """
    w = numpy.array(weights, dtype=numpy.float64)
    w_sum = numpy.sum(w)
    w = (w / w_sum).tolist()
    return w


def is_built_on_zero_rank():
    """
    Determines if the current distributed rank is the one responsible for building datasets. 

    Returns:
        bool: True if the current rank is responsible for building resources, False otherwise.
    """
    from megatron.training import get_args
    args = get_args()

    is_built = False
    if not args.no_shared_fs \
        and torch.distributed.get_rank() == 0:
        is_built = True 
    elif args.no_shared_fs \
        and int(os.environ["LOCAL_RANK"]) == 0:
        is_built = True 
    else:
        is_built = False
    
    return is_built
