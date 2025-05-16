"""Hierarchy for SOC.
Usage: provides information regarding the specified code.
    soc = load_hierarchy(soc_df, soc_index_df)
    soc["1"].
"""

import pandas as pd

from occupational_classification.meta.soc_meta import SocMeta

_LEVEL_DICT = {1: "Major", 2: "Sub-Major", 3: "Minor", 4: "Unit"}
_SOC_CODE_LENGTH = 4


class SocCode:
    """Validate SOC code. Checks the length of the code and assigns the Group Level."""

    def __init__(self, code: str):
        """Initializes SocCode class.

        This method validates the code type and length, and assigns the correct
            group level.

        Args:
            code (str): SOC code, must be a string of 1, 2, 3, or 4 digits.
            level_name (dict): Classificaiton of the group level, based on code length.
        """
        SocCode._validate_code(code)

        self.code = code

        self.level_name = _LEVEL_DICT

    def code_length(self):
        return len(self.code)

    @staticmethod
    def _validate_code(code: str):
        """Checks if the code is a string of digits with length 1, 2, 3, or 4.

        Args:
            code (str): SOC Code to be valitaded.

        Raises:
            TypeError: If code is other type, than a string.
            ValueError: If code is an empty string.
            ValueError: If code contains other characters than digits.
            ValueError: If code length is too long.
        """
        if not isinstance(code, str):
            raise TypeError("SOC code must be a string")
        if code == "":
            raise ValueError("Cannot be empty string.")
        if not code.isdigit():
            raise ValueError("Code must consist of digits only.")
        n_digits = len(code)
        if n_digits > _SOC_CODE_LENGTH:
            raise ValueError("Code length needs to be between 1 and 4 digits.")

    def group_classification(self):
        """Assigns the group level based on the length of the code.

        Returns:
            str: Name of the group level (Major/Sub-Major/Minor/Unit)
        """
        code = self.code
        n_digits = SocCode(code).code_length()
        group = _LEVEL_DICT[n_digits]
        return group


class SocNode:
    """Creates a SOC object that is used for hierarchy operations."""

    def __init__(self, soc_code: str, group_title: str, group_description: str):
        """Creates a SOC object that is used for hierarchy operations.

        Args:
            soc_code (str): SOC code.
            group_title (str): Group Title related to the SOC code.
            group_description (str): Group Description related to the SOC code.

        Attributes:
            soc_code (str): SOC code.
            group_title (str): Group Title related to the SOC code.
            group_description (str): Group Description related to the SOC code.
            group_level (str): Group level related to the SOC code.
            tasks (list): Only for Unit group - list of tasks associated with
                the group.
            parent (NoneType): Parent of the current SOC code.
            children (list): Children of the current SOC code.
            qualifications (NoneType): Only for Unit group - entry route and
                associated qualificaitons for the current SOC code.
            job_titles (list): Only for Unit group - example job titles.
        """
        self.soc_code = soc_code
        self.group_title = group_title
        self.group_description = group_description

        self.group_level = SocCode(soc_code).group_classification()
        self.tasks = []
        self.parent = None
        self.children = []
        self.qualifications = None
        self.job_titles = []

    def __repr__(self):
        return f'SocNode({self.soc_code!r}, "{self.group_title}", "{self.group_description}")'

    def is_leaf(self):
        """Checks if an object is of the most disaggregated level.

        Returns:
            bool: False when is not a leaf, True if is a leaf.
        """
        return not self.children

    def print_all(self):
        """Prints all information about the SOC hierarchy.
        - code as "Code": A 1, 2, 3, or 4 digit code identifying group.
        - soc2020_group_title as "Group Title": A short group title for the group code in SOC 2020.
        - parent (if applicable) as Parent:  a code for parnt, followed with the group title.
        - group_description as "Group Description": More in-depth description of the group.
        - children (if applicable) as Children: a code for children, followed with the group title.
        - tasks (if applicable) as Tasks: A list of tasks that are typically associated with the Unit group.
        """
        print(f"SOC Code: {self.soc_code}")
        print(f"\nGroup Level: {self.group_level}")
        print(f"\nParent:  {self.parent}")
        print(f"\nChildren: {self.children}")
        print(f"\nGroup Title: {self.group_title}")
        print(f"\nGroup Description: {self.group_description}")
        print(f"\nTasks: {self.tasks}")
        print(
            f"\nTypical Entry Routes And Associated Qualifications: {self.qualifications}"
        )
        print(f"\nExample Job Titles: {self.job_titles}")


