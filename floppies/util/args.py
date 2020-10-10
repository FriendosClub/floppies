import argparse


def arguments():
    parser = argparse.ArgumentParser(
        description='generate color pallettes from images in bulk'
    )
    parser.add_argument(
        '--db-file', '--db',
        help='Specifies which JSON file to use.',
        type=str,
        default='database.json'
    )
    parser.add_argument(
        '--image-dir',
        help='The directory in which to search for images.',
        type=str,
        default='images'
    )
    parser.add_argument(
        '--accept-ext',
        help='Which file extensions to process. '
        + 'Can be specified multiple times.',
        default=['.jpg', '.png'],
        action='append'
    )
    parser.add_argument(
        '--max-colors',
        help='Maximum number of colors to extract from the image.',
        type=int,
        default=6
    )
    parser.add_argument(
        '--color-threshold',
        help='How prevalent a color must be in an image to be stored. '
        + '(0.0-1.0)'
        + 'A value of 0 disables this feature.',
        type=float,
        default=0.01
    )
    debug_group = parser.add_argument_group(title="Debug")
    debug_group.add_argument(
        '--force-update',
        help='Forces processing of images already in the database.',
        action='store_true'
    )
    debug_group.add_argument(
        '--max-images',
        help='The maximum number of images to process. '
        + 'A value of 0 disables this functionality (default).',
        type=int,
        default=0
    )

    return parser
