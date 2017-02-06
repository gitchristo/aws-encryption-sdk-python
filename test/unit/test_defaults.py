"""Test suite to verify calculated values in aws_encryption_sdk.internal.defaults"""
import unittest
import aws_encryption_sdk.internal.defaults


class TestDefaults(unittest.TestCase):

    def test_max_frame_count(self):
        max_frame_count = pow(2, 32) - 1
        assert aws_encryption_sdk.internal.defaults.MAX_FRAME_COUNT == max_frame_count

    def test_max_frame_size(self):
        max_frame_size = pow(2, 31) - 1
        assert aws_encryption_sdk.internal.defaults.MAX_FRAME_SIZE == max_frame_size

    def test_max_single_block_size(self):
        max_single_block_size = pow(2, 36) - 32
        assert aws_encryption_sdk.internal.defaults.MAX_SINGLE_BLOCK_SIZE == max_single_block_size

    def test_max_byte_array_size(self):
        max_byte_array_size = pow(2, 16) - 1
        assert aws_encryption_sdk.internal.defaults.MAX_BYTE_ARRAY_SIZE == max_byte_array_size
