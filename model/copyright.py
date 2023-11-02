from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, CatchAll


@dataclass_json
@dataclass
class CopyRight:
    copyright_name: str = field(metadata=config(field_name="copyright_name"))  # 著作权名称
    complete_org: str = field(metadata=config(field_name="department"))  # 完成单位
    project_name: str = field(metadata=config(field_name="project"))  # 所属项目/课题名称
    contract_code: str = field(metadata=config(field_name="project_no"))  # 项目/课题合同编号
    project_category: str = field(metadata=config(field_name="project_category"))  # 项目分类
    project_domain: str = field(metadata=config(field_name="project_domain"))  # 项目所属领域
    country: str = field(metadata=config(field_name="country"))  # 申请/注册国家
    status: str = field(metadata=config(field_name="status"))  # 状态
    date_start: int = field(metadata=config(field_name="start_date"))  # 起始日期
    date_end: int = field(metadata=config(field_name="end_date"))  # 终止日期
    apply_date: int = field(metadata=config(field_name="application_date"))  # 申请日期
    grant_date: int = field(metadata=config(field_name="authorization_date"))  # 授权日期
    copyright_holder: str = field(metadata=config(field_name="patentee"))  # 专利权人
    certificate_code: str = field(metadata=config(field_name="certifi_no"))  # 著作权证书编号
    software_reg_code: str = field(metadata=config(field_name="software_no"))  # 软件登记号
    remarks: str = field(metadata=config(field_name="remark"))  # 备注

    persons_str: str = field(metadata=config(field_name="inventor"))  # 发明人/设计人 字符串
    persons_total_num: int = field(metadata=config(field_name="persons_total_num:"))  # 总人数
    person_rank: str = field(metadata=config(field_name="person_rank"))  # 本人排名

