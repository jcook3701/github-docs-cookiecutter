def test_bake_with_custom_name(cookies):
    """Ensure custom project_name works."""
    result = cookies.bake(extra_context={"project_name": "custom_name"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "custom_name"
