from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, CatchAll


@dataclass_json
@dataclass
class Patent:
    patent_name: str = field(metadata=config(field_name="patent_name"))  # 专利名称
    complete_org: str = field(metadata=config(field_name="department"))  # 完成单位
    project_name: str = field(metadata=config(field_name="project"))  # 所属项目/课题名称
    contract_code: str = field(metadata=config(field_name="project_no"))  # 项目/课题合同编号
    country: str = field(metadata=config(field_name="country"))  # 申请/注册国家
    status: str = field(metadata=config(field_name="status"))  # 状态
    patent_type: str = field(metadata=config(field_name="patent_category"))  # 专利类别
    patent_holder: str = field(metadata=config(field_name="patentee"))  # 专利权人
    apply_code: str = field(metadata=config(field_name="application_no"))  # 申请号
    patent_code: str = field(metadata=config(field_name="patent_no"))  # 专利号
    certificate_code: str = field(metadata=config(field_name="certificate_no"))  # 证书号
    apply_date: int = field(metadata=config(field_name="application_date"))  # 申请日期
    grant_date: int = field(metadata=config(field_name="authorization_date"))  # 授权日期

    persons_str: str = field(metadata=config(field_name="inventor"))  # 发明人/设计人 字符串
    persons_total_num: int = field(metadata=config(field_name="persons_total_num"))  # 总人数
    person_rank: str = field(metadata=config(field_name="person_rank"))  # 本人排名

