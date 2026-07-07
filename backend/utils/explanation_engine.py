
def generate_explanation(match_score, skills):

    explanations = []

    if match_score >= 85:
        explanations.append(
            "Excellent semantic match with the job description."
        )

    elif match_score >= 70:
        explanations.append(
            "Good semantic similarity with the job description."
        )

    else:
        explanations.append(
            "Low semantic similarity with the job description."
        )

    if len(skills) >= 8:
        explanations.append(
            "Candidate has a broad technical skill set."
        )

    elif len(skills) >= 5:
        explanations.append(
            "Candidate has a good range of technical skills."
        )

    else:
        explanations.append(
            "Candidate has limited detected technical skills."
        )

    if "python" in skills:
        explanations.append(
            "Python matches the job requirements."
        )

    if "react" in skills:
        explanations.append(
            "React experience detected."
        )

    if "machine learning" in skills:
        explanations.append(
            "Machine Learning knowledge detected."
        )

    if "sql" in skills:
        explanations.append(
            "Database skills identified."
        )

    return explanations