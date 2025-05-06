import pytest

from src.occupational_classification.hierarchy import soc_hierarchy

# SocCode
# Check code validation - edge cases:


def test_soc_code_is_a_string_else_error():
    with pytest.raises(TypeError):
        soc_hierarchy.SocCode(1)


def test_soc_code_is_not_empty_string_else_error():
    with pytest.raises(ValueError):
        soc_hierarchy.SocCode("")


def test_soc_code_is_digits_only_else_error():
    with pytest.raises(ValueError):
        soc_hierarchy.SocCode("1ab2")


def test_soc_code_not_whitespace_else_error():
    with pytest.raises(ValueError):
        soc_hierarchy.SocCode(" ")


def test_soc_code_is_not_long_else_error():
    with pytest.raises(ValueError):
        soc_hierarchy.SocCode("12345")


# Check code validation - typical case
def test_soc_code_one_digit_string():
    code = "1"
    obj = soc_hierarchy.SocCode(code)
    assert obj.code == code


# Check code length
# _LEVEL_DICT = {1: "Major", 2: "Sub-Major", 3: "Minor", 4: "Unit"} group_classification


def test_soc_code_length():
    code = "123"
    obj = soc_hierarchy.SocCode(code)
    assert obj.code_length() == len(code)


# Check the group assignment
@pytest.mark.parametrize(
    "code, expected_level",
    [("1", "Major"), ("12", "Sub-Major"), ("123", "Minor"), ("1234", "Unit")],
)
def test_group_assignment(code, expected_level):
    # When
    group = soc_hierarchy.SocCode(code).group_classification()

    # Then
    assert str(group) == expected_level


# SocNode
# Check initialization assignment


def test_soc_node_object():
    code = "1"
    group_title = "Title"
    group_desctiption = "Description"

    node = soc_hierarchy.SocNode(code, group_title, group_desctiption)

    assert node.soc_code == code
    assert node.group_title == group_title
    assert node.group_description == group_desctiption


# Check correctness of leaf assignemnt
@pytest.mark.parametrize("children, expected_is_leaf", [([], True), (["Child"], False)])
def test_leaf_assingment(children, expected_is_leaf):
    # When
    node = soc_hierarchy.SocNode("1", "Title", "Description")
    node.children = children

    # Then
    assert node.is_leaf() == expected_is_leaf


# SOC
# Test generator functions (all_group_descriptions, all_gorup_titles, all_group_job_titles, all_group_qualificaitons, all_group_tasks functions)


@pytest.mark.parametrize(
    "nodes, expected_descriptions",
    [
        (
            [
                soc_hierarchy.SocNode("1", "Title1", "Description1"),
                soc_hierarchy.SocNode("2", "Title2", "Description2"),
            ],
            [
                {"code": "1", "text": "Description: Description1"},
                {"code": "2", "text": "Description: Description2"},
            ],
        ),
        ([], []),
    ],
)
def test_soc_all_descriptions(nodes, expected_descriptions):
    obj = soc_hierarchy.SOC(nodes, lookup={})
    result = list(obj.all_group_descriptions())
    assert result == expected_descriptions


# Group Titles
@pytest.mark.parametrize(
    "nodes, expected_group_titles",
    [
        (
            [
                soc_hierarchy.SocNode("1", "Title1", "Description1"),
                soc_hierarchy.SocNode("2", "Title2", "Description2"),
            ],
            [
                {"code": "1", "text": "Title: Title1"},
                {"code": "2", "text": "Title: Title2"},
            ],
        ),
        ([], []),
    ],
)
def test_soc_all_titles(nodes, expected_group_titles):
    obj = soc_hierarchy.SOC(nodes, lookup={})
    result = list(obj.all_group_titles())
    assert result == expected_group_titles


# Tasks
@pytest.mark.parametrize(
    "nodes, initial_tasks, expected_group_tasks",
    [
        (
            ("1", "Title1", "Description1"),
            ["Task1", "Task2"],
            [{"code": "1", "text": "Tasks: Task1, Task2"}],
        ),
    ],
)
def test_soc_all_tasks(nodes, initial_tasks, expected_group_tasks):
    code, title, description = nodes
    node = soc_hierarchy.SocNode(code, title, description)
    node.tasks = initial_tasks
    obj = soc_hierarchy.SOC([node], lookup={})
    result = list(obj.all_group_tasks())
    assert result == expected_group_tasks


# Job Titles
@pytest.mark.parametrize(
    "nodes, initial_job_titles, expected_job_titles",
    [
        (
            ("1", "Title1", "Description1"),
            ["Job1", "Job2"],
            [{"code": "1", "text": "Example Job Titles: Job1, Job2"}],
        ),
    ],
)
def test_soc_all_job_titles(nodes, initial_job_titles, expected_job_titles):
    code, title, description = nodes
    node = soc_hierarchy.SocNode(code, title, description)
    node.job_titles = initial_job_titles
    obj = soc_hierarchy.SOC([node], lookup={})
    result = list(obj.all_group_job_titles())
    assert result == expected_job_titles


def test_soc_all_group_qualifications():
    node1 = soc_hierarchy.SocNode("1", "Title1", "Description1")
    node1.qualifications = "Qualification1"
    node1 = [node1]

    obj = soc_hierarchy.SOC(node1, lookup={})
    result = list(obj.all_group_qualifications())
    assert result == [
        {
            "code": "1",
            "text": "Typical Entry Routes And Associated Qualifications: Qualification1",
        }
    ]
