# pylint: disable=C0301
import pytest

from src.occupational_classification.lookup import soc_lookup


@pytest.mark.parametrize(
    "description, expected_label",
    [
        ("benefits fraud investigator (government)", "4111"),
        ("saw doctor", "8139"),
        ("vice president (banking)", "1131"),
        ("zoologist", "2112"),
    ],
)
def test_soc_lookup_find_code_for_title(description, expected_label):
    lookup = soc_lookup.SOCLookup().lookup_dict[description]
    assert lookup == expected_label


@pytest.mark.parametrize(
    "description, expected_meta",
    [
        (
            "benefits fraud investigator (government)",
            {
                "description": "benefits fraud investigator (government)",
                "code": "4111",
                "code_meta": {
                    "code": "4111",
                    "group_title": "National government administrative occupations",
                    "group_description": "National government administrative occupations undertake a variety of administrative and clerical duties in national government departments, and in local offices of national government departments.",
                    "entry_routes_and_quals": "Entry is possible to junior grades within this group with GCSEs/S grades, and/or relevant practical experience higher grades require A levels/H grades or equivalent, although many entrants are graduates. NVQs/SVQs, apprenticeships and professional qualifications are available for certain areas of work.",
                    "tasks": [
                        "assists senior government officers with policy work, external liaison or general administrative work",
                        "undertakes administrative duties specific to the operation of HM Revenue and Customs offices, Job Centres, Benefits Agency offices and other local offices of national government",
                        "maintains and updates correspondence, documents, data and other records for storage in files or on computer",
                        "classifies, sorts and files publications, correspondence etc. in offices and libraries",
                        "responds to telephone enquiries and other forms of correspondence",
                        "performs miscellaneous clerical tasks such as proof reading printed material, drafting letters, taking minutes etc",
                    ],
                },
                "code_major_group": "4",
                "code_major_group_meta": {
                    "code": "4",
                    "group_title": "Administrative and secretarial occupations",
                    "group_description": "Occupations within this major group undertake general administrative, clerical and secretarial work, and perform a variety of specialist client-orientated administrative duties. The main tasks involve retrieving, updating, classifying and distributing documents, correspondence and other records held electronically and in storage files; typing, word-processing and otherwise preparing documents; operating other office and business machinery; receiving and directing telephone calls to an organisation; and routing information through organisations. Most job holders in this major group will require a good standard of general education. Certain occupations will require further additional vocational training or professional occupations to a well-defined standard.",
                    "entry_routes_and_quals": "",
                    "tasks": [],
                },
            },
        ),
        (
            "zoologist",
            {
                "description": "zoologist",
                "code": "2112",
                "code_meta": {
                    "code": "2112",
                    "group_title": "Biological scientists",
                    "group_description": "Biological scientists examine and investigate the morphology, structure, and physical characteristics of living organisms, including their inter-relationships, environments and diseases.",
                    "entry_routes_and_quals": "Entrants usually possess a degree and some roles may require a postgraduate qualification. Entry may also be possible with an appropriate BTEC/SQA award, an HNC/NHD, or other academic qualifications. Further specialist training is provided on the job. Some employers may expect entrants to gain professional qualifications.",
                    "tasks": [
                        "studies the physical form, structure, composition and function of living organisms",
                        "researches the effects of internal and external environmental factors on the life processes and other functions of living organisms",
                        "observes the structure of communities of organisms in the laboratory and in their natural environment",
                        "advises farmers, medical staff and others, on the nature of field crops, livestock and produce and on the treatment and prevention of disease",
                        "monitors the distribution, presence and behaviour of plants, animals and aquatic life, and performs other scientific tasks related to conservation not performed by Job holders in MINOR GROUP 215: Conservation and Environment Professionals",
                    ],
                },
                "code_major_group": "2",
                "code_major_group_meta": {
                    "code": "2",
                    "group_title": "Professional occupations",
                    "group_description": "This major group covers occupations whose main tasks require a high level of knowledge and experience in the natural sciences, engineering, life sciences, social sciences, humanities and related fields. The main tasks consist of the practical application of an extensive body of theoretical knowledge, increasing the stock of knowledge by means of research and communicating such knowledge by teaching methods and other means. Most occupations in this major group will require a degree or equivalent qualification, with some occupations requiring postgraduate qualifications and/or a formal period of experience-related training.",
                    "entry_routes_and_quals": "",
                    "tasks": [],
                },
            },
        ),
    ],
)
def test_lookup(description, expected_meta):
    lookup = soc_lookup.SOCLookup().lookup(description)
    assert lookup == expected_meta


