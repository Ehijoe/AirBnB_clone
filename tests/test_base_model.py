#!/usr/bin/python3
"""Unittests for the Base model."""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime, timedelta


class BaseModelTests(TestCase):
    """Tests for the Base models."""

    def test_base_model_creation(self):
        b = BaseModel()
        self.assertTrue(
            b.created_at - datetime.now() < timedelta(seconds=1)
        )
