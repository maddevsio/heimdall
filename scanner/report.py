def estimate_quality(report):
    issues = report.get('issues')
    badge = 'basge-success.svg'
    if issues:
        badge = 'badge-error.svg'

    with open(badge, 'r') as f:
        badge = f.read()
    return badge

