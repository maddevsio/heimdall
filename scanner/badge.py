import anybadge

def badge_generator(status):
    thresholds = {
        'critical': 'red',
        'minor': 'yellow',
        'passed': 'green',
    }.get(status)

    badge = anybadge.Badge('Heimdall', status, thresholds=thresholds)
    return badge.badge_svg_text