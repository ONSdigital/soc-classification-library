"""Tests for SocMeta exact-match behaviour."""

from occupational_classification.meta.soc_meta import SocMeta


def test_get_meta_by_code_returns_exact_unit_metadata():
    """get_meta_by_code returns unit-level metadata for a known SOC code."""
    meta = SocMeta().get_meta_by_code("1111")
    assert "error" not in meta
    assert meta["code"] == "1111"
    assert meta["group_title"] == "Chief executives and senior officials"


def test_get_meta_by_code_does_not_fallback_to_parent_group():
    """get_meta_by_code returns an error for unknown codes instead of parent fallback."""
    meta = SocMeta().get_meta_by_code("9999")
    assert meta == {"error": "No metadata found for SOC code 9999"}


def test_get_meta_by_code_exact_matches_get_meta_by_code():
    """get_meta_by_code_exact delegates to get_meta_by_code with the same result."""
    soc_meta = SocMeta()
    assert soc_meta.get_meta_by_code_exact("2112") == soc_meta.get_meta_by_code("2112")
