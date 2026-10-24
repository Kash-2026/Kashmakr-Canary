from typing import List, Dict, Any

def calculate_skill_coverage(projects: List[Dict[str, Any]]) -> Dict[str, int]:
    skill_coverage = {}
    for project in projects:
        for skill in project.get("skills", []):
            if skill in skill_coverage:
                skill_coverage[skill] += 1
            else:
                skill_coverage[skill] = 1
    return skill_coverage

def identify_skill_gaps(
    projects: List[Dict[str, Any]], required_skills: List[str]
) -> List[str]:
    existing_skills = set(
        skill for project in projects for skill in project.get("skills", [])
    )
    return [skill for skill in required_skills if skill not in existing_skills]

def generate_portfolio_report(projects: List[Dict[str, Any]]) -> Dict[str, Any]:
    report = {
        "total_projects": len(projects),
        "skill_coverage": calculate_skill_coverage(projects),
        "skill_gaps": [],
    }
    all_skills = set(skill for project in projects for skill in project.get("skills", []))
    # A skill gap is a skill present in the portfolio but missing from the
    # lead (first) project -- it is covered elsewhere but not by the flagship.
    lead_skills = set(projects[0].get("skills", [])) if projects else set()
    report["skill_gaps"] = sorted(skill for skill in all_skills if skill not in lead_skills)
    return report