from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, CatchAll
from typing import Optional


@dataclass_json
@dataclass
class Paper:
    title_publish: str = field(metadata=config(field_name="paper_name"))  # 发表论文题目
    title_submit: str = field(metadata=config(field_name="report_name"))  # 论文申报题目
    project_name: str = field(metadata=config(field_name="proj_name"))  # 所属项目名称
    is_accepted: str = field(metadata=config(field_name="reception"))  # 中稿与否
    is_published: str = field(metadata=config(field_name="publish"))  # 是否发布
    repositories: str = field(metadata=config(field_name="scope"))  # 收录范围
    year: int = field(metadata=config(field_name="publish_year"))  # 发表年度
    publication_name: str = field(metadata=config(field_name="publication_name"))  # 刊物名称
    details: str = field(metadata=config(field_name="detail"))  # 论文发表详情
    remarks: str = field(metadata=config(field_name="remark"))  # 备注
    first_author: str = field(metadata=config(field_name="first_author"))  # 第一作者
    persons_str: str = field(metadata=config(field_name="author_sort"))  # 作者排序
    persons_total_num: str = field(metadata=config(field_name="persons_total_num"))  # 总人数
    person_rank: str = field(metadata=config(field_name="person_rank"))  # 本人排名
