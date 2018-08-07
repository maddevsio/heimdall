import anybadge

def badge_generator(status):
    thresholds = {
        'critical': 'red',
        'minor': 'yellow',
        'passed': 'green',
    }.get(status)

    badge = anybadge.Badge('Mythril Scanner:', status, thresholds=thresholds)
    return badge.badge_svg_text