from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, CatchAll
from typing import Optional


@dataclass_json
@dataclass
class ProjectReward:
    project_name: str = field(metadata=config(field_name="project_name"))  # 获奖项目名称
    org_name: str = field(metadata=config(field_name="department"))  # 获奖单位名称
    grant_org_name: str = field(metadata=config(field_name="award_unit"))  # 授奖单位名称
    apply_level: str = field(metadata=config(field_name="app_rank"))  # 申报级别
    year: str = field(metadata=config(field_name="honor_year"))  # 奖励年度
    award_name: str = field(metadata=config(field_name="honor_name"))  # 奖项名称
    award_level: str = field(metadata=config(field_name="award_rank"))  # 授奖级别 厂处级、局级、省部级、国家级
    reward_level: str = field(metadata=config(field_name="honor_rank"))  # 奖励等级 一等奖、二等奖、三等奖

    persons_str: str = field(metadata=config(field_name="honor_people"))  # 获奖人员 字符串
    persons_total_num: str = field(metadata=config(field_name="persons_total_num"))  # 总人数
    person_rank: str = field(metadata=config(field_name="person_rank"))  # 本人排名

    achievement: Optional[str] = field(default=None, metadata=config(field_name="achievement"))  # 成果简介
    innovation_point: Optional[str] = field(default=None, metadata=config(field_name="innovation_point"))  # 创新点
    apply_effect: Optional[str] = field(default=None, metadata=config(field_name="apply_effect"))  # 应用效果

