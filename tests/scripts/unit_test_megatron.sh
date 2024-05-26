export PYTHONPATH=./megatron:$PYTHONPATH
export PYTHONPATH=./../../FlagScale/:$PYTHONPATH

cd megatron

# passed 
torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_basic.py
torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_imports.py
torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_optimizer.py
torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_training.py
torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_utils.py
torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_parallel_state.py

## unpassed no test
# torchrun --nproc_per_node=8 -m pytest -x tests/unit_tests/test_utilities.py