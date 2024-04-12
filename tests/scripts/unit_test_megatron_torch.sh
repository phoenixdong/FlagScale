export PYTHONPATH=./megatron:$PYTHONPATH
cd megatron

torchrun -m pytest tests/unit_tests/data/test_mock_gpt_dataset.py \
                        tests/unit_tests/data/test_multimodal_dataset.py \
                        tests/unit_tests/data/test_preprocess_data.py \
                        tests/unit_tests/data/test_preprocess_mmdata.py
