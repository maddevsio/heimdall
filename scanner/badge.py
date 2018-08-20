import anybadge


def badge_generator(status):
    thresholds = {
        'critical': 'red',
        'minor': 'yellow',
        'passed': 'green',
        'processing': 'lightgrey',
    }
    badge = anybadge.Badge('Smart Contracts', status, thresholds=thresholds)
    return badge.badge_svg_text
