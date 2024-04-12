export PYTHONPATH=./megatron:$PYTHONPATH
cd megatron

pytest -x tests/unit_tests/test_basic.py \
            tests/unit_tests/test_imports.py \
            tests/unit_tests/test_utils.py \
            tests/unit_tests/data/test_mock_gpt_dataset.py \
            tests/unit_tests/data/test_multimodal_dataset.py \
            tests/unit_tests/data/test_preprocess_data.py \
            tests/unit_tests/data/test_preprocess_mmdata.py \

