def data_cleaner(records):
    """
    Cleans student records, validates scores, calculates total score,
    average score, and assigns grades.
    """

    cleaned_records = []

    for row in records:
        # Skip records with missing critical fields
        if row.get("full_name") == 0 or row.get("student_id") == 0 or row.get("course") == 0:
            continue

        # Validate and normalize scores
        for score_key in ("score1", "score2", "score3"):
            score = row.get(score_key, 0)
            if not isinstance(score, (int, float)) or score < 0 or score > 100:
                row[score_key] = 0

        # Calculate total and average
        total_score = row["score1"] + row["score2"] + row["score3"]
        average_score = round(total_score / 3)

        # Assign grade
        if average_score >= 70:
            grade = "A"
        elif average_score >= 60:
            grade = "B"
        elif average_score >= 50:
            grade = "C"
        elif average_score >= 45:
            grade = "D"
        else:
            grade = "F"

        # Update record
        row["total_score"] = total_score
        row["average_score"] = average_score
        row["grade"] = grade

        cleaned_records.append(row)

    return cleaned_records