@pytest.mark.parametrize(
    "code, expected_meta",
    [
        (
            "4111",
            {
                "code_major_group": "4",
                "code_major_group_meta": {
                    "code": "4",
                    "group_title": "Administrative and secretarial occupations",
                    "group_description": "Occupations within this major group undertake general administrative, clerical and secretarial work, and perform a variety of specialist client-orientated administrative duties. The main tasks involve retrieving, updating, classifying and distributing documents, correspondence and other records held electronically and in storage files; typing, word-processing and otherwise preparing documents; operating other office and business machinery; receiving and directing telephone calls to an organisation; and routing information through organisations. Most job holders in this major group will require a good standard of general education. Certain occupations will require further additional vocational training or professional occupations to a well-defined standard.",
                    "entry_routes_and_quals": "",
                    "tasks": [],
                },
            },
        ),
        (
            "2112",
            {
                "code_major_group": "2",
                "code_major_group_meta": {
                    "code": "2",
                    "group_title": "Professional occupations",
                    "group_description": "This major group covers occupations whose main tasks require a high level of knowledge and experience in the natural sciences, engineering, life sciences, social sciences, humanities and related fields. The main tasks consist of the practical application of an extensive body of theoretical knowledge, increasing the stock of knowledge by means of research and communicating such knowledge by teaching methods and other means. Most occupations in this major group will require a degree or equivalent qualification, with some occupations requiring postgraduate qualifications and/or a formal period of experience-related training.",
                    "entry_routes_and_quals": "",
                    "tasks": [],
                },
            },
        ),
    ],
)
def test_lookup_code_major_group(code, expected_meta):
    lookup = soc_lookup.SOCLookup().lookup_code_major_group(code)
    assert lookup == expected_meta


@pytest.mark.parametrize(
    "candidates, expected_meta",
    [
        (
            [{"soc_code": "2111"}, {"soc_code": "2431"}],
            [
                {
                    "code_major_group": "2",
                    "code_major_group_meta": {
                        "code": "2",
                        "group_title": "Professional occupations",
                        "group_description": "This major group covers occupations whose main tasks require a high level of knowledge and experience in the natural sciences, engineering, life sciences, social sciences, humanities and related fields. The main tasks consist of the practical application of an extensive body of theoretical knowledge, increasing the stock of knowledge by means of research and communicating such knowledge by teaching methods and other means. Most occupations in this major group will require a degree or equivalent qualification, with some occupations requiring postgraduate qualifications and/or a formal period of experience-related training.",
                        "entry_routes_and_quals": "",
                        "tasks": [],
                    },
                }
            ],
        ),
        (
            [{"soc_code": "2111"}, {"soc_code": "4111"}],
            [
                {
                    "code_major_group": "2",
                    "code_major_group_meta": {
                        "code": "2",
                        "group_title": "Professional occupations",
                        "group_description": "This major group covers occupations whose main tasks require a high level of knowledge and experience in the natural sciences, engineering, life sciences, social sciences, humanities and related fields. The main tasks consist of the practical application of an extensive body of theoretical knowledge, increasing the stock of knowledge by means of research and communicating such knowledge by teaching methods and other means. Most occupations in this major group will require a degree or equivalent qualification, with some occupations requiring postgraduate qualifications and/or a formal period of experience-related training.",
                        "entry_routes_and_quals": "",
                        "tasks": [],
                    },
                },
                {
                    "code_major_group": "4",
                    "code_major_group_meta": {
                        "code": "4",
                        "group_title": "Administrative and secretarial occupations",
                        "group_description": "Occupations within this major group undertake general administrative, clerical and secretarial work, and perform a variety of specialist client-orientated administrative duties. The main tasks involve retrieving, updating, classifying and distributing documents, correspondence and other records held electronically and in storage files; typing, word-processing and otherwise preparing documents; operating other office and business machinery; receiving and directing telephone calls to an organisation; and routing information through organisations. Most job holders in this major group will require a good standard of general education. Certain occupations will require further additional vocational training or professional occupations to a well-defined standard.",
                        "entry_routes_and_quals": "",
                        "tasks": [],
                    },
                },
            ],
        ),
    ],
)
def test_unique_code_major_group(candidates, expected_meta):
    lookup = soc_lookup.SOCLookup().unique_code_major_group(candidates)
    assert lookup == expected_meta
