from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, CatchAll

from model.copyright import CopyRight
from model.honor import Honor
from model.paper import Paper
from model.patent import Patent
from model.project_reward import ProjectReward


@dataclass_json
@dataclass
class Person:
    sap: str
    name: str
    department: str
    excel_template: str  # Excel模板
    patents: list[Patent]
    project_rewards: list[ProjectReward]
    copyrights: list[CopyRight]
    papers: list[Paper]
    honors: list[Honor]
