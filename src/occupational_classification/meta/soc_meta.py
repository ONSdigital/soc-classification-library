"""Module that defines the SOC metadata structure aligned with SOC 2020.

This module contains the SOC metadata structure used by lookup enrichment.
The structure follows the same pattern as SIC metadata: an in-code dictionary
plus a small meta lookup class.

The in-code SOC entries were generated from the SOC 2020 Volume 1 descriptions
data (converted CSV), then normalised into this static map format for package
runtime use.
"""

# pylint: disable=C0301,C0302

from occupational_classification.meta.classification_meta import ClassificationMeta

SOCmeta: dict = {}
SOCmeta["1"] = {
    "group_title": "Managers, directors and senior officials",
    "group_description": "This major group covers occupations whose tasks consist of planning, directing and coordinating resources to achieve the efficient functioning of organisations and businesses. Working proprietors in small businesses are included, although allocated to separate minor groups within the major group. Most occupations in this major group will require a significant amount of knowledge and experience of the production processes, administrative procedures or service requirements associated with the efficient functioning of organisations and businesses.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["11"] = {
    "group_title": "Corporate managers and directors",
    "group_description": "Job holders in this sub-major group formulate government policy; direct the operations of major organisations, local government, government departments and special interest organisations organise; and direct production, processing, maintenance and construction operations in industry; formulate, implement and advise on specialist functional activities within organisations; direct the operations of branches of financial institutions; organise and co-ordinate the transportation of passengers, the storage and distribution of freight, and the sale of goods; direct the operations of the emergency services, revenue and customs, the prison service and the armed forces; and co-ordinate the provision of health and social services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["111"] = {
    "group_title": "Chief executives and senior officials",
    "group_description": "Jobholders in this minor group plan, organise and direct the operations of large companies and organisations and of special interest organisations direct government departments and local authorities; and formulate national and local government policy.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1111"] = {
    "group_title": "Chief executives and senior officials",
    "group_description": "Chief executives and senior officials head large enterprises and organisations. They plan, direct and co-ordinate, with directors and managers, the resources necessary for the various functions and specialist activities of these enterprises and organisations. The chief executives of hospitals will be classified in this unit group. Senior officials in national government direct the operations of government departments. Senior officials in local government participate in the implementation of local government policies and ensure that legal, statutory and other provisions concerning the running of a local authority are observed. Senior officials of special interest organisations ensure that legal, statutory and other regulations concerning the running of trade associations, employers\u2019 associations, learned societies, trades unions, charitable organisations and similar bodies are observed. Chief executives and senior officials also act as representatives of the organisations concerned for the purposes of high-level consultation and negotiation.",
    "entry_routes_and_quals": "Entry may be by appointment or internal promotion, as appropriate, and is usually based on relevant experience although candidates may also require academic or professional qualifications for some posts.",
    "tasks": [
        "~analyses economic, social, legal and other data, and plans, formulates and directs at strategic level the operation of a company or organisation ~consults with subordinates to formulate, implement and review company/organisation policy, authorises funding for policy implementation programmes and institutes reporting, auditing and control systems ~prepares, or arranges for the preparation of, reports, budgets, forecasts or other information ~plans and controls the allocation of resources and the selection of senior staff ~evaluates government/local authority departmental activities, discusses problems with government/local authority officials and administrators and formulates departmental policy ~negotiates and monitors contracted out services provided to the local authority by the private sector ~studies and acts upon any legislation that may affect the local authority ~stimulates public interest by providing publicity, giving lectures and interviews and organising appeals for a variety of causes ~directs or undertakes the preparation, publication and dissemination of reports and other information of interest to members and other interested parties",
    ],
}
SOCmeta["1112"] = {
    "group_title": "Elected officers and representatives",
    "group_description": "Elected representatives in national government formulate and ratify legislation and government policy, act as elected representatives in Parliament, Regional Parliaments or Assemblies, and as representatives of the government and its executive. Elected officers in local government act as representatives in the local authority and participate in the formulation, ratification and implementation of local government policies.",
    "entry_routes_and_quals": "Entry is by election.",
    "tasks": [
        "~represents constituency within the legislature and advises and assists constituents on a variety of issues ~acts as a Party representative within the constituency ~participates in debates and votes on legislative and other matters ~holds positions on parliamentary or local government committees ~tables questions to ministers and introduces proposals for government action ~recommends or reviews potential policy or legislative change, and offers advice and opinions on current policy ~advises on the interpretation and implementation of policy decisions, acts and regulations ~studies and acts upon any legislation that may affect the local authority",
    ],
}
SOCmeta["112"] = {
    "group_title": "Production managers and directors",
    "group_description": "Job holders in this minor group plan, organise, direct and co-ordinate all activities and resources involved with production, manufacturing, construction and mining operations in industry.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1121"] = {
    "group_title": "Production managers and directors in manufacturing",
    "group_description": "Production managers and directors in manufacturing plan, organise, direct and co-ordinate the activities and resources necessary for production in manufacturing industries including the maintenance of engineering items, equipment and machinery.",
    "entry_routes_and_quals": "There are no pre-set entry standards. Entry is possible with either a degree or equivalent qualification, and/or relevant experience. On-the-job training is provided, and professional qualifications are available, as are S/NVQs in Management at levels 3 to 5.",
    "tasks": [
        "~liaises with other managers to plan overall production activity and daily manufacturing activity, sets quality standards and estimates timescales and costs ~manages production to ensure that orders are completed to an agreed date and conform to customer and other requirements ~monitors production and production costs and undertakes or arranges for the preparation of reports and records ~oversees supervision of the production line and its staff, ensures targets are met",
    ],
}
SOCmeta["1122"] = {
    "group_title": "Production managers and directors in construction",
    "group_description": "Production managers and directors in construction direct and co-ordinate resources for the construction and maintenance of civil and structural engineering works including houses, flats, factories, roads and runways, bridges, tunnels and railway works, harbour, dock and marine works and water supply, drainage and sewage works.",
    "entry_routes_and_quals": "There are no pre-set entry standards. Entry is possible with either a degree or equivalent qualification and/or relevant experience, via apprenticeships or S/NVQs in Management at levels 3 to 5. On-the-job training is provided, and professional qualifications are available.",
    "tasks": [
        "~liaises with other managers to plan overall production activity and construction activities, sets quality standards and estimates timescales and costs ~receives invitations to tender, arranges for estimates and liaises with client, architects, Chartered architectual technologists and engineers for the preparation of contracts ~plans, directs and co-ordinates the construction and maintenance of civil and structural engineering works, including demolition, pipelines and pilings ~receives reports upon work in progress to ensure that materials and construction methods meet with specifications and statutory requirements and that there are no deviations from agreed plans",
    ],
}
SOCmeta["1123"] = {
    "group_title": "Production managers and directors in mining and energy",
    "group_description": "Production managers and directors in mining, energy and water supply plan, organise, direct and co-ordinate the activities and resources necessary for the extraction of minerals and other natural deposits, the utilisation of sustainable and renewable energy sources and the production, storage and provision of gas, water and electricity supplies.",
    "entry_routes_and_quals": "There are no pre-set entry standards. Entry is possible with either GCSEs/S grades or A levels/H grades, a BTEC Diploma, an apprenticeship, NVQ (level 3), a degree or equivalent qualification with relevant experience. Off and on-the-job training is provided and can lead to professional qualifications.",
    "tasks": [
        "~co-ordinates the activities of mines and open-cast mining operations, quarries, drilling operations, offshore installations, solar power stations, wind farms and other renewable energy generating facilities ~co-ordinates and supervises coal-face production activities and ensures compliance with health and safety regulations ~determines staffing, material and other needs ~ensures that all haulage, storage, purification and distribution work is performed efficiently and in compliance with statutory and other regulations ~arranges for the provision of gas, water and electricity supplies ~ensures compliance with issues relating to the environmental impact of operations",
    ],
}
SOCmeta["113"] = {
    "group_title": "Functional managers and directors",
    "group_description": "Functional managers and directors plan, organise and advise on specialist functions or fields of activity in an organisation. They formulate and administer policies concerning the financial, advertising, marketing, sales, purchasing, work methods, public relations, human resources, information technology and telecoms operations of an organisation.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1131"] = {
    "group_title": "Financial managers and directors",
    "group_description": "Financial managers and directors plan, organise, direct and co-ordinate the financial information of companies, the activities and resources of financial institutions, such as banks and insurance companies, and advise on company financial policy.",
    "entry_routes_and_quals": "Entry is most common with a relevant degree or equivalent qualification, although it is possible with A levels/H grades, S/NVQ levels 4 and 5. Those with higher qualifications may obtain accelerated training. Internal promotion to management is possible and on-the-job training is provided. Professional qualifications are available and are required or mandatory for certain posts.",
    "tasks": [
        "~participates in the formulation of strategic and long-term business plans, assesses the implications for the organisation financial mechanisms and oversees their implementation ~plans external and internal audit programmes, arranges for the collection and analysis of accounting, budgetary and related information, and manages the company\u2019s financial systems ~determines staffing levels appropriate for accounting activities ~assesses and advises on factors affecting business performance ~plans, organises, directs and co-ordinates the activities of financial institutions ~ensures compliance with accounting, recording and information storage, retrieval procedures and the statutory regulatory framework",
    ],
}
SOCmeta["1132"] = {
    "group_title": "Marketing, sales and advertising directors",
    "group_description": "Marketing, sales and advertising directors plan, organise and direct advertising campaigns and market research and formulate and implement an organisation\u2019s marketing, sales and social media policies.",
    "entry_routes_and_quals": "Entry is generally via career progression from related occupations (e.g. marketing manager, advertising accounts manager, sales manager), although in practice most will hold a degree. Professional qualifications are also available and off and on-the-job training is possible. Entrants to professional qualifications from relevant bodies (such as the Chartered Institute of Marketing) require GCSEs/S grades, A levels/H grades, a BTEC/SQA award, a degree or equivalent qualification and/or relevant experience.",
    "tasks": [
        "~liaises with client to discuss product/service to be marketed and develops the most appropriate strategy to deliver the objectives ~discusses employer\u2019s or clients\u2019 requirements, plans and monitors surveys and analyses of customers\u2019 reactions to products ~defines target group for advertising campaigns and implements strategy through appropriate media planning work ~conceives advertising campaigns to impart the desired product image in an effective and economical way ~examines and analyses sales figures, advises on and monitors marketing campaigns and promotional activities ~controls the recruitment and training of staff ~stays abreast of changes in market trends and advertising rates ~produces and/or assesses reports and recommendations concerning marketing, advertising and sales strategies",
    ],
}
SOCmeta["1133"] = {
    "group_title": "Public relations and communications directors",
    "group_description": "Public relations and communications directors plan, organise, direct and co-ordinate the public relations, communications and public information activities of an organisation or on behalf of clients.",
    "entry_routes_and_quals": "Entry is generally via career progression from related occupations (e.g. communications officer, public relations officer) and although there are no pre-set entry standards, in practice most communications and public relations directors hold a degree. Off and on-the-job training is provided.",
    "tasks": [
        "~develops and reviews the public relations policy and direction of an organisation ~directs and oversees the work of the communications department of an organisation or work on behalf of clients at a public relations firm ~liaises with client to discuss their needs and develops the most appropriate strategy to deliver the objectives directs public relations campaigns and communicates messages through a variety of media ~reviews and revises campaign strategy and takes appropriate corrective measures if necessary ~stays abreast of changes in media, readership or viewing figures ~directs the arranging of conferences, exhibitions, seminars, etc. to promote the image of a product, service or organisation",
    ],
}
SOCmeta["1134"] = {
    "group_title": "Purchasing managers and directors",
    "group_description": "Purchasing managers and directors (not retail) plan, organise, direct and co-ordinate the purchasing functions of industrial, commercial, government organisations and public agencies to ensure cost-effectiveness.",
    "entry_routes_and_quals": "Although not restricted to a particular qualification, entry is most common with a degree or equivalent qualification but is also possible with A levels/H grades, a BTEC/SQA award, S/NVQs at level 3 or above, or an apprenticeship. Off and on-the-job training is provided, and professional qualifications are available. Chartered status may also be achieved.",
    "tasks": [
        "~determines what goods, services and equipment need to be sourced ~devises purchasing policies, decides on whether orders should be put out to tender and evaluates suppliers\u2019 bids ~negotiates prices and contracts with suppliers and draws up contract documents ~arranges for quality checks of incoming goods and ensures suppliers deliver on time ~interviews suppliers\u2019 representatives and visits trade fair ~researches and identifies new products and suppliers ~stays abreast of and ensures adherence to relevant legislation regarding tendering and procurement procedures",
    ],
}
SOCmeta["1135"] = {
    "group_title": "Charitable organisation managers and directors",
    "group_description": "Charitable organisation managers and directors plan, organise, co-ordinate and direct the activities of organisations in the charitable and not-for-profit sector.",
    "entry_routes_and_quals": "Entry is generally via career progression from a related occupation (e.g. charity coordinator) and relevant experience of the charitable sector is often required. In some fields a relevant degree or equivalent qualification may be required.",
    "tasks": [
        "~plans, organises, coordinates and directs the resources of a special interest or charitable organisation ~helps to formulate and implement charitable organisations' policies and ensures these meet legal and statutory provisions ~represents their charity in consultation and negotiation with government, employees, trustees and other bodies ~generates income by co-ordinating funding bids, organising appeals, and managing relationships with funders ~stimulates public interest by providing publicity, giving lectures and interviews and organising appeals ~directs or undertakes the preparation, publication and dissemination of reports and other information pertaining to the organisation",
    ],
}
SOCmeta["1136"] = {
    "group_title": "Human resource managers and directors",
    "group_description": "Human resource managers and directors plan, organise and direct the personnel, training and industrial relations policies of organisations, advise on resource allocation and utilisation problems, measure the effectiveness of an organisation\u2019s systems, methods and procedures and advise on, plan and implement procedures to improve utilisation of labour, equipment and materials.",
    "entry_routes_and_quals": "There are no pre-set entry standards, although entry is most common with a degree or equivalent qualification. Relevant experience is important and internal promotion to management is possible. Off and on-the-job training is provided, and professional qualifications are available. Apprenticeships are available. NVQs/SVQs in relevant subjects are available at levels 3, 4 and 5.",
    "tasks": [
        "~determines staffing needs ~oversees the preparation of job descriptions, drafts advertisements and interviews candidates ~oversees the monitoring of employee performance and career development needs ~provides or arranges for provision of training courses ~undertakes industrial relations negotiations with employees\u2019 representatives or trades unions ~develops and administers salary, health and safety and promotion policies ~examines and reports on company and departmental structures, chains of command, information flows, etc. and evaluates efficiency of existing operations ~considers alternative work procedures to improve productivity ~stays abreast of relevant legislation, considers its impact on the organisation\u2019s HR strategy and recommends appropriate action",
    ],
}
SOCmeta["1137"] = {
    "group_title": "Information technology directors",
    "group_description": "Information technology directors plan, organise, direct and co-ordinate the work and resources necessary to provide and operate IT infrastructure and services, including networks, devices, servers and software that runs on the infrastructure within an organisation. IT programme managers and directors direct and provide technical oversight to particular IT programmes of a discrete duration and/or budget.",
    "entry_routes_and_quals": "There are no pre-set entry requirements although candidates usually possess a degree or equivalent qualification together with substantial, relevant work experience. A variety of professional and postgraduate qualifications is available.",
    "tasks": [
        "~develops in consultation with other senior management the IT strategy of the organisation ~directs the implementation within the organisation of IT strategy, infrastructure, procurement, procedures and standards ~develops the periodic business plan and operational budget for IT to deliver agreed service levels ~considers the required IT staffing levels, oversees recruitment and appointment of staff and directs training policy ~prioritises and schedules major IT projects ~ensures that new technologies are researched and evaluated in the light of the organisation\u2019s broad requirements ~works with client or senior management to establish and clarify the aims, objectives and requirements of an IT programme ~plans, directs, reviews and provides technical oversight to IT programmes, involving the co-ordination of multiple IT projects",
    ],
}
SOCmeta["1139"] = {
    "group_title": "Functional managers and directors n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of senior management tasks in respect of other specialist functions or fields of activity in organisations not elsewhere classified in minor group 113: Functional managers and directors.",
    "entry_routes_and_quals": "Entry standards will vary according to the specific function and requirements of the organisation concerned, as will options for training off and on-the-job.",
    "tasks": [
        "~helps to formulate and implement local government policy and ensures legal and statutory provisions are observed ~organises local authority office work and resources, negotiates contracted out services ~plans, organises, coordinates and directs the resources of their organisation ~formulates and directs the implementation of an organisation\u2019s policies ~drives innovation in the working practices of their organisation ~represents union, association or business in consultation and negotiation with government, employees and other bodies ~stimulates public interest by providing publicity, giving lectures and interviews ~directs or undertakes the preparation, publication and dissemination of reports and other information pertaining to the organisation",
    ],
}
SOCmeta["114"] = {
    "group_title": "Directors in logistics, warehousing and transport",
    "group_description": "Directors in logistics, warehousing and transport plan, organise, direct and co-ordinate at a strategic level the activities and resources necessary for the efficient and convenient transportation of passengers or freight, and the loading, unloading, storage, warehousing and distribution of goods and materials.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1140"] = {
    "group_title": "Directors in logistics, warehousing and transport",
    "group_description": "Directors in logistics, warehousing and transport plan, organise, direct and co-ordinate the activities and resources necessary for the safe, efficient and economic movement of passengers and freight by road, rail, sea and air transport, and the receipt, storage and warehousing of goods and the maintenance of stocks at an optimal level.",
    "entry_routes_and_quals": "Candidates are recruited with a variety of academic qualifications and/or with relevant experience. Entrants to management trainee schemes in logistics offered by larger companies will require GCSEs/S grades, A levels/H grades, a degree or other equivalent qualifications. Off and on-the-job training is provided. Professional qualifications are available and may be required for some roles. NVQs/SVQs in a number of relevant areas including supply chain and operations management are available at levels 2, 3, 4 and 5.",
    "tasks": [
        "~plans the optimum utilisation of staff and operating equipment, and co-ordinates maintenance activities to ensure least possible disruption to services examines traffic reports, load patterns, traffic receipts and other data and revises transport services or freight rates accordingly ~oversees and directs the movement, handling and storage of freight in transit and the operations of transport hubs such as airports, railways stations and harbours ~arranges for maintenance of airport runways and buildings, liaises with fuel and catering crews to ensure adequate supplies and resolves any complaints and problems raised by airport users. ~ensures that regulations regarding hours of work, the licensing of crews and transport equipment, the operational safety and efficiency of equipment, the insurance of vehicles and other statutory regulations are complied with ~liaises with production, maintenance, sales and other departments to determine the materials and other items required for current and future production schedules and sales commitments ~reviews, develops and implements stock control, handling and distribution policies to maximise use of space, money, labour and other resources ~advises purchasing department on type, quality and quantity of goods required and dates by which they must be available ~prepares reports on expenditure and advises on materials and parts standardisation, future stores and stock control policies ~decides on storage conditions for particular items, allocates warehouse space and arranges for regular stock inspections to detect deterioration or damage",
    ],
}
SOCmeta["115"] = {
    "group_title": "Managers and directors in retail and wholesale",
    "group_description": "Managers and directors in retail and wholesale plan, organise, direct and co-ordinate the activities necessary for the sale of wholesale and retail goods to customers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1150"] = {
    "group_title": "Managers and directors in retail and wholesale",
    "group_description": "Retail and wholesale managers and directors plan, organise, direct and co-ordinate the operations of major retail and wholesale establishments in order to maximise business performance and meet financial goals.",
    "entry_routes_and_quals": "Entry requirements vary from company to company. Entrants may possess GCSEs/S grades, A levels/H grades, GNVQs/GSVQs, a BTEC/SQA award, a degree or equivalent qualification. Entry is also possible through promotion after gaining sufficient experience. NVQs/SVQs in Retail Operations are available at level 4.",
    "tasks": [
        "~appoints staff, assigns tasks and monitors and reviews staff performance ~liaises with other staff to provide information about merchandise, special promotions etc. to customers ~ensures that adequate reserves of merchandise are held and that stock keeping is carried out efficiently ~ensures customer complaints and queries regarding sales and service are appropriately handled ~oversees the maintenance of financial and other records and controls security arrangements for the premises ~authorises payment for supplies received and decides on vending price, discount rates and credit terms ~examines quality of merchandise and ensures that effective use is made of advertising and display facilities",
    ],
}
SOCmeta["116"] = {
    "group_title": "Senior officers in protective services",
    "group_description": "Senior officers in protective services direct the operations of police stations, fire stations and prisons; supervise customs, excise and immigration staff and oversee inspections of goods and persons entering or leaving the country; and serve as commissioned officers in His Majesty\u2019s armed forces and in foreign and Commonwealth armed forces.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1161"] = {
    "group_title": "Officers in armed forces",
    "group_description": "Officers in armed forces serve as commissioned officers in His Majesty\u2019s armed forces, foreign and Commonwealth armed forces plan, direct, organise and administer military operations; and perform duties for which there is no civilian equivalent.",
    "entry_routes_and_quals": "Entry to a commission in the UK armed forces is possible with GCSEs/S grades and A levels/H grades, or with higher academic qualifications, or by promotion from NCO or other rank. Each arm of the forces has different age restrictions. Candidates must pass a medical examination and interview.",
    "tasks": [
        "~advises and provides information on military aspects of defence policy ~plans, directs and co-ordinates military training and manoeuvres ~supervises the operation of military units and monitors the activities of junior officers, NCOs and other ranks ~plans, directs and administers aid to civilian authorities as requested or when faced with civil disorder, natural disaster or other emergency",
    ],
}
SOCmeta["1162"] = {
    "group_title": "Senior police officers",
    "group_description": "Senior police officers plan, organise, direct and co-ordinate the resources and activities of a specific geographical or functional area of generalised or specialised police work. Senior officers of the British Transport Police direct the specialised police service for the railway network across Britain.",
    "entry_routes_and_quals": "Promotion to the rank of inspector can be by qualifying examination and practical assessment. There are no qualifying examinations to ranks above inspector; promotion is by selection only. There are accelerated promotion schemes available as well as the Direct Entry scheme which recruits external entrants with relevant skills directly to senior positions in the police force. All police forces have age restrictions and medical requirements.",
    "tasks": [
        "~liaises with senior officers to determine staff, financial and other short- and long-term needs ~plans, directs and co-ordinates general policing for an area or functional unit ~directs and monitors the work of subordinate officers ~establishes contacts and sources of information concerning crimes planned or committed ~directs and co-ordinates the operation of record keeping systems and the preparation of reports",
    ],
}
SOCmeta["1163"] = {
    "group_title": "Senior officers in fire, ambulance, prison and related services",
    "group_description": "Fire officers plan, organise, direct and co-ordinate the activities and resources of a specific physical or functional area of a statutory or private fire brigade/service and the resources necessary for the protection of property at fires within a salvage corps area. Ambulance officers plan, organise, direct and co-ordinate the resources necessary for the provision of ambulance services. Prison officers (principal officer and above) plan, organise, direct, and co-ordinate the activities and resources necessary for the running of a prison, remand or detention centre. Customs officers plan and direct the work of customs, excise and immigration staff in the monitoring and inspection of goods and persons crossing national borders.",
    "entry_routes_and_quals": "The position of senior fire officer is achieved by internal promotion. Entry to senior positions within the prison service and revenue and customs is either by internal promotion or by open competition; both organisations operate accelerated promotion schemes available to internal and external applicants. Entry to the prison and fire services are subject to age restrictions, and both the prison service and revenue and customs impose nationality conditions. Entry to senior positions within the ambulance service is largely by internal promotion from supervisory roles.",
    "tasks": [
        "~liaises with other senior officials and/or government departments to determine staffing, financial and other short- and long-term needs ~prepares reports for insurance companies, the Home Office, Scottish Home and Health Department, and other bodies as necessary ~advises on the recruitment, training and monitoring of staff ~fire officers plan, direct and co-ordinate an operational plan for one or more fire stations, attend fires and other emergencies to minimise danger to property and people, arrange for the salvaging of goods, immediate temporary repairs and security measures for fire damaged premises as necessary ~ambulance officers plan, organise, direct and co-ordinate the activities of ambulance personnel and control room assistants, for the provision of ambulance services for emergency and non-emergency cases ~prison officers interview prisoners on arrival and discharge/departure, receive reports on disciplinary problems and decide on appropriate action, make periodic checks on internal and external security, and provide care and support to prisoners in custody ~revenue and customs, excise and immigration officers advise on the interpretation of regulations concerning taxes, duties and immigration requirements and enforce these regulations through monitoring of premises, examining goods entering the country to ensure correct duty is paid and establishing that passengers have the necessary authorisation for crossing national borders",
    ],
}
SOCmeta["117"] = {
    "group_title": "Health and social services managers and directors",
    "group_description": "Managers and directors in health and social services plan, organise, direct and co-ordinate the activities and resources necessary for the efficient provision of primary and secondary health care services, social and other welfare services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1171"] = {
    "group_title": "Health services and public health managers and directors",
    "group_description": "Managers and directors in this unit group plan, organise, direct and co-ordinate the resources and activities of health care providers and purchasers at both district and unit levels.",
    "entry_routes_and_quals": "Entrants require a degree or equivalent qualification, a professional qualification and/or relevant experience. Off and on-the-job training is provided through management training schemes. The nature of schemes varies between regions and occupational areas.",
    "tasks": [
        "~implements policies of the board, ensures statutory procedures are followed, with particular emphasis on patient safety and the management of risk ~liaises with health care professionals to determine short and long-term needs and how to meet these objectives within budgetary constraints ~oversees the day-to-day management of the unit or service and provides leadership to staff ~uses statistical information to monitor performance and assist with planning ~negotiates and manages contracts with providers and purchasers of health care services ~manages staff, including recruitment, appraisal and development ~monitors and reports upon the effectiveness of services with a view to improving the efficiency of health care provision ~coordinates the promotion of public health and wellbeing in the actions and policies of public agencies and their social partners ~monitors and reports upon the state of public health and wellbeing",
    ],
}
SOCmeta["1172"] = {
    "group_title": "Social services managers and directors",
    "group_description": "Social services managers and directors plan, organise, direct and co-ordinate the resources and commission the services necessary to protect the welfare of certain groups within local authorities including children and young people, families under stress, people with disabilities, elderly people and people needing help as a result of illness.",
    "entry_routes_and_quals": "Entry is usually through internal promotion for those with the appropriate professional qualifications and relevant experience. Post-qualifying professional qualifications and in-service training are available.",
    "tasks": [
        "~provides leadership and management to ensure services are delivered in accordance with statutory requirements and in line with the local authority social services department\u2019s policies and procedures ~determines staffing, financial, material and other short and long-term needs ~plans work schedules, assigns tasks and delegates responsibilities of social services staff ~monitors and evaluates departmental performance with a view to improving social service provision ~studies and advises upon changes in legislation that will impact upon social service provision ~liaises with representatives of other relevant agencies",
    ],
}
SOCmeta["12"] = {
    "group_title": "Other managers and proprietors",
    "group_description": "Job holders in this sub-major group, either as employees or proprietors, manage agriculture related services; manage and co-ordinate the operations of health service general practices, residential and day care establishments and domiciliary care services; co-ordinate and direct the activities of businesses such as restaurants, hotels, entertainment establishments, sports and leisure facilities, travel and property agencies, independent shops, garages, waste disposal and environmental services, hairdressing establishments, the creative industries, betting and gambling establishments, hire services, consultancy services and agencies providing services outsourced by other organisations.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["121"] = {
    "group_title": "Managers and proprietors in agriculture related services",
    "group_description": "Jobholders in this minor group plan, organise, direct, and control the activities and resources of agricultural, forestry, fishing and similar establishments and services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1211"] = {
    "group_title": "Managers and proprietors in agriculture and horticulture",
    "group_description": "Managers and proprietors in this unit group plan, organise and co-ordinate the activities and resources of farming and mixed farming establishments cultivating arable crops, fruits, trees and shrubs, and/or raising cattle, sheep, pigs and poultry. Managers and proprietors in horticulture oversee the production of plants for wholesale and/or retail.",
    "entry_routes_and_quals": "Whilst no formal academic qualifications are required by proprietors in this area, most farm and horticultural managers have a vocational agricultural qualification (such as a BTEC/SQA award) and prior practical farming experience. Many farm and horticultural management jobs require a degree or equivalent qualification in a relevant subject. A small number of large farm and farm consultancy companies run graduate management training schemes. Apprenticeships are also available, as well as NVQs/SVQs in Agriculture at level 4.",
    "tasks": [
        "~determines financial, staffing and other short and long-term needs ~produces and maintains records of production, finance and breeding ~decides or advises on the types of crops and/or produce to be grown or livestock raised ~plans intensity and sequence of farm or horticultural operations and orders seed, fertiliser, equipment and other supplies ~markets and arranges for the sale of crops, livestock and other farm or horticultural produce",
    ],
}
SOCmeta["1212"] = {
    "group_title": "Managers and proprietors in forestry, fishing and related services",
    "group_description": "Managers and proprietors in this unit group plan, organise and co-ordinate the activities and resources of forestry, fishing, animal husbandry and related operations and establishments.",
    "entry_routes_and_quals": "Whilst no formal qualifications are required for proprietors in this area, forestry managers usually require a degree or equivalent qualification in forestry and prior relevant work experience. BTEC qualifications in fish farm management are available. Skippers of offshore fishing vessels require prior work experience and must undertake basic safety training by the Maritime and Coastguard Agency. Apprenticeships are available in some areas. Minimum age limits may apply in some areas of employment.",
    "tasks": [
        "~determines financial, staffing and other short- and long-term needs ~manages and trains staff ~decides, or advises on, type of animal to be bred and/or trained, and selects, buys and trains animals accordingly ~plans and directs the establishment and maintenance of forest /woodland areas and regularly inspects forest work ~liaises with neighbouring landowners, contractors and local authorities ~oversees facilities such as visitor centres, nature trails, footpaths, etc. ~selects suitable breeding grounds for shellfish, sea and freshwater fish and purchases stock ~arranges rearing and feeding and ensures health of fish stocks ~oversees maintenance of equipment and fish habitats ~plans fishing voyages, maintains vessel/s and equipment and oversees operational safety ~arranges for sale of catch, liaises with onshore agents ~ensures observance of maritime laws and international fishing regulations",
    ],
}
SOCmeta["122"] = {
    "group_title": "Managers and proprietors in hospitality and leisure services",
    "group_description": "Workers in this minor group plan, organise, direct and co-ordinate (usually with the help of other managers) the activities and resources of hotels, public houses and similar establishments, restaurants, recreation and entertainment establishments, leisure and sports facilities and travel agencies.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1221"] = {
    "group_title": "Hotel and accommodation managers and proprietors",
    "group_description": "Hotel and accommodation managers and proprietors plan, organise, direct and co-ordinate the activities and resources of halls of residence, hotels, hostels, caravan sites, holiday camps, holiday flats and chalets, and organise the domestic, catering, and entertainment facilities on passenger ships.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience. Candidates for these usually require a BTEC/SQA award, a degree or equivalent qualification, or a professional qualification. Off and on-the-job training is provided, and large hotel chains normally offer management trainee schemes. NVQs/SVQs in management for hospitality, leisure and tourism are available at levels 3 and 4 and apprenticeships at level 3.",
    "tasks": [
        "~analyses demand and decides on type, standard and cost of services to be offered ~determines financial, staffing, material and other short- and long-term needs ~ensures physical comfort of residents or passengers and makes special arrangements for children, the elderly and the infirm if required ~approves and arranges shipboard entertainment and shore trips and liaises with ship\u2019s agent to ensure that ship is adequately provisioned ~arranges for payment of bills, keeps accounts and ensures adherence to licensing and other statutory regulations",
    ],
}
SOCmeta["1222"] = {
    "group_title": "Restaurant and catering establishment managers and proprietors",
    "group_description": "Restaurant and catering establishment managers and proprietors plan, direct and co-ordinate the catering services of restaurants, hotels and large-scale catering services within other organisations.",
    "entry_routes_and_quals": "There are no set entry routes. Entry is possible with a variety of academic qualifications and/or relevant experience. Larger restaurants and catering chains offer managerial trainee schemes, entry to which may be based on a variety of qualifications and/or relevant experience. Off and on-the-job training is provided. Various vocational qualifications are available at levels 2 to 4.",
    "tasks": [
        "~plans catering services and directs staff ~decides on range and quality of meals and beverages to be provided ~discusses customer\u2019s requirements for special occasions ~purchases or directs the purchasing of supplies and arranges for preparation of accounts ~verifies that quality of food, beverages and waiting service is as required, that kitchen and dining areas are kept clean and appropriate hygiene standards are maintained in compliance with statutory requirements ~plans and arranges food preparation in collaboration with other staff and organises the provision of waiting or counter staff ~checks that supplies are properly used and accounted for to prevent wastage and loss and to keep within budget limit ~determines staffing, financial, material and other short- and long-term requirements",
    ],
}
SOCmeta["1223"] = {
    "group_title": "Publicans and managers of licensed premises",
    "group_description": "Publicans and managers of licensed premises organise, direct and co-ordinate the activities and resources of public houses (non-residential and residential) and bar and catering facilities at non-residential clubs.",
    "entry_routes_and_quals": "No formal academic qualifications are required. Relevant experience is advantageous, and candidates must be over 18 years of age and complete the personal licence holders\u2019 qualification. Larger chains offer accelerated promotion for holders of degrees or equivalent qualifications. Off and on-the-job training is provided. NVQs/SVQs relevant to licensed premises management are available at levels 2 to 4.",
    "tasks": [
        "~arranges purchase of alcoholic and other beverages, bar snacks, cigarettes and other items and ensures that stocks are stored in proper conditions ~supervises bar, kitchen and cleaning staff and, if necessary, assists with the serving of drinks ~observes licensing laws and other statutory regulations and regulates behaviour of customers as necessary ~maintains financial records for the establishment determines financial, staffing, material and other short- and long-term needs",
    ],
}
SOCmeta["1224"] = {
    "group_title": "Leisure and sports managers and proprietors",
    "group_description": "Leisure and sports managers organise and proprietors, direct and co-ordinate the activities and resources required for the provision of sporting, artistic, theatrical and other recreational and amenity services.",
    "entry_routes_and_quals": "Both graduate and non-graduate entry is possible. Off and on-the-job training is provided. Apprenticeships at level 3 and NVQs/SVQs at levels 3 and 4 are available in relevant areas. Professional qualifications may also be required for some posts.",
    "tasks": [
        "~organises timetable of activities/schedule of programmes ~ensures that facilities are kept clean and in good condition and that appropriate health and safety requirements are adhered to ~keeps abreast of new trends and developments in recreational activities and arranges exhibitions, theatrical productions, concerts, demonstrations, etc ~advises on the facilities available and promotes publicity in relation to shows, games, races, new theme parks, etc ~determines financial, staffing, material and other short and long-term needs ~recruits, supervises and trains staff ~ensures custody of all cash receipts and organises regular stock checks",
    ],
}
SOCmeta["1225"] = {
    "group_title": "Travel agency managers and proprietors",
    "group_description": "Travel agency managers and proprietors plan, organise, direct and co-ordinate the resources and activities of travel agencies and booking offices.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades but is possible with other academic qualifications and/or relevant experience. Off and on-the-job training is available. BTEC/SQA awards and NVQs/SVQs at level 3 are available.",
    "tasks": [
        "~plans work schedules and assigns tasks and responsibilities ~co-ordinates the activities of clerical, secretarial and other staff ~discusses client\u2019s requirements and advises on road, rail, air and sea travel and accommodation ~makes and confirms travel and accommodation bookings, arranges group holidays, tours and individual itineraries ~advises on currency and passport/visa regulations and any necessary health precautions needed ~determines financial, staffing, material and other short- and long-term needs",
    ],
}
SOCmeta["123"] = {
    "group_title": "Managers and proprietors in health and care services",
    "group_description": "Job holders in this minor group manage and coordinate the work and resources of health care practices, residential and day care establishments and domiciliary care services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1231"] = {
    "group_title": "Health care practice managers",
    "group_description": "Healthcare practice managers plan, organise, direct and co-ordinate the work and resources of medical, dental and other types of healthcare practice, including veterinary practices.",
    "entry_routes_and_quals": "There are no pre-set entry requirements. Candidates are recruited with a variety of academic qualifications or with relevant experience. Professional qualifications are available and are required for certain posts.",
    "tasks": [
        "~plans work schedules, assigns tasks and delegates responsibilities of practice staff ~oversees staff training and monitors training needs ~takes responsibility for health and safety matters within the practice ~negotiates contracts for services with other health care providers and purchasers ~maintains patient files on medical history, consultations and treatment undertaken and/or drugs prescribed ~organises duty rosters for professional and support staff in practice ~takes responsibility for stock control of practice equipment, drugs, etc ~liaises with relevant outside organisations (e.g. NHS trust, PCT, social services, drug companies, professional bodies) ~responsible for budgeting, pricing and accounting activities within the practice",
    ],
}
SOCmeta["1232"] = {
    "group_title": "Residential, day and domiciliary care managers and proprietors",
    "group_description": "Managers and proprietors in this group plan, organise, direct and co-ordinate the resources necessary in the provision and running of residential and day care establishments and domiciliary care services for persons who require support or specialised care and/or supervision.",
    "entry_routes_and_quals": "Although there are no pre-set academic entry requirements there are a variety of entry routes. However, entrants must be registered with the relevant statutory body and hold the appropriate qualification for the job they do. Off and on-the-job training is provided, and a range of qualifications are available including NVQs/SVQs in Health and Social Care at levels 3 and 4. Background checks including a DBS check are required.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term requirements ~plans work schedules, assigns tasks and delegates responsibilities to staff ~arranges for payment of bills, keeps accounts and adheres to health, safety and other statutory requirements ~maintains contact between service users and the local community and/or family and friends ~assesses service users\u2019 needs and ensures they have access to health and social care services as required ~creates a friendly, secure atmosphere to gain the trust and confidence of those using the service ~ensures that the physical comfort and all material needs of service users are provided and attempts to resolve problems that may arise",
    ],
}
SOCmeta["1233"] = {
    "group_title": "Early education and childcare services proprietors",
    "group_description": "Early childhood and childcare services proprietors plan, organise, direct and co-ordinate the activities and resources of residential or day nurseries, play groups, and similar establishments.",
    "entry_routes_and_quals": "Whilst no formal academic qualifications are required by proprietors in this area, a range of relevant courses in early years childcare and management are available. A DBS check is necessary if you run or own a childcare organisation.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term requirements ~plans work schedules, assigns tasks and delegates responsibilities of staff ~oversees the learning of young children and ensures that Early Years Foundation Stage and OFSTED standards are met ~provides leadership and management to staff to ensure services are delivered to a high quality ~develops relationships with children's parents and other educational establishments ~ensures the facilities are well maintained and that health and safety standards and other relevant regulations are met",
    ],
}
SOCmeta["124"] = {
    "group_title": "Managers in logistics, warehousing and transport",
    "group_description": "Managers in logistics, warehousing and transport plan, organise, and co-ordinate the activities and resources necessary for the efficient and convenient transportation of passengers or freight, and the loading, unloading, storage, warehousing and distribution of goods and materials.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1241"] = {
    "group_title": "Managers in transport and distribution",
    "group_description": "Managers in transport and distribution plan, organise, and co-ordinate the activities and resources necessary for the safe, efficient and economic movement of passengers and freight by road, rail, sea and air transport.",
    "entry_routes_and_quals": "Candidates are recruited with a variety of academic qualifications and/or with relevant experience. Entrants to management trainee schemes offered by larger companies will require GCSEs/S grades, A levels/H grades, a degree or other equivalent qualifications. Off and on-the-job training is provided. Professional qualifications are available and may be required for some roles. NVQs/SVQs in a number of relevant areas including supply chain and operations management are available at levels 2, 3, 4 and 5.",
    "tasks": [
        "~plans the optimum utilisation of staff and operating equipment, and co-ordinates maintenance activities to ensure least possible disruption to services ~co-ordinates the transportation of passengers, the movement, handling and storage of freight in transit, and reviews space utilisation, staffing and distribution expenditure to determine future distribution policies ~ensures that regulations regarding hours of work, the licensing of crews and transport equipment, the operational safety and efficiency of equipment, the insurance of vehicles and other statutory regulations are complied with ~ensures that harbour channels and berths are maintained and liaises with ship owners, crew, customs officials, dock and harbour staff to arrange entry, berthing and servicing of ships ~supervises day-to-day activities in a railway station ~arranges for maintenance of airport runways and buildings, liaises with fuel and catering crews to ensure adequate supplies and resolves any complaints and problems raised by airport users",
    ],
}
SOCmeta["1242"] = {
    "group_title": "Managers in storage and warehousing",
    "group_description": "Managers in storage and warehousing plan, organise, and co-ordinate the activities and resources necessary for the safe and efficient receipt, storage and warehousing of goods and for the maintenance of stocks at an optimal level.",
    "entry_routes_and_quals": "Candidates are recruited with a variety of academic qualifications and/or with relevant experience. Entrants to management trainee schemes offered by larger companies will require GCSEs/S grades, A levels/H grades, a degree or other equivalent qualifications. Off and on-the-job training is provided. Professional and vocational qualifications covering a number of areas including supply chain and operations management are available at NVQ/SVQ levels 2, 3, 4 and 5.",
    "tasks": [
        "~liaises with production, maintenance, sales and other departments to determine the materials and other items required for current and future production schedules and sales commitments ~reviews, develops and implements stock control, handling and distribution policies to maximise use of space, money, labour and other resources ~advises purchasing department on type, quality and quantity of goods required and dates by which they must be available ~prepares reports on expenditure and advises on materials and parts standardisation, future stores and stock control policies ~decides on storage conditions for particular items, allocates warehouse space and arranges for regular stock inspections to detect deterioration or damage",
    ],
}
SOCmeta["1243"] = {
    "group_title": "Managers in logistics",
    "group_description": "Managers in logistics plan, co-ordinate and organise the supply chain of goods and services between the point of production and consumption, including their efficient transportation, storage and retailing.",
    "entry_routes_and_quals": "Candidates are recruited with a variety of academic qualifications and/or with relevant experience. Entrants to management trainee schemes offered by larger companies will require GCSEs/S grades, A levels/H grades, a degree or other equivalent qualifications. Off and on-the-job training is provided. Professional qualifications are available and may be required for some roles. NVQs/SVQs in a number of relevant areas including supply chain and operations management are available at levels 2, 3, 4 and 5.",
    "tasks": [
        "~management and planning of supply chains from source to the point of consumption to ensure goods get from suppliers to distribution centres as efficiently as possible ~co-ordinates the transportation and storage of goods ~monitors the distribution of goods and stock levels to ensure the organisation's needs are met and reports on overall performance ~advises purchasing department on type, quality and quantity of goods required and dates by which they must be available and negotiates contracts with suppliers ~ensures that regulations regarding hours of work, the licensing of crews and transport equipment, the operational safety and efficiency of equipment, the insurance of vehicles and other statutory regulations are complied with",
    ],
}
SOCmeta["125"] = {
    "group_title": "Managers and proprietors in other services",
    "group_description": "Job holders in this minor group plan, co-ordinate and direct the activities and resources of property services, garages, hairdressers and other personal services, , waste and recycling facilities, the creative industries, betting and gambling establishments, hire services, consultancy services, and other services not elsewhere classified in sub-major group 12: Other Managers and Proprietors.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["1251"] = {
    "group_title": "Property, housing and estate managers",
    "group_description": "Property, housing and estate managers manage shopping centres, residential areas, offices and private estates, arrange for the sale, purchase, rental and leasing of property on behalf of clients and employers, and provide facilities management services for businesses",
    "entry_routes_and_quals": "There are no formal academic requirements, although entrants usually possess a BTEC/SQA award, a degree or equivalent qualification. Apprenticeships are available in some areas. Many employers expect the attainment of membership to a relevant professional body.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term requirements ~manages general upkeep, maintenance and security of the estate\u2019s amenities ~makes sure that the amenities meet health and safety standards and legal requirements ~oversees the support services of a business, such as catering, IT, utilities and physical environment ~advises on energy efficiency ~discusses client\u2019s requirements and may advise client on the purchase of property and land for investment and other purposes ~conducts or arranges for structural surveys of properties and undertakes any necessary valuations of property or agricultural land, and deals with grant and subsidy applications ~negotiates land or property purchases and sales or leases and tenancy agreements and arranges legal formalities with solicitors, building societies and other parties ~maintains or arranges for the maintenance of estate accounts and records and produces financial forecasts ~acts as arbiter in disputes between landlord and tenant and ensures that both fulfil their legal obligations ~examines and assesses housing applications, advises on rent levels, investigates complaints and liaises with tenants\u2019 association and social workers to resolve any family problems",
    ],
}
SOCmeta["1252"] = {
    "group_title": "Garage managers and proprietors",
    "group_description": "Garage managers and proprietors plan, organise, direct and co-ordinate the day-to-day running of garages and specialist vehicle maintenance and repair establishments.",
    "entry_routes_and_quals": "There are no pre-set entry requirements, although some employers may require relevant experience and GCSEs/S grades or vocational qualifications such as Automotive NVQs/SVQs at level 3. Off and on-the-job training is provided.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term requirements ~ensures that necessary spare parts, materials and equipment are available or obtainable at short notice ~arranges for maintenance staff to perform necessary maintenance and repair work on vehicles or motorcycles ~checks completed work for compliance with safety and other statutory regulations ~maintains records of repair work to detect recurrent faults ~provides information about garage merchandise for staff and customers ~ensures the business accounts are maintained",
    ],
}
SOCmeta["1253"] = {
    "group_title": "Hairdressing and beauty salon managers and proprietors",
    "group_description": "Hairdressing and beauty salon managers and proprietors plan, organise, direct and co-ordinate the activities and resources of hairdressing and nail salons, beauty treatment, pet grooming and similar establishments.",
    "entry_routes_and_quals": "No formal qualifications are required for entry although entrants usually possess a BTEC/SQA award, an NVQ/SVQ in Hairdressing at level 3, an apprenticeship and/or relevant experience.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term needs ~controls the allocation, training and remuneration of staff ~provides clients with information and advice on styles and treatments, and resolves any complaints or problems ~ensures clients\u2019 records are maintained ~undertakes and/or directs hair treatments and/or beauty therapy ~checks and maintains any equipment, and ensures that all safety requirements are met ~demonstrates, advises on and sells hair and/or beauty products ~ensures financial accounts for the business are maintained",
    ],
}
SOCmeta["1254"] = {
    "group_title": "Waste disposal and environmental services managers",
    "group_description": "Waste disposal and environmental services managers plan, organise, direct and co-ordinate the operations and development of waste disposal and related environmental services facilities within private firms or public authorities.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications, including a degree or equivalent qualification in a related subject, and/or relevant experience. Apprenticeships and NVQs at levels 3 and 4 and professional qualifications are available. Professional qualifications are available from the Chartered Institute of Wastes Management and may be mandatory in some operational management posts.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term requirements ~manages and delegates tasks to staff and co-ordinates the maintenance and optimum utilisation of waste disposal and related equipment to provide an efficient service ~monitors levels of waste disposal, recycling and related environmental services, compiles statistics and produces reports ~liaises with members of the local community to educate and promote the concept of recycling and appropriate waste management ~keeps up to date with new legislation and liaises with appropriate regulatory bodies to ensure compliance with legislation regarding waste disposal and environmental services ~co-ordinates the resources and activities relating to the procurement, collection, storage, processing and sale of scrap metal and related products",
    ],
}
SOCmeta["1255"] = {
    "group_title": "Managers and directors in the creative industries",
    "group_description": "Managers and directors in creative industries plan, organise, direct and co-ordinate the activities and resources of organisations in sectors such as arts, publishing, music, media, design and architecture.",
    "entry_routes_and_quals": "Entry requirements vary according to the specific sector. Most post holders will have relevant experience and while some fields do not require candidates to have academic qualifications others require a degree or equivalent qualification. Off and on-the-job training may be provided, and vocational qualifications are available in many of these sectors.",
    "tasks": [
        "~plans, organises, directs and co-ordinates the activities and resources of organisations in the creative industries, such as publishing firms, art galleries and television companies ~liaises with clients, generates new business and promotes their organisation by attending and organising conferences, exhibits and other events ~helps set the creative direction of their organisation and finds new talent, such as artists, writers and musicians, as well as pieces such as artworks, scripts and music ~keeps up to date with new releases, publications and trends in relevant fields ~establishes client's requirements and oversees the conception and development of multiple projects ~reviews and revises creative teams' work across multiple projects ~determines staffing, material, financial, and other short- and long-term needs",
    ],
}
SOCmeta["1256"] = {
    "group_title": "Betting shop and gambling establishment managers",
    "group_description": "Betting shop managers plan, organise, direct and co-ordinate the activities of betting shops and gambling establishments.",
    "entry_routes_and_quals": "There are no formal qualifications for entry although entrants may be required to pass a maths test and have relevant experience. NVQs in Gambling Operations at level 2 and 3 are available.",
    "tasks": [
        "~co-ordinates the work of other staff, plans work schedules and assigns tasks and responsibilities ~maintains the accounts of betting shops and manages the budget ~determines staffing, material, financial and other short- and long-term needs. ~ensures compliance with relevant legislation and regulations ~provides customer service and deals with customer complaints ~promotes the betting shop and generates new business",
    ],
}
SOCmeta["1257"] = {
    "group_title": "Hire services managers and proprietors",
    "group_description": "Managers and proprietors in hire services plan, organise and direct the activities of businesses which hire goods and services, such as tools, heavy machinery and vehicles.",
    "entry_routes_and_quals": "There are no pre-set qualification requirements however, relevant experience is usually essential and qualifications in engineering or other relevant services may be an advantage.",
    "tasks": [
        "~plans the optimum utilisation of staff and operating equipment, and co-ordinates maintenance activities to ensure least possible disruption to services. ~ensures that necessary spare parts, materials and equipment are available or obtainable at short notice ~liaises with clients, generates new business and negotiates contracts with suppliers and clients ~determines staffing, financial, material and other short- and long-term requirements ~ensures compliance with safety and other statutory regulations ~provides information about machinery, tools and other goods for hire to staff and customers ~ensures the business accounts are maintained",
    ],
}
SOCmeta["1258"] = {
    "group_title": "Directors in consultancy services",
    "group_description": "Directors in consultancy services plan, organise, direct and co-ordinate the activities, resources and development of consultancies working in a variety of sectors, liaise with clients and promotes their business.",
    "entry_routes_and_quals": "Relevant experience is required and depending on the field you may need a relevant technical qualification at degree level or a vocational qualification at levels 4 and 5. On-the-job training may be available, and some firms offer accelerated promotion for graduates. Professional qualifications are available.",
    "tasks": [
        "~determines staffing, financial and other short- and long-term requirements ~plans work schedules, assigns tasks and delegates responsibilities to staff ~builds relationships with clients, the local business community and relevant organisations and promotes their business ~oversees and advises multiples projects to ensure they are delivered on time and to a high quality and contributes to the assessment of clients' needs ~plans and directs research into business' strategy, policy, organisation, procedures, methods and markets and evaluates the results ~reviews and advises on recommendations to clients with a view to maximising growth and improving business performance",
    ],
}
SOCmeta["1259"] = {
    "group_title": "Managers and proprietors in other services n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of managerial tasks in other service industries not elsewhere classified in minor group 125: Managers and proprietors in other services.",
    "entry_routes_and_quals": "Entry requirements vary according to the particular company and/or service. Some companies do not require candidates to have academic qualifications, but others require a degree or equivalent qualification. Off and on-the-job training may be provided.",
    "tasks": [
        "~determines staffing, financial, material and other short- and long-term requirements ~ensures that adequate reserves of merchandise are held and that stock keeping is carried out efficiently ~authorises payment for supplies received and decides on vending price and credit terms ~examines quality of merchandise and ensures that effective use is made of advertising and display facilities ~manages agencies to provide services out-sourced by other organisations and businesses ~ensures maintenance of appropriate service levels to meet the objectives of the business",
    ],
}
SOCmeta["2"] = {
    "group_title": "Professional occupations",
    "group_description": "This major group covers occupations whose main tasks require a high level of knowledge and experience in the natural sciences, engineering, life sciences, social sciences, humanities and related fields. The main tasks consist of the practical application of an extensive body of theoretical knowledge, increasing the stock of knowledge by means of research and communicating such knowledge by teaching methods and other means. Most occupations in this major group will require a degree or equivalent qualification, with some occupations requiring postgraduate qualifications and/or a formal period of experience-related training.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["21"] = {
    "group_title": "Science, research, engineering and technology professionals",
    "group_description": "Professionals in this sub-major group undertake research and consultancy activities within the physical and social sciences and in the humanities; technically supervise the development, installation and maintenance of mechanical, chemical, structural and electrical systems; advise upon and direct the technical aspects of production programmes; provide consultancy and development services in the provision and utilisation of information technology; direct and advise upon the conservation and protection of the environment; design and develop websites, use illustrative, sound, visual and multimedia techniques in marketing, film, computer games and other areas, and direct and advise upon the research and development operations of an organisation.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["211"] = {
    "group_title": "Natural and social science professionals",
    "group_description": "Natural and social science professionals are involved in planning, directing and undertaking research across all of the natural sciences and in the social sciences which encompasses the humanities.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2111"] = {
    "group_title": "Chemical scientists",
    "group_description": "Chemical scientists analyse and research physical aspects of chemical structure and change within substances and develop chemical techniques used in the manufacture or modification of natural substances and processed products.",
    "entry_routes_and_quals": "Entrants usually possess a degree. Entry may also be possible with an appropriate BTEC/SQA award, an Advanced GNVQ/GSVQ level III, or other academic qualifications. Further specialist training is provided on the job. Some employers may expect entrants to gain professional qualifications.",
    "tasks": [
        "~develops experimental procedures, instruments and recording and testing systems ~operates specialised scientific equipment and conducts experiments to identify chemical composition, energy and chemical changes in natural substances and processed materials ~analyses results and experimental data ~tests techniques and processes for reliability under a variety of conditions ~develops procedures for quality control of manufactured products",
    ],
}
SOCmeta["2112"] = {
    "group_title": "Biological scientists",
    "group_description": "Biological scientists examine and investigate the morphology, structure, and physical characteristics of living organisms, including their inter-relationships, environments and diseases.",
    "entry_routes_and_quals": "Entrants usually possess a degree and some roles may require a postgraduate qualification. Entry may also be possible with an appropriate BTEC/SQA award, an HNC/NHD, or other academic qualifications. Further specialist training is provided on the job. Some employers may expect entrants to gain professional qualifications.",
    "tasks": [
        "~studies the physical form, structure, composition and function of living organisms ~researches the effects of internal and external environmental factors on the life processes and other functions of living organisms ~observes the structure of communities of organisms in the laboratory and in their natural environment ~advises farmers, medical staff and others, on the nature of field crops, livestock and produce and on the treatment and prevention of disease ~monitors the distribution, presence and behaviour of plants, animals and aquatic life, and performs other scientific tasks related to conservation not performed by Job holders in MINOR GROUP 215: Conservation and Environment Professionals",
    ],
}
SOCmeta["2113"] = {
    "group_title": "Biochemists and biomedical scientists",
    "group_description": "Biochemists and biomedical scientists examine and investigate the chemical processes of living organisms, including their inter-relationships, environments and diseases, and perform laboratory tests on tissue, blood and other samples to diagnose diseases, toxins or health conditions.",
    "entry_routes_and_quals": "Entrants usually possess a degree. Entry may also be possible with an appropriate BTEC/SQA award, an HNC/NHD, or other academic qualifications. Further specialist training is provided on the job. Some employers may expect entrants to hold a postgraduate qualification or gain professional qualifications.",
    "tasks": [
        "~studies the chemical form, structure, composition and function of living organisms ~identifies and studies the chemical substances, including microbial infections, involved in physiological processes and the progress of disease ~performs tests to study physiological and pathological characteristics within cells and other organisms ~researches the effects of internal and external environmental factors on the life processes and other functions of living organisms ~performs tests to help clinicians diagnose and treat various conditions, evaluates existing treatments and researches new ways to treat diseases ~researches, develops and quality checks new products in the pharmaceuticals, food production and agricultural Industries",
    ],
}
SOCmeta["2114"] = {
    "group_title": "Physical scientists",
    "group_description": "Physical scientists study relationships between matter, energy and other physical phenomena, the nature, composition and structure of the Earth and other planetary bodies and forecast weather conditions and electrical, magnetic, seismic and thermal activity.",
    "entry_routes_and_quals": "Entrants usually possess a degree, although entry may also be possible with an appropriate BTEC/SQA award. Further specialist training is provided on the job. Higher degrees and professional qualifications are available, and some employers may require a postgraduate qualification.",
    "tasks": [
        "~conducts experiments and tests and uses mathematical models and theories to investigate the structure and properties of matter, transformations and propagations of energy, the behaviour of particles and their interaction with various forms of energy ~uses surveys, seismology and other methods to determine the earth\u2019s mantle, crust, rock structure and type, and to analyse and predict the occurrence of seismological activity ~observes, records and collates data on atmospheric conditions from weather stations, satellites, and observation vessels to plot and forecast weather conditions ~applies mathematical models and techniques to assist in the solution of scientific problems in industry and commerce and seeks out new applications of mathematical analysis",
    ],
}
SOCmeta["2115"] = {
    "group_title": "Social and humanities scientists",
    "group_description": "Social and humanities scientists study and analyse human behaviour and the origin, structure and characteristics of language undertake research in areas such as sociology, economics, politics, archaeology, history, philosophy, literature, the arts organise the collection of qualitative and quantitative information and perform subsequent analyses.",
    "entry_routes_and_quals": "Entry is most common with a degree or equivalent qualification but is possible with other academic qualifications and/or relevant experience. Postgraduate qualifications may be required for some jobs.",
    "tasks": [
        "~studies society and the manner in which people behave and impact upon the world ~undertakes research across the humanities that furthers understanding of human culture and creativity ~traces the evolution of word and language forms, compares grammatical structures and analyses the relationships between ancient, parent and modern languages ~identifies, compiles and analyses economic, demographic, legal, political, social and other data to address research objectives ~administers questionnaires, carries out interviews, organises focus groups and implements other social research tools ~undertakes analyses of data, presents results of research to sponsors, the media and other interested organisations ~addresses conferences and publishes articles detailing the methodology and results of research undertaken",
    ],
}
SOCmeta["2119"] = {
    "group_title": "Natural and social science professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of scientific research and related activities not elsewhere classified in minor group 211: Natural and social science professionals.",
    "entry_routes_and_quals": "Entry is most common with a degree or equivalent qualification but is possible with other academic qualifications and/or relevant experience. On-the-job training and/or support for postgraduate study may be provided. Professional qualifications are available in some areas of activity.",
    "tasks": [
        "~plans, directs and undertakes research into natural phenomena ~provides technical advisory and consulting services ~designs tests and experiments to address research objective and find solutions ~applies models and techniques to medical, industrial, agricultural, military and similar applications ~analyses results and writes up results of tests and experiments undertaken ~presents results of scientific research to sponsors, addresses conferences and publishes articles outlining the methodology and results of research undertaken ~designs and develops an appropriate research methodology in order to address the research objective ~compiles and analyses quantitative and qualitative data, prepares reports and presents results to summarise main findings and conclusions ~advises government, private organisations and special interest groups on policy issues ~writes journal articles, books, and addresses conferences, seminars and the media to reveal research findings",
    ],
}
SOCmeta["212"] = {
    "group_title": "Engineering professionals",
    "group_description": "Engineering professionals plan, organise and technically supervise the construction, testing, installation and maintenance of mechanical, structural, chemical, electrical, electronic, aeronautical and astronautical systems and equipment, advise and direct technical aspects of production programmes, and plan production schedules and work procedures to ensure efficiency and quality. Engineering project managers and project engineers schedule, manage and oversee engineering projects.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2121"] = {
    "group_title": "Civil engineers",
    "group_description": "Civil engineers undertake research and design, direct construction and manage the operation and maintenance of civil and mining engineering structures.",
    "entry_routes_and_quals": "Civil engineers usually possess an accredited three or four year degree in civil engineering or engineering science or an accredited Higher National Diploma or Certificate. The status of \u2018incorporated engineer\u2019 is obtained upon the completion of further training at work and associate membership of a chartered engineering institution. The status of \u2018chartered engineer\u2019 is achieved through the completion of postgraduate training and full membership of a chartered engineering institution.",
    "tasks": [
        "~undertakes research and advises on soil mechanics, concrete technology, hydraulics, water and waste water treatment processes and other civil engineering matters ~determines and specifies construction methods, materials, quality and safety standards and ensures that equipment operation and maintenance comply with design specifications ~designs foundations and earthworks ~designs structures such as roads, dams, bridges, railways, hydraulic systems, sewerage systems, industrial and other buildings and plans the layout of tunnels, wells and construction shafts ~organises and plans projects, arranges work schedules, carries out inspection work and plans maintenance control ~organises and establishes control systems to monitor operational efficiency and performance of materials and systems",
    ],
}
SOCmeta["2122"] = {
    "group_title": "Mechanical engineers",
    "group_description": "Mechanical engineers undertake research, design and development, direct the manufacture and manage the operation and maintenance of engines, machines, vehicle and ships\u2019 structures, building services and other mechanical items.",
    "entry_routes_and_quals": "Mechanical engineers usually possess an accredited university degree. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution is attainable. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship leading to an NVQ/SVQ at level 4, followed by periods of training and relevant experience.",
    "tasks": [
        "~undertakes research and advises on energy use, materials handling, thermodynamic processes, fluid mechanics, vehicles and environmental controls ~determines materials, equipment, piping, capacities, layout of plant or system and specification for manufacture ~designs and develops mechanical equipment, such as steam, internal combustion and other non-electrical motors for railway locomotives, road vehicles and other machinery ~ensures that equipment, operation and maintenance comply with design specifications and safety standards ~organises and establishes control systems to monitor operational efficiency and performance of materials and systems",
    ],
}
SOCmeta["2123"] = {
    "group_title": "Electrical engineers",
    "group_description": "Electrical engineers undertake research and design, direct construction and manage the operation and maintenance of electrical equipment, power stations, building control systems and other electrical products and systems.",
    "entry_routes_and_quals": "Electrical engineers usually possess an accredited university degree or equivalent qualification. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution is attainable. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship leading to an NVQ/SVQ at level 4. All routes are followed by periods of appropriate training and relevant experience.",
    "tasks": [
        "~conceives and develops engineering designs from product ideas in electrical engineering ~supervises, controls and monitors the operation of electrical generation, transmission and distribution systems ~determines and specifies manufacturing methods of electrical systems ~ensures that manufacture, operation and maintenance comply with design specifications and contractual arrangements ~organises and establishes control systems to monitor the performance and safety of electrical assemblies and systems",
    ],
}
SOCmeta["2124"] = {
    "group_title": "Electronics engineers",
    "group_description": "Electronics engineers undertake research and design, direct construction and manage the operation and maintenance of electronic motors, communications systems, microwave systems, and other electronic equipment.",
    "entry_routes_and_quals": "Electronics engineers usually possess an accredited university degree or equivalent qualification. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution is attainable. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship. All routes are followed by periods of appropriate training and relevant experience.",
    "tasks": [
        "~undertakes research and advises on all aspects of telecoms equipment, radar, telemetry and remote-control systems, data processing equipment, microwaves and other electronic equipment ~conceives and develops engineering designs from product ideas in electronics engineering ~determines and specifies appropriate production and/or installation methods and quality and safety standards ~organises and establishes control systems to monitor performance and evaluate designs ~tests, diagnoses faults and undertakes repair of electronic equipment",
    ],
}
SOCmeta["2125"] = {
    "group_title": "Production and process engineers",
    "group_description": "Production and process engineers advise on and direct technical aspects of production programmes to ensure cost-effectiveness and efficiency. This unit group incorporates: planning and quality control engineers who plan production schedules, work sequences, and manufacturing and processing procedures to ensure accuracy, quality and reliability; and chemical engineers who undertake research on commercial scale chemical processes and processed products, design and provide specifications and direct the construction, operation, maintenance and repair of chemical plants and control systems.",
    "entry_routes_and_quals": "Production and process engineers usually possess an accredited university degree. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship leading to an NVQ/SVQ at level 4. All routes are followed by periods of appropriate training and relevant experience.",
    "tasks": [
        "~studies existing and alternative production methods, regarding work flow, plant layout, types of machinery and cost ~recommends optimum equipment and layout and prepares drawings and specifications ~devises and implements production control methods to monitor operational efficiency ~investigates and eliminates potential hazards and bottlenecks in production ~advises management on and ensures effective implementation of new production methods, techniques and equipment ~liaises with materials buying, storing and controlling departments to ensure a steady flow of supplies ~undertakes research and develops processes to achieve physical and/or chemical change for oil, pharmaceutical, synthetic, plastic, food and other products ~designs, controls and constructs process plants to manufacture products",
    ],
}
SOCmeta["2126"] = {
    "group_title": "Aerospace engineers",
    "group_description": "Aerospace engineers research develop and design aircraft, spacecraft and their components.",
    "entry_routes_and_quals": "Job holders in this unit group usually possess a degree or equivalent qualification in a relevant field. Qualified aircraft engineers need a licence issued by the Civil Aviation Authority.",
    "tasks": [
        "~conceives and develops engineering designs from product ideas in aerospace engineering ~organises and plans projects, arranges work schedules, carries out inspection work and plans maintenance control ~analyses test data",
        "undertakes research and advises on all aspects of aircraft, spacecraft and their systems ~ensures that equipment, operation and maintenance comply with design specifications and safety standards ~inspects completed aircraft maintenance work to certify that it meets standards and the aircraft is ready for operation",
    ],
}
SOCmeta["2127"] = {
    "group_title": "Engineering project managers and project engineers",
    "group_description": "Engineering project managers and project engineers schedule, manage and oversee engineering projects for quality of work, timeliness and completion within budget, plan, design and specify materials and equipment for the project and create necessary technical drawings.",
    "entry_routes_and_quals": "Engineering project managers and project engineers usually possess an accredited university degree. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution is attainable. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship leading to an NVQ/SVQ at level 4. All routes are followed by periods of appropriate training and relevant experience.",
    "tasks": [
        "~draws up budgets and timescales for new engineering projects based on clients\u2019 requirements ~briefs project team, contractors and suppliers ~assembles information for invoicing at the end of projects ~plans work schedules for engineering projects based on prior discussion with client and contractors ~regularly inspects and monitors progress and quality of work, ensures legal requirements are met ~identifies defects in work and proposes corrections ~records, monitors and reports progress ~ensures that equipment, operation and maintenance comply with design specifications and safety standards",
    ],
}
SOCmeta["2129"] = {
    "group_title": "Engineering professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of professional engineering functions not elsewhere classified in minor group 212: Engineering professionals.",
    "entry_routes_and_quals": "Chartered engineers possess an accredited university degree. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution is attainable. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship leading to an NVQ/SVQ at level 4. All routes are followed by periods of appropriate training and relevant experience.",
    "tasks": [
        "~researches into problem areas to advance basic knowledge, evaluate new theories and techniques and to solve specific problems ~establishes principles and techniques to improve the quality, durability and performance of materials such as textiles, glass, rubber, plastics, ceramics, metals and alloys ~designs new systems and equipment with regard to cost, market requirements and feasibility of manufacture ~devises and implements control systems to monitor operational efficiency and performance of system and materials ~prepares sketches, drawings and specifications showing materials to be used, construction and finishing methods and other details ~examines and advises on patent applications ~provides technical consultancy services",
    ],
}
SOCmeta["213"] = {
    "group_title": "Information technology professionals",
    "group_description": "Information technology professionals advise clients (both internal and external) as to the effective utilisation of information technology, develop and implement systems and software for those clients, manage major information technology projects and carry out specialised information technology.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2131"] = {
    "group_title": "IT project managers",
    "group_description": "IT project managers manage, coordinate and technically supervise specific IT projects of a discrete duration and/or budget.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~works with client or senior management to establish and clarify the aims, objectives and requirements of the IT project ~plans the stages of the project, reviews actions and amends plans as necessary ~coordinates and supervises the activities of the project team ~manages third party contributions to the project ~monitors progress including project budget, timescale and quality ~coordinates and oversees implementation of the project ~reports on project to senior management and/or client",
    ],
}
SOCmeta["2132"] = {
    "group_title": "IT managers",
    "group_description": "IT managers plan, organise, manage and coordinate the provision of IT and telecommunications services and functions in an organisation.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~plans, coordinates and manages the organisation\u2019s IT and telecommunications provision or a specialist area of IT activity ~liaises with users, senior staff and internal/external clients to clarify IT and telecommunications requirements and development needs ~takes responsibility for managing the development of an aspect of IT and telecommunications provision such as user support, network operations, service delivery or quality control ~supervises the technical team and coordinates training ~plans and monitors work and maintenance schedules to ensure agreed service levels are achieved ~reports on IT and telecommunications activities to senior management",
    ],
}
SOCmeta["2133"] = {
    "group_title": "IT business analysts, architects and systems designers",
    "group_description": "IT business analysts, architects and systems designers proviide advice on the effective utilisation of IT and design IT systems in order to meet the business objectives or to enhance the business effectiveness of the organisation.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~liaises with internal/external clients to analyse business procedure, clarify clients\u2019 requirements and to define the scope of existing software, hardware and network provision ~undertakes feasibility studies for major IT developments incorporating costs and benefits, and presents proposals to clients ~communicates the impact of emerging technologies to clients and advises upon the potential introduction of such technology ~provides advice and assistance in the procurement, provision, delivery, installation, maintenance and use of IT systems and their environments ~examines existing business models and flows of data and designs functional specifications and test plans for new systems in order to meet clients\u2019 needs ~researches, analyses, evaluates and monitors network infrastructure and performance ~works closely with clients to implement new systems",
    ],
}
SOCmeta["2134"] = {
    "group_title": "Programmers and software development professionals",
    "group_description": "Programmers and software development professionals design, develop, test, implement and maintain software systems on a range of platforms in order to meet the specifications and business objectives of the information system; they also design and develop specialist software e.g. for computer games.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~examines existing software and determines requirements for new/modified systems in the light of business needs ~undertakes feasibility study to design software solutions ~writes and codes individual programs according to specifications ~develops user interfaces ~tests and corrects software programs ~writes code for specialist programming for computer games, (for example, artificial intelligence, 3D engine development) ~implements and evaluates the software ~plans and maintains database structures ~writes operational documentation and provides subsequent support and training for users ~develops website and website interfaces and establishes methods to ensure appropriate website security and recovery",
    ],
}
SOCmeta["2135"] = {
    "group_title": "Cyber security professionals",
    "group_description": "Cyber security professionals design, implement, test and maintain cyber security systems and track, investigate and analyse data linked to cybercrime.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~examines IT system for potential threats to its security and integrity and draws up response plans for situations where security is compromised ~develops test plans for security systems and undertakes and documents the testing of security systems weaknesses and errors, identifies source of problems and proposes solutions ~develops quality standards and validation techniques ~makes recommendations concerning software/system quality ~deals with and reports on breaches in security ~uses specialist software to gather and analyse information and evidence relating to cybercrime and presents findings to law enforcement officials or private clients",
    ],
}
SOCmeta["2136"] = {
    "group_title": "IT quality and testing professionals",
    "group_description": "IT quality and testing professionals test the quality of IT software, systems and computer games and identify and recommend solutions to problems and improvements that could be made.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~undertakes the testing of software, systems or computer games for errors, identifies source of problems and proposes solutions ~develops, implements and documents test plans for IT software, systems and computer games ~develops quality standards and validation techniques ~makes recommendations concerning software/system quality",
    ],
}
SOCmeta["2137"] = {
    "group_title": "IT network professionals",
    "group_description": "IT network professionals design, set up and maintain computer networks, support the network users and fix problems which arise.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~implements and evaluates new networking environments, including software and hardware ~monitors performance and makes recommendations concerning network quality. ~creates users' accounts and provides troubleshooting service to users ~ensures network security, reports on, investigates and fixes network faults ~writes operational documentation and provides subsequent support and training for users",
    ],
}
SOCmeta["2139"] = {
    "group_title": "Information technology professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of tasks not elsewhere classified in minor group 213: Information technology professionals.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~provides support to organisations in the operation of their IT software, hardware and networks ~meets with clients to determine their requirements and designs, tests and installs new systems to meet client's needs ~organises training for users and prepares documentation on IT systems ~manages and develops the content and operation of websites, monitors traffic, and ensures the functionality of websites and web servers",
    ],
}
SOCmeta["214"] = {
    "group_title": "Web and multimedia design professionals",
    "group_description": "Web and multimedia design professionals design, develop and maintain websites and applications, use illustrative, sound, visual and multimedia techniques to convey messages, and create special visual effects and animations for computer games, film, interactive and other media.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2141"] = {
    "group_title": "Web design professionals",
    "group_description": "Web design professionals design, develop and maintain websites and web and mobile applications to meet a client\u2019s specified requirements.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification, although entry with other academic qualifications and/or significant relevant experience is possible. There is a variety of relevant vocational, professional and postgraduate qualifications available.",
    "tasks": [
        "~liaises with internal/external client in order to define the requirements for the website or applications ~presents design options to the client ~designs web pages and applications including graphics, animation and functionality to maximise visual effectiveness and facilitate appropriate access ~designs web interfaces for relational database systems",
    ],
}
SOCmeta["2142"] = {
    "group_title": "Graphic and multimedia designers",
    "group_description": "Graphic and multimedia designers use illustrative, sound, visual and multimedia techniques to convey a message for information, entertainment, advertising, promotion or publicity purposes, and create special visual effects, 3D models and animations for computer games, film, interactive and other media.",
    "entry_routes_and_quals": "Entrants have usually completed a foundation course, a BTEC/SQA award, a degree and/or postgraduate qualification. NVQs/SVQs in Design (in various disciplines) are available at levels 2 and 3. Portfolio work is also important for entry.",
    "tasks": [
        "~liaises with client to clarify aims of project brief, discusses media, software and technology to be used, establishes timetable for project and defines budgetary constraints ~undertakes research into project, considers previous related projects and compares costs of using different processes ~prepares sketches, scale drawings, models, colour schemes and other mock-ups to show clients and discusses any required alterations ~prepares specification and instructions for realisation of the project ~liaises with other parts of the production team to ensure graphic design fits with other elements, processes and timescales ~produces or oversees creation of the final product",
    ],
}
SOCmeta["215"] = {
    "group_title": "Conservation and environment professionals",
    "group_description": "Conservation and environment professionals use specialist skills and knowledge to manage and conserve the environment, its associated species and its cycles of life, to address the environmental impacts of human activities and industrial processes, and to promote the sustainable use of resources and a wider public understanding and enjoyment of the environment. (It should be noted that Conservators are classified with Librarians and Related Professionals in minor group 245).",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2151"] = {
    "group_title": "Conservation professionals",
    "group_description": "Conservation professionals are responsible for ensuring that landscapes, habitats and species are protected and enhanced via appropriate management and conservation. They promote public understanding and awareness of the natural environment and help to develop and implement appropriate policies to achieve these objectives.",
    "entry_routes_and_quals": "Entrants normally require a degree in a relevant subject, sometimes with a related postgraduate qualification. Entry is also possible with a relevant BTEC/SQA Award or HND. Prior practical work experience (which may be obtained on a voluntary basis) is needed for most posts. Additional on-the-job training is available",
    "tasks": [
        "~promotes and implements local and national biodiversity action plans, particularly with regard to threatened species and habitats ~carries out environmental impact assessments and field surveys ~implements, evaluates and monitors schemes for the management and protection of natural habitats ~provides advice and information to government at national and local levels, clients, landowners, planners and developers to facilitate the protection of the natural environment ~liaises with other groups in the selection and maintenance of the Protected Site System including Special Areas of Conservation (SACs), Ramsar sites, and Sites of Special Scientific Interest (SSSIs) and National Nature Reserves (NNRs) ~maintains and develops knowledge in relevant policy areas within a national and European legislative context ~promotes conservation issues via educational talks, displays, workshops and literature and liaison with the media ~prepares applications for funding to other organisations, and assessing applications for funding from other organisations ~carries out research into aspects of the natural world",
    ],
}
SOCmeta["2152"] = {
    "group_title": "Environment professionals",
    "group_description": "Environment professionals investigate, address, and advise on a variety of terrestrial and marine environment and resource management issues, including the development and implementation of environmental policies and remedies that address the impacts of human activities and industrial processes on the environment.",
    "entry_routes_and_quals": "A good degree in a relevant subject is normally a minimum entry qualification, and some employers will require a postgraduate qualification. Relevant work experience to complement academic qualifications is highly desirable. Professional qualifications across a wide range of areas of work are available",
    "tasks": [
        "~identifies contamination of land, air or water and assesses any adverse impact on the environment ~advises on and provides solutions for mitigating the effects of such contamination ~implements remediation works ~carries out environment-related desk-based research and fieldwork to collect, analyse and interpret data to determine their validity, quality and significance ~carries out or assists in environmental audits and environmental impact assessments ~communicates scientific and technical information to relevant audiences in an appropriate form, via reports, workshops, educational events, public hearings ~assists organisations to conduct their activities in an environmentally appropriate manner ~implements, reviews and advises on regulatory and legislative standards, guidelines and policies ~provides professional guidance to clients, government agencies, regulators and other relevant bodies, having regard for sustainable approaches and solutions",
    ],
}
SOCmeta["216"] = {
    "group_title": "Research and development (r&d) and other research professionals",
    "group_description": "Jobholders in this unit group plan, organise, direct and advise on the research and development operations of an organisation.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2161"] = {
    "group_title": "Research and development (r&d) managers",
    "group_description": "Managers in this unit group plan, organise, co-ordinate and manage resources to undertake the systematic investigation necessary for the development of new, or to enhance the performance of existing, products and services.",
    "entry_routes_and_quals": "Entrants usually possess a relevant degree or equivalent qualification. Training is usually provided on-the-job, although support may be provided for postgraduate study. Professional qualifications are available.",
    "tasks": [
        "~establishes product design and performance objectives in consultation with other business functions ~liaises with production departments to investigate and resolve manufacturing problems ~develops research methodology, implements and reports upon research investigations undertaken ~plans work schedules, assigns tasks and delegates responsibilities to the research and development team ~monitors the standards of scientific and technical research undertaken by the research team",
    ],
}
SOCmeta["2162"] = {
    "group_title": "Other researchers, unspecified discipline",
    "group_description": "Other researchers, unspecified discipline perform research activities across a variety of disciplines for academic purposes or to provide the systematic investigation necessary for the development of new products and services, or to enhance the performance of existing ones.",
    "entry_routes_and_quals": "Entrants usually possess a relevant degree or equivalent qualification, although postgraduate qualifications may be required for some jobs. Training is usually provided on-the-job.",
    "tasks": [
        "~plans, directs and undertakes research into areas of academic interest or commercial importance to their organisation ~designs tests and experiments to address research objective and find solutions ~applies models and techniques to medical, industrial, agricultural, military and similar applications ~analyses results and writes up results of tests and experiments undertaken ~presents results of scientific research to sponsors, addresses conferences and publishes articles outlining the methodology and results of research undertaken ~designs and develops an appropriate research methodology in order to address the research objective ~compiles and analyses quantitative and qualitative data, prepares reports and presents results to summarise main findings and conclusions ~advises government, private organisations and special interest groups on policy issues",
    ],
}
SOCmeta["22"] = {
    "group_title": "Health professionals",
    "group_description": "Health professionals provide medical treatments and diagnosis for people and animals, conduct research into treatment and drugs, dispense pharmaceutical compounds, provide therapeutic treatments for medical conditions, and administer nursing and midwifery care.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["221"] = {
    "group_title": "Medical practitioners",
    "group_description": "Health professionals diagnose mental and physical injuries, disorders and diseases, provide treatment with drugs, surgery and corrective devices, carry out medical tests and recommend preventative action to patients and conduct research into treatments and drugs.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2211"] = {
    "group_title": "Generalist medical practitioners",
    "group_description": "Generalist medical practitioners diagnose mental and physical injuries, disorders and diseases, prescribe and give treatment, recommend preventative action, and conduct medical education and research activities. They work in hospitals or in general practice and, where necessary, refer the patient to a specialist.",
    "entry_routes_and_quals": "Entrants require a university degree from a medical school recognised by the General Medical Council followed by two years of pre-registration training as a house officer. Some medical schools operate graduate entry schemes. Once the pre-registration period as house officer is completed, further postgraduate training in a general practice training programme is completed",
    "tasks": [
        "~examines patient, arranges for any necessary x-rays or other tests and interprets results ~diagnoses condition and prescribes and/or administers appropriate treatment ~administers medical tests and inoculations against communicable diseases ~supervises patient\u2019s progress and advises on diet, exercise and other preventative action ~refers patient to specialist where necessary and liaises with specialist ~prepares and delivers lectures, undertakes research, and conducts and participates in clinical trials ~supervises the implementation of care and treatment plans by other healthcare providers",
    ],
}
SOCmeta["2212"] = {
    "group_title": "Specialist medical practitioners",
    "group_description": "Specialist medical practitioners specialise in particular areas of modern medicine, diagnose mental and physical injuries, disorders and diseases within their specialism, prescribe and give treatment, recommend preventative action, and conduct medical education and research activities",
    "entry_routes_and_quals": "Entrants require a university degree from a medical school recognised by the General Medical Council followed by two years of pre-registration training as a house officer, and further postgraduate training in a chosen speciality. Some medical schools operate graduate entry schemes.",
    "tasks": [
        "~examines patient, arranges for any necessary x-rays or other tests and interprets results ~diagnoses condition and prescribes and/or administers appropriate treatment/surgery ~administers medical tests and inoculations against communicable diseases ~supervises patient\u2019s progress and advises on diet, exercise and other preventative action ~provides specialist advice to generalist medical practitioners or other specialists ~performs specialist medical tasks such as surgery, anaesthetisation and diagnostic or interventional radiology ~prepares and delivers lectures, undertakes research, and conducts and participates in clinical trials ~takes overall responsibility for, supervises and directs the implementation of care and treatment plans by other healthcare providers",
    ],
}
SOCmeta["222"] = {
    "group_title": "Therapy professionals",
    "group_description": "Workers in this minor group plan and apply physical, therapeutic and other treatments or activities to assist in the physical and psychological recovery from illness and injury, and to minimise the effects of disabilities.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2221"] = {
    "group_title": "Physiotherapists",
    "group_description": "Physiotherapists plan and apply massage, promote and encourage movement and exercise, use hydrotherapy, electro-therapy and other technological equipment in the treatment of a wide range of injuries, diseases and disabilities in order to assist rehabilitation by developing and restoring body systems.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades and A levels/H grades followed by up to four years training on an approved degree scheme necessary for state registration as a physiotherapist. Some science and other graduates are eligible for accelerated two year pre-registration MSc degree programmes in Physiotherapy or Rehabilitation Science. Relevant apprenticeships are available.",
    "tasks": [
        "~examines medical reports and assesses patient to determine the condition of muscles, nerves or joints in need of treatment ~writes up patients\u2019 case notes and reports, maintains their records and manages caseload ~plans and undertakes therapy to improve circulation, restore joint mobility, strengthen muscles and reduce pain ~explains treatment to and instructs patient in posture and other exercises and adapts treatment as necessary ~offers advice and education on how to avoid injury and promote patient\u2019s future health and well-being ~supervises physiotherapy assistants ~monitors patient\u2019s progress and liaises with others concerned with the treatment and rehabilitation of patient, and refers patients requiring other specific medical attention",
    ],
}
SOCmeta["2222"] = {
    "group_title": "Occupational therapists",
    "group_description": "Occupational therapists work with people who have a physical or learning disability or mental illness, actively engaging them in purposeful activities in order to maximise self-confidence, independent functioning and well-being.",
    "entry_routes_and_quals": "Entrants usually possess A levels/H grades, an HND/HNC, a BTEC/SQA award or equivalent qualifications followed by training on an approved degree scheme necessary for state registration as an occupational therapist. There is a minimum age limit of 18 years to enter training.",
    "tasks": [
        "~considers the physical, psychological and social needs of a patient that may result from illness, injury, congenital condition or lifestyle problems ~devises, designs, initiates and monitors carefully selected and graded treatments and activities as part of the assessment and intervention process ~liaises with a wide variety of other professionals in planning and reviewing ongoing treatments ~trains students and supervises the work of occupational therapy assistants ~makes home visits to clients, families and carers to organise support and rehabilitation and assist them to deal and cope with disability ~counsels clients in ways to promote a healthy lifestyle, prevention of illness and/or preparation for coping with increasing stages of illness ~maintains patient records, manages caseloads",
    ],
}
SOCmeta["2223"] = {
    "group_title": "Speech and language therapists",
    "group_description": "Speech and language therapists are responsible for the assessment, diagnosis and treatment of speech, language, fluency and voice disorders caused by disability, injury or illness.",
    "entry_routes_and_quals": "Entrants require a recognised graduate or postgraduate degree that encompasses both theory and clinical practice. Successful completion of these courses leads to eligibility for a certificate to practice and membership of the Royal College of Speech and Language Therapists. Full membership is granted after completion of a year of supervised, post-qualifying experience.",
    "tasks": [
        "~assesses, tests and diagnoses a client\u2019s condition ~designs and initiates appropriate rehabilitation and/or remedial programmes of treatment ~treats speech and language disorders by coaching and counselling clients or through the use of artificial communication devices ~attends case conferences and liaises with other specialists such as doctors, teachers, social workers and psychologists ~counsels relatives to help cope with the problems created by a patient\u2019s disability ~writes reports and maintains client caseloads",
    ],
}
SOCmeta["2224"] = {
    "group_title": "Psychotherapists and cognitive behaviour therapists",
    "group_description": "Psychotherapists and cognitive behaviour therapists use a variety of therapies in one-on-one or group settings to help people with mental health issues, stress, emotional and relationship problems.",
    "entry_routes_and_quals": "Job holders in this unit group will usually possess a postgraduate qualification or equivalent accredited qualification. Training usually lasts 4 years. A DBS check may be required for work with vulnerable individuals or children.",
    "tasks": [
        "~assesses and provides treatment for people suffering with mental illness, stress, and emotional and relationship problems ~talks with patients about their emotions, relationships and personal history ~analyses events, behaviour, and habits to understand their mode of thinking and feelings ~helps people come up with new ways to cope with their problems and to change their ways of thinking",
    ],
}
SOCmeta["2225"] = {
    "group_title": "Clinical psychologists",
    "group_description": "Clinical psychologists work with people experiencing emotional, psychological or behavioural distress, perform tests and assess their emotional, cognitive and behavioural processes, and determine treatments to help patients improve their mental wellbeing.",
    "entry_routes_and_quals": "Entrants require a degree in psychology recognised by the British Psychology Society. Postgraduate and professional qualifications relating to different areas of psychology are available and are required for certain posts.",
    "tasks": [
        "~administers tests to assess patients' needs through interviews, psychometric tests and observation of their behaviour ~determines appropriate treatment and may refer patients to other mental health professionals ~provides treatment or guidance using a variety of therapy and counselling techniques ~helps patients to manage their own psychological conditions ~maintains required contacts with family members, education or other health professionals, as appropriate, and recommends possible solutions to problems presented ~writes reports on their work and conducts applied research",
    ],
}
SOCmeta["2226"] = {
    "group_title": "Other psychologists",
    "group_description": "Psychologists research, study and assess emotional, cognitive and behavioural processes and abnormalities in human beings and animals and how these are affected by genetic, physical and social factors.",
    "entry_routes_and_quals": "Entrants require a degree in psychology recognised by the British Psychology Society. Postgraduate and professional qualifications relating to different areas of psychology are available and are required for certain posts.",
    "tasks": [
        "~develops and administers tests to measure intelligence, abilities, aptitudes, etc. and assesses results ~develops treatment and guidance methods and gives treatment or guidance using a variety of therapy and counselling techniques ~observes and experiments on humans and animals to measure mental and physical characteristics ~analyses the effect of hereditary, social and physical factors on thought and behaviour ~studies psychological factors in the treatment and prevention of mental illness or emotional and personality disorders ~maintains required contacts with family members, education or other health professionals, as appropriate, and recommends possible solutions to problems presented ~applies professional knowledge and techniques within the workplace, addressing issues such as job design, work groups, motivation etc ~applies psychological treatment methods to help athletes achieve optimum mental health and enhance sporting performance",
    ],
}
SOCmeta["2229"] = {
    "group_title": "Therapy professionals n.e.c.",
    "group_description": "Job holders in this unit group plan and apply physical and therapeutic treatments and activities to assist recovery from physical and mental illness and to minimise the effects of disabilities not elsewhere classified in minor group 222: Therapy professionals.",
    "entry_routes_and_quals": "Entrants usually possess an accredited degree or postgraduate qualification. Training can take between two to five years depending upon the chosen method of study. Courses provide a mixture of theoretical study and practical experience. Membership of professional bodies may be mandatory in some areas.",
    "tasks": [
        "~prescribes diet therapy and gives advice to patients, health care professionals and the public on dietetic and nutritional matters for those with special dietary requirements or to prevent illness amongst the general population ~diagnoses and treats disorders of vision and eye movements, monitors subsequent progress and recommends further optical, pharmacological or surgical treatment as required ~manipulates and massages patient to discover the cause of pain, relieve discomfort, restore function and mobility and to correct irregularities in body structure ~prevents, recognises and treats injuries incurred playing sports or doing exercise and helps people manage injuries and rehabilitate themselves ~adopts a holistic approach in assessing the overall health of the patient, and treats by inserting needles under the skin at particular locations according to the disorder being treated ~diagnoses and treats behavioural problems in animals ~provides support and guidance to patients regarding hereditary conditions and genetic testing.",
    ],
}
SOCmeta["223"] = {
    "group_title": "Nursing professionals",
    "group_description": "Nursing professionals provide nursing care for the sick and injured and prenatal and postnatal care for mothers and babies, working with and providing high level support for other health professionals, within teams of other healthcare providers and/or working autonomously across defined areas of significant responsibility.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2231"] = {
    "group_title": "Midwifery nurses",
    "group_description": "Midwifery nurses deliver, or assist in the delivery of babies, provide antenatal and postnatal care and advise parents on baby care. They work with other healthcare professionals and advise on and teach midwifery practice.",
    "entry_routes_and_quals": "A degree in midwifery is essential. Registered nurses can do a 12-18 month shortened course but graduates from other disciplines must undertake the full three or four year degree programme. Entry to midwifery training without a degree or HND is also possible. Applicants must have a minimum of five GCSEs (or equivalent) and at least two A-levels (or equivalent) for degree programmes.",
    "tasks": [
        "~monitors condition and progress of patient and baby throughout pregnancy ~delivers babies in normal births and assists doctors with difficult deliveries ~monitors recovery of mother in postnatal period and supervises the nursing of premature and other babies requiring special attention ~advises on baby care, exercise, diet and family planning issues ~supervises more junior staff and directs the work of the midwifery unit ~plans and manages midwifery care services ~delivers lectures and other forms of training in midwifery practice",
    ],
}
SOCmeta["2232"] = {
    "group_title": "Registered community nurses",
    "group_description": "Registered community nurses provide general nursing care for the sick, injured and others in need of care, and assist medical doctors with their tasks in settings outside of acute hospitals, such as clinics, health centres or visits to patients\u2019 homes.",
    "entry_routes_and_quals": "Qualification as a nurse is via a diploma or degree course, both of which are provided by universities, or through an apprenticeship. Courses comprise both theoretical and practical work, including placements in hospital and community settings. Full time diploma courses last three years; degree courses last three or four years. Accelerated programmes are available to graduates with a health-related degree. Post-registration training is available to become a specialist practitioner in community nursing.",
    "tasks": [
        "~plans, manages, provides and evaluates nursing care services within a community care setting ~provides basic care and monitors patients' general health such as blood pressure or body temperature ~administers drugs and medicines, applies surgical dressings and gives other forms of treatment ~assists medical doctors in conducting examinations and other medical procedures ~manages own case load ~plays an educational role for patients and families, helping to develop rehabilitation routines and advising on how to care for their condition in everyday life, disease prevention and nutrition",
    ],
}
SOCmeta["2233"] = {
    "group_title": "Registered specialist nurses",
    "group_description": "Registered specialist nurses provide specialised nursing care and plan ongoing treatment for the sick, injured and others in need of care, take responsibility for patients within their sphere of practice and assist medical doctors with their tasks, work with other healthcare professionals and within teams of healthcare workers. They advise on and teach nursing practices.",
    "entry_routes_and_quals": "A degree or equivalent qualification is required as well as significant relevant experience. Courses comprise both theoretical and practical work, including placements in hospital and community settings. Full time diploma courses last three years; degree courses last three or four years. Accelerated programmes are available to graduates with a health-related degree. Post-registration training is available for a range of clinical specialisms.",
    "tasks": [
        "~provides specialist care in their area of expertise, assesses patients, determines treatments and conducts a variety of medical procedures ~consults with and provides guidance to other nurses and healthcare professionals within their specialism ~gives consultations with patients and their families to explain a patient's condition and possible treatments ~plans duty rotas and organises and directs the work and training of ward and theatre nursing staff ~advises on nursing care, disease prevention, nutrition, etc. and liaises with hospital board/management on issues concerning nursing policy ~plans, manages, provides and evaluates nursing care services for patients, supervises the implementation of nursing care plans ~delivers lectures, and other forms of formal training relating to nursing practice",
    ],
}
SOCmeta["2234"] = {
    "group_title": "Registered nurse practitioners",
    "group_description": "Registered nurse practitioners provide nursing care for the sick, injured and others in need of such care, assist medical doctors with their tasks and also provide care independently, including diagnosing patients, the ordering and interpretation of tests, the determination of treatment and prescription of medication.",
    "entry_routes_and_quals": "Qualification as a nurse is via a diploma or degree course, both of which are provided by universities, or through an apprenticeship. Courses comprise both theoretical and practical work, including placements in hospital and community settings. To become an advanced nurse practitioner significant experience and qualification to a postgraduate level is usually required.",
    "tasks": [
        "~assists medical doctors and works with other healthcare professionals to deal with emergencies and pre-planned treatment of patients ~manages own case load ~interviews and diagnoses patients, orders tests and interprets results and determines appropriate treatments ~monitors patient\u2019s progress, administers drugs and medicines, applies surgical dressings and gives other forms of treatment ~plans duty rotas and organises and directs the work and training of ward and theatre nursing staff ~plans, manages, provides and evaluates nursing care services for patients, supervises the implementation of nursing care plans",
    ],
}
SOCmeta["2235"] = {
    "group_title": "Registered mental health nurses",
    "group_description": "Registered mental health nurses support and care for people with a range of mental health conditions, in hospital and community settings, and help them towards recovery and management of their conditions.",
    "entry_routes_and_quals": "Entrants will need a degree level qualification in mental health nursing, an enhanced DBS check, and registration with the Nursing and Midwifery Council.",
    "tasks": [
        "~provides day to day support for and, in some cases, physical care for patients with a variety of mental health conditions ~participates in the preparation for physical and psychological treatment of patients with mental health conditions ~monitors patient\u2019s progress, encourages patients to participate in different therapies ~administers drugs and gives other forms of treatment ~works with other mental health professionals ~provides information to patients and their families about a patient's condition, how to manage it and possible treatments",
    ],
}
SOCmeta["2236"] = {
    "group_title": "Registered children's nurses",
    "group_description": "Registered children's nurses nurses provide general or acute nursing care for children and young people with chronic or acute conditions and assist medical doctors with their tasks.",
    "entry_routes_and_quals": "Entrants will need a degree or equivalent qualification in children's nursing and to register with the Nursing and Midwifery Council. A DBS check is also required.",
    "tasks": [
        "~assists medical doctors and works with other healthcare professionals to deal with emergencies and pre-planned treatment of patients ~manages own case load ~monitors children's progress, including the interpretation of the behaviour of young children too young to communicate ~administers drugs and medicines, applies surgical dressings and gives other forms of treatment ~works with parents to explain procedures and health conditions and to help them care for children when they return home ~advises on nursing care, disease prevention, and nutrition ~plans, manages, provides and evaluates nursing care services for patients, supervises the implementation of nursing care plans",
    ],
}
SOCmeta["2237"] = {
    "group_title": "Other registered nursing professionals",
    "group_description": "Other registered nursing professionals provide general nursing care for the sick, injured and others in need of such care, assist medical doctors with their tasks and work with other healthcare professionals and within teams of healthcare workers in a variety of other professional nursing occupations not elsewhere classified in minor group 223: Nursing Professionals.",
    "entry_routes_and_quals": "Qualification as a nurse is via a diploma or degree course, both of which are provided by universities, or through an apprenticeship. Courses comprise both theoretical and practical work, including placements in hospital and community settings. Full time diploma courses last three years; degree courses last three or four years. Accelerated programmes are available to graduates with a health-related degree.",
    "tasks": [
        "~assists medical doctors and works with other healthcare professionals to deal with emergencies and pre-planned treatment of patients ~manages own case load ~monitors patient\u2019s progress, administers drugs and medicines, applies surgical dressings and gives other forms of treatment ~cares for the physical and emotional wellbeing of patients in their care ~informs and advises patients and their relatives on their health problems and how to care for themselves ~teach nursing professionals clinical skills, patient care methods, and best collaboration practices",
    ],
}
SOCmeta["224"] = {
    "group_title": "Veterinarians",
    "group_description": "Veterinarians provide care and medical services for pets, livestock and wild animals, advise owners on general and medical care and perform tasks relating to food safety policy.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2240"] = {
    "group_title": "Veterinarians",
    "group_description": "Veterinarians diagnose and treat animal injuries, diseases and disorders, and advise on preventative action. They may work in practices, specialising according to their location in either a rural or urban area, or in the public sector or associated industries such as pharmaceuticals, food production or drug regulation.",
    "entry_routes_and_quals": "Entrants will require a university degree in veterinary science and registration as a member of the Royal College of Veterinary Surgeons (RCVS). Pre-entry experience in a veterinary practice may be required for entry to a university veterinary school.",
    "tasks": [
        "~examines animals, diagnoses condition and prescribes and administers appropriate drugs, dressings, etc., and arranges or undertakes any necessary x-ray or other tests ~inoculates animals against communicable diseases ~administers local or general anaesthetics and performs surgery ~investigates outbreaks of animal diseases and advises owners on feeding, breeding and general care ~euthanises old, sick, terminally ill and unwanted animals ~performs tasks relating to food safety policy, regulation of veterinary drugs, quality control of veterinary products ~performs ante-mortem inspection of animals destined for the food chain, and animal post-mortem examinations ~carries out expert witness work and undertakes teaching of veterinary students ~maintains records, raises and forwards reports and certificates in compliance with current legislation",
    ],
}
SOCmeta["225"] = {
    "group_title": "Other health professionals",
    "group_description": "Other health professionals dispense drugs and corrective devices, diagnose and treat dental and oral diseases, operate dental and medical testing equipment, assist in post-mortems, fit artificial limbs and hearing aids, provide emergency aid and transport people to hospitals, diagnose and treat ailments of the human foot and lower limb and assist in a range of other medical tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2251"] = {
    "group_title": "Pharmacists",
    "group_description": "Pharmacists dispense drugs and medicaments in hospitals and pharmacies and advise on and participate in the development and testing of new drugs, compounds and therapies. They counsel on the proper use and adverse effects of drugs and medicines.",
    "entry_routes_and_quals": "Entrants possess a degree in pharmacy. To register with the General Pharmaceutical Council (GPhC), entrants must have completed a one year period of pre-registration training and passed a registration exam. Further training is available to permit pharmacists to prescribe medicines independently.",
    "tasks": [
        "~prepares or directs the preparation of prescribed medicaments in liquid, powder, tablet, ointment or other form following prescriptions issued by medical doctors and other health professionals ~advises health professionals on the selection and appropriate use of medicines ~highlights a drug\u2019s potential side effects, identifies harmful interactions with other drugs and assesses the suitability of treatments for patients with particular health conditions ~checks that recommended doses are not being exceeded and that instructions are understood by patients ~maintains prescription files and records issue of narcotics, poisons and other habit-forming drugs ~liaises with other professionals regarding the development, manufacturing and testing of drugs ~tests and analyses drugs to determine their identity, purity and strength ~ensures that drugs and medicaments are in good supply and are stored properly",
    ],
}
SOCmeta["2252"] = {
    "group_title": "Optometrists",
    "group_description": "Ophthalmic opticians test patients\u2019 vision, diagnose defects and disorders and prescribe glasses or contact lenses as required.",
    "entry_routes_and_quals": "Entrants require a degree in Optometry, must have passed the Professional Qualifying Examination of the General Optical Council, and have completed a pre-registration year. Advanced training in specialised areas is available.",
    "tasks": [
        "~examines eyes and tests vision of patient, identifies problems, defects, injuries and ill health ~prescribes appropriate spectacle lenses, contact lenses and other aids ~advises patient on proper use of glasses, contact lenses and other aids, and on appropriate lighting conditions for reading and working ~refers patient to a specialist, where necessary ~carries out research with glass and lens manufacturers",
    ],
}
SOCmeta["2253"] = {
    "group_title": "Dental practitioners",
    "group_description": "Dental practitioners diagnose dental and oral diseases, injuries and disorders, prescribe and administer treatment, recommend preventative action and, where necessary, refer the patient to a specialist.",
    "entry_routes_and_quals": "Entrants require an approved university degree and must have completed a period of postgraduate vocational training. Graduate entry to dental school is sometimes possible. Registration with the General Dental Council is a pre-requisite to practise. Specialist fields require further study and training.",
    "tasks": [
        "~examines patient\u2019s teeth, gums and jaw, using dental and x-ray equipment, diagnoses dental conditions ~assesses and recommends treatment options to patients ~administers local anaesthetics ~carries out clinical treatments, restores teeth affected by decay etc., treats gum disease and other disorders ~constructs and fits braces, inlays, dentures and other appliances ~supervises patient\u2019s progress and advises on preventative action ~educates patients on oral health care ~refers patient to specialist, where necessary ~maintains patients\u2019 dental health records ~prepares and delivers lectures, undertakes research, and conducts and participates in clinical trials",
    ],
}
SOCmeta["2254"] = {
    "group_title": "Medical radiographers",
    "group_description": "Medical (diagnostic) radiographers operate x-ray machines, ultrasound, magnetic resonance imaging and other imaging devices for diagnostic and therapeutic purposes, assist in the diagnosis of injuries and diseases and are involved in intervention procedures such as the removal of kidney stones. They operate under the supervision of senior staff. Therapeutic radiographers specialise in the planning and administration of radiotherapy treatment for patients with cancer.",
    "entry_routes_and_quals": "Entrants for medical radiography possess a degree in radiography recognised by the Health Professions Council (HPC). Those with a relevant first degree may qualify by completing a pre-registration postgraduate diploma or a Masters qualification. Post-qualifying courses are available for specialist areas.",
    "tasks": [
        "~uses a range of imaging devices for diagnostic and therapeutic purposes ~assesses patients and interprets clinical requirements to determine appropriate radiographic treatments ~verifies identity of patient and ensures that necessary preparations have been made for the examination/treatment ~decides length and intensity of exposure or strength of dosage of isotope ~positions patient and operates x-ray, scanning or fluoroscopic equipment ~maintains records of all radiographic/therapeutic work undertaken ~plans course of treatment with clinical oncologists and physicists ~calculates radiation dosage and maps volume to be treated ~explains treatment to patient and management of any side effects ~carries out post-treatment reviews and follow-ups",
    ],
}
SOCmeta["2255"] = {
    "group_title": "Paramedics",
    "group_description": "Paramedics provide first aid and life support treatment in emergency situations and transport sick and injured people who require skilled treatment.",
    "entry_routes_and_quals": "Entry is via a student paramedic position with an ambulance service trust or completion of an approved full-time university course in paramedical science. Qualification requirements for entry to university courses vary (GCSEs, A levels or equivalent). A full, manual driving licence (with appropriate classifications) is required. Paramedics working in the NHS must be registered with the Health Professions Council.",
    "tasks": [
        "~drives ambulance or accompanies driver to respond to calls for assistance at accidents, emergencies and other incidents ~assesses the nature of injuries, provides first aid treatment and ascertains appropriate method of conveying patient ~resuscitates and/or stabilises patient using relevant techniques, equipment and drugs ~transports and accompanies patients who either require or potentially require skilled treatment whilst travelling ~briefs other medical staff when handing over the patient, and completes patient report forms describing the patient\u2019s condition and any treatment provided",
    ],
}
SOCmeta["2256"] = {
    "group_title": "Podiatrists",
    "group_description": "Podiatrists (formerly known as chiropodists) diagnose and treat ailments and abnormalities of the human foot and lower limb, deal with minor infections, injuries and deformities, and conditions resulting from other major health disorders such as diabetes.",
    "entry_routes_and_quals": "Entry requires a degree in podiatry approved by the Health Professions Council and registration with and membership of the Society of Chiropodists and Podiatrists. Degree courses combine theoretical and practical training. Qualified podiatrists must undertake 30 hours of Continuing Professional Development each year.",
    "tasks": [
        "~examines patient\u2019s feet to determine the nature and extent of disorder ~provides vascular and neurological assessment for the long-term management of chronic disorders and high-risk patients ~administers local anaesthetic where appropriate ~treats conditions of the skin, nails and soft tissues of feet by minor surgery, massage and heat treatment, padding and strapping or drugs ~prescribes, makes and fits pads and other orthotic appliances to correct and/or protect foot disorders ~those with advanced training may carry out minor surgery on the feet ~advises patients on aspects of foot care to avoid recurrence of foot problems ~delivers foot health education to groups such as the elderly, children, the homeless, those with medical problems such as arthritis ~refers patients who require further medical or surgical attention",
    ],
}
SOCmeta["2259"] = {
    "group_title": "Other health professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of other health-related professional occupations not elsewhere classified in minor group 225: Other health professionals. They may work autonomously or in teams with other health workers.",
    "entry_routes_and_quals": "Entry is via a variety of relevant academic and/or professional qualifications.",
    "tasks": [
        "~provides expert technical and technological support in the delivery of critical care ~provides high level support within surgical teams before, during and after surgery ~operate heart-lung machines during surgical procedures ~conducts medical education relevant to specialism and provides team leadership and supervision ~diagnoses and treats patients with a variety of hearing-related problems ~conducts specialised diagnostic tests for a variety of health conditions and advise on treatment ~provides prosthetic devices to patients and advises on rehabilitation",
    ],
}
SOCmeta["23"] = {
    "group_title": "Teaching and other educational professionals",
    "group_description": "Teaching and educational professionals plan, organise and undertake teaching and research activities within educational establishments and plan, organise, direct and co-ordinate the administrative work and financial resources of these establishments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["231"] = {
    "group_title": "Teaching professionals",
    "group_description": "Teaching professionals plan, organise and provide instruction in academic, technical, vocational, diversionary and other subjects.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2311"] = {
    "group_title": "Higher education teaching professionals",
    "group_description": "Higher education teaching professionals deliver lectures and teach students to at least first degree level, undertake research and write journal articles and books in their chosen field of study.",
    "entry_routes_and_quals": "Entry will require a good honours first degree plus a higher degree or an equivalent professional qualification. For vocational subjects, practical experience and additional qualifications may also be required. A DBS check may be required.",
    "tasks": [
        "~prepares, delivers and directs lectures, seminars and tutorials ~prepares, administers and marks examinations, essays and other assignments ~advises students on academic matters and encourages independent research ~provides pastoral care or guidance to students ~participates in decision making processes regarding curricula, budgetary, departmental and other matters ~directs the work of postgraduate students ~undertakes research, writes articles and books and attends conferences and other meetings",
    ],
}
SOCmeta["2312"] = {
    "group_title": "Further education teaching professionals",
    "group_description": "Further education teaching professionals supervise and teach trade, technical, commercial, adult education, secondary and post-secondary courses to students beyond minimum school leaving age.",
    "entry_routes_and_quals": "Further education lecturers normally require a professional or academic qualification in the subject area they intend to teach, relevant professional, industrial or business experience and an appropriate teaching qualification. A DBS check may be required.",
    "tasks": [
        "~prepares, delivers and directs lectures, seminars and tutorials ~prepares, administers and marks examinations, essays and other assignments ~arranges instructional visits and periods of employment experience for students ~assists with the administration of teaching and the arranging of timetables ~liaises with other professional and commercial organisations to review course content",
    ],
}
SOCmeta["2313"] = {
    "group_title": "Secondary education teaching professionals",
    "group_description": "Secondary (and middle school deemed secondary), and sixth form education teaching professionals plan, organise and provide instruction in one or more subjects, including physical education and diversionary activities, within a prescribed curriculum.",
    "entry_routes_and_quals": "Entry is with a first degree that provides QTS (qualified teacher status) or, in Scotland, TQ (teaching qualification); or other relevant degree followed by further postgraduate training (most commonly PGCE \u2013 Postgraduate Certificate in Secondary Education, or, in Scotland, PGDE \u2013 Professional Graduate Diploma in Education). Further and higher professional qualifications are required for some teaching posts. A DBS check is mandatory.",
    "tasks": [
        "~prepares and delivers courses and lessons in accordance with curriculum requirements and teaches one or more subjects ~prepares, assigns and corrects exercises and examinations to record and evaluate students\u2019 progress ~prepares students for external examinations and administers and invigilates these examinations ~maintains records of students\u2019 progress and development ~supervises any practical work and maintains classroom discipline ~undertakes pastoral duties ~supervises teaching assistants and trainees ~discusses progress with student, parents and/or other education professionals ~assists with or plans and develops curriculum and rota of teaching duties",
    ],
}
SOCmeta["2314"] = {
    "group_title": "Primary education teaching professionals",
    "group_description": "Primary (and middle school deemed primary) and education teaching professionals plan, organise and provide instruction to children at all levels up to the age of entry into secondary education.",
    "entry_routes_and_quals": "Entry is with a first degree that provides QTS (qualified teacher status) or, in Scotland, TQ (teaching qualification); or other relevant degree followed by further postgraduate training (most commonly PGCE \u2013 Postgraduate Certificate in Primary Education, or, in Scotland, PGDE \u2013 Professional Graduate Diploma in Education). Further and higher professional qualifications are required for some teaching posts. A DBS check is mandatory.",
    "tasks": [
        "~prepares and delivers courses and lessons in accordance with curriculum requirements and teaches a range of subjects ~prepares, assigns and corrects exercises and examinations to record and evaluate students\u2019 progress ~prepares students for external examinations and administers and invigilates these examinations ~maintains records of students\u2019 progress and development ~teaches simple songs and rhymes, reads stories and organises various activities to promote language, social and physical development ~undertakes pastoral duties ~supervises teaching assistants and trainees ~discusses progress with student, parents and/or other education professionals ~assists with or plans and develops curriculum and rota of teaching duties",
    ],
}
SOCmeta["2315"] = {
    "group_title": "Nursery education teaching professionals",
    "group_description": "Nursery education teaching professionals care for and teach children up to the age of entry into primary school.",
    "entry_routes_and_quals": "Entrants will usually possess a relevant degree or postgraduate qualification or relevant experience. Early years teacher status or equivalent is required. A DBS check is mandatory.",
    "tasks": [
        "~prepares and delivers lessons in accordance with early years foundation stages curriculum and encourages and stimulates children's learning ~teaches simple songs and rhymes, reads stories and organises various activities to promote language, social and physical development ~supervises and cares for children, provides a secure learning environment and ensures their health and safety is maintained during all activities ~undertakes pastoral duties ~supervises teaching assistants and trainees ~observes and assesses students and discusses their progress with parents and/or other education professionals ~assists with or plans and develops curriculum and rota of teaching duties",
    ],
}
SOCmeta["2316"] = {
    "group_title": "Special and additional needs education teaching professionals",
    "group_description": "Special and additional needs education teaching professionals organise and provide instruction at a variety of different levels to children who have emotional, behavioural or learning difficulties or physical disabilities. These professionals may also work with exceptionally gifted pupils.",
    "entry_routes_and_quals": "Entry is with a first degree that provides QTS (qualified teacher status) or, in Scotland, TQ (teaching qualification); or other relevant degree followed by further postgraduate training (most commonly PGCE \u2013 Postgraduate Certificate in Secondary Education, or, in Scotland, PGDE \u2013 Professional Graduate Diploma in Education). Additionally, prior experience in mainstream teaching is usually required, and further training for special needs teaching may be mandatory. A DBS check is mandatory",
    "tasks": [
        "~creates a safe, stimulating and supportive learning environment for students ~assesses student\u2019s abilities, identifies student\u2019s needs and devises curriculum and rota of teaching duties accordingly ~gives instruction, using techniques appropriate to the student\u2019s disability ~develops and adapts conventional teaching methods to meet the individual student\u2019s needs ~encourages the student to develop self-help skills to circumvent the limitations imposed by their disability ~prepares, assigns and corrects exercises to record and evaluate students\u2019 progress ~supervises students in classroom and maintains discipline ~liaises with other professionals, such as social workers, speech and language therapists and educational psychologists ~updates and maintains students\u2019 records to monitor development and progress ~discusses student\u2019s progress with parents and other teaching professionals",
    ],
}
SOCmeta["2317"] = {
    "group_title": "Teachers of english as a foreign language",
    "group_description": "Teachers of English as a foreign language teach students to speak and write the English language, either for the first time or building on their existing knowledge.",
    "entry_routes_and_quals": "There are no pre-set academic entry requirements, however, many employers may require you to have a Teaching English as a Foreign Language course. TEFL courses require students to be 18 and to have a good level of English. A DBS check may be required.",
    "tasks": [
        "~teaches English as a foreign language and assists in the tuition of foreign languages ~plans and prepares language lessons and materials ~encourages conversations in English to improve students confidence and understanding ~sets and marks tests and gives feedback on student's performance ~organises students' participation in cultural activities and social events",
    ],
}
SOCmeta["2319"] = {
    "group_title": "Teaching professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of other teaching occupations not elsewhere classified in minor group 231: Teaching and educational professionals.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications, professional qualifications and/or relevant experience. A DBS check may be required.",
    "tasks": [
        "~designs and implements methods of assessing the performance of students, co-ordinates and undertakes the evaluation of assessments and awards grades of merit based upon performance ~manages/owns and teaches in private drama, music and dancing schools, training centres and similar establishments ~provides private academic, vocational and other instruction to individuals or groups",
    ],
}
SOCmeta["232"] = {
    "group_title": "Other educational professionals",
    "group_description": "Job holders in this unit group plan, organise, direct and co-ordinate the administration, support systems and activities that facilitate the effective running of a school, university, college or other educational establishment.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2321"] = {
    "group_title": "Head teachers and principals",
    "group_description": "Head teachers and principals plan, organise, direct and co-ordinate the running of schools, colleges and other educational establishments.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification and have gained significant relevant experience in the field of education. Specialist training courses to become a head teacher are available. A DBS check may be required.",
    "tasks": [
        "~sets the school's values, provides leadership to staff and helps create an encouraging environment for learning ~considers staffing, financial, material and other short- and long-term needs ~leads or contributes to decision making processes regarding curricula, budgetary, disciplinary and other matters ~monitors schools performance and sets goals for student's academic achievements ~liaises with parents and pupils ~assists with recruitment, public relations and marketing activities ~coordinates and maintains quality assurance procedures",
    ],
}
SOCmeta["2322"] = {
    "group_title": "Education managers",
    "group_description": "Education managers plan, organise, direct and co-ordinate the administration, support systems and activities that facilitate the effective running of a school, university, college or other educational establishment.",
    "entry_routes_and_quals": "Job holders will usually hold a degree, and some academic posts will require a degree. Significant professional experience will be needed for some roles. Relevant vocational qualifications at up to level 4 are also available. A DBS check may be required.",
    "tasks": [
        "~considers staffing, financial, material and other short- and long-term needs ~provides administrative support to the academic team ~leads or contributes to decision making processes regarding curricula, budgetary, disciplinary and other matters ~controls administrative aspects of student admission, registration and graduation ~acts as secretary to statutory and other bodies/committees associated with the educational establishment ~drafts and interprets regulations, deals with queries and complaints procedures and coordinates and maintains quality assurance procedures ~organises examinations, invigilation and any security procedures required ~assists with recruitment, public relations and marketing activities ~designs and implements methods of assessing the performance of students, co-ordinates and undertakes the evaluation of assessments and awards grades of merit based upon performance",
    ],
}
SOCmeta["2323"] = {
    "group_title": "Education advisers and school inspectors",
    "group_description": "Education advisers and school inspectors plan, organise and direct the educational activities and resources in a local authority education area, and undertake inspections of schools and other training establishments excluding universities.",
    "entry_routes_and_quals": "Job holders usually possess an education-related degree or relevant postgraduate qualification and have gained relevant experience in teaching and/or school management. Before being appointed, an inspector has to attend a course of training provided or approved by OFSTED. Most inspectors are or have been head teachers, deputy heads or heads of department. A DBS check may be required.",
    "tasks": [
        "~advises on all aspects of education and ensures that all statutory educational requirements are being met ~plans and advises on the provision of special schools for children with physical or learning disabilities ~appoints and controls teaching staff ~verifies that school buildings are adequately maintained ~arranges for the provision of school medical and meals services ~observes teaching, assesses learning level and discusses any apparent faults with teachers, heads of department and head teachers ~prepares reports on schools concerning teaching standards, educational standards being achieved, the spiritual, moral and social development of pupils, resource management etc",
    ],
}
SOCmeta["2324"] = {
    "group_title": "Early education and childcare services managers",
    "group_description": "Early education and childcare services managers plan, organise, direct and co-ordinate the administration, support systems and activities that facilitate the effective running of nurseries and early education centres.",
    "entry_routes_and_quals": "Entrants will usually have a degree or level 3 qualification in childcare and significant relevant experience. Early years teacher status may be required. An additional management qualification may also be required by some employers. Entry is possible with a variety of academic qualifications, professional qualifications and/or relevant experience. A DBS check is mandatory.",
    "tasks": [
        "~directs and co-ordinates the day-to-day activities of nurseries and early years education centres ~helps create a friendly, secure atmosphere to encourage the development of social and language skills and other learning ~determines staffing, financial, material and other short- and long-term requirements and ensures facility meets health, safety, Ofsted and other standards ~writes reports on children\u2019s development and maintains awareness of health and safety issues ~communicates with parents and colleagues on children\u2019s development and well-being",
    ],
}
SOCmeta["2329"] = {
    "group_title": "Other educational professionals n.e.c",
    "group_description": "Job holders in this unit group perform a variety of other educational professional occupational roles not elsewhere classified in minor group 232: Other educational professionals.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications, professional qualifications and/or relevant experience.",
    "tasks": [
        "~designs and implements methods of assessing the performance of students ~co-ordinates and undertakes the evaluation of assessments and awards grades of merit based upon performance ~manages and trains exam invigilators and updates invigilators on current rules and regulations ~advises educational establishments on educational policies and procedures, and the introduction of new technologies ~mark exams and moderates coursework samples ~develop, plan and implement international student recruitment strategies",
    ],
}
SOCmeta["24"] = {
    "group_title": "Business, media and public service professionals",
    "group_description": "Jobholders in this sub-major group advise and act on behalf of clients in legal matters, preside over judicial proceedings, collect and analyse financial information, perform accounting duties, advise on business and management matters, and perform a variety of other professional occupations within the public, welfare, regulatory and voluntary sectors, and within the media.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["241"] = {
    "group_title": "Legal professionals",
    "group_description": "Legal professionals advise and act on behalf of individuals, businesses, organisations and government in legal matters; preside over judicial proceedings; and perform related professional legal duties.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2411"] = {
    "group_title": "Barristers and judges",
    "group_description": "Barristers and judges prepare and conduct court cases on behalf of clients, preside over judicial proceedings, and pronounce judgements within a variety of court settings and tribunals.",
    "entry_routes_and_quals": "Entry to training requires a qualifying law degree or postgraduate diploma. Entrants then undertake a one year Bar Professional Training Course followed by pupillage in one of the Inns of Court. The system for training of advocates in Scotland requires a postgraduate Diploma in Professional Legal Practice, followed by two years\u2019 training as a solicitor and period of professional training lasting several months. The position of judge is obtained by appointment of those who have substantial post-qualifying experience in legal practice.",
    "tasks": [
        "~becomes acquainted with the facts of a case through reading statements, law reports, and consulting with clients or other professionals ~advises client on the basis of legal knowledge, research and past precedent as to whether to proceed with legal action ~drafts pleadings and questions in preparation for court cases, appears in court to present evidence to the judge and jury, cross examines witnesses and sums up why the court should decide in their client\u2019s favour ~hears, reads and evaluates evidence, and instructs or advises the jury on points of law or procedure ~conducts trials according to rules of procedure, announces the verdict and passes sentence and/or awards costs and damages",
    ],
}
SOCmeta["2412"] = {
    "group_title": "Solicitors and lawyers",
    "group_description": "Solicitors advise and act on behalf of individuals, organisations, businesses and government departments in legal matters.",
    "entry_routes_and_quals": "Entry to training usually requires a qualifying law degree or postgraduate diploma. Apprenticeships are also available. Graduates in subjects other than law must first take a one year conversion course. All entrants undertake a one year legal practice course, followed by a two year training contract. From 2021 Solicitors also need to pass the Solicitor's Qualifying Examination.",
    "tasks": [
        "~draws up contracts, leases, wills and other legal documents ~undertakes legal business on behalf of client in areas of business law, criminal law, probate, conveyancing and litigation, and acts as trustee or executor if required ~instructs counsel in higher and lower courts and pleads cases in lower courts as appropriate ~scrutinises statements, reports and legal documents relevant to the case being undertaken and prepares papers for court ~represents clients in court",
    ],
}
SOCmeta["2419"] = {
    "group_title": "Legal professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of other professional legal occupations not elsewhere classified in minor group 241: Legal professionals.",
    "entry_routes_and_quals": "Entry to training usually requires a qualifying law degree or postgraduate diploma. Entrants then undertake a further year of academic training and then complete up to four years of assessed supervised experience in legal practice. Entrants may also require up to five years post qualifying experience in legal practice.",
    "tasks": [
        "~co-ordinates the activities of magistrates courts and advises magistrates on law and legal procedure ~provides legal advice to individuals within Citizens Advice, Law Centres and other such establishments ~drafts and negotiates contracts on behalf of employers ~advises employers, local and national government and other organisations on aspects of law and legislative implications of decisions made ~advises on, drafts documents for and assists in all aspects of property conveyancing ~collates information, drafts briefs and other documents, interviews and advises clients and undertakes preparatory work for cases ~represents public and private organisations in court as necessary",
    ],
}
SOCmeta["242"] = {
    "group_title": "Finance professionals",
    "group_description": "Finance professionals perform accountancy duties, advise industrial, commercial and other establishments on financial matters, collect and analyse financial information, advise on tax matters and assess tax liabilities and manage investments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2421"] = {
    "group_title": "Chartered and certified accountants",
    "group_description": "Chartered and certified accountants provide accounting and auditing services, advise clients on financial matters, collect and analyse financial information and perform other accounting duties required by management for the planning and control of an establishment\u2019s income and expenditure.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification. Apprenticeships are also available. To qualify as an accountant, entrants must undertake a period of training within an approved organisation and successfully complete professional examinations. Exemptions to some professional examinations are available to those with appropriate academic qualifications.",
    "tasks": [
        "~plans and oversees implementation of accountancy system and policies ~prepares financial documents and reports for management, shareholders, statutory or other bodies ~audits accounts and book-keeping records ~prepares tax returns, advises on tax problems and contests disputed claim before tax official ~conducts financial investigations concerning insolvency, fraud, possible mergers, etc. ~evaluates financial information for management purposes ~liaises with management and other professionals to compile budgets and other costs ~prepares periodic accounts, budgetary reviews and financial forecasts ~conducts investigations and advises management on financial aspects of productivity, stock holding, sales, new products, etc",
    ],
}
SOCmeta["2422"] = {
    "group_title": "Finance and investment analysts and advisers",
    "group_description": "Finance and investment analysts and advisers advise customers, who may be individuals, companies or specialist groups, on the purchase of investments, insurance, mortgages, pensions and other financial services and products.",
    "entry_routes_and_quals": "There are no formal academic requirements although entrants usually possess GCSEs/S grades and a degree in a relevant subject is sometimes required. Training may be undertaken in-house or entrants may attend courses run by professional institutions. Registration with a regulatory authority is required in some positions.",
    "tasks": [
        "~predicts the likely long- and short-term future performance of securities and other financial products and advises upon what will be an appropriate investment for their clients ~analyses the financial position of clients, considering outgoings, dependants and commitments ~advises on the relative merits of pension schemes, insurance policies and mortgages that best meet the needs of clients given their personal circumstances ~monitors information on the socio-economic environment and interprets the implications of such information for their clients ~prepares summary reports of findings for fund managers ~keeps up to date with financial products, legislation and requirements for compliance with the relevant regulatory authority ~identifies and attracts new clients by arranging visits and explaining the benefits of financial products",
    ],
}
SOCmeta["2423"] = {
    "group_title": "Taxation experts",
    "group_description": "Taxation experts advise on tax matters and assess tax liabilities.",
    "entry_routes_and_quals": "Entry is possible with GCSEs/S grades or a BTEC/ SQA award, although many entrants possess a degree or equivalent qualification. A professional qualification is required in either accountancy or taxation. Training is undertaken on-the-job and usually takes approximately four years to complete.",
    "tasks": [
        "~examines accounts of industrial, commercial and other establishments to determine their tax liability and adjusts claims where necessary ~considers particular problems concerning all forms of personal and company taxation ~stays abreast of all changes in tax law and precedent ~discusses disputed cases with accountants and other specialists ~represents Government, client or employer in contested claims before tax officials or an independent tribunal",
    ],
}
SOCmeta["243"] = {
    "group_title": "Business, research and administrative professionals",
    "group_description": "Business, research and administrative professionals advise industrial, commercial and other establishments on management, business and administrative matters, collect and analyse financial and other information, direct and co-ordinate marketing activities and find new business and negotiate contracts for an organisation, ensures that companies conform to relevant legal, statutory and financial requirements, and carry out research in non-scientific areas of activity.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2431"] = {
    "group_title": "Management consultants and business analysts",
    "group_description": "Management consultants and business analysts advise industrial, commercial and other establishments on a variety of management and business-related matters to assist in the formulation of financial and business policies in order to maximise growth or improve business performance.",
    "entry_routes_and_quals": "Entry is most common with a degree or equivalent qualification but is possible with other academic qualifications. Professional qualifications are available and will be a requirement in some areas.",
    "tasks": [
        "~assesses the functions, objectives and requirements of the organisation seeking advice ~identifies problems concerned with business strategy, policy, organisation, procedures, methods and markets ~determines the appropriate method of data collection and research methodology, analyses and interprets information gained and formulates and implements recommendations and solutions ~advises governments, commercial enterprises, organisations and other clients in light of research findings ~runs workshops, and addresses seminars, conferences and the media to present results of research activity or to express professional views",
    ],
}
SOCmeta["2432"] = {
    "group_title": "Marketing and commercial managers",
    "group_description": "Marketing and commercial managers manage, plan and oversee the promotion of services, products, companies or brands, find new business, plan specifications and prepare details of the requirements for a project and negotiate contracts.",
    "entry_routes_and_quals": "There are no pre-set academic entry requirements. A degree or equivalent qualification in a relevant field may be advantageous and significant relevant experience is usually required.",
    "tasks": [
        "~liaises with other senior staff to determine the range of goods or services to be sold, contributes to the development of sales strategies and setting of sales targets ~discusses employer\u2019s or client\u2019s requirements, carries out surveys or other market research and analyses customers\u2019 reactions to product, packaging, price, etc ~compiles and analyses sales figures, prepares proposals for marketing campaigns and promotional activities ~produces reports and recommendations concerning marketing and sales strategies for senior management ~manages a marketing team and directs the implementation of marketing strategies for products and services ~builds relationships with clients, negotiates new business contracts, plans specifications and prepares details of the requirements for a project",
    ],
}
SOCmeta["2433"] = {
    "group_title": "Actuaries, economists and statisticians",
    "group_description": "Actuaries, economists and statisticians apply theoretical principles and practical techniques to assess risk and formulate probabilistic outcomes in order to inform economic and business policy, and to analyse and interpret data used to assist in the formulation of financial, business and economic policies in order to maximise growth or improve business performance.",
    "entry_routes_and_quals": "Entry is most common with a relevant degree or equivalent qualification. Professional qualifications are available and mandatory for actuarial occupations.",
    "tasks": [
        "~assesses the objectives and requirements of the organisation seeking advice ~uses a variety of techniques and theoretical principles to establish probability and risk in respect of e.g. life insurance or pensions ~uses appropriate techniques and theoretical principles to determine an appropriate method of data collection and research methodology, analyse and interpret information gained and formulate recommendations on issues such as future trends, improved efficiency ~designs and manages surveys and uses statistical techniques in order to analyse and interpret the quantitative data collected ~provides economic or statistical advice to governments, commercial enterprises, organisations and other clients in light of research findings ~addresses seminars, conferences and the media to present results of research activity or to express professional views",
    ],
}
SOCmeta["2434"] = {
    "group_title": "Business and related research professionals",
    "group_description": "Business and related research professionals carry out a variety of research activities for the broadcast and print media, for the police and armed forces intelligence services, for national security agencies and in other non-scientific areas.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification. Training is usually provided on-the-job, or support may be given for postgraduate study. Professional qualifications are available in some areas.",
    "tasks": [
        "~liaises with production team to generate and develop ideas for film, television and radio programmes ~research sources for accurate factual material, finds suitable contributors to programmes or print features and deals with any copyright issues ~briefs presenters, scriptwriters or journalists as required via verbal or written reports ~provides administrative support for programme development such as booking facilities ~provides support to criminal intelligence or to military or other security operations by gathering and verifying intelligence data and sources ~presents findings in the required format, via written reports or presentations ~researches images for clients in a wide range of media using specialist picture libraries and archives, museums, galleries etc., or commissions new images ~liaises with client on the appropriate image/s to be used ~deals with copyright issues and negotiates fees ~liaises with client to understand their market research needs, establishes an appropriate quantitative and qualitative market research methodology and prepares proposals outlining programmes of work and details of costs ~manages and directs research, collates and interprets findings and presents results to clients ~discusses possible changes that need to be made in terms of design, price, packaging, marketing and promotion etc. in light of market research with appropriate departments",
    ],
}
SOCmeta["2435"] = {
    "group_title": "Professional/chartered company secretaries",
    "group_description": "Chartered company secretaries and governance professionals ensure companies conform to relevant legal, statutory and financial requirements and monitors standards of corporate governance.",
    "entry_routes_and_quals": "Entrants usually possess a relevant degree and significant relevant experience. To gain chartered status you must pass the Governance Institute's qualifying scheme, which is required to be the secretary of a public limited company.",
    "tasks": [
        "~coordinates governances meetings, such as board and annual general meetings, writes minutes and resolutions ~analyses internal processes and systems, recommends and implements procedural and policy changes ~advises on the company's legal responsibilities and relevant regulations and liaises with external regulators, auditors, lawyers and other professionals ~produces registers of shareholders, annual company reports ~submits companies information to Companies House and the Stock Exchange ~maintains registers of shareholders and administers share options schemes and payment of dividends ~oversees various administrative functions such as the pensions and insurance cover of employees, health and safety, auditing and estate management",
    ],
}
SOCmeta["2439"] = {
    "group_title": "Business, research and administrative professionals n.e.c.",
    "group_description": "Job holders in this unit group advise on the formulation and implementation of policy in the public and private sectors, develop and implement substantial business, statistical and administrative systems, and perform a variety of functions not elsewhere classified in minor group 243: Business, research and administrative professionals.",
    "entry_routes_and_quals": "Entrants typically possess a degree or an equivalent qualification. Entry is also possible by internal promotion for those with appropriate experience. Training is often provided on-the-job in the form of short courses for specialist areas.",
    "tasks": [
        "~coordinates the organisation\u2019s services and resources, liaising with other senior staff ~analyses internal processes and systems, recommends and implements procedural and policy changes ~recruits and manages staff, assigns and delegates tasks and duties, makes changes in procedures to deal with variations in workload ~develops plans, sets objectives and monitors and evaluates performance ~prepares and reviews operational and financial reports ~controls and administers budgets ~advises national and local government on the interpretation and implementation of policy decisions, acts and regulations, and provides technical assistance in the formulation of policy ~co-ordinates and directs the activities of Revenue and Customs offices, Job Centres, Benefits Agency offices and other local offices of national government ~registers and maintains records of all births, deaths and marriages in local authority area, issues appropriate certificates and reports any suspicious causes of death to the coroner. ~negotiates and monitors contracted out services provided by the private sector to local government studies and acts upon any legislation that may affect the local authority",
    ],
}
SOCmeta["244"] = {
    "group_title": "Business and financial project management professionals",
    "group_description": "Job holders in this minor group manage and oversee major projects across all sectors of modern industry, commerce and the public sector, in areas such as e-commerce, business analysis, finance, product development, marketing, and human resources.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2440"] = {
    "group_title": "Business and financial project management professionals",
    "group_description": "Business and financial project management professionals manage and oversee major projects across all sectors of modern industry, commerce and the public sector, in areas such as e-commerce, business analysis, finance, product development, marketing, human resources.",
    "entry_routes_and_quals": "Entry may be via a degree or postgraduate qualification in project management or a subject relevant to the particular sector or via significant relevant work experience in that sector.",
    "tasks": [
        "~finds out what the client or company wants to achieve ~agrees timescales, costs and resources needed ~draws up a detailed plan for how to achieve each stage of the project ~selects and leads a project team ~negotiates with contractors and suppliers for materials and services ~ensures that each stage of the project is progressing on time, on budget and to the right quality standards ~reports regularly on progress to the client or to senior managers",
    ],
}
SOCmeta["245"] = {
    "group_title": "Architects, chartered architectural technologists, planning officers, surveyors and construction professionals",
    "group_description": "Architects, Chartered architectural technologists, town planners and surveyors conduct surveys to determine the exact position of natural and constructed features, design, provide technical solutionsand plan the layout of buildings for commercial, residential, industrial and other uses, prepare bills of quantities for construction projects, manage major construction projects and provide architectural design services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2451"] = {
    "group_title": "Architects",
    "group_description": "Architects plan and design the construction and development of buildings and land areas with regard to functional and aesthetic requirements.",
    "entry_routes_and_quals": "Entrants require a professional qualification in architecture that will encompass an accredited degree and postgraduate qualification, and at least two years practical experience.",
    "tasks": [
        "~liaises with client and other professionals to establish building type, style, cost limitations and landscaping requirements ~studies condition and characteristics of site, taking into account drainage, topsoil, trees, rock formations, etc. ~analyses site survey and advises client on development and construction details and ensures that proposed design blends in with the surrounding area ~prepares detailed scale drawings and specifications for design and construction and submits these for planning approval ~monitors construction work in progress to ensure compliance with specifications",
    ],
}
SOCmeta["2452"] = {
    "group_title": "Chartered architectural technologists, planning officers and consultants",
    "group_description": "Chartered architectural technologists, planning officers and consultants direct or undertake the planning of the layout and the co-ordination of plans for the development of urban and rural areas, provide architectural design services, and negotiate and manage the development from conception to completion of construction projects and lead on a variety of technical functions and solutions in the design of buildings and the layout of urban and rural areas.",
    "entry_routes_and_quals": "Entrants possess a variety of qualifications including GCSEs/S grades, a BTEC/SQA award, an Honours or Masters degree. Membership of professional institutions may be required for some posts. To gain professional status an accredited Honours degree or postgraduate qualification is usually required, as well as continuing professional development. Chartered Architectural Technologists must join the Chartered Institute of Architectural Technologists and satisfy its\u2019 education, practice and professional standards to qualify via an accredited honours degree or equivalent, monitored and assessed practical experience and pass a professional interview. Town planners are also required to complete at least two years of work experience.",
    "tasks": [
        "~analyses information to establish the nature, extent, growth rate and likely development requirements of the area ~examines and evaluates development proposals, consults statutory bodies and other interested parties to ensure that local interests are catered for and recommends acceptance, modification or rejection drafts and presents graphic and narrative plans affecting the use of public and private land, housing and transport facilities ~develops construction project briefs and design programmes and advises clients on methods project procurement, environmental, regulatory, legal and contractual issues and assesses environmental impact ~monitors compliance with design, statutory, and professional requirements, administers contracts and certification, carries out design stage risk assessments and manages health and safety ~evaluates and advises on refurbishment, recycling and deconstruction of buildings ~prepares designs, building plans and drawings for use by contracts and investigates proposed design with regard to practicality, cost and use ~surveys land uses and prepares report for planning authority and issues development permits as authorised ~liaises with engineers and building contractors regarding technical construction problems and attends site meetings, as the lead consultant or as part of the team. ~provides expert advice on issues related to planning and development, including practical, regulatory, legal and statutory matters ~Chartered architectural technologists specialise in design, underpinned by building science, engineering and technology applied to architecture within projects.",
    ],
}
SOCmeta["2453"] = {
    "group_title": "Quantity surveyors",
    "group_description": "Quantity surveyors advise on financial and contractual matters relating to, and prepare bills of quantities for, construction projects and provide other support functions concerning the financing and materials required for building projects.",
    "entry_routes_and_quals": "Entry is through professional training and membership of an appropriate professional organisation. Entry to professional examinations will require a degree or equivalent qualification. Apprenticeships are also available. Candidates usually undertake a period of probationary training and professional assessment.",
    "tasks": [
        "~liaises with client on project costs, formulates detailed cost plan and advises contractors and engineers to ensure that they remain within cost limit ~examines plans and specifications and prepares details of the material and labour required for the project ~prepares bills of quantities for use by contractors when tendering for work ~examines tenders received, advises client on the most acceptable and assists with preparation of a contract document ~measures and values work in progress and examines any deviations from original contract ~measures and values completed contract for authorisation of payment",
    ],
}
SOCmeta["2454"] = {
    "group_title": "Chartered surveyors",
    "group_description": "Chartered surveyors conduct surveys related to the measurement, management, valuation and development of land, natural resources, buildings, other types of property, and infrastructure such as harbours, roads and railway lines.",
    "entry_routes_and_quals": "Entrants usually possess an accredited degree, equivalent qualification and/or postgraduate qualification. Entrants must also have successfully completed a probationary training period and professional assessment. Entry requirements to professional bodies vary.",
    "tasks": [
        "~surveys, measures and describes land surfaces to establish property boundaries and to aid with construction or cartographic work ~surveys mines, prepares drawings of surfaces, hazards and other features to control the extent and direction of mining ~surveys buildings to determine necessary alterations and repairs ~measures shore lines, elevations and underwater contours, establishes high and low water marks, plots shore features and defines navigable channels",
    ],
}
SOCmeta["2455"] = {
    "group_title": "Construction project managers and related professionals",
    "group_description": "Construction project managers and related professionals manage and oversee major construction and civil engineering projects and major building contracts for quality of work, safety, timeliness and completion within budget, forecast travel patterns and develop strategies for managing the impact of traffic-related demand.",
    "entry_routes_and_quals": "Entrants normally possess a degree in a relevant subject or equivalent qualification and/or substantial work experience at an appropriate level. Further Continuing Professional Development is available in some areas.",
    "tasks": [
        "~draws up budgets and timescales for new construction projects based on clients\u2019 requirements ~briefs project team, contractors and suppliers ~assembles information for invoicing at the end of projects ~plans work schedules for construction projects based on prior discussion with architects, Chartered architectural technologists, surveyors etc. ~hires and may supervise site staff, establishes temporary site offices, takes delivery of materials ~regularly inspects and monitors progress and quality of work, ensures legal requirements are met ~identifies defects in work and proposes corrections ~records, monitors and reports progress ~forecasts the impact on traffic and transport of new developments (e.g. shopping centre) ~assesses schemes to manage traffic such as congestion charging and parking controls ~examines accident \u2018blackspots\u2019 to improve road safety ~writes reports for funding bids and planning authorities and acts as expert witness",
    ],
}
SOCmeta["246"] = {
    "group_title": "Welfare professionals",
    "group_description": "Workers in this minor group provide information, advice and support to protect the welfare of vulnerable groups; supervise, counsel and help offender\u2019s and provide spiritual motivation and guidance.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2461"] = {
    "group_title": "Social workers",
    "group_description": "Social workers provide information, advice and support to those who are socially excluded or are experiencing crisis; they protect the welfare of vulnerable groups including children, young people, people with disabilities, elderly people and people who are mentally or physically ill, and they may specialise in specific areas of work.",
    "entry_routes_and_quals": "Social work is a regulated profession and practitioners must be registered with the appropriate statutory body. To register a social worker must satisfy the criteria for registration. Non-graduates must undertake a three year degree in social work; graduates with relevant experience may take a two year postgraduate diploma/Master\u2019s degree. Prior relevant work experience or relevant voluntary work is encouraged. Background checks including a DBS check are required.",
    "tasks": [
        "~liaises with other health and social care professionals and agencies to identify those in need and at risk within the local community ~interviews individuals and groups to assess and review the nature and extent of difficulties ~undertakes and writes up assessments to specified standards ~arranges for further counselling or assistance in the form of financial or material help ~organises support and develops care plans to address service users\u2019 needs ~keeps case records, prepares reports and participates in team meetings ~gives evidence in court ~participates in training and supervision",
    ],
}
SOCmeta["2462"] = {
    "group_title": "Probation officers",
    "group_description": "Probation officers work to rehabilitate offenders. They supervise, counsel and help them before trial, during any prison or community sentence and on release from prison",
    "entry_routes_and_quals": "Candidates are recruited with a variety of academic qualifications or with relevant experience. In England and Wales all candidates must complete a two year Diploma in Probation studies. In Scotland and Northern Ireland, entry requirements are the same as for social workers. Background checks including a DBS check are required.",
    "tasks": [
        "~produces pre-sentence reports to the court about an individual\u2019s crime, their personal circumstances, the suitability of sentencing, the likelihood of re-offending and the future risk to the public ~enforces court orders and serves the public by providing a wide range of supervision programmes for those in receipt of a community sentence ~draws up probation plans with offenders and helps them follow it, advises them on any work and helps them with any family or social problems ~works with prisoners in giving advice on problems such as drug and alcohol abuse, addressing training needs, finding work and getting accommodation ~keeps accurate and comprehensive records",
    ],
}
SOCmeta["2463"] = {
    "group_title": "Clergy",
    "group_description": "Members of the clergy provide spiritual motivation and guidance, conduct worship according to the form of service of a particular faith/denomination and perform related functions associated with religious beliefs and practices.",
    "entry_routes_and_quals": "Entrants typically possess a degree or equivalent qualification. Candidates for the clergy according to the Christian faith must pass a selection procedure and attend theological college where training includes theological instruction and practical pastoral experience. Training can last up to six years depending upon age, experience and denomination. Entry routes for other religious professionals will vary according to the particular faith concerned.",
    "tasks": [
        "~prepares and delivers sermons and talks and leads congregation in worship ~interprets doctrines and instructs intending clergy members in religious principles and practices ~provides and arranges the provision of religious instruction to congregation members ~performs marriages, funerals, baptisms and other special religious rites ~provides pastoral care to members of the congregation in their homes and in hospitals and counsels those in need of spiritual or moral guidance ~undertakes administration and social duties as required",
    ],
}
SOCmeta["2464"] = {
    "group_title": "Youth work professionals",
    "group_description": "Youth work professionals look after the welfare and support the development of young people.",
    "entry_routes_and_quals": "Professional youth workers require an accredited qualification at degree level, recognised by the National Youth Agency. Experience working with young people may also be useful. Background checks including a DBS check are likely to be required.",
    "tasks": [
        "~provides activities to assist young people develop and fulfil their potential as individuals and within the community ~develops relationships with and provides guidance to young people ~advises and supports young people experiencing stress or crisis ~mentors and counsels young people with mental health problems ~manages volunteers and part-time workers, and liaises with other relevant professionals ~keeps records and controls budgets",
    ],
}
SOCmeta["2469"] = {
    "group_title": "Welfare professionals n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of welfare-related professional occupations not elsewhere classified in minor group 246: Welfare professionals.",
    "entry_routes_and_quals": "Entry is via a variety of relevant academic and/or professional qualifications. Background checks including a DBS check are likely to be required.",
    "tasks": [
        "~provides activities to assist young people develop and fulfil their potential as individuals and within the community ~advises and supports families experiencing stress or crisis ~acts as an advocate for and represents individuals and families at tribunals and similar hearings ~oversees, supervises and provides counselling for the process of adoption ~mentors and counsels those with mental health problems ~provides rehabilitation services to individuals ~manages volunteers and part-time workers, and liaises with other relevant professionals ~keeps records and controls budgets",
    ],
}
SOCmeta["247"] = {
    "group_title": "Librarians and related professionals",
    "group_description": "Librarians and related professionals appraise, obtain, organise, develop, preserve and make available collections of written and recorded material, art objects, pictures, artefacts and other items of general and specialised interest.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2471"] = {
    "group_title": "Librarians",
    "group_description": "Librarians appraise, obtain, index, collate and make available library acquisitions and organise and control other library services.",
    "entry_routes_and_quals": "Entry will normally require an accredited degree or postgraduate qualification. Most postgraduate courses require applicants to have had prior relevant work experience. Professional and relevant vocational qualifications at levels 2 and 3.",
    "tasks": [
        "~selects and arranges for the acquisition of books, periodicals, audio-visual and other material ~collects, classifies and catalogues information, books and other material ~prepares and circulates abstracts, bibliographies, book lists, etc. ~identifies the information needs of clients, seeks out and evaluates information sources ~establishes information storage systems to deal with queries and to maintain up to date records ~manages library borrowing and inter-library loan facilities ~promotes library services through displays and talks ~provides learning and cultural experiences through events such as author talks, reading groups, formal and informal teaching",
    ],
}
SOCmeta["2472"] = {
    "group_title": "Archivists, conservators and curators",
    "group_description": "Archivists, conservators and curators collect, appraise and preserve collections of recorded and other material of historical interest.",
    "entry_routes_and_quals": "Entrants require a good first degree in order to gain entry to a relevant postgraduate course. Many postgraduate courses also require applicants to have gained relevant practical experience prior to entry. Training is typically received on-the-job.",
    "tasks": [
        "~examines, appraises and advises on the acquisition of exhibits, historic records, government papers and other material ~classifies material and arranges for its safe keeping and preservation ~maintains indexes, bibliographies and descriptive details of archive material and arranges for reproductions of items where necessary ~examines objects to identify any damage and carries out necessary restoration whilst preserving original characteristics ~makes sure that storage and display conditions protect objects from deterioration and damage ~allows access to original material or material not on display for researchers ~develops and promotes ideas for exhibitions and displays ~negotiates loans of material for specialist displays ~liaises with school and other groups or individuals, publicises exhibits and arranges special displays for general, specialised or educational interest ~answers verbal or written enquiries and gives advice on exhibits or other material",
    ],
}
SOCmeta["248"] = {
    "group_title": "Quality and regulatory professionals",
    "group_description": "Quality and regulatory professionals plan, coordinate and technically supervise products or services to ensure they are fit for purpose and meet legal compliance and industry quality standards.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2481"] = {
    "group_title": "Quality control and planning engineers",
    "group_description": "Quality control and planning engineers plan production schedules, work sequences, and manufacturing and processing procedures to ensure accuracy, quality and reliability.",
    "entry_routes_and_quals": "Quality control and planning engineers usually possess an accredited university degree. After qualifying, periods of appropriate training and experience are required before membership of a chartered engineering institution is achieved. Incorporated engineers possess an accredited university degree, BTEC/SQA award or an apprenticeship leading to an NVQ/SVQ at level 4. All routes are followed by periods of appropriate training and relevant experience.",
    "tasks": [
        "~devises inspection, testing and evaluation methods for bought-in materials, components, semi-finished and finished products ~ensures accuracy of machines, jigs, fixtures, gauges and other manufacturing and testing equipment ~prepares work flow charts for individual departments and compiles detailed instructions on processes, work methods and quality and safety standards for workers ~analyses plans, drawings, specifications and safety, quality, accuracy, reliability and contractual requirements ~prepares plan of sequence of operations and completion dates for each phase of production or processing ~oversees effective implementation of adopted processes, schedules and procedures",
    ],
}
SOCmeta["2482"] = {
    "group_title": "Quality assurance and regulatory professionals",
    "group_description": "Quality assurance and regulatory professionals plan, organise, co-ordinate and direct the effective measurement monitoring and reporting on the qualitative and regulatory aspects of a specified tangible (industrial production) or non-tangible (service provision) output.",
    "entry_routes_and_quals": "Entry normally requires a degree or equivalent qualification with relevant experience. Off and on-the-job training is available. A variety of vocational qualifications that encompass quality assurance elements are available at up to level 4.",
    "tasks": [
        "~develops and implements visual, physical, functional or other appropriate measures and tests of quality ~analyses and reports upon the results of quality control tests to ensure that production remains within specification ~considers the impact of legislation upon specification requirements ~examines current operating procedures to determine how quality may be improved ~examines operating procedures to ensure the process and the product meet regulatory standards and implements changes necessary to ensure compliance",
    ],
}
SOCmeta["2483"] = {
    "group_title": "Environmental health professionals",
    "group_description": "Environmental health professionals use specialist technical skills and knowledge to protect people from health risks associated with the environment in which they live and work. They maintain and safeguard standards, including taking legal action to enforce relevant legislation with regard to public health policy.",
    "entry_routes_and_quals": "Entrants normally require a degree accredited by the Chartered Institute of Environmental Health (CIEH) or the Royal Environmental Health Institute of Scotland (REHIS). To gain chartered status an additional period of work experience is required or successful completion of the CIEH's chartered practitioner programme.",
    "tasks": [
        "~inspects businesses for compliance with legislation on health and safety, food hygiene and food standards and takes appropriate action in the event of non-compliance ~follows up complaints of unsafe workplaces, investigating accidents ~investigates outbreaks of food poisoning, infectious diseases or pests ~monitors radiation activity, levels of noise, air, land and water pollution and takes appropriate action when safety levels are exceeded ~ensures animal welfare for compliance with legislation, issues licences for premises such as pet shops, zoos and abattoirs ~gives talks at public enquiries and meetings, ensures compliance through education, advice and enforcement ~initiates legal proceedings and gives evidence in court",
    ],
}
SOCmeta["249"] = {
    "group_title": "Media professionals",
    "group_description": "Media professionals plan, coordinate and technically supervise activities in journalism, public relations and advertising.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["2491"] = {
    "group_title": "Newspaper, periodical and broadcast editors",
    "group_description": "Newspaper, periodical and broadcast editors evaluate, manage and oversee the editorial direction for the style and content of features and stories for broadcasting and for newspapers, magazines, news websites and periodicals.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification and significant relevant experience. A variety of postgraduate diplomas are available. Vocational qualifications covering various aspects of journalism are available at levels 3 and 4.",
    "tasks": [
        "~commissions articles and selects material for broadcast or publication ~checks style, grammar, accuracy and legality of content and arranges for any necessary revisions ~decides on lay out of material in news websites, newspapers, magazines, or periodicals ~liaises with production staff in checking final proof copies immediately prior to printing",
    ],
}
SOCmeta["2492"] = {
    "group_title": "Newspaper and periodical broadcast journalists and reporters",
    "group_description": "Newspaper and periodical broadcast journalists and reporters investigate and write up stories and features for broadcasting and for newspapers, magazines, news website and other periodicals.",
    "entry_routes_and_quals": "Entrants usually possess a degree or equivalent qualification. A variety of postgraduate diplomas is available. Vocational qualifications covering various aspects of journalism are available at levels 3 and 4.",
    "tasks": [
        "~determines subject matter and undertakes research by interviewing, attending public events, seeking out records, reviewing written work, attending film and stage performances etc ~responds to stories as they break ~writes articles and features and submits draft manuscripts to newspaper, magazine, new website, periodical or programme editor ~engage with the public and disseminate news stories, lifestyle and opinion pieces through social media ~builds contacts in their field to ensure a supply of news ~sub-edits other journalists' stories",
    ],
}
SOCmeta["2493"] = {
    "group_title": "Public relations professionals",
    "group_description": "Public relations professionals plan, organise and co-ordinate the activities that promote the image and understanding of an organisation and its products or services to consumers, businesses, members of the public and other specified audiences.",
    "entry_routes_and_quals": "Most entrants possess A levels/H grades and a degree or equivalent qualification. Further professional qualifications are available.",
    "tasks": [
        "~discusses issues of business strategy, products, services and target client base with senior colleagues to identify public relations requirements ~writes, edits and arranges for the effective distribution of press releases, newsletters, social media and other public relations material ~addresses individuals, clients and other target groups through meetings, presentations, the media and other events to enhance the public image of an organisation ~develops and implements tools to monitor and evaluate the effectiveness of public relations exercises",
    ],
}
SOCmeta["2494"] = {
    "group_title": "Advertising accounts managers and creative directors",
    "group_description": "Advertising accounts managers and creative directors plan, design, organise and direct the advertising activities of an organisation.",
    "entry_routes_and_quals": "Entry is generally via career progression from related occupations. There are no pre-set entry standards, but in practice most directors hold a degree. Off and on-the-job training is provided.",
    "tasks": [
        "~liaises with client to discuss product/service to be marketed, defines target group and assesses the suitability of various media ~conceives advertising campaign to impart the desired product image in an effective and economical way, including planning which media to use, such as print, television, radio or online advertising ~reviews and revises campaign in light of sales figures, surveys, etc. ~stays abreast of changes in media, readership or viewing figures and advertising rates ~arranges conferences, exhibitions, seminars, etc. to promote the image of a product, service or organisation",
    ],
}
SOCmeta["3"] = {
    "group_title": "Associate professional occupations",
    "group_description": "This major group covers occupations whose main tasks require experience and knowledge of principles and practices necessary to assume operational responsibility and to give technical support to Professionals and to Managers, Directors and Senior Officials. The main tasks involve the operation and maintenance of complex equipment; legal, business, financial and design services; the provision of information technology services; providing skilled support to health and social care professionals; and serving in protective service occupations. Culture, media and sports occupations are also included in this major group. Most occupations in this major group will have an associated high-level vocational qualification, often involving a substantial period of full-time training or further study. Some additional task-related training is usually provided through a formal period of induction.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["31"] = {
    "group_title": "Science, engineering and technology associate professionals",
    "group_description": "Science, engineering and technology associate professionals perform a variety of technical support functions to scientists, biomedical technologists, engineers architects, Chartered architectural technologists prepare technical drawings, undertake building inspections, provide technical support for IT operations and users.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["311"] = {
    "group_title": "Science, engineering and production technicians",
    "group_description": "Science, engineering and production technicians perform a variety of technical support functions to assist the work of scientists and biomedical technologists, assist in the design, development, production and maintenance of electronic systems, perform technical quality assurance related tasks, support the work of building and civil engineers, and perform various other technical support functions for engineers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3111"] = {
    "group_title": "Laboratory technicians",
    "group_description": "Laboratory technicians carry out routine laboratory tests and checks and perform a variety of technical support functions requiring the application of established or prescribed procedures and techniques to assist scientists with their research, development, analysis and testing, and to verify the physical, chemical and other characteristics of materials and products.",
    "entry_routes_and_quals": "Entry varies from employer to employer. Entrants usually possess a degree, although entry is also possible with A-levels, GCSEs/S grades, an appropriate BTEC/SQA award or HNC/HND. Professional qualifications, NVQs/SVQs at various levels, and apprenticeships are available in some areas of work. Good eyesight, and in some cases, normal colour vision are also required.",
    "tasks": [
        "~sets up and assists with the construction and the development of scientific apparatus for experimental, demonstration or other purposes ~prepares organic and inorganic material for examination and stains and fixes slides for microscope work ~operates and services specialised scientific equipment, undertakes prescribed measurements and analyses and ensures that sterile conditions necessary for some equipment are maintained ~records and collates data obtained from experimental work and documents all work carried out ~maintains and rotates stock and supplies ~disposes of chemical and biological waste safely ~keeps up to date with new technical developments",
    ],
}
SOCmeta["3112"] = {
    "group_title": "Electrical and electronics technicians",
    "group_description": "Electrical and electronics technicians perform a variety of miscellaneous technical support functions to assist with the design, development, installation, operation and maintenance of electrical and electronic systems.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades, a BTEC/ SQA award or a relevant certificate/diploma. Vocational qualifications in Electrical Installation, Electrical Engineering and other relevant fields at levels 2 to 4 and apprenticeships are available.",
    "tasks": [
        "~plans and prepares work and test schedules based on specifications and drawings ~sets up equipment, undertakes tests, takes readings, performs calculations and records and interprets data ~plans installation methods, checks completed installation for safety and controls or undertakes the initial running of the new electrical or electronic equipment or system ~diagnoses and detects faults and implements procedures to maintain efficient operation of systems and equipment ~visits and advises clients on the use and servicing of electrical and electronic systems and equipment ~interprets and reviews technical drawings",
    ],
}
SOCmeta["3113"] = {
    "group_title": "Engineering technicians",
    "group_description": "Engineering technicians perform a variety of technical support functions to assist engineers with the design, development, operation, installation and maintenance of engineering systems and constructions.",
    "entry_routes_and_quals": "Entrants to training usually possess GCSEs/S grades. Vocational training consists either of full-time study for a BTEC/SQA award followed by two years on-the-job training, or an apprenticeship leading to a qualification at level 3 or 4. An NVQ/SVQ in Aircraft Engineering Maintenance at level 3 plus further professional qualifications are required to become a licensed aircraft engineer.",
    "tasks": [
        "~plans and prepares work and test schedules based on specifications and drawings ~sets up equipment, undertakes tests, takes readings, performs calculations and records and interprets data ~prepares estimates of materials, equipment and labour required for engineering projects ~diagnoses and detects faults and implements procedures to maintain efficient operation of systems and equipment ~inspects completed aircraft maintenance work to certify that it meets standards and the aircraft is ready for operation",
        "~visits and advises clients on the use and servicing of mechanical and chemical engineering products and services ~provides health and safety inductions and adheres to health and safety procedures ~completes documentation such as project records, safety reports ~carries out stock takes",
    ],
}
SOCmeta["3114"] = {
    "group_title": "Building and civil engineering technicians",
    "group_description": "Building and civil engineering technicians perform a variety of technical support functions to assist civil and building engineers.",
    "entry_routes_and_quals": "Entrants usually possess a relevant BTEC/SQA award, level 3 diploma or HNC/HND. Some entrants may posess a degree. The status of engineering technician is obtained after a period of further training at work and upon gaining the membership of a professional engineering institution.",
    "tasks": [
        "~sets up apparatus and equipment and undertakes field and laboratory tests of soil and work materials ~performs calculations and collects, records and interprets data ~sets out construction site, supervises excavations and marks out position of building work to be undertaken ~inspects construction materials and supervises work of contractors to ensure compliance with specifications and arranges remedial work as necessary ~creates and designs plans (using computer aided software) ~estimates project costs ~estimates timescales for project delivery",
    ],
}
SOCmeta["3115"] = {
    "group_title": "Quality assurance technicians",
    "group_description": "Quality assurance technicians perform a variety of technical inspections and testing and monitoring tasks to detect processing, manufacturing and other defects.",
    "entry_routes_and_quals": "Entrants normally possess a degree, GCSEs/S grades, a BTEC/ SQA award or A levels/H grades. Training is typically received on-the-job, supplemented by training courses where instruction in specific techniques is required. Various industry-specific qualifications encompass aspects of quality control.",
    "tasks": [
        "~sets up scientific, electronic, or other technical equipment to perform functional and inspection tests ~analyses and interprets the results of tests undertaken and writes up reports upon completion ~supervises the work of routine inspection staff and notes any defects reported ~assists quality control engineers in undertaking production audits ~liaises with production engineers and staff to maintain the quality of output and to develop quality management systems. ~establishes product specifications ~maintains equipment and systems used",
    ],
}
SOCmeta["3116"] = {
    "group_title": "Planning, process and production technicians",
    "group_description": "Planning, process and production technicians perform a variety of technical support functions to assist production, process and planning engineers with production programmes and schedules and with manufacturing and processing procedures in order to ensure accuracy, cost-effectiveness and efficiency",
    "entry_routes_and_quals": "Entrants to training usually possess GCSEs/S grades. Vocational training consists either of full-time study for a BTEC/SQA National award followed by two years on-the-job training, or an apprenticeship leading to an NVQ/SVQ at level 3.",
    "tasks": [
        "~supports planning and production engineers in assessing existing and alternative production methods ~works from, and helps implement, professional engineers\u2019 drawings and specifications for equipment and layout, and helps implement modifications required for existing plant machinery/layout ~works with engineers on production control methods to monitor operational efficiency and helps to eliminate potential hazards and bottlenecks in production ~liaises with materials buying, storing and controlling departments to ensure a steady flow of supplies ~supports professional engineers in reviewing safety, quality, accuracy, reliability and contractual requirements ~supports implementation of plans of sequence of operations and completion dates for each phase of production or processing ~ensures implementation of inspection, testing and evaluation methods for bought-in materials, components, semi-finished and finished products ~plans and coordinates maintenance activities involved in manufacturing and processing procedures ~ensures accuracy of manufacturing and testing equipment ~ensures effective completion and implementation of detailed instructions on processes, work methods and quality and safety standards for workers ~reviews and analyses production data ~plans the cost impact and staff resources for projects",
    ],
}
SOCmeta["3119"] = {
    "group_title": "Science, engineering and production technicians n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of technical support functions not elsewhere classified in minor group 311: Science, engineering and production technicians.",
    "entry_routes_and_quals": "Entry varies from employer to employer. Entrants usually possess GCSEs/S grades, a BTEC/SQA award or HNC/HND. Professional qualifications are available and may be required in some areas of work.",
    "tasks": [
        "~sets up apparatus for experimental, demonstration or other purposes ~undertakes tests and takes measurements and readings ~performs calculations and records and interprets data ~otherwise assists technologists as directed ~sets up school laboratories for demonstrations and experiments, operates and maintains equipment and supports the teaching of students",
    ],
}
SOCmeta["312"] = {
    "group_title": "Cad, drawing and architectural technicians",
    "group_description": "Workers in this minor group prepare technical drawings, plans and charts and operate and maintain 3D printers. Architectural technicians contribute to and co-ordinate the detailed design process and design information.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3120"] = {
    "group_title": "CAD, drawing and architectural technicians",
    "group_description": "CAD, drawing and architectural technicians design and prepare technical drawings, plans, maps, charts and similar items and install, operate and maintain 3D printers.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades, BTEC/ SQA awards or another appropriate certificate/diploma or A levels/H grades. Further training consists of courses of study and supervised practical experience.",
    "tasks": [
        "~examines design specification and technical information to determine general requirements ~considers the suitability of different materials with regard to the dimensions and weight and calculates the likely fatigue, stresses, tolerances, bonds and threads ~prepares regulatory and statutory applications ~monitors health and safety in design and contributes to design stage risk assessment ~prepares design drawings, plans or sketches using CAD and traditional methods and checks feasibility of construction and compliance with health and safety regulations ~prepares detailed drawings, plans, charts or maps that include natural features, desired surface finish, elevations, electrical circuitry and other details as required ~arranges for completed drawings to be reproduced for use as working drawings ~installs, maintains and repairs 3D printers and assists in the development of CAM plans and the operation of 3D printers",
    ],
}
SOCmeta["313"] = {
    "group_title": "Information technology technicians",
    "group_description": "Workers in this minor group are responsible for the day-to-day running and maintenance of IT systems, databases, websites and networks, and provide technical support, advice and guidance for users and customers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3131"] = {
    "group_title": "IT operations technicians",
    "group_description": "IT operations technicians are responsible for the day-to-day running of IT systems and networks including the preparation of back-up systems, and for performing regular checks to ensure the smooth functioning of such systems.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience. Entrants typically possess GCSEs/S grades and A levels/H grades together with an appropriate vocational qualification. Some employers may demand a relevant degree. Training is provided off and on-the-job supplemented by specialised courses. Postgraduate and professional qualifications and apprenticeships in some areas are available.",
    "tasks": [
        "~administers, monitors and supports internal/external networks, servers, email and security systems ~configures and sets up new server systems ~schedules and performs system maintenance tasks, such as loading user applications, programs and data ~analyses systems and makes recommendations to improve performance ~identifies problems, agrees remedial action and undertakes emergency maintenance if required ~performs server backup and recovery operations and restarts systems following outages ~acts as a liaison between users, outside suppliers, and other technical teams",
    ],
}
SOCmeta["3132"] = {
    "group_title": "IT user support technicians",
    "group_description": "IT user support technicians are responsible for providing technical support, advice and guidance for internal/external users of IT systems and applications, either directly or by telephone, e-mail or other network interaction.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience. Entrants typically possess a degree or GCSEs/S grades and A levels/H grades together with an appropriate vocational qualification. Some employers may demand a relevant degree. Training is provided off and on-the-job supplemented by specialised courses. Postgraduate and professional qualifications and apprenticeships in some areas are available.",
    "tasks": [
        "~provides technical support to IT users ~advises users on how to resolve hardware and software problems ~installs and upgrades hardware, cables, operating systems and/or appropriate software ~facilitates user access to systems ~refers more complex or intractable problems to appropriate IT professionals ~researches possible solutions in user guides, technical manuals and other documents ~maintains a log of work in progress, calls received, actions taken and problems detected ~reports on commonly occurring queries to detect underlying problems",
    ],
}
SOCmeta["3133"] = {
    "group_title": "Database administrators and web content technicians",
    "group_description": "Database administrators and web content technicians administer, maintain and provide user support for databases and websites and assist in the design and development of databases; and monitors social media sites for posts and comments on behalf of companies.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience, although some employers may require a relevant degree. Training is provided off and on-the-job supplemented by specialised courses. Postgraduate qualifications and apprenticeships in some areas are available.",
    "tasks": [
        "~assists in database design and creation and amends existing databases ~tests databases and writes user guides for their operation ~administers, monitors and supports databases and website content ~extracts data and assists others in the use of the database ~writes and publishes content and monitors and maintains functionality of websites ~trains colleagues in the use of the databases and websites ~proof reads social media content and checks content of videos before publication on websites",
    ],
}
SOCmeta["32"] = {
    "group_title": "Health and social care associate professionals",
    "group_description": "Health and social care associate professionals provide a variety of technical support functions and services for health professionals in the treatment of patients to assist physical and psychological recovery, assist teachers in the education of young people, and provide social care and related community services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["321"] = {
    "group_title": "Health associate professionals",
    "group_description": "Workers in this minor group provide a variety of technical support functions for a range of health professionals such as fitting spectacles, dispensing medicines, and providing complementary medical care.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3211"] = {
    "group_title": "Dispensing opticians",
    "group_description": "Dispensing opticians supply, fit and service spectacles, contact lenses and other optical aids in accordance with a prescription from an optician or optometrist.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades or equivalent qualifications or experience, followed by up to three years training approved by the General Optical Council (GOC). To practice entrants must pass professional exams and register with the GOC. Full-time, day-release or distance-learning options are available.",
    "tasks": [
        "~interprets prescription and measures patient\u2019s face to determine distance between pupil centres, height of bridge of nose, etc. ~advises patient on lens type and choice of spectacle frames ~prepares detailed instructions for workshop ~ensures that completed spectacles conform to specification and fit the patient correctly and comfortably ~fits spectacles and advises patient on lens care and any other difficulties likely to be experienced",
    ],
}
SOCmeta["3212"] = {
    "group_title": "Pharmaceutical technicians",
    "group_description": "Pharmaceutical technicians work in hospitals or in the community and assist pharmacists in the preparation and dispensing of drugs and medicines.",
    "entry_routes_and_quals": "Entrants to training usually possess GCSEs/S grades or the equivalent. Training is typically a combination of practical experience and study at a college or by open learning towards vocational qualifications. An approved competency and an approved knowledge based qualification and two years\u2019 experience is required to register as a pharmacy technician with the General Pharmaceutical Council (GPhC).",
    "tasks": [
        "~checks received prescriptions for legality and accuracy ~prepares drugs and medicines under the supervision of pharmacist ~prepares specialised, tailor-made drugs for intravenous administration by hospital medical staff ~labels and checks items prior to dispensing ~maintains records of prescriptions received and drugs issued ~advises patients or customers on the use of drugs prescribed or medication purchased over the counter ~checks stock levels, orders new stock from pharmaceutical companies and ensures that drugs are stored appropriately",
    ],
}
SOCmeta["3213"] = {
    "group_title": "Medical and dental technicians",
    "group_description": "Medical and dental technicians operate, calibrate and maintain cardiographic and encephalographic testing equipment, assist in the conduct of post mortems, give simple dental treatments, fit artificial limbs and hearing aids, and undertake a wide range of related medical and dental tasks.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades, BTEC/SQA awards, an Intermediate GNVQ/GSVQ level II or A levels/H grades. Training may last up to five years depending upon the field and method of study. Professional qualifications and NVQs/SVQs at level 3 are available in some areas.",
    "tasks": [
        "~operates equipment to diagnose and record or treat hearing, heart, brain, lung and kidney ailments ~undertakes scaling and polishing of teeth, applies medicaments, carries out post-operative hygiene work and advises on preventative dentistry ~makes dentures, crowns, bridges, orthodontic and other dental appliances according to individual patient requirements ~measures patients for, and fits them with, surgical appliances, hearing aids and artificial limbs ~performs related medical tasks including treating hair and scalp disorders and conducting tests on glaucoma patients ~takes samples for clinical examination",
    ],
}
SOCmeta["3214"] = {
    "group_title": "Complementary health associate professionals",
    "group_description": "Complementary health associate professionals use non-mainstream treatments in support of conventional medical treatments.",
    "entry_routes_and_quals": "Entry requirements vary in different fields. Some employers require a degree level qualification. Professional qualifications are available, and membership of professional bodies is mandatory in some areas.",
    "tasks": [
        "~advises and prescribes in areas of complementary and alternative medicine ~prescribes and prepares homeopathic remedies ~manipulates and massages patient to discover the cause of pain, relieve discomfort, restore function and mobility and to correct irregularities in body structure ~uses colour therapy to help with people\u2019s mental and physical problems ~administers aromatic herbs and oils and massages body to relieve pain and restore health ~massages reflex points in the hands and feet to relieve pain and promote healing in other parts of the body ~uses hypnotherapy to relieve or treat health conditions and to change habits",
    ],
}
SOCmeta["3219"] = {
    "group_title": "Health associate professionals n.e.c.",
    "group_description": "Job holders in this unit group carry out a variety of technical health support functions not elsewhere classified in minor group 321: Health associate professionals.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic and vocational qualifications. Professional qualifications are also available in some areas. Courses provide a mixture of theoretical study and practical experience. Membership of professional bodies may be mandatory in some areas.",
    "tasks": [
        "~provides information, support and advice on diet ~counsels people on their problems, feelings and dealing with stress ~provides information, support and advice on healthy living and helps people develop healthier lifestyles ~teaches parents about pregnancy, delivery and early parenthood ~examines horses\u2019 teeth for health problems and provides dental treatments which do not need to be provided by a vet",
    ],
}
SOCmeta["322"] = {
    "group_title": "Welfare and housing associate professionals",
    "group_description": "Welfare and housing associate professionals organise and provide social welfare and related community services including working with children and young people, address the housing needs of individuals or localities, assist those with physical and mental disabilities or illnesses, investigate cases of abuse or neglect, provide counselling services and perform other welfare functions.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3221"] = {
    "group_title": "Youth and community workers",
    "group_description": "Youth and community workers provide support to individuals or groups of individuals through a range of activities or services that aim to encourage participation in social and community life and promote personal and social development. Workers in this group also provide family support activities in the home and community, to both parents and children.",
    "entry_routes_and_quals": "Entrants will require a qualification accredited by the National Youth Agency at level 2 or 3. Apprenticeships are also available. Some employers may require people to be aged over 21 years of age. Background checks including a DBS check are likely to be required.",
    "tasks": [
        "~organises social, recreational and educational activities in local community and youth groups ~undertakes the day-to-day running of community centres and supervises the activities of part-time and voluntary workers ~liaises and supports voluntary workers running groups in village halls, churches, mosques and other places of worship ~advises individuals with particular needs or problems through informal discussion, individual counselling or formal group discussion ~helps set up credit unions, encourages parents to establish playgroups, works with other groups to find solutions to shared concerns or problems",
    ],
}
SOCmeta["3222"] = {
    "group_title": "Child and early years officers",
    "group_description": "Child and early years officers work with babies and with children up to 14 years of age (or 16 for those with special needs), providing support, help and advice to individuals or within a family context.",
    "entry_routes_and_quals": "There are no formal qualification requirements for entry although many employers will expect those appointed to have A-levels and to be working towards a relevant diploma or degree, together with work experience in a relevant field. For some roles workers must be registered with the appropriate statutory body. Some jobs are regulated and require job holders to satisfy the criteria for registration (including holding appropriate qualifications). Background checks including a DBS check are mandatory.",
    "tasks": [
        "~deals with issues relating to poor attendance at school ~works with social worker to identify, plan and deliver appropriate support to families facing a variety of difficulties ~advises clients and their families on available resources ~writes up case notes, prepares reports, keeps up-to-date records on clients ~makes referrals to other agencies such as social services and educational psychologists ~attends meetings with colleagues and outside agencies",
    ],
}
SOCmeta["3223"] = {
    "group_title": "Housing officers",
    "group_description": "Housing officers assess and address housing needs of particular localities and individuals and oversee the day-to-day management of rented properties belonging to local authorities or housing associations.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant work experience. Vocational qualifications in Housing are available at levels 2, 3,4 and 5. Professional qualifications are available and may be required for some posts.",
    "tasks": [
        "~oversees the day-to-day running of rented properties including arranging for the signing of leases, rent collection and maintenance work ~interviews prospective tenants and allocates properties to waiting list applicants ~carries out regular inspections of properties to assess and ensure they are in a good state of repair ~ensures that special needs accommodation is suited to the needs of particular groups such as the elderly and disabled, and that statutory requirements for providing accommodation are met ~refers tenants to appropriate sources of benefits and welfare ~deals with payment of rents and arrears, arranges for legal action where necessary ~supports tenants\u2019 groups ~works closely with other agencies such as social services departments and welfare rights groups",
    ],
}
SOCmeta["3224"] = {
    "group_title": "Counsellors",
    "group_description": "Counsellors provide counselling services to clients with a wide variety of problems by means of assisting them to reach their own resolutions to the difficulties they face. Counsellors may specialise in a particular area or client group or address a wide range of issues.",
    "entry_routes_and_quals": "There are no formal qualifications requirements for entry but relevant experience is necessary. Many employers will expect entrants to have achieved or be working towards accreditation with a professional body via certification or a diploma in counselling. Background checks including a DBS check are likely to be required for counsellors working with vulnerable adults and/or families.",
    "tasks": [
        "~meets clients face-to-face, working either one-to-one or with couples or families, or by telephone or internet ~encourages clients to discuss their feelings in relation to their problems, aiming to ensure that an understanding of the issues is achieved ~presents different perspectives to the problem areas identified ~refers to other appropriate sources of help ~keeps accurate and confidential records",
    ],
}
SOCmeta["3229"] = {
    "group_title": "Welfare and housing associate professionals n.e.c.",
    "group_description": "Job holders in this unit group provide pastoral care relating to religious denominations, student support (from 15 years of age), and a variety of welfare-related services including advice on benefits, health, disability and residential care not elsewhere classified in minor group 322: Welfare and housing associate professionals.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or experience. Professional qualifications may be required for some posts. Background checks including a DBS check are likely to be required for those working with vulnerable adults and/or families.",
    "tasks": [
        "~advises on rights and entitlements in relation to benefits, health, discrimination and welfare ~advises individuals and families experiencing problems about available resources to assist them ~assists and liaises with professionals in social work, the probation service and related welfare areas ~organises day, residential and home care services ~helps to put together care plans and follows professional\u2019s care plans ~maintains records and compiles reports on clients ~keeps up to date with legislation ~performs pastoral care duties, preaches sermons and conducts some services in accordance with the relevant faith or denomination",
    ],
}
SOCmeta["323"] = {
    "group_title": "Teaching and childcare associate professionals",
    "group_description": "Jobholders in this unit group assist teachers in the education and care of children from nursery to secondary school age.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3231"] = {
    "group_title": "Higher level teaching assistants",
    "group_description": "Higher level teaching assistants (HLTA\u2019s) assist teachers with their day-to-day classroom work, the provision and planning of and the creation of lesson materials. HLTA\u2019s teach classes on their own and may be trained in relevant learning strategies such as literacy. They may support students with special/additional needs and work in special and additional needs schools.",
    "entry_routes_and_quals": "Entrants must achieve Higher level Teaching Assistant status. Academic qualifications may be required by some employers and significant relevant experience is usually necessary. NVQs at level 4 are available. A DBS check is mandatory.",
    "tasks": [
        "~assists with development of lesson plans and materials ~assists teacher with preparation or clearing up of classroom ~gives lessons to classes and individual students independently of the teacher ~assess, record and report on pupils' progress ~manages and supports other teaching assistants ~listens to children read, reads to them or tells stories ~assists children with washing or dressing for outdoor and similar activities ~makes simple teaching aids and constructs thematic displays of educational material or children\u2019s work ~helps with outings and other out-of-classroom activities",
    ],
}
SOCmeta["3232"] = {
    "group_title": "Early education and childcare practitioners",
    "group_description": "Early education and childcare practitioners lead the learning and development of and care for children from birth up to five years of age in a school, nursery, or childcare environment.",
    "entry_routes_and_quals": "Qualified practitioners need to have achieved an early years degree qualification, such as Early Years Professional, Early Years Teacher, Early Childhood Studies Degree, Early Childhood Graduate Practitioner Competencies. A DBS check is mandatory.",
    "tasks": [
        "~plans children\u2019s day and activities and leads on social, language and numerical development ~coordinates observation and assessment on children\u2019s play, development and learning ~identifies and responds to health and safety issues ~leads on preparing children for transitions to different settings, including school. ~communicates with parents, colleagues and external professionals on children\u2019s development and health and well-being ~supervises and supports other early education and childcare workers ~coordinates nurturing care in bathing, dressing, preparation of feeds, feeding babies, and in changing babies and toddlers clothing whenever necessary ~provides a secure and supportive environment and supervises young children at mealtimes ~promotes and leads physical activities and children\u2019s games, play, creativity, and problem solving",
    ],
}
SOCmeta["324"] = {
    "group_title": "Veterinary nurses",
    "group_description": "Workers in this minor group provide assistance to veterinarians in the treatment and care of sick or injured animals.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3240"] = {
    "group_title": "Veterinary nurses",
    "group_description": "Veterinary nurses assist veterinarians in the treatment and care of sick or injured animals.",
    "entry_routes_and_quals": "Entrants require GCSEs/S grades or an equivalent qualification. Entrants must obtain employment at an approved veterinary practice to gain practical experience and tuition with an employer for a minimum duration of two years. Candidates must also pass professional examinations before qualifying as a veterinary nurse.",
    "tasks": [
        "~assists the veterinary surgeon during surgical and medical treatments of animals ~prepares operating theatre, sterilises equipment and assists in theatre as required ~dispenses and administers medication and applies dressings to animals under direction from the veterinarian ~handles animals during treatment ~collects and analyses blood, urine and other samples ~cares for animals in hospital accommodation and keeps accurate records ~maintains the biosecurity of the veterinary premises ~advises clients on preventative medicine to maintain appropriate animal health and welfare",
    ],
}
SOCmeta["33"] = {
    "group_title": "Protective service occupations",
    "group_description": "Workers in protective service occupations serve in the armed forces, the police force, fire service, prison service and perform other protective service roles.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["331"] = {
    "group_title": "Protective service occupations",
    "group_description": "Workers in this minor group serve in His Majesty\u2019s, foreign and Commonwealth armed forces, investigate crimes and maintain law and order, fight fires and advise on fire prevention, guard inmates and maintain discipline at prisons and detention centres, and perform other miscellaneous protective service roles.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3311"] = {
    "group_title": "Non-commissioned officers and other ranks",
    "group_description": "Those holding jobs in this unit group are full-time members of the armed forces of the UK, the Commonwealth and other foreign countries and perform military duties for which there is no civilian equivalent.",
    "entry_routes_and_quals": "For most positions entry does not depend upon academic qualifications. Entrants generally have to pass a selection interview and physical and medical examinations. Entry to certain trades requires GCSEs/S grades or equivalent qualifications.",
    "tasks": [
        "~receives and responds to commands from senior officers ~monitors, operates, services and repairs military equipment ~takes part in military operations in situations of conflict and provides aid if required in emergency situations such as civil disorder, natural disasters and major accidents ~engages in peacekeeping operations and enforces ceasefire agreements ~stands watch and guards military establishments and other buildings ~trains and exercises using various military equipment and tactics ~undertakes specialist activities such as operating communications equipment, driving military vehicles ~patrols areas of possible military activity ~leads and trains new recruits and lower ranks, looks after their discipline and welfare",
    ],
}
SOCmeta["3312"] = {
    "group_title": "Police officers (sergeant and below)",
    "group_description": "Police officers (sergeant and below) co-ordinate and undertake the investigation of crimes, patrol public areas, arrest offenders and suspects and enforce law and order. Officers of the British Transport Police operate within the specialised police service for the railway network across britain.",
    "entry_routes_and_quals": "There are no academic requirements for entry to the civilian (Home Office) police although eligibility criteria vary across individual police forces. Entrants must sit an entry test and pass a medical examination. All police officers undergo a two year probationary training period. Residency, nationality and age restrictions apply, and background security checks are carried out in respect of entrants. Entrants may join via the Police Constable Degree Apprenticeship (PCDA).",
    "tasks": [
        "~receives instructions from senior officers and patrols an assigned area on foot, horseback, motorcycle, motor car or boat to check security and enforce regulations ~directs and controls traffic or crowds at demonstrations and large public events ~investigates complaints, crimes, accidents, any suspicious activities or other incidents ~interviews suspects, takes statements from witnesses and stops, searches and/or arrests suspects ~attends accidents ~prepares briefs or reports for senior officers ~works on station reception desk and or in communications room ~gives evidence in court cases",
    ],
}
SOCmeta["3313"] = {
    "group_title": "Fire service officers (watch manager and below)",
    "group_description": "Fire service officers (watch manager and below) co-ordinate and participate in firefighting activities, provide emergency services in the event of accidents or bomb alerts, and advise on fire prevention.",
    "entry_routes_and_quals": "There are no formal academic requirements, although applicants to fire control roles must demonstrate basic literacy and numeracy, keyboard and communication skills. Applicants to fire-fighter roles must pass psychological, physical and medical tests. Some Fire and Rescue Services operate direct entry recruitment processes to managerial operational roles. There is a minimum age limit of 18 years for entry to fire-fighter and control operator roles and DBS checks can be required.",
    "tasks": [
        "~inspects premises to identify potential fire hazards and to check that firefighting equipment is available and in working order and that statutory fire safety regulations are met ~arranges fire drills and tests alarm systems and equipment ~travels to fire or other emergency by vehicle and locates water mains if necessary ~operates hose pipes, ladders, chemical, foam, gas or powder fire extinguishing appliances ~rescues people or animals trapped by fire or other emergency situations such as flooding and administers first aid ~removes goods from fire damaged premises, clears excess water, makes safe any structural hazards and takes any other necessary steps to reduce damage to property ~attends and deals with bomb alerts and accidents involving spillage of hazardous substances ~advises on fire safety measures in new buildings ~supervises a watch",
    ],
}
SOCmeta["3314"] = {
    "group_title": "Prison service officers (below principal officer)",
    "group_description": "Prison service officers (below principal officer) direct, co-ordinate and participate in guarding inmates and maintaining discipline in prisons and other detention centres.",
    "entry_routes_and_quals": "There are no formal academic requirements for entry, but candidates must pass a pre-entry test and full medical examination. Basic training is followed by a 12 month probationary period during which further on-the-job training is provided. Background checks are required for entrants, and there are generally nationality restrictions and a lower age limit of 18 years.",
    "tasks": [
        "~escorts prisoners to and from cells and supervises them during meals, recreation and visiting periods ~watches for any infringements of regulations and searches prisoners and cells for weapons, drugs and other contraband items ~guards entrances and perimeter walls ~investigates disturbances or any other unusual occurrences ~escorts prisoners transferred from one institution to another ~runs prisoner rehabilitation and support programmes ~provides care and support to prisoners in custody including prevention of self-harm ~trains and supervises prison staff ~reports on prisoners\u2019 conduct as necessary",
    ],
}
SOCmeta["3319"] = {
    "group_title": "Protective service associate professionals n.e.c.",
    "group_description": "Job holders in this unit group inspect goods to ensure compliance with regulations concerning payment of duty, establish that persons entering and leaving the UK have necessary authorisation for crossing national borders, monitor maritime conditions, undertake search and rescue operations, plan and coordinate services of private detective agencies and security measures for individuals, establishments or organisations, investigates activities such as fraud and other crimes, and perform other security and protective service occupations not elsewhere classified in minor group 331: Protective service occupations.",
    "entry_routes_and_quals": "These posts have varying entry requirements. Some posts require no academic qualifications whereas others require GCSEs/S grades and/or relevant practical experience. Entry to some occupations is followed by periods of assessed probationary training and professional examinations.",
    "tasks": [
        "~examines, weighs and counts goods imported by ship or aircraft, ensures that the declared value of goods is satisfactory, and that duties and taxes have been paid ~examines passports, visas, work permits and other immigration documents, and allows or refuses entry into the UK ~maintains revenue control at breweries, tobacco factories and other premises where dutiable goods are manufactured, processed or stored ~visits racecourses, greyhound stadiums and betting shops to ensure compliance with legal requirements ~broadcasts information on weather and maritime conditions, monitors shipping and provides instruction to navigators ~receives distress messages, alerts other appropriate rescue services and participates in search and rescue operations ~photographs, fingerprints and undertakes other forms of forensic examination at the scene of a crime ~analyses security requirements, advises clients, and develops, monitors and improves security measures ~supervises and assigns duties to security and detection staff ~investigates crimes, including fraud, trading practices and the private affairs of individuals",
    ],
}
SOCmeta["34"] = {
    "group_title": "Culture, media and sports occupations",
    "group_description": "Workers in this sub-major group create and restore artistic works; write, edit and evaluate literary material; perform in acts of entertainment; arrange and perform musical compositions; produce television, film and stage presentations; present television and radio broadcasts; operate camera, sound and lighting equipment; design commercial and industrial products; compete in sporting events for financial reward; and provide training and instruction for sporting and recreational activities.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["341"] = {
    "group_title": "Artistic, literary and media occupations",
    "group_description": "Workers in this minor group create and restore artistic work; write, evaluate and edit literary material; translate written and spoken statements; perform in films, theatre and other acts of entertainment; write, arrange and perform musical compositions; produce, direct, present and participate in television programmes, films and stage presentations; create artistic content for various media; and promote and administer artistic and cultural activities.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3411"] = {
    "group_title": "Artists",
    "group_description": "Artists create artistic works using appropriate techniques, materials and media; design artwork and illustrations; and restore damaged pieces of art.",
    "entry_routes_and_quals": "No specific academic qualifications are required although a variety of vocational qualifications, degrees and postgraduate courses are available. Entry can be based upon portfolio work.",
    "tasks": [
        "~conceives and develops ideas and ways of working for artistic composition ~selects appropriate materials, medium and method ~prepares sketches, scale drawings or colour schemes ~builds up composition into finished work by carving, sculpting, etching, painting, engraving, drawing, etc. ~approaches managers of galleries and exhibitions in order to get finished work displayed ~uses artistic skills to restore damaged artworks ~liaises with writers and publishers to produce book illustrations ~markets and sells finished work directly to customers ~produces works on commission basis for clients",
    ],
}
SOCmeta["3412"] = {
    "group_title": "Authors, writers and translators",
    "group_description": "Authors, writers and translators write, edit and evaluate literary material for publication excluding material for newspapers, magazines and other periodicals but including scripts and narrative for film, TV, radio and computer games and animations; and translate spoken and written statements into different languages.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience. Postgraduate and professional qualifications are available and are required for some occupations.",
    "tasks": [
        "~determines subject matter and researches as necessary by interviewing, attending public events, seeking out records, observing etc. ~generates and develops creative ideas for literary material ~selects material for publication, checks style, grammar and accuracy of content, arranges for any necessary revisions and checks proof copies before printing ~negotiates contracts with freelance agents and with buyer on behalf of writer ~writes instruction manuals and user guides, technical reports, catalogues and indexes, prepares sales literature and writes technical articles for trade journals ~converts documents or spoken statements from original or source language into another language ~provides communication support for the hard of hearing or the visually impaired",
    ],
}
SOCmeta["3413"] = {
    "group_title": "Actors, entertainers and presenters",
    "group_description": "Actors, entertainers and presenters sing, portray roles in dramatic productions, perform comedy routines, gymnastic feats and tricks of illusion, train animals to perform and perform with them, and introduce and present radio and television programmes.",
    "entry_routes_and_quals": "Entry does not depend on academic qualifications although some drama schools require candidates to have GCSEs/S grades or A levels/H grades or a degree. Entry can be based upon an audition. Membership of the appropriate trade union is usually required. Vocational qualifications in performing arts are available.",
    "tasks": [
        "~studies script",
        "play or book and prepares and rehearses interpretation ~assumes character created by a playwright or author and communicates this to an audience ~performs singing, comedy, acrobatic, illusion and conjuring routines ~trains animals to perform entertaining routines and may perform with them ~introduces and presents radio and television programmes, reads news bulletins and makes announcements ~conducts interviews and prepares reports for news broadcasts, current affairs programmes and documentaries ~plays pre-recorded music at nightclubs, discotheques, and private functions",
    ],
}
SOCmeta["3414"] = {
    "group_title": "Dancers and choreographers",
    "group_description": "Dancers and choreographers devise, direct, rehearse and perform classical and contemporary dance routines.",
    "entry_routes_and_quals": "There are no formal academic requirements, although some dance schools may require candidates to have passed relevant dance graded examinations. Entry to courses is often via audition. Medical and physical assessments are required. Performers\u2019 courses typically last three years and lead to a diploma or certificate awarded by the school. Some degree courses are also available.",
    "tasks": [
        "~builds and maintains stamina, physical strength, agility and general health through fitness exercises and healthy eating ~attends rehearsals to develop and practice dance routines for performance ~participates in dance performance ~demonstrates and directs dance moves, monitors and analyses technique and performance, and determines how improvements can be made",
    ],
}
SOCmeta["3415"] = {
    "group_title": "Musicians",
    "group_description": "Musicians write, arrange, orchestrate, conduct and perform musical compositions.",
    "entry_routes_and_quals": "There are no formal academic entry requirements although many possess a degree and/or diploma. Entry to a degree or graduate diploma course requires A levels/H grades. Entrants to the performers\u2019 diploma course generally possess GCSEs/S grades and associated board graded examination passes in their chosen instrument(s) and will be required to audition.",
    "tasks": [
        "~conceives and writes original music ~tunes instrument and studies and rehearses score ~plays instrument as a soloist or as a member of a group or orchestra ~scores music for different combinations of voices and instruments to produce desired effect ~auditions and selects performers and rehearses and conducts them in the performance of the composition",
    ],
}
SOCmeta["3416"] = {
    "group_title": "Arts officers, producers and directors",
    "group_description": "Arts officers, producers and directors assume creative, financial and organisational responsibilities in the production and direction of television and radio programmes, films, stage presentations, content for other media, and the promotion and exhibition of other creative activities.",
    "entry_routes_and_quals": "Entry can be via academic qualifications, BTEC/SQA awards, diplomas or degrees in sector-relevant subjects. Apprenticeships are available at NVQ levels 2 and 3 in some areas.",
    "tasks": [
        "~chooses writers, scripts, technical staff and performers, and assumes overall responsibility for completion of project on time and within budget ~directs actors, designers, camera team, sound crew and other production and technical staff to achieve desired effects ~breaks script into scenes and formulates a shooting schedule that will be most economical in terms of time, location and sets ~prepares rehearsal and production schedule for main events, design of sets and costumes, technical rehearsals and dress rehearsals ~ensures necessary equipment, props, performers and technical staff are on set when required ~manages health and safety issues ~selects, contracts, markets and arranges for the presentation and/or distribution of performance, visual and heritage arts",
    ],
}
SOCmeta["3417"] = {
    "group_title": "Photographers, audio-visual and broadcasting equipment operators",
    "group_description": "Photographers, audio-visual and broadcasting equipment operators operate and assist with still, cine and television cameras, operate other equipment to record, manipulate and project sound and vision for entertainment, cultural, commercial and industrial purposes and operate drones to provide aerial video and photographs.",
    "entry_routes_and_quals": "There are no set academic requirements although entrants usually possess GCSEs/S grades, A levels/H grades and are able to demonstrate proof of pre- entry work experience. A variety of diplomas, degrees and postgraduate qualifications are available. Vocational qualifications in Photography are available at levels 1,2 and 3.",
    "tasks": [
        "~selects subject and conceives composition of picture or discusses composition with colleagues ~arranges subject, lighting, camera equipment and any microphones ~inserts lenses and adjusts aperture and speed settings as necessary ~operates scanning equipment to transfer image to computer and manipulates image to achieve the desired effect ~photographs subject or follows action by moving camera ~takes, records and manipulates digital images and digital video footage ~controls transmission, broadcasting and satellite systems for television and radio programmes, identifies and solves related technical problems ~checks operation and positioning of projectors, vision and sound recording equipment, and mixing and dubbing equipment ~operates equipment to record, edit and play back films and television programmes ~manages health and safety issues ~operates sound mixing and dubbing equipment to obtain desired mix, level and balance of sound ~maintains, repairs, programs and operates unmanned aircraft to provide aerial photographs and video",
    ],
}
SOCmeta["342"] = {
    "group_title": "Design occupations",
    "group_description": "Workers in this minor group design industrial and commercial products, clothing and fashion accessories and interior spaces.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3421"] = {
    "group_title": "Interior designers",
    "group_description": "Interior designers plan, direct and undertake the creation of designs for interior spaces, procure materials and oversee implementation of the plans.",
    "entry_routes_and_quals": "Employers often require a relevant degree, although entry may be possible with a foundation course or HNC/HND.",
    "tasks": [
        "~liaises with client to determine the purpose, cost, and scope of the project, which may include the entire building or one room such as the kitchen or bathroom ~prepares designs to meet the client's needs and draws up sketches for consideration by the client ~advises on colours and the materials to be used, ~establishes estimated costs, specifies materials and provides detailed drawing of the agreed design ~sources fixtures, furniture and other necessary materials ~hires staff and oversees project progress ~ensures building and safety regulations are adhered to",
    ],
}
SOCmeta["3422"] = {
    "group_title": "Clothing, fashion and accessories designers",
    "group_description": "Clothing, fashion and accessories designers plan, direct and undertake the creation of designs for new clothing and related fashion accessories.",
    "entry_routes_and_quals": "Entrants have usually completed a foundation course, BTEC/SQA award, degree and/or postgraduate qualification. Vocational qualifications in Fashion Design and Design are available at level 2 and 3, as are apprenticeships at levels 2 and 3.",
    "tasks": [
        "~liaises with client to determine the purpose, cost, technical specification and potential uses/users of clothing or related fashion accessory ~undertakes research to determine market trends, production requirements, availability of resources and formulates design concepts ~prepares sketches, designs, patterns or prototypes for textiles, clothing, footwear, jewellery, fashion accessories ~submits design to management, sales department or client for approval, communicates design rationale and makes any necessary alterations ~specifies materials, production method and finish for aesthetic or functional effect ~oversees production of sample and/or finished product or produces one-off products for fashion shows ~observes and manages intellectual property issues",
    ],
}
SOCmeta["3429"] = {
    "group_title": "Design occupations n.e.c.",
    "group_description": "Job holders in this unit group plan, direct and undertake the creation of designs for new industrial and commercial products, stage sets, and other areas not elsewhere classified in minor group 342: Design occupations.",
    "entry_routes_and_quals": "Entrants have usually completed a foundation course, BTEC/SQA award, degree and/or postgraduate qualification. A variety of vocational qualifications are available.",
    "tasks": [
        "~liaises with client to determine the purpose, cost, technical specification and potential uses/users of product ~prepares sketches, designs, patterns, prototypes, mock-ups and storyboards for consideration by theatre/film director, management, sales department or a client ~undertakes research to determine market trends, production requirements, availability of resources and formulates design concepts ~specifies materials, production method and finish for aesthetic or functional effect, and oversees production of sample and/or finished product ~observes and manages intellectual property issues ~create many types of special effects make-up, which can include prosthetics ~define, design and implement a creative visual merchandising strategy",
    ],
}
SOCmeta["343"] = {
    "group_title": "Sports and fitness occupations",
    "group_description": "Workers in this minor group prepare for and compete in sporting events for financial gain, train amateur and professional sportsmen and women to enhance performance, promote participation and standards in sport, organise and officiate at sporting events, and provide instruction, training and supervision for various forms of exercise and other recreational activities.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3431"] = {
    "group_title": "Sports players",
    "group_description": "Professional sportsmen and women train and compete, either individually or as part of a team, in their chosen sport for financial gain.",
    "entry_routes_and_quals": "No academic qualifications are required. Entry is based upon talent that can be further developed through coaching and training.",
    "tasks": [
        "~participates in exhibitions, pre-qualifying events, tournaments and competitions ~attends training sessions to develop skills and practice individual or team moves and tactics ~builds stamina, physical strength and agility through running, fitness exercises and weight training ~maintains clothing and other specialised sporting equipment ~discusses performance problems with coaches, physiotherapists, dieticians and doctors",
    ],
}
SOCmeta["3432"] = {
    "group_title": "Sports coaches, instructors and officials",
    "group_description": "Sports coaches, instructors and officials work with amateur and professional sportsmen and women to enhance performance, encourage greater participation in sport, supervise recreational activities such as canoeing and mountaineering, and organise and officiate at sporting events according to established rules.",
    "entry_routes_and_quals": "There are no formal academic requirements although individuals must have experience in their sport and the relevant coaching and refereeing qualifications. Applicants to coaching courses must normally be over 18 years old and hold a first-aid certificate. Some courses encompass coaching awards within broader programmes of study. Vocational qualifications in coaching are available in the context of certain sports. Background checks including a DBS check are required for those working with children.",
    "tasks": [
        "~coaches teams or individuals by demonstrating techniques and directing training and exercise sessions ~controls team selection and discipline and recruits ancillary staff such as coaches or physiotherapists ~monitors and analyses technique and performance, and determines how future improvements can be made ~deals with administrative aspects such as arranging matches, contests or appearances for athlete or team, and organising required transport and accommodation ~provides information and develops facilities to encourage greater participation in sport, and to enhance the standards of participants ~understands health and safety aspects of various activities and ensures any statutory requirements are met ~inspects and maintains specialised clothing and equipment ~manages the playing areas and competitors, starts race, competition or match and controls its progress according to established rules",
    ],
}
SOCmeta["3433"] = {
    "group_title": "Fitness and wellbeing instructors",
    "group_description": "Fitness and wellbeing instructors deliver training in a range of fitness activities, including weight training, yoga, Pilates, personal training and other forms of exercise at private health and fitness centres, local authority run sports and leisure centres, other public and community establishments, and in private homes.",
    "entry_routes_and_quals": "There are no formal academic requirements. Entrants must, however, possess coaching qualifications recognised by the appropriate governing body. Applicants to coaching courses must normally be over 18 years old and hold a first-aid certificate. Background checks including a DBS check are required for those working with children.",
    "tasks": [
        "~assesses the fitness levels of clients ~devises programmes of training appropriate to the needs of clients with varying levels of strength, fitness and ability ~demonstrates and leads fitness activities and supervises exercise classes ~ensures that clients do not injure themselves through over exertion or using incorrect training techniques ~plans and monitors personal fitness schedules ~understands the health and safety aspects of different forms of exercise and ensures that any statutory requirements are met",
    ],
}
SOCmeta["35"] = {
    "group_title": "Business and public service associate professionals",
    "group_description": "Business and public service associate professionals command and control the movement of air and sea traffic; organise the administrative work of legal practices; deal in commodities, stocks and shares, underwrite insurance and perform specialist financial tasks; estimate the value or cost of goods, services and projects; assist in planning and organising projects; analyse and interpret data; purchase goods and materials; provide technical sales advice to clients; order stock and set prices for stores; arrange for the trading and leasing of property on behalf of clients; organise conferences and related events; undertake recruitment, training and industrial relations activities; perform administrative functions in government; and undertake statutory inspections of health and safety.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["351"] = {
    "group_title": "Transport associate professionals",
    "group_description": "Workers in this minor group command and navigate aircraft and vessels, perform technical functions to operate and maintain such craft, and plan and regulate the ground and air movements of aircraft.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3511"] = {
    "group_title": "Aircraft pilots and air traffic controllers",
    "group_description": "Aircraft pilots and air traffic controllers navigate and pilot aircraft, prepare flight plans, authorise flight departures and arrivals, maintain radio, radar and/or visual contact with aircraft to ensure the safe movement of air traffic, check, regulate, adjust and test engines and other equipment prior to take-off and give flying lessons.",
    "entry_routes_and_quals": "Entrants with GCSEs/S grades and A levels/H grades, a BTEC/ SQA award or equivalent qualification can apply for an airline sponsorship. Private residential training as a pilot is available to candidates with GCSEs/S grades or appropriate BTEC/SQA or other certificates/diplomas or to holders of Private Pilots Licences who have 700 hours flying experience. Training lasts up to 15 months and consists of courses of study and flying instruction. Airlines may have additional age and height requirements. Air traffic controllers training lasts 74 weeks including study and practical experience. Entrants must be 18 to hold a Student Licence and 21 for a full air traffic controller licence awarded by the Civil Aviation Authority. Normal colour vision is required for pilots and air traffic controllers and candidates also undergo a medical examination.",
    "tasks": [
        "~studies flight plan and makes any necessary adjustments ~directs or undertakes checks on engines, instruments, control panels, cargo distribution, fuel supplies, aircraft's stability, response to controls and overall performance ~directs or undertakes the operation of controls to fly airplanes and helicopters, complying with air traffic control and aircraft operating procedures ~monitors fuel consumption, air pressure, engine performance and other indicators during flight and advises pilot of any factors that affect the navigation or performance of the aircraft ~maintains radio contact and discusses weather conditions with air traffic controllers ~directs the movement of aircraft and maintains radio and/or radar or visual contact en-route to its destination, in and out of controlled airspace or into holding areas ready for landing ~gives landing Instructions to pilot and monitors descent ~plans flight route, calculate fuel consumption and optimum flying height and obtains information on weather and other conditions, such as cargo distribution ~handles emergencies, unscheduled traffic and other unanticipated incidents ~accompanies pupil on training flights and demonstrates flying techniques",
    ],
}
SOCmeta["3512"] = {
    "group_title": "Ship and hovercraft officers",
    "group_description": "Ship and hovercraft officers command and navigate ships and other craft, co-ordinate the activities of officers and deck and engine room ratings, operate and maintain communications equipment on board ship and undertake minor repairs to engines, boilers and other mechanical and electrical equipment.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades and A levels/H grades. Good colour vision without spectacles or contact lenses is required for some posts and candidates must undergo a medical examination. Training lasts three to four years and combines taught courses and assessed training at sea.",
    "tasks": [
        "~allocates duties to ship\u2019s officers and co-ordinates and directs the activities of deck and engine room ratings ~directs or undertakes the operation of controls to inflate air cushions, run engines and propel and steer ships, hovercraft and other vessels ~locates the position of vessel using electronic and other navigational aids such as charts and compasses and advises on navigation where appropriate ~monitors the operation of engines, generators and other mechanical and electrical equipment and undertakes any necessary minor repairs ~maintains radio contact with other vessels and coast stations ~prepares watch keeping rota and maintains a look-out for other vessels or obstacles ~maintains log of vessel\u2019s progress, weather conditions, conduct of crew, etc",
    ],
}
SOCmeta["352"] = {
    "group_title": "Legal associate professionals",
    "group_description": "Legal associate professionals organise the administrative work of legal practices and perform specialised legal duties.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3520"] = {
    "group_title": "Legal associate professionals",
    "group_description": "Legal associate professionals provide administrative support for legal professionals and investigate and make recommendations on legal matters that do not fall within the province of a normal court of law.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades and A levels/H grades in appropriate subject areas. Off and on-the-job training is available. Membership of professional institutions will be required for some posts. Candidates must pass professional examinations and complete up to five years of practical experience.",
    "tasks": [
        "~runs chambers on behalf of principals, develops the practice, manages the flow of work, decides which cases to accept, arranges appropriate fees and prepares financial records ~ensures judges have the necessary legal other documents, manages their diary and carries out other administrative duties collates information, drafts briefs and other documents ~attends court to assist barristers and solicitors in the presentation of a case ~ensures their organisation complies with relevant regulations and their organisational policies ~assists in all aspects of probate and common law practice ~draws up schedules of legal costs and advises on the allocation of legal costs and the level of legal fees",
    ],
}
SOCmeta["353"] = {
    "group_title": "Finance associate professionals",
    "group_description": "Finance associate professionals underwrite insurance policies and assess liability regarding claims, deal in commodities and financial assets, and assist accounting and financial professionals in managing an organisation\u2019s financial affairs and its accounts.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3531"] = {
    "group_title": "Brokers",
    "group_description": "Brokers deal in commodities, stocks, shares and foreign exchange on behalf of clients or on own account, broker insurance and reinsurance, and buy and sell shipping and freight space.",
    "entry_routes_and_quals": "There are no formal academic requirements although many employers require entrants to possess a degree or equivalent qualification. Training is typically undertaken in-house, although entrants may attend courses run by professional institutions. Registration with a regulatory authority may be required in some positions.",
    "tasks": [
        "~advises client on the suitability of insurance schemes and places insurance on behalf of client ~discusses buying and or selling requirements of client and gives advice accordingly ~analyses information concerning market trends for commodities, financial assets and foreign exchange and advises client and employer on the suitability of investments ~records and transmits buy and sell orders for stocks, shares and bonds and calculates transaction costs ~provides independent advice on the suitability of insurance schemes and places insurance on behalf of client ~arranges the production of auction catalogues, fixes reserve prices, attends auction and bids on behalf of client, or negotiates purchase/sale by private treaty of goods not sold at auction ~obtains cargo space, fixes freight charges and signs and issues bills of loading ~collects freight charges from client and undertakes all necessary formalities concerning customs and the loading/unloading of cargo",
    ],
}
SOCmeta["3532"] = {
    "group_title": "Insurance underwriters",
    "group_description": "Insurance underwriters identify and measure the risks associated with an activity, determine whether this risk is insurable and issue insurance policies which provide financial compensation in the event of loss.",
    "entry_routes_and_quals": "There are no formal academic requirements, although many employers expect entrants to study for and attain the associateship examinations of the Chartered Insurance Institute. Entrants to professional examinations usually require GCSEs/S grades and A levels/H grades, or a BTEC/SQA award.",
    "tasks": [
        "~receives and assesses proposals and propositions for insurance from brokers and clients ~identifies and evaluates the risks associated with a proposal ~liaises with insurance surveyors, actuaries and risk managers where the risks associated with a proposal are not clear ~calculates premiums, provides quotations and, if acceptable to the client, issues policies ~ensures that the insurance policy clearly defines the liabilities accepted and any exceptions or exclusions ~negotiates terms of reinsurance contracts",
    ],
}
SOCmeta["3533"] = {
    "group_title": "Financial and accounting technicians",
    "group_description": "Financial and accounting technicians work alongside accountants and other financial professionals in managing the financial affairs of organisations.",
    "entry_routes_and_quals": "There are no formal academic requirements. Professional qualifications are available from the Association of Chartered Certified Accountants and the Association of Accounting Technicians. Vocational qualifications in Accounting are available at levels 2, 3 and 4. Exemptions to professional examinations may be granted to those with certain academic qualifications.",
    "tasks": [
        "~maintains profit and loss accounts, budgets, cash flow forecasts and other accounting records ~produces, collates and reports financial information for managers ~liaises with clients to ensure that payments are made on time and credit limits are not exceeded ~ensures invoices and payments are correct and sent out on time ~monitors accounting systems to determine accounts are being maintained effectively and provides information on accounting practices to auditors",
    ],
}
SOCmeta["3534"] = {
    "group_title": "Financial accounts managers",
    "group_description": "Financial accounts managers manage client accounts or departments within financial institutions (such as banks and insurance companies) or manage a variety of financial accounts within other organisations.",
    "entry_routes_and_quals": "There are no formal academic requirements although professional qualifications in accountancy may be required by some employers. Vocational qualifications in Accounting are available at levels 2, 3 and 4, and apprenticeships are available in some areas.",
    "tasks": [
        "~develops and manages business accounts to increase sales of financial products ~takes responsibility for the efficient and effective operation of several business accounts ~manages teams handling insurance claims ~checks customers\u2019 credit rating with banks and credit reference agencies, and decides whether to offer credit ~establishes terms of credit and ensures timely payment by customer, renegotiates payment terms and initiates legal action to recover debts if necessary ~carries out and/or supervises general accounting and administrative work",
    ],
}
SOCmeta["354"] = {
    "group_title": "Business associate professionals",
    "group_description": "Business associate professionals calculate the probable costs of projects, assess the value of properties, advise clients on financial and accounting matters, import and export goods, organise, plan, monitor and direct projects, gather, analyse and communicate their findings on different types of data, and advise on the effectiveness of an organisation\u2019s procedures, systems and methods.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3541"] = {
    "group_title": "Estimators, valuers and assessors",
    "group_description": "Estimators, valuers and assessors plan and undertake the calculation of probable costs of civil, mechanical, electrical, electronic and other projects, estimate the value of property and chattels, and investigate insurance claims to assess their validity and to assign liability.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications. Entrants typically possess GCSEs/S grades, A levels/H grades, GNVQs/GSVQs or BTEC/SQA awards. Professional qualifications are available and may be required by some employers.",
    "tasks": [
        "~examines plans, drawings, specifications, parts lists, etc. and specifies the materials and components required ~assesses condition, location, desirability and amenities of property to be valued ~assesses costs of materials, labour and other factors such as required profit margins, transport costs, tariffs and fare structures, possible hazards, etc. ~prepares comprehensive estimates of time and costs and presents these in report or tender form ~examines insurance documents to assess extent of liability and gathers information about incident from police, medical records, ship\u2019s log, etc. and investigates potential fraudulent claims",
    ],
}
SOCmeta["3542"] = {
    "group_title": "Importers and exporters",
    "group_description": "Importers and exporters buy commodities from overseas for the home market and sell home-produced commodities to overseas markets.",
    "entry_routes_and_quals": "Entry does not depend on academic qualifications although some employers require candidates to have a degree or equivalent qualification. Some posts require candidates to have knowledge of a foreign language. Professional qualifications are available. Entrance to professional examinations requires GCSEs/S grades and A levels/H grades or equivalent qualifications.",
    "tasks": [
        "~investigates and evaluates home and overseas demand for commodities ~obtains orders from buyers and arranges payment by bill of exchange, letter of credit or other means ~arranges for shipment of commodities overseas and ensures that insurance and export licences are in order ~carries out customs clearance procedures for imports, arranges their storage and delivery and sells them personally or through a commodity broker ~advises home and overseas producers on the likely future demand for their goods",
    ],
}
SOCmeta["3543"] = {
    "group_title": "Project support officers",
    "group_description": "Project support officers assist in the organisation, planning, monitoring and direction of a project and ensure it is adequately resourced and on schedule.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although entrants typically possess GCSEs/S grades, A levels/H grades, a BTEC/SQA award or equivalent qualifications. On-the-job training is usually provided, and professional qualifications are available.",
    "tasks": [
        "~analyses project components, organises them into a logical sequence and establishes the minimum time required for the project ~creates and maintains a project timetable, helps ensure the project proceeds on schedule and manages relevant administrative elements of the project ~advises on project procedures and assists the project team in decision making ~liaises with and ensures effective communication between the project team, other departments, the project manager, the client and/or senior management ~monitors the progress of the project and provides updates to project team, clients and other stakeholders",
    ],
}
SOCmeta["3544"] = {
    "group_title": "Data analysts",
    "group_description": "Data analysts gather and organise a variety of data and analyse it to understand what it means for their organisation or society.",
    "entry_routes_and_quals": "Entrants usually possess a relevant degree, although vocational qualifications and apprenticeships are also available.",
    "tasks": [
        "~gathers, cleans and collates datasets and develops data management processes and policies ~analyses data to identify trends and patterns in a variety of fields, such as opinion polling, predicting demand for goods and services, or the testing of new medications ~creates visual representations of data, such as data dashboards and graphs ~presents findings for technical or non-technical audiences to inform the decisions of companies, government or other organisations",
    ],
}
SOCmeta["3549"] = {
    "group_title": "Business associate professionals n.e.c.",
    "group_description": "Job holders in this unit group advise on the effectiveness of an organisation\u2019s procedures, systems and methods and perform other business and related functions not elsewhere classified in minor group 354: Business associate professionals.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although entrants typically possess GCSEs/S grades, A levels/H grades, a BTEC/SQA award or equivalent qualifications. Professional qualifications are available and may be required by some employers.",
    "tasks": [
        "~studies department or problem area and assesses its interrelationships with other activities ~studies work methods and procedures by measuring work involved and computing standard times for specified activities, and produces report detailing suggestions for increasing efficiency and lowering costs ~purchases services, receives payment from clients, processes contracts and deals with contractual arrangements ~canvasses political opinion, writes and distributes leaflets, writes and distributes press releases and other such material to promote the image and policies of a political party or election candidate, arranges fund raising activities, and organises and participates in election campaigns",
    ],
}
SOCmeta["355"] = {
    "group_title": "Sales, marketing and related associate professionals",
    "group_description": "Sales, marketing and related associate professionals purchase raw materials, equipment and merchandise, provide technical sales advice to customers, undertake market research, support the implementation of the organisation\u2019s marketing and sales policies, decide on pricing and promotions and arrange for the trading and leasing of property on behalf of clients.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3551"] = {
    "group_title": "Buyers and procurement officers",
    "group_description": "Buyers and procurement officers organise and undertake the buying of raw materials, equipment and merchandise from manufacturers, importers, wholesalers and other sources for distribution, resale or for own internal use.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers expect A levels/H grades, BTEC/SQA awards or degrees. Employers may ask for specific experience for a particular role. Professional qualifications and vocational qualifications in Procurement at levels 3, 4 and 5 are available.",
    "tasks": [
        "~attends trade fairs, shows and demonstrations to research new product lines and suppliers, checks catalogues ~keeps up with market trends and chooses products/services ~assesses budgetary limitations and customer requirements and decides on quantity, type, range and quality of goods or services to be bought ~assesses bids from suppliers, finds suppliers and negotiates prices ~helps negotiate contract with supplier and specifies details of goods or services required ~looks at ways to improve supply networks, presents new ideas to senior management team ~ensures that delivered items comply with order, monitors quality of incoming goods and returns unsatisfactory or faulty items, monitors performance and makes sure targets are met ~supervises clerical, administrative and warehouse distribution staff, deals with recruitment and training ~works closely with merchandisers who allocate stock and develop sales forecasts ~maintains records and prepares reports as necessary",
    ],
}
SOCmeta["3552"] = {
    "group_title": "Business sales executives",
    "group_description": "Business sales executives provide advice to existing and potential customers, and receive orders for specialist machinery, equipment, materials and other products or services that require technical knowledge.",
    "entry_routes_and_quals": "There are no formal academic requirements, although entrants usually possess academic qualifications and/or relevant experience in a particular profession or speciality. Training is usually on-the-job. Professional and vocational qualifications at levels 2 and 3 are available.",
    "tasks": [
        "~discusses customer requirements and advises them on the capabilities and limitations of the goods or services being sold ~quotes prices, credit details, delivery dates and payment arrangements and arranges for delivery and installation of goods if appropriate ~makes follow up visits to ensure customer satisfaction and to obtain further orders ~stays abreast of advances in product/field and suggests possible improvements to product or service ~maintains records and accounts of sales made and handles customer complaints",
    ],
}
SOCmeta["3553"] = {
    "group_title": "Merchandisers",
    "group_description": "Merchandisers ensure that stores are supplied with goods, liaise with suppliers, decide on pricing and promotions and advise retailers on the optimum display of merchandise.",
    "entry_routes_and_quals": "Most entrants possess a degree or equivalent qualification, although there are no formal academic requirements and entry is also possible with a BTEC/SQA award, A levels/H grades, or HNC/HND.",
    "tasks": [
        "~monitors stock levels and manages the movement of goods ~predicts future demand and negotiates the supply and price of goods to ensure stores are stocked ~analyses customer requirements, the needs of individual stores and the organisation, and works with suppliers to develop a product range ~supplies information about products to the retailer and sales staff ~consults with advertising and sales staff and advises retailers on the optimal display of a product and of any promotions ~provides feedback about sales to senior managers",
    ],
}
SOCmeta["3554"] = {
    "group_title": "Advertising and marketing associate professionals",
    "group_description": "Advertising and marketing associate professionals assist in the development and implementation of projects which aim to elicit the preferences and requirements of consumers, businesses and other specified target groups so that suppliers may meet these needs.",
    "entry_routes_and_quals": "There are no formal academic requirements, although many entrants possess a BTEC/SQA award, A levels/H grades, a degree or equivalent qualification. Training is typically in-house, supplemented by short courses or professional qualifications provided by the Market Research Society.",
    "tasks": [
        "~discusses business methods, products or services and targets customer group with employer or client to identify marketing requirements ~collates and interprets findings of market research and presents results to clients ~through market research, discusses possible changes that need to be made in terms of design, price, packaging, promotion etc ~develops digital marketing strategies, such as the use of social media, to promote products, brands or services and presents options to the client ~briefs advertising team on client requirements, monitors the progress of advertising campaigns and liaises with client on potential modifications",
    ],
}
SOCmeta["3555"] = {
    "group_title": "Estate agents and auctioneers",
    "group_description": "Estate agents and auctioneers arrange for the valuation, sale, purchase, rental and leasing of property on behalf of clients, as well as the auction of livestock and antiques.",
    "entry_routes_and_quals": "There are no formal academic entry requirements although entrants to professional training via the National Federation of Property Professionals (NFOPP) will normally possess GCSEs/S grades, an NVQ/SVQ and/or relevant experience. Off and on-the-job training is possible, and apprenticeships are available in some areas.",
    "tasks": [
        "~discusses client\u2019s requirements and may advise client on the purchase of property and land for investment and other purposes ~conducts or arranges for structural surveys of properties and undertakes any necessary valuations of property or agricultural land ~advises vendors and purchasers on market prices of property, accompanies clients to view property ~markets the property on behalf of the vendor, prepares written information and press advertisements ~negotiates land or property purchases, sales, leases or tenancy agreements and arranges legal formalities with solicitors, building societies and other parties ~makes inventories of property for sale, advises vendor of suitable reserve price, issues catalogues, conducts auction, notes bids and records sale",
    ],
}
SOCmeta["3556"] = {
    "group_title": "Sales accounts and business development managers",
    "group_description": "Sales accounts and business development managers plan, organise and undertake market research to meet the requirements of an organisation\u2019s marketing and sales policies.",
    "entry_routes_and_quals": "Entrants to the professional qualifications of the Chartered Institute of Marketing require GCSEs/S grades, A levels/H grades, a BTEC/SQA award, a degree or equivalent qualification and/or relevant experience. Qualifications in sales and from other relevant professional bodies are available.",
    "tasks": [
        "~liaises with other senior staff to determine the range of goods or services to be sold, contributes to the development of sales strategies and setting of sales targets ~discusses employer\u2019s or client\u2019s requirements, carries out surveys and analyses customers\u2019 reactions to product, packaging, price, etc. ~compiles and analyses sales figures, prepares proposals for marketing campaigns and promotional activities and undertakes market research ~handles customer accounts ~recruits and trains junior sales staff ~produces reports and recommendations concerning marketing and sales strategies for senior management ~keeps up to date with products and competitors",
    ],
}
SOCmeta["3557"] = {
    "group_title": "Events managers and organisers",
    "group_description": "Events managers and organisers manage, organise and coordinate business conferences, exhibitions, concerts and similar events.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although entrants typically possess GCSEs/S grades, A levels/H grades, a BTEC/SQA award or equivalent qualifications. Professional qualifications are available and may be required by some employers. Off and-on-the-job training is available.",
    "tasks": [
        "~discusses conference and exhibition requirements with clients and advises on facilities ~develops proposal for the event, and presents proposal to client ~allocates exhibition space to exhibitors ~plans work schedules, assigns tasks, and co-ordinates the activities of designers, crafts persons, technical staff, caterers and other events staff ~liaises closely with venue staff to ensure smooth running of the event ~ensures that Health and Safety and other statutory regulations are met",
    ],
}
SOCmeta["356"] = {
    "group_title": "Public services associate professionals",
    "group_description": "Public services associate professionals supervise, manage and undertake general administrative functions in national and local government.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3560"] = {
    "group_title": "Public services associate professionals",
    "group_description": "Public services associate professionals supervise, manage and undertake general administrative work in national and local government departments, organise the activities of local offices of national government departments, and promote the image and understanding of an organisation and its products and services to consumers and other specified audiences.",
    "entry_routes_and_quals": "Although there are no formal academic entry requirements, entrants typically possess A levels/H grades or an equivalent qualification, and many entrants possess a degree. Entry may be possible by promotion from clerical grades for those with suitable experience. Training is typically provided on-the-job, supplemented by specialised courses. Professional qualifications are available in some areas.",
    "tasks": [
        "~manages the activities of government office staff, assigns tasks and responsibilities and makes changes in procedures to deal with variations in workload ~assists senior government officers with policy work, external liaison or general administrative work ~supervises a variety of administrative functions in government departments such as recruitment and training, the negotiation and arrangement of contracts, building and capital management, monitoring and authorising department expenditure etc. ~organises resources for the acceptance and recording of vacancy details, the selection of suitable applicants and other Job Centre activities ~authorises the payment of social security benefits, assesses the financial circumstances of claimants and investigates any state insurance contribution problems ~undertakes supervisory duties specific to the operation of Revenue and Customs offices, Job Centres, Benefits Agency offices and other local offices of national government ~advises the public or companies on general tax problems and arranges for the issue, receipt and examination of tax forms, assessment of PAYE codes and the computation of tax arrears and rebates ~discusses business strategy, products, services and target client base with management to identify public relations requirements ~writes, edits and arranges for the distribution of press releases and other public relations material, addresses target groups through meetings, presentations, the media and other events to enhance the public image of the organisation, and monitors and evaluates its effectiveness",
    ],
}
SOCmeta["357"] = {
    "group_title": "HR, training and other vocational associate guidance professionals",
    "group_description": "Job holders in this unit group advise upon and undertake recruitment, staff appraisal and industrial relations activities, give advice regarding careers, training and related opportunities, and provide information technology and other vocational and industrial training.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3571"] = {
    "group_title": "Human resources and industrial relations officers",
    "group_description": "Human resources and industrial relations officers conduct research, analyse data and advise on recruitment, training, staff appraisal and industrial relations policies and assist specialist managers with negotiations on behalf of a commercial enterprise, trade union or other organisation.",
    "entry_routes_and_quals": "There are no formal academic requirements although most entrants possess a degree or equivalent qualification and/or relevant experience. Many employers expect staff to gain membership of the Chartered Institute of Personnel Development through study for professional qualifications. Vocational qualifications in this area are available at levels 2 to 7.",
    "tasks": [
        "~undertakes research and analyses data on pay differentials, productivity and efficiency bonuses and other payments ~develops and recommends personnel and industrial relations policies, assists with their implementation and drafts staff handbooks ~assists with negotiations between management and employees or trades unions concerning pay and conditions of employment ~interviews candidates for jobs ~advises on training and recruitment, negotiating procedures, salary agreements and other personnel and industrial relations issues ~deals with grievance and disciplinary procedures, and with staff welfare and counselling provision",
    ],
}
SOCmeta["3572"] = {
    "group_title": "Careers advisers and vocational guidance specialists",
    "group_description": "Careers advisers and vocational guidance specialists give advice on careers or occupations, training courses and related matters, direct school leavers and other job seekers into employment and assess their progress.",
    "entry_routes_and_quals": "Entrants often possess a degree, an approved diploma or equivalent qualification. Professional Qualifications are available at Leve 4 and 6. NVQs/SVQs in Advice and Guidance at levels 3 and 4 are also available. Those working with young people or vulnerable adults will require a DBS check.",
    "tasks": [
        "~uses an interview, questionnaire and/or psychological or other test to determine the aptitude, preferences and temperament of the client ~advises on appropriate courses of study or avenues into employment ~visits educational and other establishments to give talks and distribute information regarding careers ~liaises with employers to determine employment opportunities and advises schools, colleges or individuals accordingly ~organises careers forums and exhibitions and establishes and maintains contact with local employers, colleges and training providers ~monitors progress and welfare of young people in employment and advises them on any difficulties",
    ],
}
SOCmeta["3573"] = {
    "group_title": "Information technology trainers",
    "group_description": "Information technology trainers provide instruction in the use of computers for professional and personal purposes and advise on, plan and organise IT training within industrial, commercial and other establishments.",
    "entry_routes_and_quals": "Entrants will usually require a relevant degree or HND/HNC and a qualification in delivering teaching or training. Professional qualifications are available from the Chartered Institute of Personnel and Development. Qualifications in Education and Training are available at levels 3, 4 and 5.",
    "tasks": [
        "~assesses IT training requirements of an organisation or individual and identifies the skills needed for certain roles or tasks ~develops training programme and prepares IT equipment, lectures, demonstrations and study aids ~supervises trainee development, assists trainees with difficulties and prepares regular progress reports on each trainee for management ~arranges work experience and instructional visits for trainees ~plans curriculum and rota of staff duties and updates or amends them in light of developments ~advises on training programmes and discusses progress or problems with staff and trainees",
    ],
}
SOCmeta["3574"] = {
    "group_title": "Other vocational and industrial trainers",
    "group_description": "Other vocational and industrial trainers provide instruction in manual, manipulative and other vocational skills and advise on, plan and organise vocational instruction within industrial, commercial and other establishments.",
    "entry_routes_and_quals": "No formal educational qualifications are required for entry, although most entrants have qualified in some other area of work and possess a qualification in delivering teaching or training. Professional qualifications are available from the Chartered Institute of Personnel and Development. Qualifications in Education and Training are available at levels 3, 4 and 5.",
    "tasks": [
        "~assesses training requirements and prepares lectures, demonstrations and study aids ~supervises trainee development, assists trainees with difficulties and prepares regular progress reports on each trainee for management ~arranges work experience and instructional visits for trainees ~plans curriculum and rota of staff duties and updates or amends them in light of developments ~advises on training programmes and discusses progress or problems with staff and trainees ~devises general and specialised training courses in response to particular needs",
    ],
}
SOCmeta["358"] = {
    "group_title": "Regulatory associate professionals",
    "group_description": "Job holders in this unit group undertake inspections and investigations to ensure statutory compliance, implement health and safety measures within establishments and organisations, and undertake inspections to ensure compliance with environmental health regulations.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["3581"] = {
    "group_title": "Inspectors of standards and regulations",
    "group_description": "Inspectors of standards and regulations undertake investigations and inspections to verify and ensure compliance with acts, regulations and other requirements in respect of: buildings, weights, measures and trade descriptions; the installation and safety of electrical, gas and water supplies and equipment; marine pollution, ships\u2019 structures, equipment and accommodation; the treatment of animals; the operation of commercial vehicles; the welfare, health and safety in factories and all work sites subject to the provisions in the Factory Acts.",
    "entry_routes_and_quals": "Entrants usually possess A levels/H grades, a degree or equivalent qualification, together with experience gained in employment. Professional qualifications, membership of professional bodies, postgraduate diplomas and NVQs/ SVQs at levels 3 and 4 are available and may be required in some occupations. On-the-job training is available in some areas.",
    "tasks": [
        "~examines building plans to ensure compliance with local, statutory and other requirements ~inspects building structures, facilities and sites to determine suitability for habitation, compliance with regulations and for insurance purposes ~inspects measuring and similar equipment in factories and visits street traders, shops, garages and other premises to check scales, weights and measuring equipment ~inspects factories and other work sites to ensure adequate cleanliness, temperature, lighting and ventilation, checks for fire hazards and inspects storage and handling arrangements of dangerous materials ~visits sites during construction and inspects completed installations of electricity, gas or water supply ~draws attention to any irregularities or infringements of regulations and advises on ways of rectifying them ~investigates industrial accidents or any complaints made by the public ~verifies the weight of commercial vehicles, checks driver\u2019s licence and hours worked ~samples and tests river water, checks and advises on premises discharging effluent to prevent pollution ~checks fishing licences and prevents illegal fishing ~visits premises where animals are kept, advises on animal care and investigates complaints ~undertakes other inspections including chemicals, drugs, flight operations, etc. ~prepares reports and recommendations on all inspections made and recommends legal action where necessary",
    ],
}
SOCmeta["3582"] = {
    "group_title": "Health and safety managers and officers",
    "group_description": "Health and safety managers and officers counsel employees to ensure and promote health and safety in the workplace and co-ordinate accident prevention and health and safety measures within an establishment or organisation.",
    "entry_routes_and_quals": "Entrants usually possess a degree or vocational qualification in Occupational Health and Safety Practice at level 6.",
    "tasks": [
        "~inspects workplace areas to ensure compliance with health and safety legislation ~helps to develop effective health and safety policies and procedures and carries out risk assessments ~instructs workers in the proper use of protective clothing and safety devices and conducts routine tests on that equipment ~compiles statistics on accidents and injuries, analyses their causes and makes recommendations to management accordingly ~maintains contact with those off work due to illness ~counsels individuals on any personal or domestic problems affecting their work ~gives talks and distributes information on accident prevention and keeps up to date with the relevant legislation",
    ],
}
SOCmeta["4"] = {
    "group_title": "Administrative and secretarial occupations",
    "group_description": "Occupations within this major group undertake general administrative, clerical and secretarial work, and perform a variety of specialist client-orientated administrative duties. The main tasks involve retrieving, updating, classifying and distributing documents, correspondence and other records held electronically and in storage files; typing, word-processing and otherwise preparing documents; operating other office and business machinery; receiving and directing telephone calls to an organisation; and routing information through organisations. Most job holders in this major group will require a good standard of general education. Certain occupations will require further additional vocational training or professional occupations to a well-defined standard.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["41"] = {
    "group_title": "Administrative occupations",
    "group_description": "Workers in this sub-major group undertake administrative and clerical work in national and local government departments and non-governmental organisations; perform specialist clerical tasks in relation to financial records and transactions, the administration of pension and insurance policies, the storage and transportation of freight, the activities of libraries and of human resources operations; and perform other general administrative tasks. They also coordinate and oversee the day-to-day running of offices and supervise office staff.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["411"] = {
    "group_title": "Administrative occupations: government and related organisations",
    "group_description": "Workers in this minor group undertake a variety of administrative and clerical work in government departments and related non-governmental organisations.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["4111"] = {
    "group_title": "National government administrative occupations",
    "group_description": "National government administrative occupations undertake a variety of administrative and clerical duties in national government departments, and in local offices of national government departments.",
    "entry_routes_and_quals": "Entry is possible to junior grades within this group with GCSEs/S grades, and/or relevant practical experience higher grades require A levels/H grades or equivalent, although many entrants are graduates. NVQs/SVQs, apprenticeships and professional qualifications are available for certain areas of work.",
    "tasks": [
        "~assists senior government officers with policy work, external liaison or general administrative work ~undertakes administrative duties specific to the operation of HM Revenue and Customs offices, Job Centres, Benefits Agency offices and other local offices of national government ~maintains and updates correspondence, documents, data and other records for storage in files or on computer ~classifies, sorts and files publications, correspondence etc. in offices and libraries ~responds to telephone enquiries and other forms of correspondence ~performs miscellaneous clerical tasks such as proof reading printed material, drafting letters, taking minutes etc",
    ],
}
SOCmeta["4112"] = {
    "group_title": "Local government administrative occupations",
    "group_description": "Local government administrative occupations undertake a variety of administrative and clerical duties in local government offices and departments.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades. Evidence of keyboard skills may also be required in some posts. Off and on-the-job training is provided. NVQs/SVQs in Administration are available at levels 2 and 3.",
    "tasks": [
        "~computes cost of product/services and maintains and balances records of financial transactions ~prepares and checks invoices and verifies accuracy of records ~receives and pays out cash and cheques and performs closely related clerical duties ~updates and maintains data, correspondence and other records for storage or despatch ~arranges, classifies and indexes publications, correspondence and other material in libraries and offices ~performs other clerical duties not elsewhere classified including preparing financial information for management, proof reading printed material and drafting letters in reply to correspondence or telephone enquiries",
    ],
}
SOCmeta["4113"] = {
    "group_title": "Officers of non-governmental organisations",
    "group_description": "Officers of non-governmental organisations perform a variety of administrative and clerical tasks in the running of trade associations, employers\u2019 associations, learned societies, trade unions, charitable organisations and similar bodies.",
    "entry_routes_and_quals": "Some roles may require GCSEs/S and pre-entry experience is usually necessary. Some organisations only employ their own members, although evidence of related work within pressure groups, the voluntary sector, trade unions or other organisations is generally sufficient.",
    "tasks": [
        "~maintains and updates records of membership details, subscription fees, mailing lists, etc. ~circulates and reports information of relevance to members and interested parties ~arranges meetings, conferences and other events and circulates agenda and other relevant material ~receives and responds to written correspondence and telephone enquiries from members and other organisations ~assists with fund raising activities within a specified geographical area ~prepares and provides measures of organisational activity for senior officials",
    ],
}
SOCmeta["412"] = {
    "group_title": "Administrative occupations: finance",
    "group_description": "Workers in this minor group perform administrative and other tasks in relation to credit control and debt collection, the maintenance of financial records within firms, financial transactions made with customers and the collection of payments from businesses and households.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["4121"] = {
    "group_title": "Credit controllers",
    "group_description": "Credit controllers perform financial, administrative and other tasks in relation to credit control and debt collection.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades but is also possible with other academic qualifications. Professional qualifications are available and may be required for some posts.",
    "tasks": [
        "~receives requests for credit submissions and lending proposals ~arranges for investigations of the credit worthiness of individuals or companies ~deals with any enquiries or difficulties concerning the acceptance or rejection of credit applications ~checks that accounting, recording and statutory procedures are adhered to for all credit transactions ~arranges for the collection of arrears of payment",
    ],
}
SOCmeta["4122"] = {
    "group_title": "Book-keepers, payroll managers and wages clerks",
    "group_description": "Book-keepers, payroll managers and wages clerks maintain and balance records of financial transactions, oversee the operation of payroll functions and calculate hours worked, wages due and other relevant contributions and deductions.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants typically possess GCSEs/S grades or equivalent qualifications, and maths may be required. Training is typically provided on-the-job. NVQs/SVQs in relevant areas are available, and apprenticeships may be available in some areas.",
    "tasks": [
        "~records and checks accuracy of daily financial transactions ~prepares provisional balances and reconciles these with appropriate accounts ~supervises payroll team and develops payroll systems and procedures ~calculates and records hours worked, wages due, deductions and voluntary contributions ~processes holiday, sick and maternity pay and travel and subsistence expenses ~compiles schedules and distributes or arranges distribution of wages and salaries ~calculates costs and overheads and prepares analyses for management",
    ],
}
SOCmeta["4123"] = {
    "group_title": "Bank and post office clerks",
    "group_description": "Bank and post office clerks deal with the payment and receipt of money, cheques and other routine financial transactions and open and close accounts. They advise upon financial products and services offered by banks, building societies and post offices.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants usually possess GCSEs/S grades, A levels/H grades or an Advanced GNVQ/GSVQ level III. On-the-job training is provided. NVQs/SVQs in relevant areas are available at levels 2, 3 and 4.",
    "tasks": [
        "~deals with enquiries from customers, other banks and other authorised enquirers ~maintains records of transactions and compiles information ~advises customers on financial services and products available ~manages the operations of a sub-post office ~receives and pays out cash, cheques, money orders, credit notes, foreign currency or travellers cheques ~provides postal services, pays state pensions, unemployment and other state benefits to claimants, supplies official forms and documentation to the public, and performs other tasks specific to the activities of a post office",
    ],
}
SOCmeta["4124"] = {
    "group_title": "Finance officers",
    "group_description": "Finance officers oversee book-keeping, general accounting and other financial and related clerical functions mainly within local government and a variety of public sector organisations.",
    "entry_routes_and_quals": "Entrants will normally possess GCSEs/S grades (including maths), a finance-related qualification at an appropriate level and have relevant work experience.",
    "tasks": [
        "~oversees the recording and checking of daily financial transactions, the preparation of provisional balances and reconciliation of accounts ~prepares or arranges the preparation of financial reports for managers ~plans work schedules and assigns tasks to financial clerks ~coordinates the activities and resources of finance departments",
    ],
}
SOCmeta["4129"] = {
    "group_title": "Financial administrative occupations n.e.c.",
    "group_description": "Job holders in this unit group carry out a variety of finance-related administrative functions not elsewhere classified in minor group 412: Administrative occupations: finance.",
    "entry_routes_and_quals": "There are no formal entry requirements although some employers may require GCSEs/S grades (including maths) and/or a relevant vocational or professional qualification at an appropriate level.",
    "tasks": [
        "~receives and pays out cash to customers in non-financial organisations such as turf accountants ~sells tickets in theatre and cinema box offices, sports stadiums etc. ~performs duties as cashier in schools, local government and other public sector organisations, legal and insurance services ~administers grants and student loans in educational institutions ~carries out clerical tasks in stockbroking companies, banking and credit card companies",
    ],
}
SOCmeta["413"] = {
    "group_title": "Administrative occupations: records",
    "group_description": "Workers in this minor group create, maintain, update and file correspondence, data, documents and information held both in hard copy and electronically for storage, reference purposes and despatch.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["4131"] = {
    "group_title": "Records clerks and assistants",
    "group_description": "Records clerks and assistants maintain and update electronic and/or hard copy documents, correspondence and other records, and organise their storage.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants typically possess GCSEs/S grades or equivalent qualifications. Training is normally provided on-the-job. Apprenticeships and NVQs/SVQs in Administration at levels 1 and 2 are available.",
    "tasks": [
        "~examines and sorts incoming material ~classifies, files, archives and locates documents and other records ~copies or duplicates documents or other records ~performs specialised clerical tasks in connection with conveyancing, litigation and the maintenance of medical records",
    ],
}
SOCmeta["4132"] = {
    "group_title": "Pensions and insurance clerks and assistants",
    "group_description": "Pensions and insurance clerks and assistants provide general clerical support to senior colleagues and perform specialist clerical tasks in relation to the administration of pensions and insurance policies.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants usually possess GCSEs/S grades. Training is usually provided on-the-job. NVQs/ SVQs, apprenticeships and professional qualifications are available in some areas.",
    "tasks": [
        "~answers queries from clients and assists in interpreting and completing information requested on forms ~checks forms completed by clients and contacts clients to obtain additional information or to clarify details ~makes arrangements for financial advisers to visit clients and potential customers ~transfers information from application forms and other documentation to computerised records ~receives notice of changes to personal circumstances and updates files ~issues application forms, policy documents, reminders, claims forms and other standard documentation ~performs general clerical duties to support senior staff",
    ],
}
SOCmeta["4133"] = {
    "group_title": "Stock control clerks and assistants",
    "group_description": "Stock control clerks and assistants receive orders from customers, prepare requisitions or despatch documents for ordered goods, maintain and update records, files and other correspondence in relation to the storage and despatch of goods.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants usually possess GCSEs/S grades. Training is usually provided on-the-job. NVQs/ SVQs in relevant areas are available at levels 2 and 3.",
    "tasks": [
        "~receives and checks in deliveries from suppliers or completed stock to be despatched to customers ~allocates appropriate storage space in accordance with stock control and space utilisation policies ~receives enquiries and orders from customers, and quotes prices, discounts, delivery dates and other relevant information ~prepares requisitions, consignments and other despatch documents ~checks requisitions against stock records and forwards to issuing department ~adjusts stock records as orders are received, reports on damaged stock and prepares requisitions to replenish damaged stock",
    ],
}
SOCmeta["4134"] = {
    "group_title": "Transport and distribution clerks and assistants",
    "group_description": "Transport and distribution clerks and assistants perform various clerical functions relating to the transport and distribution of goods and freight.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants usually possess GCSEs/S grades. Training is usually provided on-the-job. NVQs/ SVQs in relevant areas are available at levels 1, 2 and 3.",
    "tasks": [
        "~processes customer orders and forwards requisition documentation to storage and distribution personnel ~formulates delivery loads, vehicle schedules and routes to be followed by delivery staff ~monitors tachograph readings and maintains records of hours worked and distance travelled by drivers ~obtains customs clearance and processes import and export documentation necessary for the movement of goods between countries ~maintains records regarding the movement and location of freight, containers and staff",
    ],
}
SOCmeta["4135"] = {
    "group_title": "Library clerks and assistants",
    "group_description": "Library clerks and assistants classify, sort and file publications, documents, audio-visual and computerised material in libraries and offices.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants usually possess GCSEs/S grades or A-levels/H grades. Training is usually provided on-the-job. NVQs/ SVQs in Information and Library Services are available at levels 2 and 3.",
    "tasks": [
        "~sorts, catalogues and maintains library records ~locates and retrieves material on request for borrowers ~issues library material and records date of issue/ due date for return ~classifies, labels and indexes new books ~performs simple repairs on old books",
    ],
}
SOCmeta["4136"] = {
    "group_title": "Human resources administrative occupations",
    "group_description": "Human resources administrative occupations provide administrative support for the human resources (HR) operations within organisations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may require degree level qualifications and most entrants possess GCSE/S grades. Certification from the Chartered Institute of Personnel and Development is available, along with relevant NVQs/SVQs at various levels.",
    "tasks": [
        "~supports senior HR staff in the development and implementation of HR and industrial relations policies ~arranges advertisements for jobs in the relevant media ~provides practical support for recruitment and selection procedures such as checking application forms, arranging interviews of candidates and ensuring the interview panel receive all relevant documentation ~provides administrative support for training courses, work placements etc ~implements and maintains HR records systems",
    ],
}
SOCmeta["414"] = {
    "group_title": "Administrative occupations: office managers and supervisors",
    "group_description": "Workers in this minor group coordinate the day-to-day running of offices providing the administrative services of commercial, industrial and other non-governmental organisations and public agencies, and supervise the staff within those offices.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["4141"] = {
    "group_title": "Office managers",
    "group_description": "Office managers plan, organise and co-ordinate the activities and resources of offices within commercial, industrial and other non-governmental organisations and public agencies. (National and local government office managers are classified to unit group 3561: Public services associate professionals.)",
    "entry_routes_and_quals": "Some employers may require A-level or equivalent qualifications, although entry will usually be possible with GCSEs/S grades, other academic qualifications and/or relevant experience. Professional qualifications are available in some areas of work.",
    "tasks": [
        "~plans work schedules, assigns tasks and delegates responsibilities ~advises on the handling of all correspondence and enquiries relating to accounts, sales, statistical and vacancy records ~ensures that procedures for considering, issuing, amending and endorsing insurance policies are adhered to ~plans, organises and co-ordinates the activities and resources of other offices not elsewhere classified including box offices, other ticket offices and accommodation bureaux",
    ],
}
SOCmeta["4142"] = {
    "group_title": "Office supervisors",
    "group_description": "Office supervisors oversee operations and directly supervise and coordinate the activities of those carrying out general administrative and clerical work and performing specialist administrative and clerical duties in relation to finance, records, sales and other services to a variety of commercial, industrial and other non-governmental organisations and public agencies.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entrants will normally have significant relevant work experience and may require professional qualifications in some areas.",
    "tasks": [
        "~directly supervises and coordinates the activities of office staff ~establishes and monitors work schedules to meet the organisation\u2019s requirements ~liaises with managers and other senior staff to resolve operational problems ~determines or recommends staffing and other needs to meet the organisation\u2019s requirements ~reports as required to managerial staff on work-related matters",
    ],
}
SOCmeta["4143"] = {
    "group_title": "Customer service managers",
    "group_description": "Customer service managers plan, organise and co-ordinate resources necessary for receiving and dealing with the responses, complaints or further requirements of purchasers and users of a product or service, and manage customer service occupations.",
    "entry_routes_and_quals": "There are no pre-set entry requirements. Candidates are recruited with a variety of academic qualifications and/or relevant experience. Specialist qualifications may be required for work within certain sectors.",
    "tasks": [
        "~develops and implements policies and procedures to deal effectively with customer requirements and complaints ~co-ordinates and controls the work of those within customer services departments ~discusses customer responses with other managers with a view to improving the product or service provided ~plans and co-ordinates the operations of help and advisory services to provide support for customers and users",
    ],
}
SOCmeta["415"] = {
    "group_title": "Other administrative occupations",
    "group_description": "Workers in this minor group perform a variety of general, data entry and sales-related administrative tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["4151"] = {
    "group_title": "Sales administrators",
    "group_description": "Sales administrators provide support to the process of selling equipment, materials and other products or services.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants typically possess GCSEs/S grades or equivalent qualifications. Training is normally provided on-the-job. NVQs/SVQs in Administration are available at levels 1 and 2.",
    "tasks": [
        "~provides information to customers on products and prices ~help customers to place orders online through social media platforms ~fields telephone enquiries from prospective customers on behalf of the sales team ~prepares sales invoices and maintains records and accounts of sales activity ~handles customer complaints or forwards them to relevant member of sales team ~carries out general sales and marketing administrative duties",
    ],
}
SOCmeta["4152"] = {
    "group_title": "Data entry administrators",
    "group_description": "Data entry administrators enter a variety of information into databases using various software packages and assist colleagues in retrieving information.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although GCSEs/S grades or equivalent qualifications may be useful. Entrants are expected to have relevant experience and some employers require minimum typing speeds. On-the-job training is often provided. Relevant vocational qualifications such as NVQs in administration and apprenticeships are available.",
    "tasks": [
        "~enters customers' personal details and other Information into a database using the appropriate software ~transfers paper-based information into electronic databases ~updates records, such as sales or patient data ~updates website product descriptions and details ~assists other employees and/or customers in accessing information ~analyses data to identify trends and patterns",
    ],
}
SOCmeta["4159"] = {
    "group_title": "Other administrative occupations n.e.c.",
    "group_description": "Job holders in this unit group are responsible for recording, filing and disseminating information for a business, organisation or individual not elsewhere classified in minor group 415: Other administrative occupations",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants usually possess GCSEs/S grades. Training is usually provided on-the-job. NVQs/ SVQs in Administration are available at levels 2 and 3.",
    "tasks": [
        "~stores information by filling in forms, writing notes and filing records ~types reports, memos, notes, minutes and other documents ~receives and distributes incoming and outgoing correspondence ~checks figures, prepares invoices and records details of financial transactions made",
    ],
}
SOCmeta["42"] = {
    "group_title": "Secretarial and related occupations",
    "group_description": "Secretarial occupations perform general secretarial, clerical and organisational duties in support of management and other workers and provide specialist secretarial support for medical and legal activities.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["421"] = {
    "group_title": "Secretarial and related occupations",
    "group_description": "Workers in this minor group provide dictation services, type, edit and print documents, perform general clerical and organisational duties in support of management or other workers, and receive and direct clients and visitors to commercial, government and other establishments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["4211"] = {
    "group_title": "Medical secretaries",
    "group_description": "Medical secretaries deal with correspondence, make appointments and handle patients\u2019 queries file and maintain medical and other records transcribe notes and dictation and perform other clerical tasks in hospitals/surgeries and other medical establishments.",
    "entry_routes_and_quals": "Entrants require GCSEs/S grades or an Intermediate GNVQ/GSVQ level II. Professional qualifications as a medical secretary are available entrants take a one year full-time or two year part-time diploma in medical secretarial studies. NVQs/SVQs in Administration are available at levels 2, 3 and 4.",
    "tasks": [
        "~sorts and files correspondence and maintains diary of the person/s for whom they work ~transcribes dictation into required format ~maintains patients\u2019 records and arranges appointments ~answers enquiries and refers patient to appropriate experts ~organises and attends meetings and takes minutes of proceedings ~books resources such as rooms and refreshments, and orders stationery and other supplies as appropriate",
    ],
}
SOCmeta["4212"] = {
    "group_title": "Legal secretaries",
    "group_description": "Legal secretaries file and maintain legal and other records, transcribe notes and dictation into typewritten form and perform other routine clerical tasks in legal practices.",
    "entry_routes_and_quals": "There are no formal academic requirements, although employers may expect candidate to possess a legal secretarial qualification. Entrants to professional legal courses typically require GCSEs/ S grades or equivalent qualifications. NVQs/SVQs in Administration are available at levels 2, 3 and 4.",
    "tasks": [
        "~types letters and legal documents such as wills and contracts ~maintains court and clients\u2019 records, organises diaries and arranges appointments ~answers enquiries and directs clients to appropriate experts ~attends meetings and keeps records of proceedings ~delivers and collects documents ~sorts and files correspondence and carries out general clerical work",
    ],
}
SOCmeta["4213"] = {
    "group_title": "School secretaries",
    "group_description": "School secretaries provide administrative support in schools by keeping and maintaining school records and performing a range of routine clerical tasks within the school.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although many employers expect entrants to possess GCSEs/S grades, and professional secretarial courses typically require GCSEs/S grades. NVQs/SVQs in Administration are available at levels 2, 3 and 4.",
    "tasks": [
        "~sorts, files and otherwise deals with incoming and outgoing correspondence ~types directly or transcribes letters, reports and other documents, and prints or photocopies documents as required ~maintains administrative records relating to pupils and staff, and generates statistical and other reports ~handles enquiries from parents and arranges meetings with members of staff ~undertakes reception duties for visitors, handles face-to-face and telephone enquiries and passes on messages ~orders equipment and stationery ~arranges payment of invoices, handles cash",
    ],
}
SOCmeta["4214"] = {
    "group_title": "Company secretaries and administrators",
    "group_description": "Company secretaries (excluding professional/chartered company secretaries) file and maintain company records, translate notes and dictation into typewritten form and perform other clerical tasks within commercial organisations.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entrants to professional secretarial courses typically require GCSEs/S grades. NVQs/SVQs in Administration are available at levels 2, 3 and 4.",
    "tasks": [
        "~opens, sorts, distributes and files correspondence (both hard copy and electronic) ~uses appropriate software to produce correspondence, memoranda, reports, presentations and other documents from drafts, handwritten copy or by transcribing dictation ~deals directly with routine correspondence ~files and retrieves documents, sets up and maintains filing systems and reproduces copies of documentation as required ~keeps appointments diary, makes travel arrangements and arranges conference and other functions ~arranges meetings, circulates agenda and other meeting documents, attends meetings, and takes and prepares minutes ~answers, screens, handles and directs telephone requests and enquiries, takes messages and forwards to the appropriate member of staff ~undertakes reception responsibilities by greeting visitors and arranging refreshments ~ensures office supplies such as stationery and equipment are maintained",
    ],
}
SOCmeta["4215"] = {
    "group_title": "Personal assistants and other secretaries",
    "group_description": "Personal assistants and other secretaries provide administrative and secretarial support to individuals, departmental or management teams within organisations.",
    "entry_routes_and_quals": "There are no minimum academic requirements, although entry to professional secretarial courses typically requires GCSEs/S grades. NVQs/SVQs are available in Administration at levels 2, 3 and 4.",
    "tasks": [
        "~acts as a first point of contact for a manager or team with colleagues and people from outside organisations, fields telephone enquiries, takes and passes on messages ~arranges appointments, keeps business diary, organises travel arrangements, makes reservations and organises a variety of functions ~opens, sorts, distributes and files correspondence (in hard copy and electronic) and deals directly with routine correspondence ~uses appropriate software to produce correspondence, memoranda, reports, presentations and other documents from drafts, handwritten copy or by transcribing dictation ~arranges and attends meetings, takes minutes and prepares records of proceedings ~translates documents and liaises with overseas clients and suppliers",
    ],
}
SOCmeta["4216"] = {
    "group_title": "Receptionists",
    "group_description": "Receptionists receive and direct telephone calls and visitors to commercial, government and other establishments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although many employers expect entrants to possess GCSEs/S grades. There are a variety of relevant vocational qualifications available. NVQs/SVQs in Administration are available at level 2 that encompass various aspects of reception work. Professional qualifications are also available.",
    "tasks": [
        "~receives callers and clients and directs them to the appropriate person or department ~records the details of enquiries and makes appointments and reservations ~answers, screens and forwards or otherwise deals with telephone enquiries ~supplies brochures, pamphlets and other information for clients ~records details of visitors, issues security passes and informs visitors of any actions to be taken in case of an emergency ~maintains reception area in good order",
    ],
}
SOCmeta["4217"] = {
    "group_title": "Typists and related keyboard occupations",
    "group_description": "Typists and related keyboard occupations type letters, memos, reports and other documents from draft, handwritten or dictated matter, using appropriate software packages.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades. Entrants are normally expected to have obtained minimum typing speeds and hold vocational certificates. Units in keyboarding skills and producing documents are included in NVQs/SVQs in Administration at levels 1 to 4.",
    "tasks": [
        "~types letters, memos, reports, presentations and other documents using the appropriate software ~inserts logos and other special features and formats as specified ~proof reads, edits and corrects errors to produce clean copy to specified layout ~adjusts settings of printer as necessary and monitors quality of printed document",
    ],
}
SOCmeta["5"] = {
    "group_title": "Skilled trades occupations",
    "group_description": "This major group covers occupations whose tasks involve the performance of complex physical duties that normally require a degree of initiative, manual dexterity and other practical skills. The main tasks of these occupations require experience with, and understanding of, the work situation, the materials worked with and the requirements of the structures, machinery and other items produced. Most occupations in this major group have a level of skill commensurate with a substantial period of training, often provided by means of a work-based training programme.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["51"] = {
    "group_title": "Skilled agricultural and related trades",
    "group_description": "Skilled agricultural and related trades cultivate crops, raise animals and catch fish for consumption, grow plants and trees for sale, tend gardens, parks, sports pitches and other recreational areas, and maintain areas of forestry.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["511"] = {
    "group_title": "Agricultural and related trades",
    "group_description": "Those working in agricultural and related trades occupations cultivate crops and raise animals for consumption, grow plants, trees, shrubs and flowers for sale, tend private and public gardens, parks, sports pitches and other recreational areas, and perform a variety of other skilled occupations related to agriculture and fishing.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5111"] = {
    "group_title": "Farmers",
    "group_description": "Farmers and related occupations cultivate arable crops, fruits and trees, and raise cattle, sheep, pigs, poultry and other livestock for consumption.",
    "entry_routes_and_quals": "No formal academic qualifications are required, but prior practical farming experience is normally needed. Training is typically received on-the-job and via a variety of vocational qualifications in agriculture, including NVQs/SVQs at levels 1 to 4. Apprenticeships are also available in some areas.",
    "tasks": [
        "~feeds and waters animals, takes responsibility for livestock health and welfare, treats minor ailments and calls vet if necessary ~plants, propagates, sprays, fertilises and harvests field crops ~undertakes farm maintenance tasks such as fencing, hedging, cleaning and building maintenance ~operates and maintains farm machinery such as combine harvesters, straw balers, milking machines and tractors ~arranges for the sale of crops, livestock and other farm produce ~maintains records of production, finance and breeding ~ensures good environmental practice is observed in all tasks",
    ],
}
SOCmeta["5112"] = {
    "group_title": "Horticultural trades",
    "group_description": "Horticultural trades workers intensively cultivate vegetables, plants, fruit, shrubs, trees and flowers in greenhouses, market gardens, nurseries and orchards.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. NVQs/SVQs in Horticulture are available at levels 1, 2 and 3. Relevant apprenticeships and professional qualifications from the Royal Horticultural Society are also available.",
    "tasks": [
        "~prepares soil in field, bed or pot by hand or machine ~mixes soil, composts, fertilisers and/or organic matter and spreads fertiliser and manure ~sows seeds and bulbs and transplants seedlings ~propagates plants by taking cuttings and by grafting and budding, applies weed-killer, fungicide and insecticide to control pests and diseases ~prunes and thins trees and shrubs ~supports trees by staking and wiring",
    ],
}
SOCmeta["5113"] = {
    "group_title": "Gardeners and landscape gardeners",
    "group_description": "Gardeners and landscape gardeners cultivate flowers, trees, shrubs and other plants in public and private gardens, construct features to improve the appearance of existing terrain, and cut and lay turf.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. NVQs/SVQs in Horticulture are available at levels 1, 2 and 3. Relevant apprenticeships and professional qualifications are also available.",
    "tasks": [
        "~levels ground and installs drainage system as required ~prepares soil and plants and transplants, prunes, weeds and otherwise tends plant life ~protects plants from pests and diseases ~cuts and lays turf using hand and machine tools and repairs damaged turf ~prepares or interprets garden design plans ~moves soil to alter surface contour of land using mechanical equipment and constructs paths, rockeries, ponds and other features ~performs general garden maintenance",
    ],
}
SOCmeta["5114"] = {
    "group_title": "Groundsmen and greenkeepers",
    "group_description": "Groundsmen and greenkeepers cut and lay turf and maintain areas for golf courses and other sports grounds.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. NVQs/SVQs in Sports Turf Management are available at level 4. Apprenticeships and professional qualifications are also available.",
    "tasks": [
        "~levels ground and installs drainage system as required ~cuts and lays turf using hand and machine tools and repairs damaged turf ~moves soil to alter surface contour of land using mechanical equipment and constructs appropriate landscaping features and maintains such features ~monitors and maintains the quality and condition of turf ~rolls, mows and waters grass, marks out pitches",
    ],
}
SOCmeta["5119"] = {
    "group_title": "Agricultural and fishing trades n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of agricultural, practical conservation activities, and fishing tasks not elsewhere classified in minor group 511: Agricultural and related trades.",
    "entry_routes_and_quals": "No formal academic qualifications are required. Training is typically received on-the-job. A variety of vocational and academic qualifications in fish farming, forestry, horse and other animal care are available. Professional qualifications are also available and may be mandatory in some areas.",
    "tasks": [
        "~nets river fish and feeds and maintains them in spawning pens, cultivates and harvests oysters, mussels and clams on natural and artificial beds, treats water and diseased fish, and empties and cleans outdoor tanks ~navigates and maintains shipping vessels, assists with the shooting, hauling and repairing of fishing nets, prepares, lays and empties baited pots, and guts, sorts and stows fish ~establishes and maintains forest nurseries, forestry and woodland, and diagnoses and treats diseased trees ~patrols a designated area of the countryside to monitor damage, erosion, access to rights of way and the state of footpaths and other facilities, and carries out remedial maintenance work as necessary ~monitors and maintains the level of wildfowl on public and private estates ~manages areas of the countryside and the wider environment, carries out practical conservation activities and assists in promoting awareness of the natural environment",
    ],
}
SOCmeta["52"] = {
    "group_title": "Skilled metal, electrical and electronic trades",
    "group_description": "Workers in this sub-major group shape and join metal, erect and maintain metal structures and fixtures; set up and operate metal working machinery and install and repair industrial plant and machinery; assemble parts in the manufacture of metal goods; make and calibrate precision instruments; install, test and repair air conditioning systems; maintain and repair motor vehicles; and install, test and repair industrial, domestic and commercial electrical and electronic equipment.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["521"] = {
    "group_title": "Metal forming, welding and related trades",
    "group_description": "Metal forming, welding and related trades workers shape, cast, finish and join metal, and erect, install, maintain and repair metal structures and fixtures.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5211"] = {
    "group_title": "Sheet metal workers",
    "group_description": "Sheet metal workers mark out, cut, shape and join sheet metal using hand or machine tools to make and repair sheet metal products and components (excluding vehicle bodywork).",
    "entry_routes_and_quals": "Entrants typically possess GCSEs/S grades. Training is usually via apprenticeship including practical experience and technical training and relevant NVQs at level 2 and 3 are available.",
    "tasks": [
        "~examines drawings and specifications to assess job requirements ~uses template, measuring instruments and tools to mark out layout lines and reference points ~uses hand or machine tools to bend, roll, fold, press or beat cut sheet metal ~assembles prepared parts and joins them by bolting, welding or soldering ~finishes product by grinding, filing, cleaning and polishing ~repairs damaged metal parts such as copper sheets and tubes by beating, riveting, soldering, welding and fitting replacement parts ~checks final product to ensure conformity with specifications",
    ],
}
SOCmeta["5212"] = {
    "group_title": "Metal plate workers, smiths, moulders and related occupations",
    "group_description": "Metal plate workers, smiths, moulders and related occupations mark off, drill, shape, position, rivet and seal metal plates and girders to form structures and frameworks operate power hammers and presses to shape heated metal to requirements and to make and repair a variety of metal articles and make moulds and cores for casting metal and pour or inject molten metal into dies.",
    "entry_routes_and_quals": "Entrants typically possess GCSEs/S grades. Training is usually via apprenticeship including practical experience and technical training. NVQs at levels 2 and 3 are available.",
    "tasks": [
        "~examines drawings and specifications to determine operational requirements ~marks out metal plate with guidelines and reference points and cuts metal plate using hand or machine tools ~uses machine tools to bend, curve, punch, drill and straighten metal plate as required ~uses hydraulic jacks to position and align metal platework or frame for welding and bolting and rivets together metal plate and girders ~creates mould units out of sand, loam or plaster by hand or machine and fits cores into mould to form hollow parts in casting ~seals seams with caulking compound, smooths welds, fixes metal doors, metal collars, portholes, tank and hatch covers and performs other metal plate finishing tasks using a variety of hand and power tools ~heats metal for forging and positions heated metal on anvil or other work surface ~operates press or hammer and repositions workpiece between strokes ~uses forging tools to shape and cut metal and bends or shapes metal by hand forging methods using hammers, punches, drifts and other hand tools ~tempers and hardens forged pieces, as required, by quenching in oil or water ~fits and secures horses shoes ~scoops molten metal from furnace into die or die casting machine",
    ],
}
SOCmeta["5213"] = {
    "group_title": "Welding trades",
    "group_description": "Welding trades workers join metal parts by welding, brazing and soldering, and cut and remove defects from metal using a variety of equipment and techniques.",
    "entry_routes_and_quals": "Entrants typically possess GCSEs/S grades. Training is typically by apprenticeship incorporating practical experience and technical training. NVQs/SVQs at levels 1, 2 and 3 and apprenticeships are available. Welders must normally pass a competency test in the particular type of welding to be carried out.",
    "tasks": [
        "~selects appropriate welding equipment such as electric arc, gas torch, etc. ~connects wires to power supply, or hoses to oxygen, acetylene, argon, carbon dioxide, electric arc, or other source and adjusts controls to regulate gas pressure and rate of flow ~cuts metal pieces using gas torch or electric arc ~guides electrode or torch along line of weld, burns away damaged areas, and melts brazing alloy or solder into joints ~cleans and smooths weld ~checks finished workpiece for defects and conformity with specification",
    ],
}
SOCmeta["5214"] = {
    "group_title": "Pipe fitters",
    "group_description": "Pipe fitters install pipe systems and maintain and repair pipes in major utilities, industrial and construction settings and sites.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may expect entrants to possess GCSEs/S grades. Training is usually via apprenticeship including practical experience and technical training. NVQs/SVQs at levels 2 and 3 are available.",
    "tasks": [
        "~examines drawings and specifications to determine layout of piping ~measures and cuts required lengths of copper, lead, steel, iron, aluminium or plastic piping using hand or machine tools ~installs pipes for heating, ventilating, fire prevention, water and similar systems in industrial and construction settings, including oil rigs and terminals, sewerage systems and other mains networks ~fits piping into position and joins sections by welding, soldering, cementing, fusing, screwing or by other methods ~tests pipe work for leaks and makes necessary adjustments",
    ],
}
SOCmeta["522"] = {
    "group_title": "Metal machining, fitting and instrument making trades",
    "group_description": "Metal machining, fitting and instrument making trades workers mark out metal for machine tool working, set up and operate lathes, boring, drilling, grinding, milling machines and presses, assemble and repair machine tools, install and repair plant and industrial machinery, fit and assemble parts and sub-assemblies in the manufacture of metal products, make, calibrate, test and repair precision and optical instruments, and install and repair air-conditioning and refrigeration systems.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5221"] = {
    "group_title": "Metal machining setters and setter-operators",
    "group_description": "Metal machining setters and setter-operators operate machines to drill, bore, grind, cut, mill or otherwise shape metal workpieces.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Engineering apprenticeships, BTEC and City and Guilds qualifications are available together with on-the-job training. NVQs/ SVQs at level 2 and 3 are available.",
    "tasks": [
        "~examines drawings and specifications to determine appropriate method, sequence of operations and machine setting ~selects and fixes work-holding devices and appropriate cutting, shaping, grinding and/or forming tools ~sets machine controls for rotation speeds, depth of cut and stroke, and adjusts machine table, stops and guides ~operates automatic or manual controls to feed tool to workpiece or vice versa and checks accuracy of machining ~repositions workpiece, changes tools and resets machine as necessary during production run ~instructs operators on the safe and correct method of operation of the machine",
    ],
}
SOCmeta["5222"] = {
    "group_title": "Tool makers, tool fitters and markers-out",
    "group_description": "Tool makers, tool fitters and markers-out mark out metal for machining and fit, assemble and repair machine and press tools, dies, jigs, fixtures and other tools.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Engineering apprenticeships, BTEC and City and Guilds qualifications are available together with on-the-job training. NVQs/ SVQs at level 2 and 3 are available.",
    "tasks": [
        "~examines drawings and specifications to determine appropriate method and sequence of operations ~marks out reference points using measuring instruments and tools such as punches, rules and squares ~operates hand and machine tools to shape workpieces to specifications and checks accuracy of machining ~assembles prepared parts, checks their alignment with micrometers, optical projectors and other measuring equipment and adjusts as necessary ~repairs damaged or worn tools",
    ],
}
SOCmeta["5223"] = {
    "group_title": "Metal working production and maintenance fitters",
    "group_description": "Metal working production and maintenance fitters erect, install and repair electrical and mechanical plant and industrial machinery, fit and assemble parts and sub-assemblies in the manufacture of metal products and test and adjust new motor vehicles and engines.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades or a BTEC/SQA award. Apprenticeships in Engineering Maintenance at NVQ/SVQ level 3 are available.",
    "tasks": [
        "~examines drawings and specifications to determine appropriate methods and sequence of operations ~fits and assembles parts and/or metal sub-assemblies to fine tolerances to make marine engines, prototype metal products, agricultural machinery and machine tools ~fits and assembles, other than to fine tolerances, prepared parts and sub-assemblies to make motor vehicles, printing and agricultural machinery, orthopaedic appliances and other metal goods ~examines operation of, and makes adjustments to internal combustion engines and motor vehicles ~erects, installs, repairs and services plant and industrial machinery, including railway stock, textile machines, coin operated machines, locks, sewing machines, bicycles and gas and oil appliances",
    ],
}
SOCmeta["5224"] = {
    "group_title": "Precision instrument makers and repairers",
    "group_description": "Precision instrument makers and repairers make, calibrate, test and repair precision and optical instruments such as barometers, compasses, cameras, calibrators, watches, clocks and chronometers.",
    "entry_routes_and_quals": "Some GCSEs/S grades qualifications may be required. Training is usually via an apprenticeship including work experience and practical and technical training leading to recognised awards.",
    "tasks": [
        "~examines drawings or specifications to determine appropriate methods, materials and sequence of operation ~marks out and machines aluminium, brass, steel and plastics using machine tools such as grinders, lathes and shapers ~tests watches and clocks for repair to diagnose faults and removes, repairs or replaces damaged and worn parts ~tests completed timepiece for accuracy using electronic or other test equipment ~carries out service tasks such as cleaning, oiling and regulating ~checks prepared parts for accuracy using measuring equipment, assembles parts and adjusts as necessary using hand and machine tools ~positions, aligns and secures optical lenses in mounts ~tests, adjusts and repairs precision and optical instruments",
    ],
}
SOCmeta["5225"] = {
    "group_title": "Air-conditioning and refrigeration installers and repairers",
    "group_description": "Air-conditioning and refrigeration installers and repairers install, service and repair air-conditioning and refrigeration systems in factories, offices, shops and homes.",
    "entry_routes_and_quals": "There are no formal academic entry requirements although some employers may request GCSEs/S grades. Training is via an apprenticeship, or BTEC, City & Guilds or other specialised qualification.",
    "tasks": [
        "~examines the proposed site to establish if installation plans are practical ~plans layout of the system (pipework, ducts and control panels) ~produces detailed estimate of costs of the work ~plans work schedule and installs the system ~inspects and tests the installation ~carries our maintenance checks and repairs",
    ],
}
SOCmeta["523"] = {
    "group_title": "Vehicle trades",
    "group_description": "Vehicle trades workers repair, service and maintain the bodies, engines, parts, sub-assemblies, internal trimmings, upholstery and exterior surfaces of vehicles.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5231"] = {
    "group_title": "Vehicle technicians, mechanics and electricians",
    "group_description": "Vehicle technicians, mechanics and electricians accept calls for help and repair and service the mechanical parts and electrical/electronic circuitry and components of cars, lorries, buses, motorcycles and other motor vehicles, and repair and service auto air-conditioning systems.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may require GCSEs/S grades or an equivalent qualification. Training is undertaken Off and on-the-job. Apprenticeships at NVQ/SVQ levels 2 and 3 are available and take three to four years to complete.",
    "tasks": [
        "~visually checks, test drives or uses test equipment to diagnose engine and mechanical faults ~removes, dismantles, repairs and replaces defective parts and prepares new parts using appropriate tools ~reassembles, tests, adjusts and tunes the appropriate parts, systems or entire engine ~carries out routine maintenance checks on oil and air filters, brakes and other vehicle parts/systems ~diagnoses faults in electrical/electronic circuitry, removes faulty components and fits replacements ~checks condition of electrical/electronic systems and carries out servicing tasks ~installs additional electrical amenities such as radio/CD players, aerials ~repairs and services air conditioning, heating and engine-cooling systems",
    ],
}
SOCmeta["5232"] = {
    "group_title": "Vehicle body builders and repairers",
    "group_description": "Vehicle body builders and repairers construct and repair the bodies of road vehicles, and fit interior and exterior fittings to vehicle bodies.",
    "entry_routes_and_quals": "There are no formal academic entry requirements although some employers may require GCSEs/S grades or an equivalent qualification. Apprenticeships at NVQ/SVQ levels 2 and 3 are also available and take between three to four years to complete. Off and on-the-job training is provided.",
    "tasks": [
        "~diagnoses job requirements or ascertains work specifications from drawings or instructions ~selects, cuts, shapes and assembles materials to form parts of vehicle underframe, framework and body ~repairs damage to chassis and engine mountings using hydraulic rams, jacks and jigs ~hammers out dents in bodywork, fills in small depressions or corroded areas in solder, plastic or other filler compound and replaces body panels using hand and power tools ~installs and repairs interior fittings including seats, seatbelts and fascia in cars, sinks and special features in caravans and mobile shops ~positions, secures and repairs external fittings including windows, doors, door handles, catches and roof attachments",
    ],
}
SOCmeta["5233"] = {
    "group_title": "Vehicle paint technicians",
    "group_description": "Vehicle paint technicians apply paint, cellulose, vinyl stickers and wraps and other protective or decorative materials to the bodywork of motor vehicles.",
    "entry_routes_and_quals": "There are no formal academic entry requirements although some employers may require GCSEs/S grades or an equivalent qualification. Off and on-the-job training is provided. Apprenticeships at NVQ/SVQ levels 2 and 3 are also available and take between three to four years to complete.",
    "tasks": [
        "~applies masking material to protect areas not to be coated and removes any external fixtures ~consults vehicle colour code, chooses appropriate paint or mixes paint to achieve desired consistency and colour ~uses hand or electrostatic spray gun to coat surfaces, adjusting nozzle and pressure valves of the gun as required ~applies vinyl stickers and wraps to the bodywork of vehicles ~removes masking materials and refits external fittings after completion of spraying ~cleans and maintains spray equipment, protective clothing and spraying booth",
    ],
}
SOCmeta["5234"] = {
    "group_title": "Aircraft maintenance and related trades",
    "group_description": "Aircraft maintenance and related trades fit, service, repair and overhaul aircraft engines and assemblies. Licensed aircraft engineers are coded to Unit Group 3113.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades or a BTEC/SQA award. Apprenticeships in Engineering Maintenance at level 3 are available. NVQs/SVQs are available at level 2 and 3.",
    "tasks": [
        "~examines drawings, manuals and specifications to determine appropriate methods and sequence of operations ~fits and assembles parts and/or metal sub-assemblies to fine tolerances to make aircraft engines ~replaces engine components or complete engines, installs and tests electrical and electronic components and systems in aircraft ~examines and inspects airframes and aircraft components, including landing gear, hydraulic systems, and de-icers to detect wear, cracks, breaks, leaks, or other problems ~maintains, repairs and rebuilds aircraft structures, functional components, and parts ~maintains comprehensive repair logs",
    ],
}
SOCmeta["5235"] = {
    "group_title": "Boat and ship builders and repairers",
    "group_description": "Boat and ship builders and repairers construct, install and repair wooden structures and fittings, and shape, position, rivet and seal metal plates and girders to form the metal structures and frameworks for marine craft.",
    "entry_routes_and_quals": "Entrants typically possess GCSEs/S grades. Training is usually via apprenticeship including practical experience and technical training. Apprenticeships and vocational qualifications in boat building and relevant aspects of engineering and construction are available at levels 2 and 3.",
    "tasks": [
        "~examines drawings and specifications to determine job requirements ~uses rules, scribes and punches to mark out metal plate with guidelines and reference points and cuts plates using appropriate tools ~uses machine tools to bend, curve, punch, drill and straighten metal plate as required and positions and aligns metal platework or frame for welding and bolting ~rivets together metal plates and girders, seals seams, smooths welds, fixes metal doors, collars, portholes, tank and hatch covers ~selects and measures appropriate wood and cuts, shapes and drills to specification using saws, planes, chisels and other power or hand tools ~aligns and fixes prepared wood pieces by screwing, nailing, gluing and dowelling to form decking, small wooden marine craft and their interiors and fittings ~maintains and repairs woodwork and fittings",
    ],
}
SOCmeta["5236"] = {
    "group_title": "Rail and rolling stock builders and repairers",
    "group_description": "Rail and rolling stock builders and repairers erect, fit, assemble and repair rolling stock parts and sub-assemblies, and test and adjust new engines for trains.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades or a BTEC/SQA award. Apprenticeships at level 3 and other vocational qualifications at level 2 and 3 are available.",
    "tasks": [
        "~examines drawings and specifications to determine appropriate methods and sequence of operations ~fits and assembles parts and/or metal sub-assemblies to make train engines ~examines rolling stock for defects, removes, replaces and repairs faulty parts ~inspects and tests new and repaired machinery for conformity with standards and specifications ~oils and greases train engines ~maintains record of repairs and maintenance carried out",
    ],
}
SOCmeta["524"] = {
    "group_title": "Electrical and electronic trades",
    "group_description": "Workers in electrical and electronic trades install wiring in road and rail vehicles and aircraft and assemble, install, maintain, test and repair electrical and electronic equipment, components and systems concerned with lighting, signalling, telecoms, radio and television and other commercial, industrial and domestic functions.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5241"] = {
    "group_title": "Electricians and electrical fitters",
    "group_description": "Electricians and electrical fitters assemble parts in the manufacture of electrical and electronic equipment, and install, maintain, and repair electrical plant, machinery, appliances and wiring.",
    "entry_routes_and_quals": "Academic qualifications may not be required, though some GCSEs/S grades or an equivalent qualification may be an advantage. Relevant NVQs/SVQs are available at levels 1, 2 and 3. Apprenticeships combining practical work experience and technical training are available at levels 2 and 3. Entrants must have good eyesight and normal colour vision.",
    "tasks": [
        "~examines drawings, specifications and wiring diagrams to determine the method and sequence of operations ~selects, cuts and lays wires and connects to sockets, plugs or terminals by crimping, soldering, brazing or bolting ~cuts, bends and installs electrical conduit ~assembles parts and sub-assemblies using hand tools and by brazing, riveting or welding ~installs electrical plant, machinery and other electrical fixtures and appliances such as fuse boxes, generators, light sockets etc. ~examines electrical plant or machinery, domestic appliances and other electrical assembly for faults using test equipment and replaces worn parts and faulty wiring",
    ],
}
SOCmeta["5242"] = {
    "group_title": "Telecoms and related network installers and repairers",
    "group_description": "Telecoms and related network installers and repairers install, maintain and repair public and private telephone systems and maintain, test and repair telecoms cables.",
    "entry_routes_and_quals": "There are no formal academic requirements, although entrants typically possess GCSEs/S grades or an equivalent qualification. Apprenticeships and traineeships combining work experience and practical training are available at NVQ/SVQ levels 2 and 3.",
    "tasks": [
        "~installs internal cabling and wiring for telephone systems and networks and fits and wires junction and distribution boxes ~fixes connecting wires from underground and aerial lines to premises and connects cable terminals to inside wiring ~installs telephones, switchboards and coin operated phone boxes ~uses testing equipment to locate defective components of circuitry and makes any necessary repairs ~tests installation and makes any further necessary adjustments ~assists with the erection of wooden poles or steel towers to carry overhead lines ~connects cables and tests for any defects ~locates and repairs faults to lines and ancillary equipment ~erects and maintains mobile telecoms infrastructure",
    ],
}
SOCmeta["5243"] = {
    "group_title": "Tv, video and audio servicers and repairers",
    "group_description": "TV, video and audio engineers install, service and repair domestic television, video and audio appliances.",
    "entry_routes_and_quals": "Entrants typically possess GCSEs/S grades or an equivalent qualification. Training is provided Off and on-the-job and may be supplemented by short courses delivered by manufacturers. NVQs/SVQs are available at level 3.",
    "tasks": [
        "~examines equipment and observes reception to determine nature of defect ~uses electronic testing equipment to diagnose faults and check voltages and resistance ~dismantles equipment and repairs or replaces faulty components or wiring ~re-assembles equipment, tests for correct functioning and makes any necessary further adjustments ~carries out service tasks such as cleaning and insulation testing according to schedule ~installs, services and repairs aerials and satellite dishes",
    ],
}
SOCmeta["5244"] = {
    "group_title": "Computer system and equipment installers and servicers",
    "group_description": "IT engineers install, maintain and repair the physical components of computer systems and equipment.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience. Entrants typically possess GCSEs/S grades and A levels/H grades, BTEC/SQA awards or a degree. Training is usually provided on-the-job supplemented by specialised courses. Postgraduate and professional qualifications, and NVQs/SVQs at levels 2 and 3 are available.",
    "tasks": [
        "~installs, tests and maintains computer-related hardware (processors, memory chips, circuit boards, displays, sensors, data storage devices, printers, etc.) according to given specifications ~diagnoses hardware related faults ~repairs or replaces defective components ~advises on and installs operating soft/firm ware and may carry out upgrades ~maintains documentation to track and log work in progress and completed",
    ],
}
SOCmeta["5245"] = {
    "group_title": "Security system installers and repairers",
    "group_description": "Security system installers and repairers fit, maintain and service alarm systems and other electronic security devices which provide access control and monitoring, intruder detection and security lighting.",
    "entry_routes_and_quals": "Academic qualifications may not be required, though some GCSEs/S grades or an equivalent qualification may be an advantage. NVQs/SVQs for Providing Security, Emergency and Alarm Systems are available at levels 2 and 3. Apprenticeships combining practical work experience and technical training are available at levels 2 and 3. Entrants must have normal colour vision and security clearance.",
    "tasks": [
        "~discusses security needs with clients, responds to call outs and explains operation of equipment ~carries out on site surveys and determines security needs ~installs security systems and connects them to control panels, including intruder and fire alarms, surveillance and monitoring equipment and access control systems ~services existing systems and tests for faults ~responds to call-outs and repairs faulty or inoperative equipment",
    ],
}
SOCmeta["5246"] = {
    "group_title": "Electrical service and maintenance mechanics and repairers",
    "group_description": "Electrical service and maintenance mechanics and repairers maintain, service and repair domestic appliances, office machinery and electricity plant machinery, appliances and wiring.",
    "entry_routes_and_quals": "Academic qualifications may not be required, though some GCSEs/S grades or an equivalent qualification may be an advantage. NVQs/SVQs are available at levels 1, 2 and 3. Apprenticeships combining practical work experience and technical training are available at levels 2 and 3. Entrants must have good eyesight and normal colour vision.",
    "tasks": [
        "~examines drawings, specifications and wiring diagrams to determine the method and sequence of operations ~maintains and repairs electricity plant machinery, domestic appliances, office machinery and other electrical assembly and replaces worn parts and faulty wiring ~diagnoses faults using test equipment and investigates their causes ~writes reports on maintenance work and implements systems to ensure all equipment is properly maintained ~responds to call outs for unplanned/emergency repair work, both for domestic clients and in industrial settings",
    ],
}
SOCmeta["5249"] = {
    "group_title": "Electrical and electronic trades n.e.c.",
    "group_description": "Job holders in this group perform a variety of electrical and electronic occupations not elsewhere classified in minor group 524: Electrical and electronic trades.",
    "entry_routes_and_quals": "There are no formal academic requirements although entrants typically possess GCSEs/S grades. Training is usually by apprenticeship and combines practical work experience and technical training. Relevant NVQs/ SVQs are available at levels 2 and 3. Manufacturers may run specialised courses related to their products.",
    "tasks": [
        "~examines drawings, wiring diagrams and specifications to determine appropriate methods and sequence of operations ~places prepared parts and sub-assemblies in position, checks their alignment and secures with hand tools to install x-ray and medical equipment, aircraft instruments and other electronic equipment ~removes protective sheath from wires and cables and connects by brazing, soldering or crimping and applies conductor insulation and protective coverings ~assists with the erection of wood poles or steel towers to carry overhead lines ~connects and installs transformers, fuse gear, lightning arrestors, aircraft warning lights, cable boxes and other equipment ~connects cables to test equipment and tests for balance, resistance, insulation and any defects ~locates and repairs faults to lines and ancillary equipment",
    ],
}
SOCmeta["525"] = {
    "group_title": "Skilled metal, electrical and electronic trades supervisors",
    "group_description": "Jobholders in this minor group supervise and control technical and operational aspects of metal forming, welding and relate, metal machining, fitting and instrument making, vehicles trades and electrical and electronic trades.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5250"] = {
    "group_title": "Skilled metal, electrical and electronic trades supervisors",
    "group_description": "Skilled metal, electrical and electronic trades supervisors oversee operations and directly supervise and coordinate the activities of workers in skilled metal, electrical and electronic trades.",
    "entry_routes_and_quals": "Academic qualifications may not be required, though some GCSEs/S grades or an equivalent qualification may be an advantage. NVQs/SVQs are available at levels 1, 2 and 3. Apprenticeships combining practical work experience and technical training would be required together with significant, relevant work experience.",
    "tasks": [
        "~directly supervises and coordinates the activities of skilled metal, electrical and electronic trades workers ~establishes and monitors work schedules to meet productivity requirements ~liaises with managers and other departments and contractors to resolve operational problems ~determines or recommends staffing and other needs to meet productivity requirements ~reports as required to managerial staff on departmental activities",
    ],
}
SOCmeta["53"] = {
    "group_title": "Skilled construction and building trades",
    "group_description": "Skilled construction and building trades erect steel frames, lay stone, brick and similar materials, construct and repair roofs, install heating, plumbing and ventilating systems, fit windows, doors and other fixtures, and apply coverings and decorative material to walls, floors and ceilings.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["531"] = {
    "group_title": "Construction and building trades",
    "group_description": "Jobholders within construction and building trades erect and fit metal framework for building construction, cut, shape and lay stone, brick and similar materials, cover roofs and exterior walls, install, maintain and repair plumbing, heating and ventilating systems, construct and install wooden frameworks and fittings, fit glass into windows and doors, and perform other miscellaneous construction tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5311"] = {
    "group_title": "Steel erectors",
    "group_description": "Steel erectors fit and erect structural metal framework for buildings and other structures such as metal chimneys.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~examines drawings and specifications to assess job requirements ~erects ladders, scaffolding or working cage ~directs hoisting and positioning of girders and other metal parts and checks alignment ~arranges for or undertakes bolting and welding of metal parts ~checks alignment of metal parts using spirit level and plumb-rule",
    ],
}
SOCmeta["5312"] = {
    "group_title": "Stonemasons and related trades",
    "group_description": "Stonemasons erect and repair structures of stone and similar materials and cut, shape and polish granite, marble, slate and other stone for building, ornamental and other purposes.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~examines drawings, photographs and specifications to determine job requirements ~marks and cuts stone using hammers, mallet and hand or pneumatic chisels ~uses hand and power tools to shape, trim, carve, cut letters in and polish stone ~levels, aligns and embeds stone in mortar, concrete or steel frame with stone to make and repair structures",
    ],
}
SOCmeta["5313"] = {
    "group_title": "Bricklayers",
    "group_description": "Bricklayers erect and repair brick, pre-cut stone and concrete block structures such as walls, paving, chimney stacks and tunnel lining.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~examines drawings, photographs and specifications to determine job requirements ~measures construction site and lays out the first lines of bricks to mark position of walls ~mixes and spreads mortar on foundations and bricks ~places, levels and aligns bricks in mortar bed and walls ~uses hand and power tools to shape and trim bricks",
    ],
}
SOCmeta["5314"] = {
    "group_title": "Roofers, roof tilers and slaters",
    "group_description": "Roofers, roof tilers and slaters cover roofs and exterior walls with felting, sheeting, slates, tiles and thatch to provide a waterproof surface.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~measures roof or exterior wall and calculates required amounts of underfelt, tiles, slates or thatching material ~cuts wooden battens, felt and underfelt to required size ~lays and secures underfelt and covers with hot bitumen or other adhesive compound ~lays, aligns and secures successive overlapping layers of roofing material ~seals edges of roof with mortar and ensures that joints are watertight",
    ],
}
SOCmeta["5315"] = {
    "group_title": "Plumbers and heating and ventilating installers and repairers",
    "group_description": "Plumbers and heating and ventilating installers and repairers assemble, install, maintain and repair plumbing fixtures, heating and ventilating systems and pipes and pipeline systems in commercial, residential and industrial premises and public buildings for non-renewable and renewable energy.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 3 qualification, or through building up work experience supplemented with short courses. It is also the law that gas engineers to be registered with Gas Safe Register.",
    "tasks": [
        "~examines drawings and specifications to determine layout of system ~measures and cuts required lengths of copper, lead, steel, iron, aluminium or plastic using hand or machine tools ~installs fittings such as storage tanks, cookers, baths, toilets, taps and valves, refrigerators, boilers, heat pumps, radiators and fires ~tests completed installation for leaks and makes any necessary adjustments ~attaches fittings and joins piping by welding, soldering, cementing, fusing, screwing or other methods ~repairs burst pipes and mechanical and combustion faults and replaces faulty taps, washers, valves, etc",
    ],
}
SOCmeta["5316"] = {
    "group_title": "Carpenters and joiners",
    "group_description": "Carpenters and joiners construct, erect, install and repair wooden structures and fittings used in internal and external frameworks and cut, shape, fit and assemble wood to make templates, jigs, scale models and scenic equipment for theatres.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~examines drawings and specifications to determine job requirements ~selects and measures appropriate wood and cuts, shapes and drills to specification using saws, planes, chisels and other power or hand tools ~aligns and fixes prepared wood pieces by screwing, nailing, gluing and dowelling to form frames, shop fronts, counter units, decking, theatrical sets, furniture, small wooden craft, scale models and wooden templates ~checks accuracy of work with square, rule and spirit level ~maintains and repairs woodwork and fittings",
    ],
}
SOCmeta["5317"] = {
    "group_title": "Glaziers, window fabricators and fitters",
    "group_description": "Glaziers, window fabricators and fitters make and install pre-glazed wooden, metal or PVC framework, and cut, fit and set glass in windows, doors, shop fronts, and other structural frames.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Entry is typically through an apprenticeship in leading to an NVQ/SVQ at level 3.",
    "tasks": [
        "~examines drawings or specifications to determine job requirements ~scores plain, coloured, safety and ornamental glass with hand cutter and breaks off glass by hand or with pliers ~smooths edges of glass and positions and secures in frame or grooved lead strips ~applies mastic, putty or adhesive between glass and frame and trims off excess with knife ~fixes mirror panels to interior and exterior walls and repairs and replaces broken glass ~sets up and operates machinery to manufacture windows and window frames",
    ],
}
SOCmeta["5319"] = {
    "group_title": "Construction and building trades n.e.c.",
    "group_description": "Job holders in this unit group undertake a variety of tasks in the construction, alteration, maintenance and repair of buildings, steeples, industrial chimneys and other tall structures, and of underwater structures not elsewhere classified in minor group 531: Construction and building trades.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~selects, measures and cuts steel bars, rods and wire to required lengths, positions and fixes reinforcements into position and tensions as required using hydraulic jacks ~lays bricks, tiles and building blocks to construct, repair and decorate buildings ~pours and levels concrete, prepares surfaces for painting and plastering, and mixes and applies plaster and paint ~installs plumbing fixtures, woodwork structures and fittings, and sets glass in frames ~maintains and repairs steeples, industrial chimneys and other high structures, and installs and replaces lightning conductors ~erects and repairs fencing ~checks and puts on diving suit and equipment and descends underwater to carry out construction, maintenance and repair tasks on sites such as oil rigs, harbours, bridges etc",
    ],
}
SOCmeta["532"] = {
    "group_title": "Building finishing trades",
    "group_description": "Workers in this minor group apply plaster and cement mixtures to walls and ceilings, lay flooring covers and apply paint, varnish, wallpaper, tiles and other protective and decorative materials to walls and ceilings.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5321"] = {
    "group_title": "Plasterers",
    "group_description": "Plasterers apply dry linings, plaster and cement mixtures to walls and ceilings, fix fibrous sheets and cast and fix ornamental plasterwork to the interior or exterior of buildings.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~selects appropriate plasterboard or dry lining panels, cuts them to required size and fixes them to ceilings and walls ~mixes, or directs the mixing of, plaster to desired consistency ~applies and smooths one or more coats of plaster and produces a finished surface, using hand tools or mechanical spray ~pours liquid plaster into mould to cast ornamental plaster work ~measures, cuts, installs and secures plaster board and/or ornamental plasterwork to walls and ceilings ~covers and seals joints between boards and finishes surface ~checks surface level using line, spirit level and straight edge",
    ],
}
SOCmeta["5322"] = {
    "group_title": "Floorers and wall tilers",
    "group_description": "Floorers and wall tilers lay composition mixtures (other than mastic asphalt) to form flooring, plan, fit and secure carpet, underlay and linoleum and cover and decorate walls and floors with terrazzo and granolithic mixtures, tiles and mosaic panels.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~examines drawings and specifications to determine job requirements ~cleans floor surface, fixes wooden laying guides and mixes, pours and levels granite and terrazzo mixtures, bitumen, synthetic resin or other composition mixtures to form flooring ~examines premises to plan suitable layout and cuts, lays and secures underlay, carpet and linoleum ~finishes covering by rolling, smoothing, grouting or polishing ~mixes cement screed or other adhesive, cuts and positions floor and wall tiles and checks alignment of tiling with spirit level",
    ],
}
SOCmeta["5323"] = {
    "group_title": "Painters and decorators",
    "group_description": "Those working in this unit group apply paint, varnish, wallpaper and other protective and decorative materials to interior and exterior walls and surfaces, paint designs on wood, glass, metal, plastics and other materials, and stain, wax and French polish wood surfaces by hand.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~erects working platform or scaffolding up to five metres in height ~prepares surfaces by cleaning, sanding and filling cracks and holes with appropriate filler ~applies primer, undercoat and finishing coat(s) using brush, roller, or spray equipment ~mixes adhesive or removes self-adhesive backing and positions covering material on wall, matching up patterns where appropriate and removing wrinkles and air bubbles by hand or brush ~stains, waxes and French polishes wood surfaces by hand",
    ],
}
SOCmeta["533"] = {
    "group_title": "Construction and building trades supervisors",
    "group_description": "Workers in this minor group supervise and control technical and operational aspects of Construction and Building; and Building Finishing Trades.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5330"] = {
    "group_title": "Construction and building trades supervisors",
    "group_description": "Construction and building trades supervisors oversee operations and directly supervise and coordinate the activities of workers in construction and building trades.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an approved apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience supplemented with short courses.",
    "tasks": [
        "~directly supervises and coordinates the activities of construction and building workers and/or subcontractors ~establishes and monitors work schedules to meet productivity requirements ~liaises with managers and contractors to resolve operational problems ~determines or recommends staffing and other needs to meet productivity requirements ~reports as required to managerial staff on work-related matters",
    ],
}
SOCmeta["54"] = {
    "group_title": "Textiles, printing and other skilled trades",
    "group_description": "Workers in this sub-major group weave fabrics, make articles of clothing, soft furnishings and leather goods, upholster vehicle interiors, set and operate printing machines, prepare meat, poultry and fish, bake bread and flour-based confectionery products, prepare food and manage catering and bar operations within hotels, restaurants and other establishments, and perform a variety of other skilled trades.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["541"] = {
    "group_title": "Textiles and garments trades",
    "group_description": "Workers within textiles and garments trades weave fabrics into fibre and carpet, knit garments from yarn, upholster the seating and interior of vehicles and planes, make soft furnishings, make, repair and finish leather goods, and make, fit and alter tailored articles of clothing.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5411"] = {
    "group_title": "Upholsterers",
    "group_description": "Upholsterers upholster vehicle, aircraft and other seating, fix trimmings to the interiors of vehicles and aircraft, upholster furniture such as chairs and sofas, and make mattresses, curtains and other soft furnishings.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Training is provided Off and on-the-job. Relevant NVQs/ SVQs are available at level 2 and 3 and apprenticeships at level 2.",
    "tasks": [
        "~measures frame to be covered or examines drawings or other specifications and cuts material with shears, knife or scissors ~tacks and staples or otherwise secures webbing to furniture frame ~pads springs and secures padding by stitching, stapling, tacking, etc. ~pins sections of coverings together, joins by sewing and inserts trims, braids and buttons as required and fits upholstery unit to frame ~operates machine to compress padded spring assemblies and inserts them into mattress covers ~encases bed springs and padding with selected covering material by hand or machine stitching and fits castors where required ~replaces covering, padding, webbing or springs to repair upholstered furniture ~measures, cuts, pins, sews and trims fabrics to make curtains, cushions, loose covers and similar soft furnishings",
    ],
}
SOCmeta["5412"] = {
    "group_title": "Footwear and leather working trades",
    "group_description": "Footwear and leather working trades make and repair shoes, cut out, make up, sew, decorate and finish leather and leather substitute goods other than garments.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Training is mainly on?the-job. NVQs/SVQs are available in some areas.",
    "tasks": [
        "~uses hand tools or machine to cut out, trim, punch holes in or stitch guide lines on leather or leather substitute component parts ~positions leather and rubber footwear component parts on lasts and shapes and joins uppers to insoles and soles ~uses hand tools or machine to make up and repair saddles, harnesses, belts, straps and other leather products ~uses hand and machine tools to sew and stitch leather and/or other material in the making and decoration of footwear and leather goods other than garments ~prepares paper or paperboard master patterns of component parts of footwear ~waxes, cleans and finishes footwear and other leather goods",
    ],
}
SOCmeta["5413"] = {
    "group_title": "Tailors and dressmakers",
    "group_description": "Tailors and dressmakers prepare patterns and make, fit and alter tailored garments, dresses and other articles of clothing.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may require GCSEs/S grades. A variety of relevant vocational courses, including apprenticeships in some areas, are available leading to qualifications up to level 3.",
    "tasks": [
        "~takes customer\u2019s measurements and discusses required style and material ~prepares individual or adapts stock pattern ~examines fabrics or skins for flaws and prepares materials for cutting ~arranges pattern on correct grain of fabric, marks position and cuts out garment parts with hand shears, electric knife or cutting machine ~pins/tacks and fits garment on customer or dummy model and makes any necessary alterations ~sews garment parts together by hand or machine, makes buttonholes and sews on fasteners and trimmings ~shapes garment by pressing seams, pleats, etc. ~makes alterations to finished garments according to customer\u2019s requirements",
    ],
}
SOCmeta["5419"] = {
    "group_title": "Textiles, garments and related trades n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of textiles and related craft occupations not elsewhere classified in minor group 541: Textiles, garments and related trades.",
    "entry_routes_and_quals": "Entry does not depend on academic qualifications. Training is mainly on-the-job although relevant vocational courses and qualifications are available in some areas.",
    "tasks": [
        "~marks out, cuts and sews corsets, light clothing and hoods and aprons and makes and repairs sails, boat covers and other canvas goods ~fills and stuffs cushions, quilts, soft toys and furniture ~examines sketches and draws out patterns for the manufacture of garments and upholstery ~sets up and operates power and hand looms and machines to weave fibre into fabrics and carpets ~knits garments and other articles form yarn by machine or by hand ~shapes and steams fabric into hats or hoods and gives final shape to fibre helmets and felt hats ~performs other tasks not elsewhere classified, for example, forms mounts for wigs, makes buttons, shapes hat brims, and staples seams of industrial gloves",
    ],
}
SOCmeta["542"] = {
    "group_title": "Printing trades",
    "group_description": "Printing trades workers compose and set type and printing blocks, produce printing plates, cylinders and film, operate printing machines and bind the finished printed product.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5421"] = {
    "group_title": "Pre-press technicians",
    "group_description": "Pre-press technicians prepare, format and compose text and graphics in a form suitable for use in a variety of print processes.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Training is typically received on-the-job. Apprenticeships are available as well as BTEC certificates and diplomas and other vocational courses at NVQ/SVQ levels 2 and 3.",
    "tasks": [
        "~determines from specification the kind and size of type to be used ~uses computer applications to generate images and text ~scans and retouches digital images to create sample proofs, plans and lays out artwork to match planned design ~examines proof copies, checks for quality and accuracy and makes any necessary alterations ~processes filmsetting or desktop publishing output to produce image on film and transfers to printing plates and digital output ~arranges and pastes printing material onto paper ready for photographing",
    ],
}
SOCmeta["5422"] = {
    "group_title": "Printers",
    "group_description": "Printers set up and operate various small offset printing presses and digital printing processes.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Training is typically received on-the-job. Traineeships and apprenticeships in Machine Printing are available at NVQ/SVQ levels 2 and 3.",
    "tasks": [
        "~positions form or plate on machine, checks alignments and sets press ~mixes and loads inks and solvents, loads paper and regulates during print run ~prints and examines proof copies and adjusts press as necessary ~starts or directs start of printing run and monitors machine to ensure that printing proceeds smoothly ~pours colour into machine or directly on to screen and positions screen over item ~operates squeegee by hand or machine to press colour through screen ~dips wooden pattern block into colour tray and lays different colours on top of, and adjacent to, others to form the required pattern ~produces, transfers and outputs digital print images ~maintains, adjusts, repairs and cleans machine ~keeps production records",
    ],
}
SOCmeta["5423"] = {
    "group_title": "Print finishing and binding workers",
    "group_description": "Print finishing and binding workers bind books and other publications and finish printed items by hand or machine.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Training is typically received on-the-job. Traineeships and apprenticeships in Machine Printing are available at NVQ/SVQ levels 2 and 3.",
    "tasks": [
        "~folds, collates and sews printed sheets by hand or machine ~compresses sewn book in nipping machine to expel air and reduce swelling caused by sewing ~trims head, tail and fore-edge of book and gilds and marbles page edges as necessary ~cuts board and cloth for book cover and spine ~embosses lettering or decoration on cover by hand or machine ~repairs worn book bindings ~sets up and supervises automatic binding and finishing machine.",
    ],
}
SOCmeta["543"] = {
    "group_title": "Food preparation and hospitality trades",
    "group_description": "Workers in food preparation and hospitality trades slaughter livestock, cut, trim and prepare meat, poultry and fish, prepare, bake and finish bread and flour confectionery products, prepare food in hotels, restaurants and other establishments, and manage the catering and bar facilities in factories, shops, theatres, educational premises and similar establishments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5431"] = {
    "group_title": "Butchers",
    "group_description": "Butchers direct and undertake the slaughter of animals and prepare carcasses for storage, processing and sale.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers may require GCSEs/S grades. Training is typically by apprenticeship. NVQs/SVQs are available at levels 2 and 3. Professional qualifications are also available.",
    "tasks": [
        "~slaughters animal and removes skin, hide, hairs, internal organs, etc. ~cuts or saws carcasses into manageable portions ~removes bones, gristle, surplus fat, rind and other waste material ~cuts carcass parts into chops, joints, steaks, etc. for sale ~prepares meat for curing or other processing cleans tools and work surfaces",
    ],
}
SOCmeta["5432"] = {
    "group_title": "Bakers and flour confectioners",
    "group_description": "Bakers and flour confectioners prepare and bake dough, pastry and cake mixtures and make and finish flour confectionary products by hand.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job or by apprenticeship. Apprenticeships and traineeships leading to NVQs/SVQs or equivalent qualifications at levels 2 and 3 are available.",
    "tasks": [
        "~weighs ingredients according to recipe ~mixes ingredients using hand or machine to obtain the required consistency ~rolls and cuts pastry, stretches, kneads and moulds dough to form bread, rolls and buns ~fills and glazes pastry, mixes ingredients for cakes ~bakes bread, pastry and cakes ~makes cake decorations, spreads icing, fillings and toppings on products",
    ],
}
SOCmeta["5433"] = {
    "group_title": "Fishmongers and poultry dressers",
    "group_description": "Fishmongers and poultry dressers clean, cut and prepare fish and poultry for processing or sale.",
    "entry_routes_and_quals": "Academic qualifications are not normally required. Training is typically provided on-the-job.",
    "tasks": [
        "~scrubs, de-scales, heads, guts, washes and bones fish ~cuts and slits fish for curing by hand or machine ~Care for livestock prior to processing and through the slaughter stage ~Handles through manual or mechanical means",
        "the removal of feathers and internal organs, the extraction of edible offal, the removal of feet and head from poultry carcasses, trims, fillets, portions, trusses, dresses, weighs or prepares for packing ~Handles through manual or mechanical means",
        "the weighing, labelling, packing and stacking of finished product as required ~Oversees quality assurance, food hygiene, product changeover, or other food production KPIs, and supervise others who are conducting tasks as required",
    ],
}
SOCmeta["5434"] = {
    "group_title": "Chefs",
    "group_description": "Chefs plan menus and prepare, or oversee the preparation of food in hotels, restaurants, clubs, private households and other establishments.",
    "entry_routes_and_quals": "There are no formal academic requirements. Training is provided Off and on-the-job. NVQs/ SVQs, BTEC Certificates and Diplomas and foundation degrees are available. Apprenticeships are also available. Courses are also run by private cookery schools.",
    "tasks": [
        "~requisitions or purchases and examines foodstuffs from suppliers to ensure quality ~plans menus, prepares, seasons and cooks foodstuffs or oversees their preparation and monitors the quality of finished dishes ~supervises, organises and instructs kitchen staff and manages the whole kitchen or an area of the kitchen ~ensures relevant hygiene and health and safety standards are maintained within the kitchen ~plans and co-ordinates kitchen work such as fetching, clearing and cleaning of equipment and utensils",
    ],
}
SOCmeta["5435"] = {
    "group_title": "Cooks",
    "group_description": "Cooks prepare, season and cook food, often using pre-prepared ingredients, in clubs, private households, fast food outlets, shops selling food cooked on the premises and the catering departments and canteens of other establishments.",
    "entry_routes_and_quals": "There are no formal academic requirements. Training is provided off and on-the-job. NVQs/ SVQs in Food Preparation and Cooking are available at levels 1, 2 and 3. Apprenticeships are also available.",
    "tasks": [
        "~requisitions or purchases foodstuffs and checks quality ~plans meals, prepares, seasons and cooks foodstuffs ~cooks and sells a range of meals, such as fish and chips, over the counter ~plans and co-ordinates kitchen work such as fetching, clearing and cleaning of equipment and utensils",
    ],
}
SOCmeta["5436"] = {
    "group_title": "Catering and bar managers",
    "group_description": "Catering and bar managers plan, direct and co-ordinate the catering and bar facilities and services of licensed premises, factories, shops, theatres, educational premises and other establishments. They also manage outside catering businesses and shops selling food cooked on the premises.",
    "entry_routes_and_quals": "Entry is possible with a variety of academic qualifications and/or relevant experience. Larger catering and licensed premises chains offer managerial trainee schemes. Candidates for these usually require a BTEC/SQA award, a degree or equivalent qualification, or a professional qualification. Off and on-the-job training is provided. NVQs/SVQs in relevant areas are available at levels 2 to 4.",
    "tasks": [
        "~plans catering or bar services and supervises staff ~decides on range and quality of meals and beverages to be provided or discusses customer\u2019s requirements for special occasions ~purchases or directs the purchasing of supplies and arranges for preparation of accounts ~verifies that quality of food, beverages and waiting service are as required and that kitchen and dining areas are kept clean in compliance with statutory requirements ~checks that supplies are properly used and accounted for to prevent wastage and loss and to keep within budget limit",
    ],
}
SOCmeta["544"] = {
    "group_title": "Other skilled trades",
    "group_description": "Workers in this unit group perform a variety of other skilled craft and related trades.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["5441"] = {
    "group_title": "Glass and ceramics makers, decorators and finishers",
    "group_description": "Glass and ceramics workers, form, shape, decorate, smooth and polish glassware, earthenware, refractory goods, clay bricks and other ceramic goods.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/ SVQs at levels 1, 2 and 3 are available in some areas.",
    "tasks": [
        "~uses hand tools and operates machinery to heat, bend, shape, press, drill and cut glass ~makes artificial eyes, laminated glass sheets or blocks, glass fibre tissue, wool, filament and matting, marks optical lenses and assembles rimless spectacles ~makes models and moulds from moulding clay and plaster for use in the making and casting of pottery and other ceramic goods ~throws, casts and presses clay by hand or machine to form pottery, stoneware or refractory goods such as bricks, crucibles, ornaments, sanitary furnishings, saggars, cups, saucers, plates and roofing tiles ~cuts and joins unfired stoneware pipes to form junctions and gullies, moulds sealing bands on clay pipes, prepares and joins porcelain or earthenware components and assists crucible makers and stone workers with their tasks ~applies decorative designs and finishes to glassware, optical glass and ceramic goods by grinding, smoothing, polishing, cutting, etching, dipping, painting or transferring patterns or labels",
    ],
}
SOCmeta["5442"] = {
    "group_title": "Furniture makers and other craft woodworkers",
    "group_description": "Furniture makers and other craft woodworkers make, repair and restore wooden furniture, decorative objects and other crafted pieces of woodwork.",
    "entry_routes_and_quals": "There are no formal entry requirements, although entrants typically possess a variety of academic and vocational qualifications. Training is provided Off and on-the-job. A number of NVQs/SVQs and other vocational qualifications covering various aspects of furniture production and wood machining are available at various levels. Apprenticeships in Cabinet Making are available in some areas.",
    "tasks": [
        "~examines drawings and specifications to determine job requirements and appropriate materials ~selects, measures, cuts and shapes wood using saws, chisels, planes, powered hand tools and woodworking machines ~assembles parts with crafted joints, nails, screws, dowels or adhesives and fits locks, catches, hinges, castors, drawers, shelves and other fittings ~removes, replaces or repairs damaged parts of wooden furniture ~measures floor area to be covered and lays wood blocks, parquet panels or hardwood strips ~matches and marks out veneers ready for cutting and examines and repairs defects in veneer or plywood sheets",
    ],
}
SOCmeta["5443"] = {
    "group_title": "Florists",
    "group_description": "Florists sell flowers and related products in a wholesale or retail business, and design and make up floral bouquets, wreaths, tributes and other floral arrangements for sale to the public.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may request GCSEs/S grades. Off and on-the-job training is provided. NVQs/SVQs in Floristry are available at levels 2 and 3. Professional qualifications are also available.",
    "tasks": [
        "~orders and purchases fresh flowers, foliage and other floristry items such as ribbons, wire, cards, artificial flowers etc. from wholesalers or growers ~displays and cares for flowers, plants and ready-made floral arrangements in selling premises ~designs and makes up wreaths, bouquets, posies, corsages, headdresses and button holes using appropriate flowers, foliage, frame and trimmings ~confers with and advises customers regarding their design requirements and arranges for the delivery of floral arrangements as requested by the customer ~decorates buildings, halls, churches or other facilities for parties, weddings, etc ~sells flowers, plants, foliage etc. to the public and performs retail duties such as keeping accounts",
    ],
}
SOCmeta["5449"] = {
    "group_title": "Other skilled trades n.e.c.",
    "group_description": "Job holders in this unit group engrave jewellery and stoneware, make artificial hairpieces, charge fireworks and munitions with explosive material, make lampshades, wickerwork, toys, dolls, models, candles, artificial flowers, other fancy goods, make patterns for moulds for metal castings, make and tune musical instruments, craft precious metals and stones, and perform other hand craft occupations not elsewhere classified in minor group 544: Other skilled trades.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically via apprenticeship or through specialised courses. NVQs/SVQs are available in some areas.",
    "tasks": [
        "~uses hand or machine tools to engrave letters, patterns and other designs on jewellery and stoneware ~constructs and covers wire frames for lampshades ~makes wigs, beards and other artificial hairpieces from human hair or synthetic materials ~interweaves canes of willow, withy, bamboo, rattan or similar material to make baskets and other pieces of wickerwork ~charges fireworks, cartridges and other munitions with explosive material ~makes children\u2019s toys, dolls, models, candles, artificial flowers and other fancy goods ~makes, maintains and adapts surgical and orthopaedic appliances ~makes patterns for moulds, fits metal castings, pours plaster, fills plaster mould with resin and smooths surface ~makes musical instruments, makes and assembles parts for musical instruments, and tunes to improve pitch, tone and volume ~makes and repairs jewellery and decorative precious metal ware, sets, cuts and polishes gemstones and makes master patterns for articles of jewellery",
    ],
}
SOCmeta["6"] = {
    "group_title": "Caring, leisure and other service occupations",
    "group_description": "This major group covers occupations whose tasks involve the provision of a service to customers, whether in a public protective or personal care capacity. The main tasks associated with these occupations involve the care of the sick, the elderly and infirm; the care and supervision of children; the care of animals; and the provision of travel, personal care and hygiene services. Most occupations in this major group require a good standard of general education and vocational training. To ensure high levels of integrity, some occupations require professional qualifications or registration with professional bodies or relevant background checks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["61"] = {
    "group_title": "Caring personal service occupations",
    "group_description": "Workers in this sub-major group assist health professionals in the care of patients; undertake caring personal services within the community; supervise the activities of pre-school age children and assist teachers with non-teaching duties; provide technical assistance to veterinarians and provide other services in the care of animals; provide funeral services; and control pests hazardous to public health.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["611"] = {
    "group_title": "Teaching and childcare support occupations",
    "group_description": "Workers in childcare and related personal services supervise play and other activities for pre-school age children, assist teachers and care for children in day or residential nurseries, children\u2019s homes and private households.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6111"] = {
    "group_title": "Early education and childcare assistants",
    "group_description": "Early education and childcare assistants assist in the care of children from birth up to seven years of age in day or residential nurseries, children\u2019s homes, maternity units and similar establishments.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades followed by the award of a certificate from the Council for Awards in Children\u2019s Care and Education. An NVQ/SVQ in Child Care and Education or equivalent qualification up to level 3 may be required to work in this role. A DBS check is mandatory.",
    "tasks": [
        "~may work under the supervision of more experienced practitioners ~baths, dresses, prepares feed for and feeds babies, changes babies clothing whenever necessary ~supervises young children at mealtimes ~plans and organises games and other activities and supervises children\u2019s play ~reads stories, organises counting games to help develop language and number skills ~communicates with parents and colleagues on children\u2019s development and well-being",
    ],
}
SOCmeta["6112"] = {
    "group_title": "Teaching assistants",
    "group_description": "Teaching assistants assist teachers with their day-to-day classroom work and with routine administrative tasks.",
    "entry_routes_and_quals": "Academic qualifications may be required by some employers, although entry is possible with relevant experience (possibly on a voluntary basis) alone. NVQs at level 2 and 3 qualifications are available. DBS clearance is mandatory.",
    "tasks": [
        "~assists teacher with preparation or clearing up of classroom ~looks after lesson materials such as paper, pencils and crayons ~listens to children read, reads to them or tells stories ~assists children with washing or dressing for outdoor and similar activities ~makes simple teaching aids and constructs thematic displays of educational material or children\u2019s work ~helps with outings and other out-of-classroom activities",
    ],
}
SOCmeta["6113"] = {
    "group_title": "Educational support assistants",
    "group_description": "Educational support assistants work with teachers to provide one-to-one support for children with particular learning needs.",
    "entry_routes_and_quals": "Academic qualifications may be required by some employers, although entry is possible with relevant experience alone. A DBS check is mandatory.",
    "tasks": [
        "~supports schoolwork under teacher\u2019s supervision ~helps child understand instruction through a variety of means and encourages self-confidence and independence ~identifies signs of distress and offers reassurance ~implements care programmes, as appropriate ~helps and encourages child to communicate ~attends to child\u2019s physical needs ~provides feedback to teachers and completes and maintains records",
    ],
}
SOCmeta["6114"] = {
    "group_title": "Childminders",
    "group_description": "Childminders provide day-to-day care of children in their own homes, and supervise and participate in their play, educational and other activities.",
    "entry_routes_and_quals": "Entry may not depend upon academic qualifications, although employers may expect a candidate to possess a qualification accredited by the Council for Awards in Children\u2019s Care or other qualifications. Childminders must be registered with OFSTED to care for children under the age of 8 years. NVQs/SVQs in Child Care and Education are available at levels 2 and 3. A minimum age limit of 18 years applies, and a DBS check is mandatory.",
    "tasks": [
        "~changes babies\u2019 nappies and clothes as necessary and makes up bottles for feeds ~plans, prepares and serves children\u2019s meals and supervises children during meals ~provides, supervises and participates in children\u2019s indoor and outdoor play activities to promote their development ~takes children to participate in play groups or on appropriate outings ~takes older children to and from school ~maintains appropriate records of children\u2019s development ~complies with regulations set by OFSTED and their inspection requirements",
    ],
}
SOCmeta["6116"] = {
    "group_title": "Nannies and au pairs",
    "group_description": "Nannies and au pairs care for and supervise babies and young children in the homes of the children's families.",
    "entry_routes_and_quals": "Entry does not depend upon academic qualifications but a qualification in childcare and/or relevant experience may be useful. NVQs/SVQs in Child Care and Education are available at levels 2 and 3. A minimum age limit of 18 years applies, and a DBS check is mandatory. Nannies are not required to register with Ofsted but can become a part of the Voluntary Ofsted Childcare Register.",
    "tasks": [
        "~cares for children and babies and participates in their daily activities ~assists children to wash and dress ~changes babies\u2019 nappies and clothes as necessary and makes up bottles for feeds ~mends, washes and irons children\u2019s clothes and tidies their rooms ~organises activities and opportunities to socialise with other children ~takes children to school and other appointments ~helps develop child's learning, such as basic social skills",
    ],
}
SOCmeta["6117"] = {
    "group_title": "Playworkers",
    "group_description": "Playworkers deliver and facilitate play opportunities for children in a range of formal and informal settings including play schemes, free play locations, and in pre- and after-school activities.",
    "entry_routes_and_quals": "Entry may not depend upon academic qualifications, although some employers will expect candidates to possess or be working towards a relevant qualification. NVQs/SVQs in Child Care and Education are available at levels 2 and 3. A DBS check is mandatory.",
    "tasks": [
        "~supervises children\u2019s games and encourages the development of physical, social and language skills ~provides play areas and prepares materials for a wide range of children\u2019s activities ~encourages children\u2019s independence, self-confidence and social interaction ~organises and supervises children on excursions ~organises and supervises children\u2019s activities in accordance with Health and Safety regulations, deals accordingly with injuries and emergencies ~puts away equipment and cleans premises after use ~liaises with parents, carers and colleagues and keeps appropriate records",
    ],
}
SOCmeta["612"] = {
    "group_title": "Animal care and control services",
    "group_description": "Workers in this minor group carry out pest control services, care for animals in stables, kennels, zoos and other such establishments, provide specialised grooming and clipping services for animals and capture stray or unruly dogs.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6121"] = {
    "group_title": "Pest control officers",
    "group_description": "Pest control officers investigate the presence of pests that are hazardous to public health or cause nuisance, lay traps to capture pests and treat areas of infestation.",
    "entry_routes_and_quals": "There are no formal academic entry qualifications, though some employers may expect entrants to possess GCSEs/S grades. Training is provided on-the-job, supplemented by specialist courses covering different aspects of pest control.",
    "tasks": [
        "~receives reports from public, property owners and authorities regarding the presence of pests and infestations ~visits sites to investigate the presence of rodents, infestations and other pests that may be hazardous to public health ~lays traps to capture pests, and fumigates and disinfects areas to remove infestations ~advises property owners on courses of action to prevent the return of pests ~liaises with environmental health officers, housing officers and other relevant authorities where measures on a large scale are required to remove pests ~returns to sites to examine contents of traps laid and the continued presence of reported pests ~treats wood for effects of termites, woodworm and other infestations of timber",
    ],
}
SOCmeta["6129"] = {
    "group_title": "Animal care services occupations n.e.c",
    "group_description": "Job holders in this unit group care for animals held in kennels, stables, zoos and similar establishments, provide specialised training, grooming, clipping and trimming services for animals, and searches for and captures stray or nuisance dogs in public areas and perform a variety of animal care tasks not elsewhere classified in minor group 612: Animal care and control services.",
    "entry_routes_and_quals": "Entry is possible without formal academic qualifications, although some employers may ask for GCSEs/S grades. There is a variety of vocational qualifications available, including NVQs/SVQs in Animal Care at levels 1 and 2, in Dog Grooming at levels 2 and 3, and BTEC qualifications and apprenticeships relating to Horse Care.",
    "tasks": [
        "~feeds, washes, grooms, trims and exercises animals ~cleans animals\u2019 quarters and renews bedding as necessary ~houses, feeds, exercises, trains, grooms horses, dogs and other animals in preparation for entry to shows, races and other events ~checks animals for illness, treats minor ailments or calls for vet if further treatment is required ~meets prospective owners and advises on animal selection and animal care ~patrols public areas to search for and capture stray or nuisance dogs, and transports captured animals to kennels ~work alongside veterinary surgeons and nurses to provide vital nursing care to ensure the wellbeing of animal patients",
    ],
}
SOCmeta["613"] = {
    "group_title": "Caring personal services",
    "group_description": "Those working in caring personal services occupations transport patients by ambulance, stretcher, wheelchair or other means and assist health professionals with the care of patients in hospitals, dental surgeries, nursing homes, residential homes, clinics, day care services and within the home.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6131"] = {
    "group_title": "Nursing auxiliaries and assistants",
    "group_description": "Nursing auxiliaries and assistants assist doctors, nurses and other health professionals in caring for the sick and injured within hospitals, homes, clinics and the wider community.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Off and on-the-job training is provided. NVQs/ SVQs in Health and Social Care are available at levels 2 and 3.",
    "tasks": [
        "~performs basic clinical tasks such as taking patients\u2019 temperature and pulse, weighing and measuring, performing urine tests and extracting blood samples ~prepares patient for examination and treatment ~distributes and serves food, assists patients in feeding and prepares snacks and hot drinks ~assists patients in washing, dressing, toiletry activities and general mobility ~changes bed linen, makes beds and tidies wards",
    ],
}
SOCmeta["6132"] = {
    "group_title": "Ambulance staff (excluding paramedics)",
    "group_description": "Ambulance staff transport sick, injured and convalescent persons and give first aid treatment in emergencies and check ambulance vehicles are roadworthy, cleaned and have all the necessary equipment.",
    "entry_routes_and_quals": "Academic qualifications are not normally required. Entry requirements vary between ambulance services. Entrants must normally have possessed a full clean driving licence for one to two years and have health clearance. Entrants undertake a minimum of 2 weeks training in first aid and patient care. Successful trainees are then attached to an ambulance station where they work under the guidance of a trained supervisor for a probationary period before working unsupervised.",
    "tasks": [
        "~helps patients into and out of ambulance ~drives ambulance or accompanies driver to transport patients to hospitals or other treatment centres and homes ~ascertains nature of injuries and provides first aid treatment ~cleans and disinfects ambulance after use and carries out routine care of ambulance equipment ~replenishes medical supplies in ambulance as necessary ~checks and maintains vehicles to ensure they are roadworthy",
    ],
}
SOCmeta["6133"] = {
    "group_title": "Dental nurses",
    "group_description": "Dental nurses prepare patients for, and assist with, dental examinations, prepare and sterilise instruments and maintain case records.",
    "entry_routes_and_quals": "Entry is most common with GCSEs/S grades. Training is available both Off and on-the-job. To become a registered dental nurse, entrants need to complete a course recognised by the General Dental Council.",
    "tasks": [
        "~prepares patient for examination ~prepares and sterilises instruments and follows guidelines to maintain sterile conditions within the surgery ~hands required equipment and medication to dentist during examination ~assists with minor treatment, such as preparing materials for fillings ~removes water and saliva from patient\u2019s mouth during treatment ~maintains records, processes and mounts x-ray films and undertakes reception duties",
    ],
}
SOCmeta["6134"] = {
    "group_title": "Houseparents and residential wardens",
    "group_description": "Houseparents and residential wardens are responsible for the care and supervision of children, young people and the elderly within residential homes, schools or their own homes. An essential requirement of their work is that they reside with those for whom they are providing support.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. In most cases workers will hold or be working towards the appropriate qualification for the job. Entrants must typically be 18 years old and have experience of working in a care environment. Both Off and on-the-job training is available. A wide range of qualifications including NVQs/SVQs covering various aspects of care are available. Background checks including an enhanced DBS check, CPR and first aid certifications are likely to be required.",
    "tasks": [
        "~creates friendly, secure atmosphere and tries to gain the trust and confidence of those in the home or under supervision ~plans and participates in games and leisure activities to encourage emotional, social, physical and intellectual development ~ensures that all material needs of residents are provided and endeavours to resolve any problems that they may have ~ensures that students attend school regularly ~manage the household (domestic duties) ~may provide one-to-one counselling or group therapy ~establishes and maintains contact with members of the neighbouring community and/or the residents\u2019 family and friends ~maintains contact and discusses problems/progress with other staff and social workers ~keeps records and writes reports",
    ],
}
SOCmeta["6135"] = {
    "group_title": "Care workers and home carers",
    "group_description": "Care workers and home carers attend to the personal needs and comforts of children, the elderly, the infirm and others with care and support needs (\u2018service users\u2019) within residential care establishments, day care establishments or in their own homes.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. In most cases workers will be required to register with the appropriate statutory body which involves satisfying the registration criteria. This would normally include holding or working towards the appropriate qualification for the job. Entrants must typically be 18 years old and have experience of working in a care environment. Both Off and on-the-job training is available. A wide range of qualifications including NVQs/SVQs covering various aspects of care are available. Background checks including a DBS check are likely to be required.",
    "tasks": [
        "~assists and enables service users to dress, undress, wash, use the toilet and bathe ~serves meals to service users at table or in bed, and assists with feeding if required ~assists with service users\u2019 overall comfort and wellbeing ~provides interest and activities to stimulate and engage the service user ~helps with daily activities such as letter writing, paying bills, collecting benefits ~undertakes light cleaning and domestic duties including meal preparation as required ~monitors service users\u2019 conditions by taking temperature, pulse, respiration and weight, and contributes to record keeping ~liaises with professional staff in carrying out care plans etc.",
    ],
}
SOCmeta["6136"] = {
    "group_title": "Senior care workers",
    "group_description": "Senior care workers routinely oversee and monitor care workers, care assistants and home carers. They also attend to the personal needs and comforts of children, the elderly and the infirm and others with care and support needs (\u2018service users\u2019) within residential care establishments, day care establishments or in their own homes.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. In most cases workers will be required to register with the appropriate statutory body which involves satisfying the registration criteria. This would normally include holding or working towards the appropriate qualification for the job. A wide range of qualifications including NVQs/SVQs covering various aspects of care are available. Senior care workers must be qualified to an appropriate level (usually NVQ level 3). They often have a background in social care and have achieved a qualification in this area some may have nursing qualifications. Background checks including a DBS check are likely to be required.",
    "tasks": [
        "~routinely oversees and monitors care workers and home carers ~takes responsibility for the shift and for the service while on duty ~responds to emergencies and provides guidance and support to care workers ~assists and enables service users to dress, undress, wash, use the toilet and bathe ~serves meals to service users at table or in bed, assists with feeding if required ~assists with service users\u2019 overall comfort and wellbeing ~provides interest and activities to stimulate and engage the service user ~helps with daily activities such as letter writing, paying bills, collecting benefits ~undertakes light cleaning and domestic duties including meal preparation as required ~monitors service users\u2019 conditions by taking temperature, pulse, respiration and weight, and contributes to record keeping ~liaises with professional staff in carrying out care plans etc",
    ],
}
SOCmeta["6137"] = {
    "group_title": "Care escorts",
    "group_description": "Care escorts accompany and transport adults and children between their places of residence and other destinations and act as chaperones for under 16s engaged in theatrical, television and film productions.",
    "entry_routes_and_quals": "There are no formal qualifications, other than a clean driving licence with the appropriate classification for those who are driving in addition to escorting. DBS checks are mandatory for those working with vulnerable adults and/or children.",
    "tasks": [
        "~transports clients safely and securely between approved destinations ~supports and secures chair bound clients ~organises toilet and meal stops, as appropriate ~supervises contact between parents and separated children ~communicates with colleagues and maintains accurate records ~supervises and accompanies children who are taking part in a theatrical, television or film production",
    ],
}
SOCmeta["6138"] = {
    "group_title": "Undertakers, mortuary and crematorium assistants",
    "group_description": "Undertakers, mortuary and crematorium assistants make funeral arrangements for clients, prepare the deceased for burial or cremation, and supervise and assist the proceedings of funerals.",
    "entry_routes_and_quals": "There are no formal academic requirements although some employers require candidates to possess GCSEs/S grades. A full driving licence is often required. Training is provided on-the-job. Professional qualifications in funeral directing and embalming are available.",
    "tasks": [
        "~collects body of deceased and assists with the completion of necessary documents ~interviews relative or representative of the deceased to discuss preparations for funeral ~liaises with cemetery or crematorium authorities on behalf of client ~washes and injects body with sterilising fluid to prevent deterioration prior to funeral, and applies cosmetics, wax and other materials to restore normal appearance ~provides hearse and funeral cars and leads funeral procession ~controls the operations of crematoriums and cemeteries and processes legal documentation",
    ],
}
SOCmeta["62"] = {
    "group_title": "Leisure, travel and related personal service occupations",
    "group_description": "Workers within Leisure, Travel and Related Personal Service Occupations provide services and facilities for sporting and recreational activities; make travel arrangements for clients and provide ancillary services for travellers; provide hairdressing and beauty services undertake domestic and care-taking duties in private households, public buildings and other establishments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["621"] = {
    "group_title": "Leisure and travel services",
    "group_description": "Those working in occupations in this minor group organise and maintain services and equipment necessary for sporting and recreational activities, advise upon and make travel arrangements for customers and provide services to enhance the enjoyment, comfort and safety of holidaymakers and air, rail, and sea passengers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6211"] = {
    "group_title": "Sports and leisure assistants",
    "group_description": "Sports and leisure assistants, provide and maintain facilities for sporting and recreational activities and supervise their use, maintain the continuity of entertainment and social events, offer odds and accept bets on the result of sporting and other events, control gambling activities, work behind the scenes in production and broadcasting enterprises in a supporting role to ensure operations run smoothly.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may require GCSEs/S grades. A variety of vocational qualifications are available in Sports and Recreation and Leisure and Tourism.",
    "tasks": [
        "~maintains sports and leisure equipment and prepares equipment for use ~supervises the use of swimming pools, gymnasium apparatus, fitness machines and other recreational equipment ~work in teams patrolling popular stretches of the coast, advising people when and where they can swim safely and making rescues when necessary ~maintains hygienic operation of swimming pools and associated facilities such as hot tubs, showers and changing areas ~carries clubs for golfers, advises on the layout and distance of golf courses and appropriate choice of golf club ~announces acts, makes introductions, proposes toasts and maintains the continuity of entertainment events and social functions ~assesses likely outcome of an event and establishes odds, accepts and records bets, issues receipts and pays out on winning bets ~controls the progress of games of cards, roulette and other gambling activities according to established rules ~provides support in production and broadcasting operations, such as helping set up and maintain the set, running errands, moving equipment, looking after guests, and transporting crew and cast between locations",
    ],
}
SOCmeta["6212"] = {
    "group_title": "Travel agents",
    "group_description": "Travel agents advise travellers upon travel arrangements, make bookings and receive payment for travel arrangements made.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although many employers require entrants to possess GCSEs/S grades. Off and on-the-job training is usually available. NVQs/SVQs in travel services at levels 2 and 3, BTEC, apprenticeships and higher level qualifications are available.",
    "tasks": [
        "~discusses client requirements and shows brochures containing suitable packages ~establishes availability with tour operators and makes bookings ~consults travel time-tables, books travel tickets and accommodation ~handles cash, debit and credit card payment ~informs client of any changes in travel arrangements ~advises on issues of currency, passports, visa requirements, insurance, car hire, vaccinations and other health precautions",
    ],
}
SOCmeta["6213"] = {
    "group_title": "Air travel assistants",
    "group_description": "Air travel assistants issue travel tickets and boarding passes, examine other documentation, provide information and assistance at airport terminals and look after the welfare, comfort and safety of passengers travelling in aircraft.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades. Fluency in a foreign language may also be required in some posts. Training typically lasts between 3 to 6 weeks followed by a 6 to 12 month probationary period of on-the-job training.",
    "tasks": [
        "~receives passengers at airport terminal, examines tickets and other documentation, checks in luggage and distributes boarding passes ~checks emergency equipment, distributes reading material, blankets and other items, and ensures that the aircraft is ready for the receipt of passengers ~welcomes passengers on board the aircraft, guides them to their seats and assists with any hand luggage ~ensures that sufficient stocks of meals and beverages are on board the aircraft prior to take off and serves passengers during the flight ~sells duty-free goods during the flight ~makes announcements on behalf of the pilot, demonstrates the use of emergency equipment and checks that safety belts are fastened ~directs and instructs passengers in the event of an emergency, ensures safety procedures are followed",
    ],
}
SOCmeta["6214"] = {
    "group_title": "Rail travel assistants",
    "group_description": "Rail travel assistants issue, collect and inspect travel tickets, provide information and assistance to railway passengers, operate train doors, and perform a variety of duties on station platforms in connection with the arrival and departure of trains and the movement of goods and passengers, and on trains to ensure the safety and comfort of passengers.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although entrants are required to take a medical examination and have normal colour vision. Training is provided Off and on-the-job. NVQs/SVQs in Rail Services are available at level 2.",
    "tasks": [
        "~examines and collects tickets at the ticket barrier of a railway station ~helps with passenger enquiries and makes announcements over a public address system at stations ~loads and unloads mail, goods and luggage, operates lifts and hoists and drives small trucks ~assists passengers with special needs to board and leave trains ~attends to the safety, welfare and comfort of passengers on trains and manages train crew ~checks control panel operation before start of journey, operates train door controls and signals to driver to start or stop train ~inspects and issues tickets on trains, deals with passenger enquiries, and takes charge of goods being transported on train",
    ],
}
SOCmeta["6219"] = {
    "group_title": "Leisure and travel service occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of leisure and travel service occupations not elsewhere classified in minor group 621: Leisure and travel services.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Spoken fluency in a foreign language is needed for some posts. NVQs/SVQs in travel services are available at levels 2 and 3. Training is also received on-the-job.",
    "tasks": [
        "~observes regulations concerning the carrying capacity of vehicles and controls the boarding of passengers accordingly ~receives passengers, checks tickets and guides them to their seats, makes announcements regarding travel arrangements and places of interest, and deals with passengers\u2019 queries ~makes local arrangements at stopover points for food and accommodation ~responds to enquiries and complaints, books excursions and other entertainment and provides other assistance and advice to holidaymakers ~signals to driver when to stop and start bus, collects fares from passengers and issues tickets and changes destination indicators as necessary ~completes way-bill at scheduled points on route and balances cash taken with tickets issued ~receives passengers on ship, examines tickets and other documentation, directs them to their cabin and assists with any luggage ~makes announcements to passengers and deals with enquiries ~serves food and beverages to passengers",
    ],
}
SOCmeta["622"] = {
    "group_title": "Hairdressers and related services",
    "group_description": "Jobholders in this unit group cut, style and treat hair, apply cosmetics and give facial and body beauty treatments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6221"] = {
    "group_title": "Hairdressers and barbers",
    "group_description": "Hairdressers and barbers shampoo, cut, colour, style and treat hair.",
    "entry_routes_and_quals": "There are no minimum academic requirements for entry, although some colleges require candidates to possess GCSEs/S grades. Training is provided Off and on-the-job and lasts up to three years leading to the awarding of NVQs/SVQs at levels 1, 2 and 3. Apprenticeships leading to an NVQ/SVQ at level 3 are also available.",
    "tasks": [
        "~discusses customer requirements, analyses hair condition and other relevant features to define and advise on hair style ~washes, conditions, bleaches, tints or dyes hair and provides any necessary basic scalp treatments ~cuts and trims hair using scissors, clippers, razor and comb ~combs, brushes, blow-dries or sets wet hair in rollers to style or straighten ~shaves and trims beards and moustaches ~collects payment, arranges appointments and cleans and tidies salon ~maintains client records and keeps up-to-date with new products, styles and techniques ~ensures hair products are stored and used appropriately and observes relevant health and safety factors ~demonstrates, sells and recommends hair care products to clients and advises them on hair care",
    ],
}
SOCmeta["6222"] = {
    "group_title": "Beauticians and related occupations",
    "group_description": "Beauticians and related workers give facial and body beauty treatments, apply cosmetics and dress wigs.",
    "entry_routes_and_quals": "There are no minimum academic requirements for entry, although some colleges require candidates to possess GCSEs/S grades. NVQs/SVQs in Beauty Therapy are available at levels 1, 2 and 3. Professional qualifications are also available.",
    "tasks": [
        "~discusses clients requirements, analyses and advises client on appropriate skin care, and applies treatments to the face or body ~massages scalp, face and other parts of the body and carries out spray tanning ~uses waxing, threading, sugaring and other epilation techniques to remove any unwanted body hair ~cleans, shapes and polishes finger and toe nails, applies nail extensions ~performs specialist treatments for conditions such as acne, applies skin rejuvenation therapies ~recognises problems and refers clients to medical practitioners if appropriate ~advises clients on diet and exercise to assist in weight loss and slimming ~maintains client records, sells and advises on cosmetic products and services, and ensures appropriate health and safety issues are addressed. ~applies make-up to hide blemishes or enhance facial features and advises clients on skin care and make-up techniques",
    ],
}
SOCmeta["623"] = {
    "group_title": "Housekeeping and related services",
    "group_description": "Housekeeping and related services workers co-ordinate and undertake domestic tasks in private households, hotels, schools, hostels and other residential establishments, take care of schools, churches, offices, flats and other buildings.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6231"] = {
    "group_title": "Housekeepers and related occupations",
    "group_description": "Housekeepers and related workers perform domestic cleaning and other housekeeping tasks within private households, hotels, schools, hostels and other non-private households.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although entrants typically possess GCSEs/S grades or an equivalent qualification. NVQs/SVQs and other vocational qualifications in hospitality and catering at levels 2 and 3 are available.",
    "tasks": [
        "~controls the purchase and storing of food, cleaning materials, linen and other household supplies ~maintains household records ~performs a variety of domestic tasks including food preparation and service, cleaning and laundry ~assists employer in washing, dressing, packing and other personal activities",
    ],
}
SOCmeta["6232"] = {
    "group_title": "Caretakers",
    "group_description": "Caretakers supervise and undertake the care and maintenance of church, school, office and other buildings, their facilities, fixtures and contents.",
    "entry_routes_and_quals": "No academic qualifications are required. Previous relevant experience may be needed, and training is provided in some areas. Background checks will be required for those whose job brings them into contact with children or vulnerable adults.",
    "tasks": [
        "~locks and unlocks doors and entrances at appropriate times ~supervises and/or undertakes the cleaning and maintenance of premises ~controls heating, lighting and security systems ~undertakes minor repairs and notifies owner of need for major repairs ~checks fire and safety equipment for adequate functioning",
    ],
}
SOCmeta["624"] = {
    "group_title": "Cleaning and housekeeping managers and supervisors",
    "group_description": "Cleaning and housekeeping managers and supervisors manage and co-ordinate the cleaning and housekeeping activities in private households, hotels, schools, hostels and other residential establishments, in offices and other premises, and directly supervise the staff undertaking those tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6240"] = {
    "group_title": "Cleaning and housekeeping managers and supervisors",
    "group_description": "Cleaning and housekeeping managers and supervisors manage and supervise cleaning and other housekeeping tasks within private households, hotels, schools, hostels and other non-private households, and in offices and other premises.",
    "entry_routes_and_quals": "There are no formal academic requirements, but GCSEs/S grades and/or relevant work experience may be needed in some instances. BTEC certificates and diplomas, NVQs/SVQs and degree level courses are available in relevant areas.",
    "tasks": [
        "~recruits or participates in the selection process for cleaning and housekeeping staff and takes charge of staff training ~assigns duties and responsibilities to staff and oversees working rotas ~supervises the activities of cleaners and other housekeeping staff and inspects work undertaken ~oversees the provision of cleaning and housekeeping supplies ~arranges for replacement of broken, defective tools and handles arrangements for repairs to fixtures and fittings ~manages budget for cleaning and housekeeping supplies and keeps record of expenditure",
    ],
}
SOCmeta["625"] = {
    "group_title": "Bed and breakfast and guest house owners and proprietors",
    "group_description": "Bed and breakfast and guest house owners and proprietors plan, organise and direct the activities of bed and breakfasts and guest houses.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6250"] = {
    "group_title": "Bed and breakfast and guest house owners and proprietors",
    "group_description": "Bed and breakfast and guest house owners and proprietors plan, organise, direct and co-ordinate the activities and resources bed and breakfasts and guest houses.",
    "entry_routes_and_quals": "No formal qualifications are required for entry. A range of relevant courses in hospitality and management are available.",
    "tasks": [
        "~welcomes and ensures physical comfort of residents/guests and makes special arrangements for children, the elderly and the infirm if required ~provides certain meals for guests ~maintains and cleans establishment ~determines financial, staffing, material and other short- and long-term needs ~markets business and finds new business ~arranges for payment of bills, keeps accounts and ensures adherence to licensing and other statutory regulations",
    ],
}
SOCmeta["63"] = {
    "group_title": "Community and civil enforcement occupations",
    "group_description": "Workers in this sub-major group assist the local police in patrolling the streets and tackling a range of crime and disorder problems and enforce parking regulations.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["631"] = {
    "group_title": "Community and civil enforcement occupations",
    "group_description": "Workers in Community and Civil Enforcement Occupations assist the local police in patrolling the streets and tackling a range of crime and disorder problems and enforce parking regulations.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["6311"] = {
    "group_title": "Police community support officers",
    "group_description": "Police Community Support Officers (PCSOs) support the local police force by patrolling the streets to provide a visible and reassuring presence and to tackle a range of crime and disorder problems. PCSOs are also attached to the British Transport Police who operate the specialised police service for the railway network across Britain.",
    "entry_routes_and_quals": "There are no formal educational requirements although entrants must pass written tests and undergo a medical check including an eyesight test. Nationality restrictions apply and background security checks will be made.",
    "tasks": [
        "~patrols a geographic area to monitor and deter criminal and anti-social activity and disorderly conduct ~assists police officers at crime scenes and major events ~carries out house-to-house enquiries ~provides crime prevention advice and helps to support victims of crime ~may detain someone pending the arrival of a police officer ~may direct traffic and arrange for vehicles to be removed",
    ],
}
SOCmeta["6312"] = {
    "group_title": "Parking and civil enforcement occupations",
    "group_description": "Parking and civil enforcement occupations patrol assigned areas to detect and prevent infringements of local parking regulations and control the parking of vehicles in public and private car parks.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Candidates should be at least 18 years of age (in some areas 20-25+) and may be required to pass a medical examination. Training is typically provided on-the-job.",
    "tasks": [
        "~patrols assigned area to detect vehicles parked in no-parking zones and vehicles parked in excess of permitted time in restricted parking zones ~warns offenders or issues tickets ~advises motorists on local parking facilities and directs them as required ~notes any cases of obstruction, evasion of tax or other infringement and reports them to the police ~gives evidence in court as required ~regulates entry/exit of vehicles to and from car parks and may park cars ~issues and examines tickets in car parks, collects charges and gives change",
    ],
}
SOCmeta["7"] = {
    "group_title": "Sales and customer service occupations",
    "group_description": "This major group covers occupations whose tasks require the knowledge and experience necessary to sell goods and services, accept payment in respect of sales, replenish stocks of goods in stores, provide information to potential clients and additional services to customers after the point of sale. The main tasks involve knowledge of sales techniques, a degree of knowledge regarding the product or service being sold, familiarity with cash and credit handling procedures and a certain amount of record keeping associated with those tasks. Most occupations in this major group require a general education and skills in interpersonal communication. Some occupations will require a degree of specific knowledge regarding the product or service being sold but are included in this major group because the primary task involves selling.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["71"] = {
    "group_title": "Sales occupations",
    "group_description": "Workers in this sub-major group sell goods and services in retail and wholesale establishments, accept payment in respect of sales, obtain orders and collect payments for goods and services from private households, replenish stocks of goods in stores, create displays of merchandise and perform other sales related occupations.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["711"] = {
    "group_title": "Sales assistants and retail cashiers",
    "group_description": "Sales assistants and retail cashiers sell goods and services in retail or wholesale establishments, accept payments, give change and arrange finance as appropriate in respect of sales obtain, receive and record telephone orders for goods and services.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["7111"] = {
    "group_title": "Sales and retail assistants",
    "group_description": "Sales and retail assistants demonstrate and sell a variety of goods and services in shops, stores, showrooms and similar establishments.",
    "entry_routes_and_quals": "No minimum academic qualifications are required although some employers may require GCSEs/S grades. Training is typically provided on-the-job. Vocational qualifications in Retail Operations and relevant apprenticeships are available at various levels.",
    "tasks": [
        "~discusses customer requirements, including type and price range of goods/services desired ~advises customer on selection, purchase, use and care of merchandise and quotes prices, discounts and delivery times ~advises customer making major purchase on credit terms and arranges finance as appropriate ~receives full or partial payment, checks validity of form of payment, writes or prints bill, receipt or docket and packages merchandise for customer ~arranges and replenishes goods on display stands, undertakes stock checks and assists with the receipt of deliveries from suppliers into the stock room ~handles returns and deals with customer complaints",
    ],
}
SOCmeta["7112"] = {
    "group_title": "Retail cashiers and check-out operators",
    "group_description": "Retail cashiers and check-out operators accept payments from customers and give change in respect of sales or services.",
    "entry_routes_and_quals": "There are no minimum academic requirements although some employers may require GCSEs/S grades or relevant experience. Training is typically provided on-the-job. Vocational Operations in Retail Operations are available at levels 1 and 2.",
    "tasks": [
        "~records cost of each item on cash register or by use of bar code reader and totals the amount to be paid ~receives cash, cheque or debit or credit card payment, checks validity of form of payment, gives change and issues receipts for purchase ~debits customer\u2019s account in respect of purchases or services ~monitors fuel taken by self-service customers or refuels vehicle if required ~maintains transaction records as requested",
    ],
}
SOCmeta["7113"] = {
    "group_title": "Telephone salespersons",
    "group_description": "Telephone salespersons obtain, receive, process and record telephone orders for goods and services.",
    "entry_routes_and_quals": "Academic qualifications may be required. Training is typically received on-the-job, supplemented by short courses in practical skills. NVQs/SVQs in Sales at levels 2 and 3 and apprenticeships are available.",
    "tasks": [
        "~learns about the product(s)/service(s) to be sold ~telephones potential customers, explains purpose of call, discusses their requirements and advises on the goods/services being offered ~quotes prices, credit terms and delivery conditions and records details of orders agreed ~receives orders for goods/services by telephone and records relevant details ~arranges despatch of goods and services, information and/or brochures to customers ~maintains record of sales statistics, customers contacted and changes to customer details",
    ],
}
SOCmeta["7114"] = {
    "group_title": "Pharmacy and optical dispensing assistants",
    "group_description": "Pharmacy and optical dispensing assistants work under the supervision of pharmacists and opticians or optometrists to dispense drugs and medicines, issue pre-packaged prescriptions, sell over-the-counter medication, dispense spectacles and contact lenses and other related products.",
    "entry_routes_and_quals": "Entrants usually possess GCSEs/S grades. Training is typically received on-the-job, supplemented by study towards vocational qualifications. NVQs/ SVQs are available in relevant areas and at various levels, and apprenticeships may be available.",
    "tasks": [
        "~checks received prescriptions for legality and accuracy and confirms patients\u2019 or customers\u2019 details ~maintains records of prescriptions received and drugs issued ~checks stock levels, rotates stock, orders new stock from supplying companies and ensures that products are stored appropriately ~arranges displays of merchandise ~relays information to customers under the direction of pharmacist and opticians or optometrists ~carries out sales transaction, wraps and packages goods",
    ],
}
SOCmeta["7115"] = {
    "group_title": "Vehicle and parts salespersons and advisers",
    "group_description": "Vehicle and parts salespersons and advisers sell new and used vehicles to the general public, and vehicle accessories and parts to garages, vehicle dealerships and the general public.",
    "entry_routes_and_quals": "There are no formal academic requirements for entry but some employers may ask for GCSEs and/or some previous relevant work experience. Apprenticeships may be available in some areas. Vehicle salespersons generally require a full, clean driving licence.",
    "tasks": [
        "~discusses customer\u2019s requirements, advises on most appropriate vehicle, explains its features and arranges test drive ~negotiates sale price including any \u2018trade-in\u2019 and extra accessories, works out finance arrangements and completes sales paperwork ~carries out pre-delivery inspection and formal hand-over of vehicle to customer ~updates stock record, orders new vehicles from manufacturer, buys in used cars ~receives orders for parts by phone, email or in person and checks availability on stock record ~obtains parts from store or orders from suppliers ~organises delivery of parts and handles payment ~orders new supplies, arranges storage and updates stock records",
    ],
}
SOCmeta["712"] = {
    "group_title": "Sales related occupations",
    "group_description": "Job holders in this minor group visit private households to obtain orders and collect payments, deliver and sell food, drink and other goods in streets and open spaces from portable containers, stalls and vans, collect and deliver laundered and similarly serviced articles, replenish and display stocks of merchandise, and undertake a variety of sales occupations not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["7121"] = {
    "group_title": "Collector salespersons and credit agents",
    "group_description": "Collector salespersons and credit agents visit private households to obtain orders and collect payments for goods and services.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is provided on-the-job and may be supplemented by specialist short courses provided by employers.",
    "tasks": [
        "~calls on household, explains purpose of call and displays or describes goods/services on offer ~emphasises main selling point of goods/services to stimulate customer interest ~quotes prices and terms, collects any payments and completes hire purchase or credit arrangements ~distributes advertising literature and sample goods ~makes follow-up calls to obtain further orders",
    ],
}
SOCmeta["7122"] = {
    "group_title": "Debt, rent and other cash collectors",
    "group_description": "Debt, rent and other cash collectors collect payments due or overdue from households and businesses and empty cash from prepayment meters or machines.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is typically provided on-the-job. This may be supplemented by specialised training courses within larger agencies. To become a bailiff, you will need to be certified, which includes an enhanced DBS check.",
    "tasks": [
        "~receives payment at centralised office or calls on household/business premises ~records details of transaction, issues receipt or annotates rent book ~reads gas, water and electricity meters ~cleans, services and fills vending machines and collects money from meters, vending machines and other cash operated machinery ~collects tolls from persons wishing to gain access to private roads, bridges, piers, etc. and operates tollgates to control entry ~remits cash, cheques or credit notes to cashier, supervisor or bank, building society or post office ~serves summonses and, on court authority, takes possession of goods to the value of outstanding debt",
    ],
}
SOCmeta["7123"] = {
    "group_title": "Roundspersons and van salespersons",
    "group_description": "Roundspersons and van salespersons deliver and sell food, drink and other goods by calling on householders or by selling from a mobile shop or van and call on households to collect and receive payment for laundered or similarly serviced articles.",
    "entry_routes_and_quals": "No academic qualifications are required but candidates should hold a clean driving licence. Off and on-the-job training is provided.",
    "tasks": [
        "~loads vehicle with food, drink, or articles that have been laundered, etc. ~drives vehicle over established route and parks at recognised stopping places or households ~calls at customers\u2019 premises and delivers ordered goods ~calls out, rings bell or otherwise attracts attention to the items on sale ~sells goods, records deliveries, takes further orders or articles requiring servicing and collects cash or prepares bill ~returns to depot and hands in unsold goods and cash",
    ],
}
SOCmeta["7124"] = {
    "group_title": "Market and street traders and assistants",
    "group_description": "Market and street traders and assistants sell goods (other than refreshments) from stalls, barrows and other portable containers in streets and market places.",
    "entry_routes_and_quals": "No academic qualifications are required.",
    "tasks": [
        "~displays products on stall or barrow ~calls out or otherwise attracts attention to goods on offer ~sells goods at fixed price or by bargaining with customer ~accepts payment and may wrap goods ~cleans up site on completion of each day\u2019s trading",
    ],
}
SOCmeta["7125"] = {
    "group_title": "Visual merchandisers and related occupations",
    "group_description": "Visual merchandisers develop, deliver and communicate visual concepts and strategies to promote brands, products and services in-store, in catalogues or online, and create displays of merchandise.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job, supplemented by short courses covering practical skills and details of the product or service being sold.",
    "tasks": [
        "~consults with advertising and sales staff and advises retailers on the optimal display of a product and of any promotions ~implements plans from display designers or display managers or develops ideas and plans for merchandise display or window dressing ~prepares an area for new display, constructs or assembles displays from a variety of materials, and dismantles existing displays and returns merchandise to relevant departments ~provides feedback about displays to managers and designers",
    ],
}
SOCmeta["7129"] = {
    "group_title": "Sales related occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of sales occupations not elsewhere classified in minor group 712: Sales Related Occupations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job, supplemented by short courses covering practical skills and details of the product or service being sold. NVQs/SVQs in sales are available at levels 2 and 3.",
    "tasks": [
        "~assesses characteristics of goods/services being sold and decides on main selling points ~advises clients and agents on insurance related problems, seeks new outlets for business and quotes premiums, bonus rates, tax concessions, etc. ~obtains orders for advertising, financial, catering, printing and transportation services ~organises parties in private households to sell clothing, fashion accessories, giftware and other goods ~provides demonstrations of a product within retail stores, exhibitions and trade fairs to promote interest amongst potential customers ~negotiates agreements for the passage of supply lines over or under land/property and the siting of supporting structures and other items",
    ],
}
SOCmeta["713"] = {
    "group_title": "Shopkeepers and sales supervisors",
    "group_description": "Job holders in this minor group co-ordinate, direct and undertake the activities involved in the running of small, independent retail and wholesale establishments and supervise the activities of sales and related workers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["7131"] = {
    "group_title": "Shopkeepers and owners - retail and wholesale",
    "group_description": "Shopkeepers and proprietors in this unit group co-ordinate, direct and undertake the activities in the running of small, independent retail and wholesale establishments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. A range of management and leadership courses in retail are available, in addition to NVQs/ SVQs in at levels 2, 3 and 4.",
    "tasks": [
        "~defines the market position for the business, decides what to sell, forecasts demand and develops the brand image of the business ~determines staffing, financial, material and other short- and long-term requirements ~oversees staff training, rotas and the allocation of work ~provides information about merchandise to staff and customers and ensures customer complaints are appropriately dealt with ~ensures that adequate reserves of merchandise are held and orders new stock as required ~maintains financial and other shop records and controls security arrangements for the premises ~authorises payment for supplies received and decides on vending price and credit terms ~examines quality of merchandise and ensures that effective use is made of advertising and display facilities",
    ],
}
SOCmeta["7132"] = {
    "group_title": "Sales supervisors - retail and wholesale",
    "group_description": "Sales supervisors oversee operations and directly supervise and coordinate the activities of sales and related workers in retail and wholesale establishments.",
    "entry_routes_and_quals": "No minimum academic qualifications are required although some employers may require GCSEs/S grades or A levels/H grades along with relevant work experience. Vocational qualifications in Retail Operations are available at levels 1 and 2, and apprenticeships may be available in some areas. Professional qualifications are relevant in some areas of selling and may be an advantage.",
    "tasks": [
        "~directly supervises and coordinates the activities of sales and related workers ~establishes and monitors work schedules to meet sales and productivity targets ~liaises with managers and other departments to resolve operational problems ~determines or recommends staffing and other needs to meet sales and productivity targets ~reports as required to managerial staff on departmental activities",
    ],
}
SOCmeta["72"] = {
    "group_title": "Customer service occupations",
    "group_description": "Customer service occupations receive and respond to enquiries regarding products or services, deal with customer complaints and perform a variety of tasks in the provision of additional services to customers after the point of sale; operate switchboards and receive and direct calls in a variety of establishments; operate telecoms equipment to transmit and receive messages; conduct market research interviews; and perform other customer service tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["721"] = {
    "group_title": "Customer service occupations",
    "group_description": "Workers in this minor group receive and respond to telephone and other enquiries regarding the products and services offered by an organisation, deal with customer complaints, and provide further services to customers after the point of sale.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["7211"] = {
    "group_title": "Call and contact centre occupations",
    "group_description": "Call and contact centre occupations receive and respond to telephone calls from potential clients and existing customers regarding the products and services offered by an organisation.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although many employers expect candidates to possess GCSEs/S grades. Training is typically provided on-the-job, supplemented by specialist short courses.",
    "tasks": [
        "~answers incoming telephone calls from existing or prospective customers ~interviews caller to establish the nature of any complaint or the requirements of the client ~informs existing and potential customers on any immediate action to be taken, and refers the matter to a more senior member of staff if necessary ~advises on services available and sells additional products or services ~maintains details of calls received, the action taken as a result of a call and updates customer database as required ~arranges for field staff to visit the caller if further assistance is required",
    ],
}
SOCmeta["7212"] = {
    "group_title": "Telephonists",
    "group_description": "Telephonists receive and direct callers in commercial, industrial and other establishments, and operate telephone (public) and office (private) switchboards to advise on, and assist with, making telephone calls and to relay incoming, outgoing and internal calls.",
    "entry_routes_and_quals": "Academic qualifications may not be required. On-the-job training is provided.",
    "tasks": [
        "~receives callers and directs them to appropriate person or department ~operates switchboard to connect outgoing calls or to relay incoming or internal calls ~reports any faults on telephone operating system ~gives advice on dialling and other special features available ~provides directory information, dialling codes and details of charges ~alerts emergency services in cases of fire, crime or accident",
    ],
}
SOCmeta["7213"] = {
    "group_title": "Communication operators",
    "group_description": "Communication operators operate telecoms equipment to transmit and receive signals and messages.",
    "entry_routes_and_quals": "Academic qualifications may not be required. On-the-job training is provided.",
    "tasks": [
        "~receives messages, weather reports and other material to transmit ~tunes transmitter to required channel or wavelength and relays or receives message to/ from person or vehicle ~uses a teleprinter or telex keyboard to transmit messages to other teleprinters or telexes ~keeps record of messages sent and received ~performs routine tests and maintenance on equipment and reports faults ~receives and handles incoming calls for emergency services, transmitting to the appropriate services",
    ],
}
SOCmeta["7214"] = {
    "group_title": "Market research interviewers",
    "group_description": "Market research interviewers conduct interviews to collect information on the opinions and preferences of consumers, businesses, the electorate and other selected groups.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. Relevant professional qualifications are available.",
    "tasks": [
        "~approaches members of the public, individuals, households and organisations to arrange and conduct face-to-face interviews, telephone interviews, focus groups, panel interviews etc. ~records progress of interviews by noting answers, completing questionnaires, making audio or visual recordings or inputting responses into a computer ~collects questionnaires, diaries, and other research materials left with interviewees and conducts follow-up interviews ~collates and reviews information collected and compiles reports to pass back to the organisation/individual commissioning the market research",
    ],
}
SOCmeta["7219"] = {
    "group_title": "Customer service occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of customer service occupations not elsewhere classified in minor group 721: Customer service occupations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although many employers expect candidates to possess GCSEs/S grades. Training is typically provided on-the-job, supplemented by specialist short courses.",
    "tasks": [
        "~receives enquiries from potential and existing clients, discusses requirements, and recommends products or services ~discusses pricing processes with clients, agrees payment arrangements and handles customer accounts ~makes reservations, books tickets, organises insurance policies on behalf of customers ~follows up clients to ensure their satisfaction with a product or service and to gain renewal of customer service agreements ~addresses customer complaints and problems ~informs customers of special promotions and new product launches",
    ],
}
SOCmeta["722"] = {
    "group_title": "Customer service supervisors",
    "group_description": "Customer service supervisors plan, organise and coordinate resources and supervise the staff involved in handling the requests, complaints and further needs of customers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["7220"] = {
    "group_title": "Customer service supervisors",
    "group_description": "Customer service supervisors oversee operations and directly supervise and coordinate the activities of a customer services team dealing with the responses, complaints or further requirements of purchasers and users of a product or service.",
    "entry_routes_and_quals": "There are no pre-set entry requirements. Candidates are recruited with a variety of academic qualifications and/or relevant experience. Specialist qualifications may be required for work within certain sectors.",
    "tasks": [
        "~directly supervises and coordinates the activities of a help and advisory services to provide support for customers and users ~liaises with clients and handles more complicated or sensitive complaints and queries ~develops and plans training for their teams ~establishes and monitors work schedules to meet the organisation's requirements ~discusses customer responses with managers with a view to improving the product or service provided and to resolve operational problems",
    ],
}
SOCmeta["8"] = {
    "group_title": "Process, plant and machine operatives",
    "group_description": "This major group covers occupations whose main tasks require the knowledge and experience necessary to operate and monitor industrial plant and equipment; to assemble products from component parts according to strict rules and procedures and to subject assembled parts to routine tests; and to drive and assist in the operation of various transport vehicles and other mobile machinery. Most occupations in this major group do not specify that a particular standard of education should have been achieved but will usually have a period of formal experience-related training. Some occupations require licences issued by statutory or professional bodies.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["81"] = {
    "group_title": "Process, plant and machine operatives",
    "group_description": "Process, plant and machine operatives operate and attend machinery to manufacture, process or otherwise treat foodstuffs, beverages, textiles, chemicals, glass, ceramics, rubber, plastic, metal, synthetic and other products, operate plant and machinery to produce paper, wood and related products, extract coal and other minerals from the earth, attend and operate power generation and water treatment systems, perform routine operations in the manufacture of motor vehicles, metal goods, electrical and electronic products, clothing and other goods, and perform a variety of tasks in relation to the construction and repair of buildings, public highways, underground piping systems, railway tracks and other structures.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["811"] = {
    "group_title": "Process operatives",
    "group_description": "Process operatives set, operate and attend machinery to bake, freeze, heat, crush, mix, blend and otherwise process foodstuffs, beverages and tobacco leaves, prepare natural and synthetic fibres for processing, spin and twist fibre into yarn, thread, twine, rope and other similar material, prepare colouring matter required for printing or dyeing fabrics, and produce or otherwise treat chemical, glass, ceramics, rubber, plastic, metal, synthetic and other products.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8111"] = {
    "group_title": "Food, drink and tobacco process operatives",
    "group_description": "Food, drink and tobacco process operatives set, operate and attend machinery to bake, freeze, heat, crush, mix, blend and otherwise process foodstuffs, beverages and tobacco leaves.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though some GCSEs/S grades can be an advantage. Off and on-the-job training is available. Vocational qualifications related to food and drink manufacturing, including apprenticeships, are available at up to level 3.",
    "tasks": [
        "~sets, operates and attends machinery and ovens to mix, bake and otherwise prepare bread and flour confectionery products ~operates machinery to crush, mix, malt, cook and ferment grains and fruits to produce beer, wines, malt liquors, vinegar, yeast and related products ~attends equipment to make jam, toffee, cheese, processed cheese, margarine, syrup, ice, pasta, ice-cream, sausages, chocolate, maize starch, edible fats and dextrin ~operates equipment to cool, heat, dry, roast, blanch, pasteurise, smoke, sterilise, freeze, evaporate and concentrate foodstuffs and liquids used in food processing ~mixes, pulps, grinds, blends and separates foodstuffs and liquids with churning, pressing, sieving, grinding and filtering equipment ~processes tobacco leaves by hand or machine to make cigarettes, cigars, pipe and other tobacco products",
    ],
}
SOCmeta["8112"] = {
    "group_title": "Textile process operatives",
    "group_description": "Textile process operatives operate machines to prepare natural and synthetic fibres for processing, spin and twist fibre into yarn, thread, twine, rope and other similar material, and estimate the quantities of colouring matter required for printing and dyeing fabrics.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/ SVQs relating to textile manufacture at levels 2 and 3 and apprenticeships are available.",
    "tasks": [
        "~sets controls, starts machinery and monitors the passage of material processed ~replenishes the supply of input fibres, removes and replaces full output packages, cards and spools ~detects blockages, tangled thread, defective or broken material, and joins broken ends by hand or mechanical knotting ~checks quality of completed material, marks any flaws and removes badly damaged sections ~examines colour cards or specifications, estimates quantity of colouring material needed to print or dye fibre and calculates and mixes ingredients accordingly ~stretches, shrinks, brushes, dampens and presses fabric and shears or burns off protruding fabric fibres as required ~cleans and oils machine, detects and reports mechanical faults to technicians",
    ],
}
SOCmeta["8113"] = {
    "group_title": "Chemical and related process operatives",
    "group_description": "Chemical and related process operatives operate machinery in the processing of chemical and related materials by chemical, heat or other treatment, manufacture synthetic materials and bleach, dye or otherwise treat textiles, and treat hides, skins and pelts for making into fur, leather and skin products.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers require entrants to possess GCSEs/S grades. Training is typically received on-the-job, supplemented by specialised training courses. Vocational qualifications in Process Technology at levels 2 and 3 and apprenticeships are available.",
    "tasks": [
        "~loads prescribed quantities of ingredients into plant equipment, starts operational cycle, monitors instruments and gauges indicating conditions affecting the operation of the plant and adjusts controls as necessary ~prepares dye, bleaching, water repellent, fixing salt and other chemical solutions to finish and treat textiles ~regulates input of polymer into melting unit, extrudes polymer, gathers extruded filaments and feeds strands through rolling, cutting and treatment units to produce synthetic fibre ~operates kilns, furnaces and ovens to produce charcoal, coke and other carbon products ~operates machines to coat film and tape with sensitising material and otherwise impregnate materials by immersion, split and mould mica and produce asbestos pipes and sheets ~cuts and trims skins, hides and pelts, removes wool, hair, flesh and other waste material, and washes, limes, tans, dyes and otherwise treats hides for making into leather, skin and fur products ~withdraws samples for quality control testing, removes and regulates discharge of batch material upon completion of processing",
    ],
}
SOCmeta["8114"] = {
    "group_title": "Plastics process operatives",
    "group_description": "Plastics process operatives attend and operate moulding, extruding, thermoforming, calendering, covering, cutting and other process equipment to make and repair plastic products.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job, supplemented by specialised courses. NVQs/SVQs in Performing Manufacturing Operations at levels 1 and 2 and apprenticeships are available.",
    "tasks": [
        "~prepares machine for operation by affixing any necessary attachments ~weighs and mixes ingredients, loads machine with plastic to be worked or regulates flow from feed conveyor or hopper ~monitors controls regulating temperature, pressure, etc. and operates moulding, extruding, calendering, thermoforming and covering machines ~inspects plastic products for defects, takes measurements and repairs plastic belting and sheathing ~trims, cuts and performs other finishing operations on plastic using hand and machine tools ~makes artificial eyes and contact lens discs, and makes and repairs spectacle frames and plastic parts of artificial limbs and other orthopaedic appliances",
    ],
}
SOCmeta["8115"] = {
    "group_title": "Metal making and treating process operatives",
    "group_description": "Metal making and treating process operatives operate furnaces, ovens and other heating vessels, drawing, rolling, extruding, galvanising, forging and other metal processing equipment to smelt, shape, coat and treat metal and metal products.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. Vocational qualifications at level 2 and 3 in relevant areas, including metal and materials processing and finishing. are available.",
    "tasks": [
        "~charges furnace, operates controls to regulate furnace temperature, and adds oxidising, alloying and fluxing agents as required ~withdraws samples of molten metal for analysis, taps slag from surface of molten metal and directs flow of molten metal into casts ~sets rolling speed, tension and space between rolls, guides the metal to and from rollers, and monitors the rolling process to detect irregularities, and ensure that the gauge and finish match required specifications ~operates equipment to remove dirt, scale and other surface impurities by immersion in chemical solution ~heats metal or metal articles in furnace, allows to cool for a specified time or quenches in brine, oil or water to harden, reduces brittleness and restores ductility ~operates piercing, extruding, pressing and other metal processing equipment to shape and treat metal or metal articles ~coats metal parts and articles electrolytically, forms metal articles by electro- and vacuum-deposition, dips and sprays articles with another metal, plastic powder or material and treats articles chemically to produce desired finishes",
    ],
}
SOCmeta["8119"] = {
    "group_title": "Process operatives n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of processing occupations not elsewhere classified in minor group 811: Process operatives.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though some employers may expect entrants to possess GCSEs/S grades. Training is typically provided on-the-job, supplemented by specialist training courses. NVQs/SVQs in Performing Manufacturing Operations are available at levels 1, and 2.",
    "tasks": [
        "~packs products ready for kiln setting ~operates kilns, furnaces and ovens to produce cement clinker, linoleum cement and asphalt, to fire abrasive and carbon products, to make and treat glass and ceramic items, and otherwise cook and heat treat materials and products not elsewhere classified ~operates masticating, calendaring, mixing, forming, shaping, moulding, extruding, cutting, trimming and winding machines to make and repair rubber products ~operates machines to mix, blend, crush, wash and separate seeds and other materials not elsewhere classified ~operates machines to produce flat and corrugated asbestos cement pipes and sheets ~performs other processing tasks not elsewhere classified",
    ],
}
SOCmeta["812"] = {
    "group_title": "Metal working machine operatives",
    "group_description": "Workers in this minor group operate machines to cut, shape, abrade and otherwise machine metal use hand and power tools to remove surplus metal and rough surfaces from castings, forgings or other metal parts, and clean, smooth and polish metal workpieces.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8120"] = {
    "group_title": "Metal working machine operatives",
    "group_description": "Metal working machine operatives operate machines to cut, shape, abrade and otherwise machine metal, use hand and power tools to remove surplus metal and rough surfaces from castings, forgings or other metal parts, and clean, smooth and polish metal workpieces.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job. NVQs/SVQs in Mechanical Manufacturing Engineering are available.",
    "tasks": [
        "~secures workpiece in drilling, boring, milling, planing, grinding, lapping, honing, electrochemical, or other shaping machines, or loads metal stock on to press ~sets controls, starts machine and operates controls to feed tool to workpiece or vice versa and repositions workpiece during machining as required ~withdraws workpiece and examines accuracy using measuring instruments ~operates burning, chipping and grinding equipment to remove defects from metal parts, and files, chisels, burns and saws off surplus metal ~smooths rough surfaces with hand tools, abrasive belts and wheels, compressed air, jets of vapour, or blasting with shot, grit, sand or other abrasive material ~selects and secures polishing head to machine tool, prepares head with emery, grease or other substance, sets speed and angle of polishing head, and operates controls to feed polishing head to workpiece or vice versa",
    ],
}
SOCmeta["813"] = {
    "group_title": "Plant and machine operatives",
    "group_description": "Workers in this minor group operate plant and machinery to produce paper, wood and related products, operate drilling and excavating equipment to extract coal and other minerals, attend and operate boilers, compressors, turbines, electrical substations and other power generation equipment, operate machinery to cut, shape and finish metal, operate and attend water purifying, sedimentation and sewerage systems, and perform other miscellaneous operative tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8131"] = {
    "group_title": "Paper and wood machine operatives",
    "group_description": "Paper and wood machine operatives operate machines to treat and cut wood, to produce, treat and cut paper, paperboard, leatherboard, plasterboard and similar material, and to assemble and make wooden crates and containers.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/ SVQs/vocational qualifications in Fibreboard Operations at levels 2 and 3, and apprenticeships are available. NVQs/SVQs/vocational- qualifications in Wood Machining are available at levels 2.",
    "tasks": [
        "~cuts and shapes wood using hand and power tools, assembles parts of wooden crates, barrels and other wooden containers using nails, bolts and staples, and fits metal strips and corner pieces to strengthen container as required ~examines job requirements, ascertains necessary ingredients and loads machines to beat, mix and crush wood, cork and pulp for further processing ~attends and operates ovens, kilns, milling, filtering, straining, calendering, coating, drying, finishing, winding and other machines to produce and/or treat wood, paper, paperboard, leatherboard and plasterboard ~sets and adjusts edge guides, stops and blades of cutting machine, threads material through rollers or loads into machine hopper, starts and monitors operation of machine, removes completed work and clears machine of waste material",
    ],
}
SOCmeta["8132"] = {
    "group_title": "Mining and quarry workers and related operatives",
    "group_description": "Quarry workers erect supports in underground workings, set and detonate explosives to loosen rocks and set up and operate drilling equipment to extract coal and other minerals from the ground, and operate machinery to wash, crush or separate stone and ores.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/ SVQs in land drilling operations at level 2 and processing operations (extractive industries) at level 3 are available. There is a minimum age limit of 18 for underground work.",
    "tasks": [
        "~inspects blasting area, drills shot holes, inserts explosives and detonates charges to loosen large pieces of rock, coal or ore ~assembles drilling and cutting tools, operates controls to start machines and to regulate the speed and pressure of cutting and drilling ~erects timber or metal supports to shore up tunnel and assists tunnel miner with the excavation of vertical shafts and underground tunnels ~operates heading, ripping and cutting-loading machines to remove material from working face and monitors conveyor carrying away loose material ~conveys goods and materials to and from the workface, loads and unloads mine cars and transfers materials from underground and surface conveyors to bunkers, tubs and rail trucks ~operates agitators/vibrators to separate minerals and ensures that screened, filtered, crushed and separated material is discharged to appropriate chutes or conveyors ~performs other mining and quarrying tasks not elsewhere classified including digging clay from open pits, operating high-pressure hoses to wash china clay from open pit faces and otherwise assisting miners",
    ],
}
SOCmeta["8133"] = {
    "group_title": "Energy plant operatives",
    "group_description": "Energy plant operatives operate boilers to produce hot water or steam and attend and operate compressors, turbines, electrical substations, switchboards and auxiliary plant and machinery to fuel nuclear reactors, drive blowers and pumps, electricity generators and other equipment.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically by apprenticeship, incorporating technical training and practical experience. NVQs/ SVQs in Electrical Power Engineering at levels 2 and 3 and apprenticeships are available.",
    "tasks": [
        "~determines job requirements from switchboard attendant or operating instructions ~opens valves and operates controls to regulate the flow of fuel to boiler or generating equipment ~operates remote control panel to load fuel and remove discharged fuel elements from nuclear reactors ~adjusts controls to maintain correct running speed of turbine or generator and monitors temperature and pressure controls on boilers ~records instrument readings periodically and shuts down turbine/generator or boiler as demand decreases ~carries out minor maintenance tasks and prescribed tests and reports any faults",
    ],
}
SOCmeta["8134"] = {
    "group_title": "Water and sewerage plant operatives",
    "group_description": "Water and sewerage plant operatives operate valves to control water supplies in mains and pipelines, attend screening, filtering, water purifying and sedimentation plant, clear any blockages and patrol and maintain sewerage systems.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is provided Off and on-the-job. NVQs/ SVQs in Operating Process Plant are available at level 2.",
    "tasks": [
        "~attends water filtration and purification plant, monitors chemical treatment and regulates treatment of water supply within strict guidelines ~opens and closes valves to regulate quantity and pressure of water and reports defective valves or abnormal water pressure ~stops water supply in an emergency and informs consumers likely to be affected ~regulates flow of raw sewage into screening plant, releases screened sewage and regulates its flow into detritus pits, sedimentation tanks and filtration beds ~cleans out screen compartments, sedimentation tanks and filtration beds manually or using mechanical scraper ~patrols sections of sewer, examines for any blockages or gas releases and clears blockages by flushing or by using boring rods ~digs trench and assists pipe layers to lay, renew or repair sewerage pipes",
    ],
}
SOCmeta["8135"] = {
    "group_title": "Printing machine assistants",
    "group_description": "Printing machine assistants set and operate letterpress, platen or cylinder, lithographic and photogravure printing machines, photocopiers, office printers, duplication machines and other reprographic equipment.",
    "entry_routes_and_quals": "No academic qualifications are required. Off and on-the-job training is provided. NVQs/SVQs in Screen Printing are available at levels 1 and 2, and in Machine Printing at levels 2 and 3.",
    "tasks": [
        "~positions printing plates, loads inks into reservoirs and loads paper rolls or sheets into printing press ~sets controls to control the speed, pressure and ink flow of printing machine ~loads photocopiers, office printers, duplication machines and other reprographic equipment with stationery ~starts reprographic or printing machine and monitors operation for paper misfeeds and error messages, removes blockages and replaces damaged paper, and monitors quality of output ~carries out routine maintenance and cleaning of printing machine ~sets and operates machines for cutting paper to specified dimensions or for folding or binding to produce finished paper items ~sets and operates presses for stamping patterns and labels on textiles, clothing, pottery, footwear and other leather goods",
    ],
}
SOCmeta["8139"] = {
    "group_title": "Plant and machine operatives n.e.c.",
    "group_description": "Job holders in this unit group operate a variety of plant and machinery not elsewhere classified in minor group 813: Plant and machine operatives.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/ SVQs are available in some areas.",
    "tasks": [
        "~operates acetylene torches and other cutting equipment to dismantle boilers, cars, ships, railway track, engines, machinery and other scrap metal ~bends, coils, crimps and spins metal wires in the manufacture of cables, springs, ropes and other wire goods ~operates machines in the manufacture of nuts, bolts, nails, screws, pins, rivets, etc. ~fills grease gun with grease of appropriate grade, and applies grease or oil to grease points or lubrication holes in machinery or equipment and over bearings, axles and other similar parts ~ensures that rollers in rope haulage system are well greased and running freely ~inspects machines and equipment, and reports any faults",
    ],
}
SOCmeta["814"] = {
    "group_title": "Assemblers and routine operatives",
    "group_description": "Assemblers and routine operatives perform routine tasks in the wiring of electrical and electronic equipment, assembly of prepared parts in the manufacture of vehicles, metal and other goods, inspect, test, sort, weigh and grade products, parts and materials, fit and repair tyres, exhausts and windscreens on motor vehicles, sew and embroider garments, and perform a variety of other routine assembly operations not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8141"] = {
    "group_title": "Assemblers (electrical and electronic products)",
    "group_description": "Assemblers (electrical and electronic products) wire prepared parts and/or sub-assemblies in the manufacture of electrical and electronic equipment, make coils and wiring harnesses and assemble previously prepared parts in the batch or mass production of electrical and electronic goods and components",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job, supplemented by short courses. NVQs/SVQs in Electronic Product Assembly are available at level 1.",
    "tasks": [
        "~examines drawings, specifications and wiring diagrams to identify appropriate materials and sequence of operations ~selects, cuts and connects wire to appropriate terminals by crimping or soldering ~positions and secures switches, transformers, tags, valve holders or other parts and connects capacitors, resistors, transistors or sub-assemblies to appropriate terminals by soldering ~lays out and secures wire to make harnesses and operates machine to wind heavy and light coils of wire or copper for transformers, armatures, rotors, stators and light electrical equipment ~assembles previously prepared electrical or electronic components by winding, bolting, screwing or otherwise fastening using an assembly machine or hand tools",
    ],
}
SOCmeta["8142"] = {
    "group_title": "Assemblers (vehicles and metal goods)",
    "group_description": "Assemblers (vehicles and metal goods) undertake the routine assembly of vehicles and other metal goods or components such as frames, axles, wire brushes and wheels.",
    "entry_routes_and_quals": "No academic qualifications are required. In some cases candidates must take aptitude and dexterity tests. Normal colour vision is required for some jobs. Training varies according to the complexity of the work.",
    "tasks": [
        "~follows instructions and drawings and positions components on work bench or in assembly machine ~assembles prepared components in sequence by soldering, bolting, fastening, spot-welding, screwing and hammering using power and hand tools or assembly machine ~rejects faulty assembly components ~inspects finished article for faults, monitors assembly machine operation and reports any faults",
    ],
}
SOCmeta["8143"] = {
    "group_title": "Routine inspectors and testers",
    "group_description": "Routine inspectors and testers inspect and/or test metal stock, parts and products, electrical plant, machinery and electronic components, systems and sub-assemblies, textiles, wood, paper, food, plastics and rubber goods, parts and materials to detect processing, manufacturing and other defects.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers require candidates to possess GCSEs/S grades. Training is typically received on-the-job, supplemented by training courses where instruction in specific techniques is required. Various NVQs/SVQs encompass aspects of quality control.",
    "tasks": [
        "~examines articles for surface flaws such as cracks, dents, defective sealing or broken wires by visual inspection or using aids such as microscopes or magnifying glasses ~checks sequence of assembly operations and checks assemblies and sub-assemblies against parts lists to detect missing items ~sets up test equipment, connects items/system to power source/pressure outlet, etc. and operates controls to check performance and operation of electrical plant and machinery and electronics systems ~examines yarn packages, textile fabrics and garments, wood or wood products, paper and paperboard, plastics and rubber materials, food products, food storage containers, etc., checks specifications, marks any repairable defects and rejects faulty items ~reports any recurrent or major defects and recommends improvements to production methods",
    ],
}
SOCmeta["8144"] = {
    "group_title": "Weighers, graders and sorters",
    "group_description": "Weighers, graders and sorters weigh, grade and sort materials, goods and products.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job, supplemented by short courses relating to the specific material or product being considered.",
    "tasks": [
        "~examines hide, skins, leather, fabric, wool, rags, scrap metal, tobacco pipe bowls, fish, fibres, ceramics, produce and other goods ~assesses product quality visually and by touch, and grades according to weight, thickness, colour and other quality criteria ~ascertains material(s) required from order card, recipe, or specification and weighs and measures prescribed quantities accordingly ~uses balances, springs, weighing platforms, automatic scales and weighbridges to check the weight of goods, products and loaded vehicles ~records and calculates gross and net weight, checks delivery notes and prepares documents and labels for identification purposes ~operates machines to measure lengths of rolls of material and irregularly shaped materials such as leather or sheepskin",
    ],
}
SOCmeta["8145"] = {
    "group_title": "Tyre, exhaust and windscreen fitters",
    "group_description": "Tyre, exhaust and windscreen fitters fit, repair and adjust tyres, exhausts and windscreens on cars, buses, motorcycles and other motor vehicles.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job, or through training programmes within larger companies. NVQs/SVQs in vehicle maintenance (service replacement) are available at levels 1 and 2.",
    "tasks": [
        "~carries out inspection and assesses the nature and extent of repair necessary ~removes wheel, exhaust or windscreen using semi-automatic machinery or hand and power tools ~separates tyre from wheel and fits replacement tyre using automatic machine or by using a wheel stand and hand tools ~inflates tyre to correct pressure, refits wheel to axle and balances wheel using balancing machine ~replaces faulty parts of exhaust and refits exhaust or windscreen to vehicle",
    ],
}
SOCmeta["8146"] = {
    "group_title": "Sewing machinists",
    "group_description": "Sewing machinists sew and finish garments by hand or machine, rectify faults in manufactured textile goods and repair worn and damaged garments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is received Off and on-the-job. NVQs/ SVQs are available at levels 1 and 2.",
    "tasks": [
        "~operates standard and specialised machines to sew, finish and repair garments and other textile, fabric, fur and skin products ~examines fabrics of all types to identify imperfections and determine best method of repair ~performs hand sewing tasks in the making, trimming and finishing of fur, sheepskin, leather, upholstery, mats, carpets, umbrellas and other textile products ~embroiders decorative designs on textiles with machine stitching ~routinely cleans and oils machine and reports or remedies any mechanical faults",
    ],
}
SOCmeta["8149"] = {
    "group_title": "Assemblers and routine operatives n.e.c.",
    "group_description": "Job holders in this unit group perform assembly and routine operative tasks not elsewhere classified in minor group 814: Assemblers and routine operatives.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though some employers may require GCSEs/S grades. Some employers may set dexterity and aptitude tests for entrants. Normal colour vision may be required for some posts. NVQs/SVQs at levels 1, 2 and 3 are available in a variety of areas.",
    "tasks": [
        "~follows instructions and drawings and positions components on work bench or in assembly machine ~assembles prepared components in sequence by soldering, bolting, fastening, spot-welding, screwing, nailing, stapling, dipping and fastening using power and hand tools or assembly machine ~rejects faulty assembly components, inspects finished article for faults, monitors assembly machine operation and reports any faults ~applies enamel to jewellery and coats, lacquers, dips and touches up articles (other than ceramic) ~sets up and operates machines to apply colour to wallpaper and to coat articles (other than ceramic) with paint, cellulose or other protective/ decorative material ~performs miscellaneous painting and coating tasks not elsewhere classified including, staining articles, applying transfers, operating French polishing machines, removing surplus enamel from components and marking design outlines on articles",
    ],
}
SOCmeta["815"] = {
    "group_title": "Construction operatives",
    "group_description": "Construction operatives erect and dismantle scaffolding and working platforms, maintain tall structures, construct and maintain public highways and railway tracks, lay and repair underground piping systems, and perform a variety of tasks in relation to the construction, maintenance, repair and demolition of buildings.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8151"] = {
    "group_title": "Scaffolders, stagers and riggers",
    "group_description": "Scaffolders, stagers and riggers erect and dismantle scaffolding and working platforms, set up lifting equipment and ships\u2019 rigging, maintain and repair steeples, industrial chimneys and other tall structures and install, maintain and repair ropes, wires and cables.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is initially received on-the-job. Skilled workers must obtain Construction Skills recognised scaffolders record scheme cards through the completion of approved courses and further work experience. NVQs/SVQs in Scaffolding are available at levels 2 and 3.",
    "tasks": [
        "~examines drawings and specifications to determine job requirements ~examines scaffold tubing and couplings for defects and selects, fits and bolts scaffold tubes until scaffolding reaches required height ~lays and secures wooden planking to form working platforms and fixes guard rails, ladders, cradles and awnings as required ~erects jib, derrick and similar hoisting equipment and installs ropes, pulleys and other lifting tackle ~forms rope slings, ladders, netting and other rigging and measures, cuts and repairs wire or fibre rope",
    ],
}
SOCmeta["8152"] = {
    "group_title": "Road construction operatives",
    "group_description": "Road construction operatives construct, repair and maintain roads and lay paving slabs and kerbstones to form pavements and street gutters.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is typically provided on-the-job. All sites are required to have a \u2018trained operative\u2019 registered with the Street Workers Qualification Register. Trained operatives are required to attend accredited assessment centres. NVQs/SVQs in Highway Maintenance and Road Building are available at levels 1 and 2.",
    "tasks": [
        "~inspects road surfaces for hazards or signs of deterioration, clears mud, weeds and debris from road and spreads grit or salt as required ~sets up traffic management systems around work site such as cones, lights and barriers ~cuts away broken road surface with pick or pneumatic drill ~heats bitumen in bucket, applies it to newly laid asphalt and beats or draws tamper head on asphalt to close joints ~spreads bitumen, tar or asphalt and compacts surface using roller ~spreads aggregate over road surfaces using shovel, lays markings on road surface and repairs crash barriers ~removes damaged paving slabs and kerb stones, lays bedding of sand, concrete or mortar on prepared foundation, lays new slabs or stones and fills joints with mortar",
    ],
}
SOCmeta["8153"] = {
    "group_title": "Rail construction and maintenance operatives",
    "group_description": "Rail construction and maintenance operatives lay, re-lay, repair and examine railway track and maintain surrounding areas.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Off and on-the-job training is provided. NVQs/SVQs in Rail Engineering and apprenticeships at levels 2 and 3 are available.",
    "tasks": [
        "~patrols length of track and visually inspects rails, bolts, fishplates and chairs for distortion or fracture ~checks tightness of bolts and wedges, replaces damaged rail chairs and repacks ballast under sleepers if necessary ~lubricates points, examines fences, drains, culverts and embankments and carries out any necessary maintenance ~spreads ballast and lays sleepers or metal plates at specified intervals ~positions lengths of rail, sets of points and crossovers and secures rail with bolts, wooden wedges or clips ~fastens together sections of rail by bolting fishplates to rails",
    ],
}
SOCmeta["8159"] = {
    "group_title": "Construction operatives n.e.c.",
    "group_description": "Job holders in this unit group operate insulating equipment, fix plasterboard to ceilings and walls, help construct, maintain, repair and demolish buildings and clean and resurface eroded stonework, lay, join and examine pipe sections for drainage, gas, water or similar piping systems, install lighting systems in roads, domestic and commercial settings and carry out a variety of other construction operative tasks not elsewhere classified in minor group 815: Construction operatives.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/SVQs in Building and Construction at levels 1, 2 and 3 and apprenticeships in some areas are available.",
    "tasks": [
        "~fills machine with insulating mixture, positions hose, drills access hole and fills cavities or coats surfaces to prevent loss or absorption of heat and provide fire protections ~cuts, shapes and fits wood, lays bricks and tiles, cleans exterior surfaces of buildings and resurfaces eroded stone or brickwork, and performs other tasks in the construction, alteration, repair and demolition of buildings ~selects appropriate asbestos, clay, concrete, plastic or metal pipe sections and lowers them into prepared trenches using hoisting equipment ~joints pipe by sealing with rubber, cement, lead, etc., connects piping to manholes and attaches pipe junctions as required ~tests joints with electronic test equipment or by filling piping with water, smoke or compressed air ~installs electrical lighting in streets, homes and business/manufacturing settings",
    ],
}
SOCmeta["816"] = {
    "group_title": "Production, factory and assembly supervisors",
    "group_description": "Supervisors in this unit group oversee operations and directly supervise and coordinate the activities of workers involved in the production, manufacture and assembly of goods.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8160"] = {
    "group_title": "Production, factory and assembly supervisors",
    "group_description": "Production, factory and assembly supervisors oversee operations and directly supervise and coordinate the technical and operational work of those carrying out production, manufacturing and assembly roles.",
    "entry_routes_and_quals": "Academic qualifications may not be required but relevant experience is necessary, and some GCSEs/S grades or an equivalent academic or vocational qualification may be an advantage. Apprenticeships combining practical work experience and technical training are available in some areas.",
    "tasks": [
        "~directly supervises and coordinates the activities of production, manufacturing and assembly staff ~establishes and monitors work schedules to meet the organisation\u2019s requirements ~liaises with managers and other senior staff to resolve operational problems ~determines or recommends staffing and other needs to meet the organisation\u2019s requirements ~reports as required to managerial staff on work-related matters",
    ],
}
SOCmeta["82"] = {
    "group_title": "Transport and mobile machine drivers and operatives",
    "group_description": "Transport and mobile machine drivers and operatives drive motor vehicles to transport goods and people; drive trains and guide and monitor the movement of rail traffic; operate mechanical equipment on board boats, ships and other marine vessels; assist in the boarding, fuelling and movement of aircraft at airports; operate lifting, earth moving and earth surfacing equipment, agricultural equipment and other mobile machinery.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["821"] = {
    "group_title": "Road transport drivers",
    "group_description": "Road transport drivers collect, transport and deliver goods in Heavy Goods Vehicles (HGVs) and Large Goods Vehicles (LGVs), other lorries and vans, drive road passenger carrying vehicles, and instruct people learning to drive cars and other vehicles.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8211"] = {
    "group_title": "Heavy and large goods vehicle drivers",
    "group_description": "HGV and LGV drivers collect, transport and deliver goods in rigid vehicles over 7.5 tonnes, articulated lorries and lorries pulling trailers.",
    "entry_routes_and_quals": "No formal academic entry qualifications are required. The HGV/LGV test incorporates a medical examination, theory test and assessed road driving. HGV/LGV drivers of vehicles of 3.5 tonnes and over require a Driver CPC (Certificate of Professional Competence). The minimum age for HGV/LGV driving after obtaining the qualification is 18 years. NVQs/SVQs, other vocational courses and apprenticeships relevant to this occupation are available at various levels.",
    "tasks": [
        "~checks tyres, brakes, lights, oil, water and fuel levels and general condition of the vehicle ~drives vehicle from depot to loading/unloading point ~agrees delivery schedule and route with transport management ~assists with loading/unloading and ensures that load is evenly distributed and safely secured ~drives vehicle to destination in accordance with schedule ~maintains records of journey times, mileage and hours worked ~undertakes minor repairs and notifies supervisor of any mechanical faults",
    ],
}
SOCmeta["8212"] = {
    "group_title": "Bus and coach drivers",
    "group_description": "Bus and coach drivers drive road passenger-carrying vehicles such as buses, coaches and mini-buses.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though candidates must be in possession of a full car driving licence. All bus and coach drivers are required to hold the Driver Certificate of Professional Competence (CPC). This incorporates a theoretical examination and assessed driving. Entrants to the CPC test must be at least 18 years old. NVQs/SVQs in Road Passenger Vehicle Driving are available at level 2.",
    "tasks": [
        "~checks tyres, brakes, lights, oil, water and fuel levels and general condition of the vehicle before start of journey ~drives single- and double-decked vehicle over pre-determined route, complying with traffic regulations and keeping to time schedule ~stops and opens and closes doors at pre-arranged places to allow passengers to board and alight, observing regulations concerning the number of passengers carried ~may collect fares from passengers and issue tickets or ensure that they use a ticket machine ~may plan routes in conjunction with private hirer and assist with loading and unloading of luggage ~balances cash taken with tickets sold and may be responsible for cleanliness of vehicle ~maintains records of journey times, mileage and hours worked",
    ],
}
SOCmeta["8213"] = {
    "group_title": "Taxi and cab drivers and chauffeurs",
    "group_description": "Taxi and cab drivers and chauffeurs drive motor cars for private individuals, government departments and industrial and commercial organisations, drive taxis for public hire, drive new cars to delivery points and drive motorcycles and other motor vehicles.",
    "entry_routes_and_quals": "No academic qualifications are required but most entrants require a clean, current driving licence and a medical examination. Local authorities typically set their own tests of local knowledge and additional driving tests before awarding licences.",
    "tasks": [
        "~checks tyres, brakes, lights, oil, water and fuel levels and general condition of vehicle before start of journey ~drives passenger-carrying motor cars, taxis and other motor cars and motorcycles, complying with road and traffic regulations ~collects passengers when hailed or in response to telephone/radio message and helps them to secure their luggage ~conveys passenger to destination and helps unload luggage ~cleans, services and maintains vehicle or motorcycle",
    ],
}
SOCmeta["8214"] = {
    "group_title": "Delivery drivers and couriers",
    "group_description": "Delivery drivers and couriers collect, transport and deliver goods using a range of vehicles, including bicycles and motor vehicles up to 7.5 tonnes in weight.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Entrants must possess a clean car driving licence. In order to drive vehicles between 3.5 and 7.5 tonnes, entrants must pass an additional test for a category C1 licence. Minimum age restrictions apply according to the weight of vehicle and whether the driver holds a Driver CPC (Certificate of Professional Competence). NVQs/SVQs in relevant areas and at various levels are available.",
    "tasks": [
        "~checks tyres, brakes, lights, oil, water and fuel levels and general condition of the vehicle ~drives vehicle from depot to loading/unloading point ~assists with loading/unloading and obtains receipts from customers for goods collected/delivered ~drives vehicle to destination in accordance with schedule ~maintains records of journey times, mileage and hours worked ~undertakes minor repairs and notifies supervisor of any mechanical faults",
    ],
}
SOCmeta["8215"] = {
    "group_title": "Driving instructors",
    "group_description": "Driving instructors co-ordinate and undertake the instruction of people learning to drive cars, motorcycles, buses, fork-lifts and haulage vehicles.",
    "entry_routes_and_quals": "There are no formal academic requirements. Candidates must have held a current driving licence for four out of the last six years, have no motoring or criminal convictions and be over 21 years old. To gain registration as an Approved Driving Instructor, entrants must pass a three-part examination. Instructors for Large Goods Vehicles (LGVs), Passenger Carrying Vehicles (PCVs) and Fork-lifts are trained internally or at specialist training establishments.",
    "tasks": [
        "~checks instruction and learning standards and discusses teaching plans with other instructors ~plans lessons in accordance with the needs and abilities of individual pupils ~explains driving techniques and assists pupil with difficulties ~familiarises pupil with the Highway Code and different road and traffic conditions ~advises pupil when to apply for theoretical and practical driving tests and familiarises them with test procedures and standards",
    ],
}
SOCmeta["8219"] = {
    "group_title": "Road transport drivers n.e.c.",
    "group_description": "Job holders in this unit group drive other transport vehicles in roles not classified elsewhere in minor group 821: Road transport drivers.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Entrants must possess a clean car driving licence. In order to drive vehicles between 3.5 and 7.5 tonnes, entrants must pass an additional test for a category C1 licence. Minimum age restrictions apply according to the weight of vehicle and whether the driver holds a Driver CPC (Certificate of Professional Competence). NVQs/SVQs in relevant areas and at various levels are available.",
    "tasks": [
        "~drives vehicle to destination in accordance with schedule ~checks tyres, brakes, lights, oil, water and fuel levels and general condition of the vehicle ~maintains records of journey times, mileage and hours worked ~undertakes minor repairs and notifies supervisor of any mechanical faults",
    ],
}
SOCmeta["822"] = {
    "group_title": "Mobile machine drivers and operatives",
    "group_description": "Workers in this minor group drive and operate earth moving and surfacing equipment, cranes, power driven hoisting machinery, fork-lift trucks, tractor driven and other agricultural machinery, and operate other mobile machines not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8221"] = {
    "group_title": "Crane drivers",
    "group_description": "Crane drivers supervise and undertake the operation of cranes, jib cranes, power driven hoisting machinery and power driven stationary engines to raise and lower mine and other cages, and to lift and move equipment, materials, machinery and containers.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though GCSEs/S grades are advantageous. Entry is typically through an apprenticeship programme or college course in conjunction with on-the-job training, leading to a NVQ/SVQ level 2/3 qualification, or through building up work experience operating other heavy machinery supplemented with short courses. Operators are required to hold a Construction Plant Competence Scheme (CPCS) card owned and administered by the National Open College Network (NOCN) group, demonstrating basic skills and safety awareness.",
    "tasks": [
        "~gives signals for movement of cage carrying workers/equipment ~starts crane or engine motor and checks that cables run freely and that brakes and drum(s) are working ~manipulates levers, switches and pedals to rotate jibs into position and turns winding drum to raise or lower hook, bucket or other holding equipment ~lifts load or cage, or hauls object into required position and lowers or positions for ground workers to detach, unload or load ~watches control panel for warning lights and indications of wind speed and direction and carrying capacity of crane ~oils and greases machine and checks ropes",
    ],
}
SOCmeta["8222"] = {
    "group_title": "Fork-lift truck drivers",
    "group_description": "Fork-lift truck drivers operate fork-lift trucks in factories, warehouses, storerooms and other areas to transfer goods and materials.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. A variety of vocational qualifications in Forklift Truck Operations are available at level 2.",
    "tasks": [
        "~operates controls to pick up load on forks ~drives truck to unloading point and lowers forks to correct position on stack or ground ~ensures that truck is connected to charger or is correctly refuelled for use ~keeps records of work undertaken ~cleans, oils and greases machine",
    ],
}
SOCmeta["8229"] = {
    "group_title": "Mobile machine drivers and operatives n.e.c.",
    "group_description": "Job holders in this unit group supervise and undertake the operation of machines to transport, excavate, grade, level, and compact sand, earth, gravel and similar materials, drive piles into the ground and lay surfaces of asphalt, concrete and chippings, clear and cultivate land, to sow and harvest plants and crops, and operate other mobile machines not elsewhere classified in minor group 822: Mobile machine drivers and operatives.",
    "entry_routes_and_quals": "No academic qualifications are required. On-the-job training is provided. The appropriate current driving licence will be required for driving on public highways.",
    "tasks": [
        "~fixes any necessary extensions onto machine and loads machine with asphalt, concrete, bitumen, tar, stone chippings or any other required materials ~manipulates levers, pedals and switches to manoeuvre vehicle, regulate angle and height of blades, buckets and hammers and starts conveyor, suction or water spraying system ~watches operation and removes any likely obstacle or obstructions ~directs refilling of machine hopper and repeats operations as necessary ~operates tractors, combine harvesters or other farm vehicles, attaches plough, cultivator or other implements and adjusts depth, speed and height to requirements ~drives and operates machinery to plough, fertilise, plant, cultivate or harvest crops ~cleans, oils and greases machine and carries out minor repairs",
    ],
}
SOCmeta["823"] = {
    "group_title": "Other drivers and transport operatives",
    "group_description": "Other drivers and transport operatives drive trains and trams, assist train drivers in the operation of passenger and goods trains, guide the movement of rail coaches in coal mines, sidings and marshalling yards, control the movement of rail traffic, monitor and inspect the operations of railways, perform deck duties and operate engines, boilers and mechanical equipment on board ships, assist in the boarding, fuelling, and movement of aircraft at airports, and perform other transport related tasks not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["8231"] = {
    "group_title": "Train and tram drivers",
    "group_description": "Train and tram drivers drive diesel, diesel-electric, electric and steam locomotives that transport passengers and goods on surface and underground railways, and transport passengers in trams.",
    "entry_routes_and_quals": "There are no formal academic requirements. Entrants must pass a series of tests and a medical examination. Age restrictions apply in some areas of work. Good hearing, good eyesight and normal colour vision are required. Off and on-the-job training is provided. NVQs/SVQs are available at level 2.",
    "tasks": [
        "~checks controls, gauges, brakes and lights before start of journey and studies route, timetable and track information ~checks safety equipment, regulates the heating of passenger compartments and records engine defects or unusual incidents on the journey ~starts train or tram when directed and operates controls to regulate speed ~watches for track hazards, observes signals and temperature, pressure and other gauges ~stops as directed to allow passengers to embark/ disembark ~makes scheduled stops for the loading and unloading of freight and coupling/uncoupling of carriages and tubs ~maintains radio contact with control centre ~may make passenger announcements and controls automatic doors ~may check travel passes, collect fares and deal with passenger queries",
    ],
}
SOCmeta["8232"] = {
    "group_title": "Marine and waterways transport operatives",
    "group_description": "Marine and waterways transport operatives supervise and carry out a variety of deck duties and operate and maintain engines, boilers and mechanical equipment on board ships, boats and other marine vessels.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, although some employers may expect entrants to possess GCSEs/S grades. Candidates are expected to pass a medical examination and have good eyesight. Training takes place at nautical college and lasts between 11-13 weeks.",
    "tasks": [
        "~ensures that necessary fuel supplies are on board and inspects engine, boilers and other mechanisms for correct functioning ~removes and repairs or replaces damaged or worn parts of plant and machinery and ensures that engine and plant machinery are well lubricated ~stows cargo, assists passengers to embark and disembark, watches for hazards and moors or casts off mooring ropes as required ~steers ship, under the supervision of a duty officer, checks navigational aids and keeps bridge, wheel and chartroom clean and tidy ~performs other deck duties, including servicing and maintaining deck gear and rigging, splicing wire and fibre ropes, greasing winches and derricks, opening up and battening down hatches, securing gangways and ladders and lowering and raising lifeboats",
    ],
}
SOCmeta["8233"] = {
    "group_title": "Air transport operatives",
    "group_description": "Air transport operatives refuel, load and unload aircraft, direct the movement of aircraft at airports, and positions gangways or staircases to allow passengers to board and disembark aircraft.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though employers may require entrants to possess GCSEs/S grades for some posts. Training is provided Off and on-the-job. Vocational qualifications in Aviation Operations on the Ground at level 2 and 3 and apprenticeships are available.",
    "tasks": [
        "~refuels aircraft from mobile tankers ~directs the ground movement of aircraft at airports ~responds to emergencies or incidents on the airfield and completes runway inspections ~loads and unloads conveyor belts to transport luggage between terminal buildings and aircraft, monitors conveyor belts and clears any blockages ~loads aircraft with luggage, in-flight meals, refreshments and other items ~operates retractable gangway or positions mobile staircases to enable passengers and crew to board and disembark aircraft ~x-rays cargo and luggage",
    ],
}
SOCmeta["8234"] = {
    "group_title": "Rail transport operatives",
    "group_description": "Rail transport operatives assist drivers in the operation of passenger and goods trains, drive locomotive engines in coal mines, guide wagons and coaches in marshalling yards and sidings to make up trains, operate signals and points to control the movement of rail traffic, and monitor the operation of surface and underground railways.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Candidates may be required to have good hearing, eyesight, and normal colour vision and pass a medical examination for entry to some posts. Training is initially undertaken in training centres, followed by practical experience on-the-job. NVQs/ SVQs in Rail Services are available at level 2 and 3.",
    "tasks": [
        "~provides crews for breakdown trains, allocates relief and replacement crews as necessary, keeps crews informed of any line repairs or restrictions, and checks train running times for punctuality ~examines schedules and decides priority of movement of trains, monitors movement of trains and issues instructions to drivers, signal operatives and level crossing keepers ~operates signals and opens and closes barriers at level crossings as required ~examines shunting instructions, uncouples wagons and coaches, guides movement of carriages using manual points and wagon breaks, links-up carriages, ensures security of couplings and reconnects brake and heating systems ~assists drivers in the operation of diesel, diesel-electric, electric and steam locomotives ~checks loading of tubs and carriages, and informs driver of load distribution and any special features of route",
    ],
}
SOCmeta["8239"] = {
    "group_title": "Other drivers and transport operatives n.e.c.",
    "group_description": "Job holders in this unit group monitor the activities of bus drivers, conductors and other road transport depot drivers, undertake various tasks related to water transportation, and perform other transportation tasks not elsewhere classified in minor group 823: Other drivers and transport operatives.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is provided both Off and on-the-job. In some areas relevant vocational qualifications are available at level 2 and 3.",
    "tasks": [
        "~checks that vehicles run as scheduled, monitors number of passengers travelling particular routes and makes recommendations for improvement of services ~organises relief and replacement crews as necessary, ensures compliance with regulations regarding the carrying of passengers and luggage, and submits reports of any irregularities ~checks that goods have been correctly loaded into vehicle, monitors and records information from tachograph, and arranges for servicing, refuelling, cleaning and repair of depot vehicles ~operates and maintains lighthouses and navigational lights in harbours, and assists in mooring craft ~operates and maintains locks, opens and closes moving bridges across inland waterways and docks, and measures depth of water in canals, rivers, etc. to determine possible dumping or dredging sites ~guides horses or ponies and drives horse drawn vehicles to transport goods and passengers",
    ],
}
SOCmeta["9"] = {
    "group_title": "Elementary occupations",
    "group_description": "This major group covers occupations which require the knowledge and experience necessary to perform mostly routine tasks, often involving the use of simple hand-held tools and, in some cases, requiring a degree of physical effort. Most occupations in this major group do not require formal educational qualifications but will usually have an associated short period of formal experience-related training.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["91"] = {
    "group_title": "Elementary trades and related occupations",
    "group_description": "Occupations in this sub-major group perform agricultural, fishing and forestry related tasks, undertake general labouring duties, assist building and construction trades workers, and perform a variety of duties in foundry, engineering and other process plant related trades.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["911"] = {
    "group_title": "Elementary agricultural occupations",
    "group_description": "Job holders in this minor group cultivate and harvest crops, breed and rear animals, catch and breed fish and other aquatic life and perform forestry and related tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9111"] = {
    "group_title": "Farm workers",
    "group_description": "Farm workers perform a variety of tasks, by hand and machine, to produce and harvest crops and to breed and rear cattle, sheep, pigs and poultry.",
    "entry_routes_and_quals": "There are no minimum academic entry requirements. Training is typically received on-the-job, supplemented by vocational training at an agricultural college. A variety of vocational qualifications in Agriculture are available at levels 1, 2 and 3, together with BTEC diplomas and apprenticeships in some areas.",
    "tasks": [
        "~operates farm machinery to prepare soil, fertilise and treat crops ~cultivates growing crops by hoeing, spraying and thinning as necessary ~weighs and measures foodstuffs, feeds animals and checks them for any signs of disease ~cleans barns, sheds, pens, yards, incubators and breeding units and sterilises milking and other equipment as necessary ~Treats minor ailments, delivers vaccinations and other medicines under the direction of the veterinary surgeon, and assists the veterinary surgeon as required ~Catches, moves, and handles livestock, including in preparation for transport ~carries out maintenance on farm buildings, hedges, ditches and erects and repairs fences",
    ],
}
SOCmeta["9112"] = {
    "group_title": "Forestry and related workers",
    "group_description": "Forestry workers perform a variety of tasks related to the planting, cultivation and protection of trees.",
    "entry_routes_and_quals": "There are no minimum academic entry requirements. Training is typically received on-the-job, supplemented by short courses covering specialised skills. Vocational qualifications in Forestry and Arboriculture are available at levels 2 and 3, together with BTEC diplomas and apprenticeships in some areas.",
    "tasks": [
        "~prepares ground for planting by clearing vegetation and other debris ~drains and ploughs land and erects and maintains fences as necessary ~collects seeds, plants and prunes trees and selects and marks trees for felling ~fells trees using axe or power saw and saws wood into required lengths ~cuts coppice, removes tops of standing trees and lops branches as necessary ~assists in the control of harmful diseases, pests or forms of wildlife ~builds and maintains forest roads ~maintains watch for fires and operates firefighting equipment ~operates machinery used in the cultivation and management of trees ~monitors and patrols forests and parks to maintain grounds and prevent unauthorised entry",
    ],
}
SOCmeta["9119"] = {
    "group_title": "Fishing and other elementary agriculture occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of tasks in relation to the breeding and rearing of animals and fish, catch fish at sea and from inland waterways, assist in the picking and lifting of crops, plant and maintain hedges, oversee the incubation and hatching of eggs and perform other fishing and elementary agricultural tasks not elsewhere classified in minor group 911: Elementary agricultural occupations.",
    "entry_routes_and_quals": "There are no minimum academic entry requirements. Training is typically received on-the-job, supplemented by vocational training at an agricultural college. A variety of vocational qualifications in Agriculture and Fish Husbandry are available at levels 2 and 3 and in Maritime Studies: Sea Fishing at level2. Apprenticeships are available in some areas. Fishermen/women are required to undertake safety courses before and during the early stages of employment.",
    "tasks": [
        "~assists with the shooting, hauling and repairing of nets, prepares, lays and empties baited pots at intervals, operates winches and lifting gear, and guts, sorts and stows fish ~harvests oysters, mussels, clams and seaweed off natural or artificial beds, nets river fish and maintains them in spawning pens, assists with feeding and water treatment, and empties and cleans outdoor tanks ~cleans animals\u2019 quarters and renews bedding as necessary ~extracts semen for storage, selects appropriate semen from store, injects recipient animal and issues certificate giving pedigree and date of insemination ~incubates eggs in hatchery and supplies chicks for meat and egg production and game birds for reserves ~plants cuttings or shrubs, maintains hedges by clipping, pruning and re-planting, and picks fruit, vegetables, hops and flowers ~performs other farming and related tasks not elsewhere classified including sorting and marking livestock, catching rabbits, cutting peat, shearing sheep and sexing chickens",
    ],
}
SOCmeta["912"] = {
    "group_title": "Elementary construction occupations",
    "group_description": "Workers in this minor group assist the work of woodworking and building trades workers, electricians, plumbers, and painters and perform a variety of general labouring and construction tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9121"] = {
    "group_title": "Groundworkers",
    "group_description": "Groundworkers prepare construction sites for building work by digging out and levelling the ground and laying concrete foundations, installing pipes and drainage and building paths, roads and driveways.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is typically provided on-the-job. Vocational qualifications in Ground Works Operations at level 2 and apprenticeships are available.",
    "tasks": [
        "~mark out site area set up the construction site ~prepares site and lays concrete for shallow foundations and fabricates steel cages ~installs drainage and pipes and redirects waterways away from site ~builds paths, roads, kerbs and footpaths, using flagstones, paving and tarmac",
    ],
}
SOCmeta["9129"] = {
    "group_title": "Elementary construction occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of general labouring and construction duties to assist building, civil engineering and related trades workers in the performance of their tasks not elsewhere classified in minor group 912: Elementary construction occupations.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is typically provided on-the-job. NVQs/SVQs in a variety of construction and craft occupations are available at levels 1, 2 and 3.",
    "tasks": [
        "~conveys blocks, bricks, stone, mortar, roofing, felt, slates, wood and other building materials to the work area ~assists with the erection of ladders, scaffolding and work platforms, the rigging of cradles of hoisting equipment and the attaching of slings, hooks and guide ropes ~mixes mortar, grouting material, cement screed, and plaster, prepares adhesive, primer and paints and similar construction material, and undertakes basic decorating, painting, plumbing and other maintenance and repair tasks ~cleans equipment and tools, clears work area and otherwise assists building and woodworking trades workers as directed ~performs general labouring tasks such as loading and delivering materials and equipment, removing wall coverings, and preparing surfaces by cleaning, sanding, filling, etc. ~covers ceilings, floors, walls and exposed surfaces of boilers, pipes and plant with insulating material ~heats and breaks up blocks of asphalt, bitumen or tar, stirs melting mixture, adds aggregate if required, pours mixture into buckets ~measures and fixes timber and other structures to support excavations, cables or other rail, signal and telecoms equipment ~maintains land drainage systems and prepares graves for burial ~operates, cleans and lubricates valves and sluices, removes weeds, dead animals and other debris from waterways and carries out minor repairs to banks and footbridges ~helps diver into and out of diving suit, maintains communication with submerged diver and checks equipment and time spent under water",
    ],
}
SOCmeta["913"] = {
    "group_title": "Elementary process plant occupations",
    "group_description": "Workers in this minor group clean metal goods, machinery and industrial premises, operate printing machines and reprographic equipment, wrap, fill, label and seal containers by hand or machine and perform a variety of manual tasks in foundry, engineering and allied trades.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9131"] = {
    "group_title": "Industrial cleaning process occupations",
    "group_description": "Industrial cleaning process occupations clean manufactured goods, plant and machinery, industrial premises and building exteriors.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job. Vocational qualifications covering various aspects of industrial cleaning are available at levels 1 and 2. Qualifications are also offered by the British Institute of Cleaning Science.",
    "tasks": [
        "~uses industrial hoovering, polishing, pressure washer, steam cleaning and sandblasting equipment to clean industrial premises and building exteriors ~dismantles engines, boilers, furnaces and other industrial plant and machinery, cleans component parts and reassembles equipment ~washes, rinses, dries and cleans manufactured goods, and stacks cleaned articles ready for removal",
    ],
}
SOCmeta["9132"] = {
    "group_title": "Packers, bottlers, canners and fillers",
    "group_description": "Packers, bottlers, canners and fillers pack, wrap, fill, label and seal containers by hand or machine.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is typically provided on-the-job and varies according to the type of packing and product. Formal courses are run for specialist packing.",
    "tasks": [
        "~selects appropriate cylinder, ensures that there is no corrosion or other damage and fills with gas ~fills tubes, ampoules, bottles, drums, barrels, bags, sacks, cans, boxes and other containers by hand using measuring/weighing aid or by positioning container under feeder spout ~packs heavy goods in crates and boxes using hoist, mobile crane or similar lifting equipment ~loads machine with packaging containers, materials, adhesive, etc., loads hopper with items to be packaged/wrapped, monitors filling, wrapping and packaging, adjusts controls as necessary and clears any blockages ~examines cans, bottles and seals and rejects any that are faulty ~labels goods by hand or machine ~packs specialist items according to specifications and completes necessary documentation",
    ],
}
SOCmeta["9139"] = {
    "group_title": "Elementary process plant occupations n.e.c.",
    "group_description": "Job holders in this unit group assist the work of machine operatives and perform a variety of manual tasks in foundries, engineering and allied trades and in other process and plant operations not elsewhere classified in minor group 913: Elementary process plant occupations.",
    "entry_routes_and_quals": "No academic qualifications are required. On-the- job training is provided. NVQs/SVQs may be available in some areas.",
    "tasks": [
        "~assists with the operation of furnaces and the preparation of castings ~assists in setting up attachments on plant and machinery, and operates saws, shears or other equipment ~conveys goods, materials, equipment, etc. to work area, assists in setting up machinery and equipment and prepares tools, lamps and other equipment for use ~assists operative to mark out, bend, drill, galvanise, coat and otherwise machine metal ~loads and unloads vehicles, trucks and trolleys ~removes finished pieces from work area, paints or fixes identification labels or markers on products or containers ~clears machine blockages, cleans machinery, equipment and tools, keeps work area tidy and clears waste and any spillages ~performs a variety of manual tasks in relation to the operation of coke ovens, boilers, blast furnaces and other engineering trades",
    ],
}
SOCmeta["92"] = {
    "group_title": "Elementary administration and service occupations",
    "group_description": "Workers in this sub-major group collect, sort and deliver written correspondence, undertake elementary clerical tasks within offices, undertake elementary cleaning tasks, protect and supervise people and property, perform elementary sales related tasks, assist in the storage and transportation of goods, and perform a variety of carrying, preparation and serving tasks within hospitals, catering, domestic and other establishments.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["921"] = {
    "group_title": "Elementary administration occupations",
    "group_description": "Workers in this minor group collect, receive, sort and deliver mail, documents, correspondence or messages and perform a variety of elementary clerical tasks within offices.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9211"] = {
    "group_title": "Postal workers, mail sorters and messengers",
    "group_description": "Postal workers, mail sorters and messengers collect, receive, sort and deliver mail, documents, correspondence or messages, either between or within establishments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Entrants complete short induction courses followed by a programme of Off and on-the-job training.",
    "tasks": [
        "~collects and may x-ray mail from post boxes, receives parcels, and collects correspondence, documents and other material from individuals, offices or other establishments ~sorts mail, parcels and other incoming and outgoing material for delivery, and maintains records of material received and despatched ~delivers mail, parcels, correspondence and other materials to specified or agreed routes and schedules ~completes delivery forms, collects charges, and issues receipts for the collection and delivery of registered or recorded mail and other items",
    ],
}
SOCmeta["9219"] = {
    "group_title": "Elementary administration occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of elementary clerical and administrative tasks within offices not elsewhere classified in minor group: 921 Elementary administration occupations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided on-the-job. NVQs/ SVQs in Business Administration are available at level 1, 2 and 3.",
    "tasks": [
        "~copies, duplicates or destroys documents and other records ~records and retrieves information ~compiles, sorts and files correspondence ~takes messages and distributes internal and external correspondence to office staff",
    ],
}
SOCmeta["922"] = {
    "group_title": "Elementary cleaning occupations",
    "group_description": "Workers in this minor group clean windows, chimneys, roads and interiors of buildings, wash, dry and press household linen, clean carpets, curtains and similar articles, collect refuse from business and private premises, clean vehicles inside and out, and perform other elementary cleaning tasks not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9221"] = {
    "group_title": "Window cleaners",
    "group_description": "Window cleaners wash and polish windows and other glass fittings.",
    "entry_routes_and_quals": "No academic qualifications are required. On-the-job training may be available in larger firms. Relevant vocational qualifications at level 2 are available.",
    "tasks": [
        "~secures ladders and other equipment to gain safe access to glass ~selects appropriate cleaning or polishing implement ~washes and polishes glass with brushes, cloths, sponges, water and solvents",
    ],
}
SOCmeta["9222"] = {
    "group_title": "Street cleaners",
    "group_description": "Street cleaners clean, sweep and remove refuse from public thoroughfares.",
    "entry_routes_and_quals": "No academic qualifications are required. On-the-job training is provided. Vocational qualifications in Cleaning and Support Services Skills are available at levels 1 and 2.",
    "tasks": [
        "~sweeps pavements, gutters and roadways with hand broom or mechanical sweeper ~collects litter using hand tools ~transfers refuse into containers and empties public litter bins into containers.",
    ],
}
SOCmeta["9223"] = {
    "group_title": "Cleaners and domestics",
    "group_description": "Cleaners and domestics clean interiors of private houses, shops, hotels, schools, offices and other buildings.",
    "entry_routes_and_quals": "No academic qualifications are required. On-the-job training may be provided. Vocational qualifications in Cleaning and Support Services Skills are available at levels 1 and 2.",
    "tasks": [
        "~scrubs, washes, sweeps and polishes floors, corridors and stairs ~dusts and polishes furniture and fittings ~cleans toilets and bathrooms ~washes down walls and ceilings ~empties ashtrays, waste bins and removes rubbish",
    ],
}
SOCmeta["9224"] = {
    "group_title": "Launderers, dry cleaners and pressers",
    "group_description": "Launderers, dry cleaners and pressers supervise and undertake the washing, dry cleaning, ironing and pressing of clothing, household and other linen, carpets, curtains and other articles.",
    "entry_routes_and_quals": "Academic qualifications are not required. Training is mainly on?the-job. Vocational qualifications in Laundry Operations and Textile Care Services are available at level 2.",
    "tasks": [
        "~receives garment or item from customer for cleaning, checks pockets, buttons, zips, etc. and issues receipt ~sorts articles by fabric, colour and type and determines appropriate cleaning process ~removes difficult stains using chemicals or steam gun ~loads articles into washing and dry cleaning machines or electrically operated drum cleaning machine, operates controls to admit cleaning fluids and starts machine ~sets and operates drying machines and smooths and shapes washed garments using hand iron or machine press ~allocates washing machines to customers, ensures correct use of equipment and gives change ~performs a variety of laundering, dry cleaning and pressing tasks, including beating carpets and shaping starched collars, cuffs and hats",
    ],
}
SOCmeta["9225"] = {
    "group_title": "Refuse and salvage occupations",
    "group_description": "Refuse and salvage collectors supervise and undertake the collection and processing of refuse from household, commercial and industrial premises.",
    "entry_routes_and_quals": "No academic qualifications are required. Training is provided on-the-job. A minimum age limit of 18 years normally applies.",
    "tasks": [
        "~rides in or on refuse vehicle and alights to pick up domestic refuse ~carries waste material in dustbins or other containers from premises to refuse vehicle ~empties refuse into vehicle manually or using an electronic tipping device ~returns dustbins or other containers to premises ~collects scrap metal, salvage, paper and other recyclable material from domestic and industrial premises, and sorts material in preparation for recycling ~attends the operation of refuse tips, supervises the use of public refuse disposal facilities, and compacts and covers up refuse at landfill sites",
    ],
}
SOCmeta["9226"] = {
    "group_title": "Vehicle valeters and cleaners",
    "group_description": "Vehicle valeters and cleaners clean, wash and polish the interiors and exteriors of ships, aircraft, trains and road vehicles.",
    "entry_routes_and_quals": "No academic qualifications are required. On-the-job training may be provided. Vocational qualifications in relevant areas are available at levels 1 and 2.",
    "tasks": [
        "~vacuums, brushes and washes vehicle upholstery and interior surfaces ~empties waste bins and removes rubbish ~reports any damage or vandalism to the fabric of the vehicle interior ~washes, cleans and polishes as appropriate the exterior surfaces of vehicles",
    ],
}
SOCmeta["9229"] = {
    "group_title": "Elementary cleaning occupations n.e.c.",
    "group_description": "Job holders in this unit group perform elementary cleansing service occupations not elsewhere classified in minor group 922: Elementary cleaning occupations.",
    "entry_routes_and_quals": "No formal academic qualifications are required. Training may be provided on-the-job.",
    "tasks": [
        "~selects appropriate brush head, pushes it through flue or chimney and collects soot and other dislodged deposits from flue or chimney with brush or vacuum equipment ~cleans toilets, washrooms, rest rooms and other similar amenities ~replenishes supplies of soap, toilet paper and towels ~reports acts of vandalism and any defects in sanitary equipment ~completes worksheets to note the date and time that amenities were last cleaned",
    ],
}
SOCmeta["923"] = {
    "group_title": "Elementary security occupations",
    "group_description": "Workers in this minor group protect individuals or property from injury, theft or damage, patrol areas to detect and prevent parking infringements, assist children in crossing roads, supervise the activities of school children during break and meal times, control the parking of vehicles in car parks, and perform other elementary security tasks not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9231"] = {
    "group_title": "Security guards and related occupations",
    "group_description": "Security guards and related occupations protect merchandise, individuals, hotels, offices, factories, shops, public grounds and private estates from injury, theft or damage.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. For some vacancies a current and clean driving licence is required and entrants may have to pass a medical examination. Training is typically provided on-the-job. NVQs/SVQs covering various aspects of security guarding are available at level 2.",
    "tasks": [
        "~walks or rides near person requiring protection, watches for suspicious occurrences and defends guarded person from attack ~monitors, patrols and deals with security difficulties in hotels, factories, offices and other premises, and public or private estates to prevent theft and unauthorised entry ~checks persons and vehicles entering and leaving premises, establishes their credentials and arranges for escorts for visitors ~provides entry security, checks tickets, manages queues, takes entry fees, and escorts people from the premises where necessary in a variety of public venues such as nightclubs, pubs and bars ~receives duty sheet, time-clock and keys for premises to be visited, checks locks, doors, windows, etc. and reports any suspicious circumstances to security headquarters ~calls in civil police and gives evidence in court where necessary ~ejects persons in illegal occupation of premises ~watches for illegal fishing or attempted smuggling ~patrols airport, checks passengers baggage, operates metal detectors and x-rays and assists in responding to emergency situations ~greets and organises people attending court cases, ensures necessary parties are present, calls defendants and witnesses, directs oath taking and keeps order in the courtroom",
    ],
}
SOCmeta["9232"] = {
    "group_title": "School midday and crossing patrol occupations",
    "group_description": "School midday and crossing patrol occupations supervise the activities of school children during break and meal times and assist children to cross roads in the vicinity of schools.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Some employers may expect candidates to show previous experience in caring for children. Training is provided Off and on-the-job. A DBS check is mandatory.",
    "tasks": [
        "~supervises the playground activities of children during meal and break times ~cares for sick children and administers first aid if necessary ~assists young children with feeding, dressing, washing and toiletry activities ~meets children wanting to cross the road and directs them to wait at the kerb ~waits for a safe gap in traffic and walks to the centre of road ~signals approaching traffic to stop by using hand signals and school crossing signs ~directs children to cross the road when safe",
    ],
}
SOCmeta["9233"] = {
    "group_title": "Exam invigilators",
    "group_description": "Exam invigilators set up, run and invigilate exams to ensure exams are conducted in line with the relevant regulations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is provided Off and on-the-job.",
    "tasks": [
        "~sets up venue, lays out desks, exam papers, stationery and other equipment necessary for the exam ~directs candidates to their seats, checks attendance, and informs candidates of the exam conditions they will work under ~supervises during exams, responds to any problems or questions from candidates and deals with any violations of the exam conditions ~escorts people from the venue following the exam and collects completed papers",
    ],
}
SOCmeta["924"] = {
    "group_title": "Elementary sales occupations",
    "group_description": "Workers in this minor group remove and replace posters from hoardings, bill boards and other advertising spaces, replenish stocks of goods in retail establishments, collect and issue shopping trolleys and baskets, and perform other elementary sales related tasks.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9241"] = {
    "group_title": "Shelf fillers",
    "group_description": "Shelf fillers receive incoming goods from storage, check them for damage and place them on the appropriate shelves in the store.",
    "entry_routes_and_quals": "There are no minimum academic entry requirements. Some on-the-job training may be provided.",
    "tasks": [
        "~selects goods from storeroom and checks for any damage ~checks store layout or written instructions to determine the appropriate shelf location for the goods ~prices goods by machine and fills shelves with goods ~monitors depletion of stocks and re-fills shelves as required",
    ],
}
SOCmeta["9249"] = {
    "group_title": "Elementary sales occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of elementary sales related occupations not elsewhere classified in minor group 924: Elementary sales occupations.",
    "entry_routes_and_quals": "There are no minimum academic entry requirements. Some on-the-job training may be provided.",
    "tasks": [
        "~strips old posters from hoardings and fits new posters using brushes and working from a ladder if necessary ~collects shopping baskets and trolleys in and around wholesale/retail establishments and positions near entrance to store ~offers shopping baskets to customers entering retail establishments ~select goods and groceries ordered online by customers, ensuring orders are picked, bagged and stored ~wraps and packs goods for customers",
    ],
}
SOCmeta["925"] = {
    "group_title": "Elementary storage occupations",
    "group_description": "Workers in this minor group load and unload cargo from ships, boats and barges, supply berthed ships with water, oil and fuel, load, unload and convey furniture, goods and other equipment in and around warehouses, depots and similar establishments, and accompany motor vehicle and other road vehicle drivers.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9251"] = {
    "group_title": "Elementary storage supervisors",
    "group_description": "Elementary storage supervisors oversee operations and directly supervise and coordinate the activities of those working in warehouses, docks and other storage facilities.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Entrants will normally have significant relevant work experience. NVQs/ in Warehousing and Storage are available at levels 1, 2 and 3.",
    "tasks": [
        "~directly supervises and coordinates the activities of warehouse or dock staff ~establishes and monitors work schedules to meet the organisation\u2019s requirements ~liaises with managers and other senior staff to resolve operational problems ~determines or recommends staffing and other needs to meet the organisation\u2019s requirements ~reports as required to managerial staff on work-related matters",
    ],
}
SOCmeta["9252"] = {
    "group_title": "Warehouse operatives",
    "group_description": "Warehouse operatives load, unload and convey a variety of goods, equipment or other items in warehouses and depots, prepare requisitions or despatch documents of stocks held, and perform other elementary goods handling and storage related tasks.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided Off or on-the-job. NVQs/ in Warehousing and Storage are available at levels 1, 2 and 3.",
    "tasks": [
        "~undertakes the loading and unloading of goods and conveys goods about storage area ~packs furniture and household goods into crates and cartons for storage ~retrieves stored items as listed on order sheets, makes up orders against requisitions and prepares goods for despatch ~checks goods for damage or missing stock and maintains an inventory of stock ~cleans and maintains warehouse",
    ],
}
SOCmeta["9253"] = {
    "group_title": "Delivery operatives",
    "group_description": "Delivery operatives load and unload goods from removal vans and delivery vehicles, convey household and office furniture, goods, equipment or other items, accompany drivers of road vehicles, and perform other elementary goods handling tasks.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided off or on-the-job.",
    "tasks": [
        "~loads and unloads goods from removal vans or delivery vehicles either by hand or using trolleys and lift trucks ~takes receipt of goods from customers and maintains and accurate record of deliveries ~dismantles and packages items for transport if necessary ~accompanies driver on journey and assists with manoeuvres and to load and unload vehicle",
    ],
}
SOCmeta["9259"] = {
    "group_title": "Elementary storage occupations n.e.c.",
    "group_description": "Job holders in this unit group supply berthed ships with water, oil and petroleum, load and unload cargo from ships, boats and barges, and perform other elementary goods handling and storage related tasks not classified elsewhere in minor group 925: Elementary storage occupations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically provided off or on-the-job. Vocational qualifications in Warehousing and Storage at levels 1, 2 and 3 and in Port Operations at levels 2 and 3 are available.",
    "tasks": [
        "~attaches hoses to ship\u2019s flow connections, starts pump to transfer oil, petroleum or water to and from a ship and uncouples hose system when loading/discharging is complete ~arranges cargo on quayside or in hold for loading or unloading and selects appropriate hook, chain, rope, sling or other grappling attachment ~attaches winch or crane hooks, slings, ropes or clamps to load, signals to crane driver to commence lifting, visually checks that load is balanced and ensures that route is clear for movement ~removes grappling attachment from cargo and stows cargo in hold or loads cargo on to transport or into warehouses ~directs the movement and operation of vehicles, such as lorries and cranes, on site ~x-rays cargo",
    ],
}
SOCmeta["926"] = {
    "group_title": "Other elementary services occupations",
    "group_description": "Workers in this minor group perform manual tasks to assist nursing and domestic staff in hospitals, perform a variety of cleaning, preparation, carrying and fetching tasks in kitchens, serve food, beverages and alcoholic drinks in catering, domestic and other establishments, assist in the operation of cinemas, theatres, amusement arcades, funfairs, theme parks and holiday camps, and perform other elementary personal service occupations not elsewhere classified.",
    "entry_routes_and_quals": "",
    "tasks": [],
}
SOCmeta["9261"] = {
    "group_title": "Bar and catering supervisors",
    "group_description": "Bar and catering supervisors oversee operations and directly supervise and coordinate the activities of those working in the catering industry, in bars, restaurants and other establishments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Entrants will normally have significant relevant work experience. A variety of qualifications in hospitality and catering are available.",
    "tasks": [
        "~directly supervises and coordinates the activities of bar, waiting and catering staff ~establishes and monitors work schedules to meet the organisation\u2019s requirements ~liaises with managers and other senior staff to resolve operational problems ~determines or recommends staffing and other needs to meet the organisation\u2019s requirements ~reports as required to managerial staff on work-related matters",
    ],
}
SOCmeta["9262"] = {
    "group_title": "Hospital porters",
    "group_description": "Hospital porters perform various manual tasks in hospitals to assist nursing and domestic staff with the care of patients.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is provided Off and on-the-job. Entrants may be required to hold a driving licence.",
    "tasks": [
        "~lifts, escorts and wheels patients between hospital wards ~assists with the delivery of meals, laundry, medical supplies and post to the wards or theatres ~moves hospital equipment and furniture ~collects and disposes of refuse from wards and other departments ~assists with unloading and delivery of supplies",
    ],
}
SOCmeta["9263"] = {
    "group_title": "Kitchen and catering assistants",
    "group_description": "Kitchen and catering assistants assist in the preparation and service of food and beverages in restaurants, caf\u00e9s and other eating establishments, and perform various cleaning, fetching and carrying tasks.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job. NVQs/ SVQs in relevant areas are available at levels 1 and 2.",
    "tasks": [
        "~cleans or prepares food for cooks by hand or machine ~carries meat, vegetables and other foodstuffs from delivery van to storeroom and from storeroom to kitchen ~cleans and tidies service area, kitchen surfaces, crockery, cutlery, glassware, kitchen utensils and disposes of rubbish ~prepares and serves beverages and light refreshments, accepts payment and gives change ~keeps service area well stocked",
    ],
}
SOCmeta["9264"] = {
    "group_title": "Waiters and waitresses",
    "group_description": "Waiters and waitresses serve food and beverages in hotels, clubs, restaurants public houses and other establishments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements, though some employers may require GCSEs/S grades. Training is typically provided on-the-job. NVQs/SVQs in relevant areas are available at levels 1 and 2.",
    "tasks": [
        "~sets tables with clean linen, cutlery, crockery and glassware ~presents menus and wine lists to patrons and may describe dishes and advise on selection of food or wines ~takes down orders for food and/or drinks and passes order to kitchen and/or bar ~serves food and drinks ~presents bill and accepts payment at end of the meal",
    ],
}
SOCmeta["9265"] = {
    "group_title": "Bar staff",
    "group_description": "Bar staff prepare, mix and serve alcoholic and non-alcoholic drinks and beverages at bars in public houses, hotels, clubs and other establishments.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job. Vocational qualifications in relevant areas are available at levels 1,2 and 3.",
    "tasks": [
        "~assists in keeping bar properly stocked ~washes used glassware and cleans and tidies bar area ~takes customer orders and mixes and serves drinks ~receives payment for drinks",
    ],
}
SOCmeta["9266"] = {
    "group_title": "Coffee shop workers",
    "group_description": "Coffee shop workers make and serve coffee, food and other beverages in coffee shops and caf\u00e9s, and perform various cleaning, fetching and carrying tasks.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job. Qualifications to become a barista are available.",
    "tasks": [
        "~takes customer orders, makes and serves coffee and other refreshments ~receives payment for drinks and gives change ~cleans and tidies service area, kitchen surfaces, crockery, cutlery, glassware, kitchen utensils and disposes of rubbish ~keeps service area well stocked",
    ],
}
SOCmeta["9267"] = {
    "group_title": "Leisure and theme park attendants",
    "group_description": "Leisure and theme park attendants monitor the operation of amusement arcades, check tickets of entry to theatres and cinemas and show people to their seats, operate rides at funfairs and theme parks, entertain and look after guests at holiday camps and supervise museums and art galleries.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job.",
    "tasks": [
        "~checks tickets of people entering cinemas, theatres and sporting events, and directs people to their seats ~provides information and monitors exhibition spaces in museums and art galleries ~operates rides and supervises stalls at fairgrounds and amusement parks ~issues change at amusement arcades, monitors the operation of arcade machines and empties coins from machines ~welcomes holidaymakers, provides information about holiday camp, organises and participates in entertainment and activities for guests",
    ],
}
SOCmeta["9269"] = {
    "group_title": "Other elementary services occupations n.e.c.",
    "group_description": "Job holders in this unit group perform a variety of elementary services occupations not elsewhere classified in minor group 926: Other elementary services occupations.",
    "entry_routes_and_quals": "There are no formal academic entry requirements. Training is typically received on-the-job. NVQs/SVQs are available in some areas.",
    "tasks": [
        "~assists hotel guests with luggage etc. on arrival and departure, keeps entrance lobby tidy, deals with guests\u2019 enquiries ~assists in the movement of scenery and other stage equipment ~divines and tells fortunes by various means ~loads numbered balls into bingo machine, starts machine, removes balls and reads numbers, and checks winning bingo cards against numbers drawn ~examines and collects tickets at harbours, piers and similar thoroughfares or establishments not elsewhere classified ~collects payment, issues tickets and monitors the use of bathing huts, changing rooms, bath houses and deck chairs ~receives clothing, luggage and other articles, collects fee and issues ticket and returns item to deposit or on presentation of receipt ~dances in adult entertainment establishments",
    ],
}

soc_meta = [
    ClassificationMeta.model_validate(
        {
            "code": k,
            "soc2020_group_title": v.get("group_title", ""),
            "group_description": v.get("group_description", ""),
            "qualifications": v.get("entry_routes_and_quals", ""),
            "tasks": v.get("tasks", []),
        }
    )
    for k, v in SOCmeta.items()
]


class SocMeta:  # pylint: disable=too-few-public-methods
    """SOC metadata model class for SOC codes and descriptions."""

    def __init__(self):
        self.soc_meta = SOCmeta

    def get_meta_by_code(self, code: str) -> dict:
        """Retrieve metadata for an exact SOC code match only."""
        entry = self.soc_meta.get(code)
        if entry is None:
            return {"error": f"No metadata found for SOC code {code}"}
        return {
            "code": code,
            "group_title": entry.get("group_title", ""),
            "group_description": entry.get("group_description", ""),
            "entry_routes_and_quals": entry.get("entry_routes_and_quals", ""),
            "tasks": entry.get("tasks", []),
        }

    def get_meta_by_code_exact(self, code: str) -> dict:
        """Retrieve metadata only for an exact SOC code match."""
        return self.get_meta_by_code(code)
