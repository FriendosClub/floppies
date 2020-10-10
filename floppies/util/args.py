import argparse


def arguments():
    parser = argparse.ArgumentParser(
        description='generate color pallettes from images in bulk'
    )
    debug_group = parser.add_argument_group(title='debug arguments')

    # DB File
    parser.add_argument(
        '-d', '--database',
        help='Specifies which JSON file to use.',
        type=str,
        default='database.json',
        dest='db_file'
    )

    # Image directory
    parser.add_argument(
        '-s', '--image-source',
        help='The directory in which to search for images.',
        type=str,
        default='images',
        dest='image_dir'
    )

    # File ext filter
    parser.add_argument(
        '-i', '--include',
        help='Which file extensions to process. '
        + 'Can be specified multiple times.',
        default=['.jpg', '.png'],
        action='append',
        dest='include_ext'
    )

    # Max reported colors
    parser.add_argument(
        '-c', '--max-colors',
        help='Maximum number of colors to extract from the image.',
        type=int,
        default=6,
        dest='max_colors'
    )

    # Color threshold
    parser.add_argument(
        '-t', '--color-threshold',
        help='How prevalent a color must be in an image to be stored. '
        + '(0.0-1.0)'
        + 'A value of 0 disables this feature.',
        type=float,
        default=0.01,
        dest='color_threshold'
    )

    # Debug arguments #

    # User-defined verbosity level
    debug_group.add_argument(
        '--loglevel',
        help='Controls verbosity.',
        choices=['DEBUG', 'INFO', 'NOTICE', 'WARN', 'ERROR', 'CRITICAL'],
        default='NOTICE',
        type=str.upper  # auto case conversion
    )

    # Force database upgrade
    debug_group.add_argument(
        '--force',
        help='Forces processing of images already in the database.',
        action='store_true',
        dest='force_update'
    )

    # Max images to process
    debug_group.add_argument(
        '--max-images',
        help='The maximum number of images to process. '
        + 'A value of 0 disables this functionality (default).',
        type=int,
        default=0,
        dest='max_images'
    )

    return parser