class SOC:
    """Provides lookup functionality, based on the SocNode object and related
    to them information.

    Usage:
        soc = load_hierarchy(soc_df, soc_index_df)
        soc["1"]
    """

    def __init__(self, nodes: list, lookup: dict):
        """Initializes SOC object, used for lookups.

        Args:
            nodes (list): List of SocNode objects.
            lookup (dict): A dictionary that allows lookups
        """
        self.nodes = nodes
        self.lookup = lookup

    def __getitem__(self, key):
        return self.lookup[key]

    def all_group_descriptions(self):
        """All group descriptions. Only returns for leaf nodes."""
        return (
            {"code": node.soc_code, "text": "Description: " + node.group_description}
            for node in self.nodes
            if node.is_leaf()
        )

    def all_group_titles(self):
        """All group titles. Only returns for leaf nodes."""
        return (
            {"code": node.soc_code, "text": "Title: " + node.group_title}
            for node in self.nodes
            if node.is_leaf()
        )

    def all_group_qualifications(self):
        """All group entry routes and associated qualifications.
        Only returns for leaf nodes.
        """
        return (
            {
                "code": node.soc_code,
                "text": "Typical Entry Routes And Associated Qualifications: "
                + node.qualifications,
            }
            for node in self.nodes
            if node.is_leaf()
        )

    def all_group_job_titles(self):
        """All group job titles. Only returns for leaf nodes."""
        return (
            {
                "code": node.soc_code,
                "text": "Example Job Titles: " + ", ".join(node.job_titles),
            }
            for node in self.nodes
            if node.is_leaf()
        )

    def all_group_tasks(self):
        """All group tasks. Only returns for leaf nodes."""
        return (
            {"code": node.soc_code, "text": "Tasks: " + ", ".join(node.tasks)}
            for node in self.nodes
            if node.is_leaf()
        )

    def all_leaf_text(self):
        """Returns all short text descriptions of 4-digit level SOC.

        Includes:
            - Group descriptions,
            - Group titles,
            - Group typical entry routes and associated qualifications,
            - Group job titles,
            - Group tasks.

        Returns:
            pd.DataFrame
                Two columns `code`, `text`
        """
        gr_description = pd.DataFrame(self.all_group_descriptions())
        gr_title = pd.DataFrame(self.all_group_titles())
        tasks = pd.DataFrame(self.all_group_tasks())
        qualifications = pd.DataFrame(self.all_group_qualifications())
        job_titles = pd.DataFrame(self.all_group_job_titles())

        df = pd.concat(
            [gr_title, gr_description, tasks, qualifications, job_titles],
            ignore_index=True,
        )

        df = df.groupby("code")["text"].apply(lambda x: ", ".join(x)).reset_index()
        return df


def _define_codes_and_nodes(soc_df: pd.DataFrame):
    """Creates codes list, nodes list and code_node_dict dictionary,
    later used for SOC.
    """
    soc_meta = SocMeta()
    codes = []
    nodes = []

    code_node_dict = {}

    for code in soc_df["code"]:
        group_description = soc_meta.get_meta_by_code("1")["group description"]
        group_title = soc_meta.get_meta_by_code("1")["group title"]
        soc_node = SocNode(code, group_title=group_title, group_description=group_description)

        codes.append(code)
        nodes.append(soc_node)
        code_node_dict[code] = soc_node
    return codes, nodes, code_node_dict


def _populate_parent_child_relationships(nodes: list, code_node_dict: dict):
    """Populate the parent/child relationships in SOC. Modifies nodes in places."""
    for node in nodes:
        parent_code = find_parent(node.soc_code)
        if parent_code is not None:
            code_node_dict[parent_code].children.append(node)
            code_node_dict[node.soc_code].parent = code_node_dict[parent_code]


def _populate_tasks_and_quals(nodes: list, soc_df: pd.DataFrame):
    """Populate tasks and qualifications. Modifies nodes in places."""
    for node in nodes:
        if SocCode(node.soc_code).code_length() == _SOC_CODE_LENGTH:
            qual = soc_df.loc[soc_df["code"] == node.soc_code, "qualifications"]
            node.qualifications = qual.iloc[0]

            tasks = soc_df.loc[soc_df["code"] == node.soc_code, "tasks"]
            tasks_list = tasks.iloc[0].replace("\n", "").split("~")

            node.tasks = tasks_list[1:]


def _populate_job_titles(nodes: list, soc_index: pd.DataFrame):
    """Populate job titles. Modifies nodes in places."""
    for node in nodes:
        if SocCode(node.soc_code).code_length() == _SOC_CODE_LENGTH:
            filtered_index = soc_index[soc_index["code"] == str(node.soc_code)]

            for _index, row in filtered_index.iterrows():
                node.job_titles.append(row["title"])


def is_leaf_code(code) -> bool:
    """Checks if the code is a leaf."""
    return SocCode(code).code_length() > 1


def find_parent(code) -> str:
    """Finds a code representing a parent, if the code is a leaf."""
    if is_leaf_code(code):
        n_digits = SocCode(code).code_length()
        code = str(code)
        return code[0 : n_digits - 1]
    else:
        return None


def load_hierarchy(soc_df, soc_index):
    """Create the SOC lookups from all supporting data.

    Uses:
        - SOC structure
        - SOC index

    Once created this provides a single point of access for all
    data associated with a SOC definition.
    """
    codes, nodes, code_node_dict = _define_codes_and_nodes(soc_df)

    _populate_parent_child_relationships(nodes, code_node_dict)

    _populate_tasks_and_quals(nodes, soc_df)

    _populate_job_titles(nodes, soc_index)

    lookup = {}
    for node in nodes:
        lookup[str(node.soc_code)] = node

    return SOC(nodes, lookup)
